"""Fresh native execution; preserve historical student notebooks and failed logs."""
from __future__ import annotations

import json
import shutil
import subprocess
import sys
import traceback
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))
from masar.cost import cost_report
from masar.native_contracts import STAGES, read_stage_report
from masar.sources import profile_sources
from masar.workspace import completed_bronze_workspace


def now() -> str:
    return datetime.now(timezone.utc).isoformat()


def main() -> int:
    output = ROOT / "outputs"
    if output.exists() and any(output.iterdir()):
        raise RuntimeError("Use a fresh checkout with an empty outputs directory")
    logs = output / "recheck_logs"
    logs.mkdir(parents=True, exist_ok=True)
    summary = {
        "scope": "NEW_NATIVE_PIPELINE_AND_DBT_RECHECK",
        "started_at": now(), "status": "RUNNING",
        "commit": subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=ROOT, text=True).strip(),
        "python": sys.version, "historical_notebooks_reexecuted": False,
        "commands": [], "completed_stages": [],
    }
    code = 1
    try:
        for name, result in [
            ("source_inspection", profile_sources(ROOT / "data/masar-small-v1")),
            ("cost_model_result", cost_report()),
        ]:
            (output / f"{name}.json").write_text(json.dumps(result, indent=2) + "\n")
        for script in ["run_day01", "run_day02", "run_dbt", "run_day03", "run_day04", "run_day05"]:
            print(f"Running {script}", flush=True)
            record = {"script": script, "started_at": now()}
            summary["commands"].append(record)
            with (logs / f"{script}.log").open("w") as log:
                run = subprocess.run([sys.executable, str(ROOT / "scripts" / f"{script}.py")],
                                     cwd=ROOT, stdout=log, stderr=subprocess.STDOUT, timeout=1500)
            record.update(returncode=run.returncode, finished_at=now())
            if run.returncode:
                raise RuntimeError(f"{script} failed; see outputs/recheck_logs/{script}.log")
        work = completed_bronze_workspace(ROOT)
        for name in STAGES:
            report = read_stage_report(work, name)
            summary["completed_stages"].append({"name": name, "checks_passed": len(report["checks"])})
        attempts = sorted(output.glob("*/reports/dbt_attempt.json"))
        if len(attempts) != 1:
            raise RuntimeError("Expected exactly one fresh dbt attempt")
        dbt = json.loads(attempts[0].read_text())
        if dbt.get("status") != "PASSED_DBT_NATIVE" or dbt.get("dbt_executed") is not True:
            raise RuntimeError("Native dbt did not pass")
        if [p["rows"] for p in dbt["phases"]] != [72, 72, 75, 75]:
            raise RuntimeError("Unexpected dbt phase populations")
        summary.update(status="PASSED_NATIVE_PIPELINE_AND_DBT", workspace=str(work.relative_to(ROOT)),
                       dbt_report=str(attempts[0].relative_to(ROOT)))
        code = 0
    except Exception as exc:
        summary.update(status="FAILED", error=f"{type(exc).__name__}: {exc}")
        (logs / "recheck_traceback.log").write_text(traceback.format_exc())
    finally:
        summary["finished_at"] = now()
        (output / "native_recheck.json").write_text(json.dumps(summary, indent=2) + "\n")
        shutil.make_archive(str(ROOT / "native_recheck"), "zip", ROOT, "outputs")
        print(json.dumps(summary, indent=2), flush=True)
    return code


if __name__ == "__main__":
    raise SystemExit(main())
