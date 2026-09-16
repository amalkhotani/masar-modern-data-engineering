# EVIDENCE INDEX — فهرس الأدلة والبيئة

أمل خوتاني — Amal Khotani. برنامج **هندسة البيانات الحديثة لأنظمة الذكاء الاصطناعي — Modern Data Engineering for AI Systems (SDA-DSC-214)**، [أكاديمية سدايا](https://github.com/SDAIAAcademy). #SDAIAAcademy

مواد الدورة ودوالها: **ميعاد المري — Meaad Al-Marri**. هذه ملاحظات مبنية على المخرجات المحفوظة في الدفتر المرفوع والتقارير الأصلية؛ لم يُعد تشغيل Spark أثناء إعدادها. تفاصيل البيئة وبصمات الأدلة وحدود التحقق في [EVIDENCE_INDEX.md](EVIDENCE_INDEX.md).

## هوية المراجعة

تاريخ إعداد الملاحظات: 16 سبتمبر 2026. ملف المصدر `amal_khotani (3).ipynb` يجمع جلسات متعددة ومخرجاته محفوظة. فُصل إلى خمسة دفاتر دون إعادة تنفيذ. توضح [NOTEBOOK_ORGANIZATION.md](NOTEBOOK_ORGANIZATION.md) الخلية المضافة غير المنفذة والبيانات الموروثة من قالب الدورة. لا تمثل توقيتات GitHub Actions الموروثة تاريخ تنفيذ المتدربة.

البيئة المرصودة: Google Colab CPU، Python 3.11.13، Java 17.0.20، Spark 3.5.8، Delta Spark 3.3.3، Py4J 0.10.9.9. استخدم كود Kafka المحفوظ 4.0.2 وkafka-python 2.2.15؛ وخلية الجودة Great Expectations 1.7.0 وpandas 2.2.3. نجاح ما قبل التشغيل لا يمثل تشغيل اللاب نفسه.

المصدر: `data/masar-small-v1`. بصمة Manifest: `20a7e45bed2980b9394c10e8532da3b9f40f614366bb2df26a88610253e768e3`.

WORK: `outputs/day01_bronze_xgnqdyt3`. مؤشر الاستمرار: `outputs/day01_bronze_success.json`. معناه آخر Bronze ناجح وليس موافقة المقرر كاملًا.

## التقارير الأصلية المحفوظة

| الجزء | تقرير داخل WORK | فحوص true |
|---|---|---|
| LAB01 | `reports/bronze.json` | 7 |
| LAB02 | `reports/benchmark.json` | 4 |
| LAB03a | `reports/day02_staging_latest.json` | 5 |
| LAB03b | `reports/day02_silver.json` | 5 |
| LAB04a | `reports/day03_transactions.json` | 6 |
| LAB04b | `reports/day03_maintenance_latest.json` | 7 |
| LAB05 | `reports/day04_stream_latest.json` | 13 |
| LAB06 | `reports/day04_quality_latest.json` | 9 |
| LAB07 | `reports/day05_recovery.json` | 4 |
| LAB08 | `reports/day05_serving_latest.json` | 16 |

أرقام a/b أجزاء داخل اللابين 03 و04، وليست لابات إضافية. أعداد true مستخرجة من التقارير الفعلية الموجودة في ZIP؛ ليست درجات تقييم.

## دليل dbt المستعاد بإعادة تنفيذ فعلية

ورد `amal_khotani (4).ipynb` بعد إعادة التنفيذ، مع `dbt_evidence_83b24dcb.zip` بحجم 3,669,449 بايت و717 مدخلًا. طوبقت المخرجات الجديدة مع الأرشيف؛ الحالة `PASSED_DBT_NATIVE`، والمراحل الأربع 72/72/75/75 رحلة، و1794.60/1794.60/1875.60/1875.60 ريالًا.

التقرير: `outputs/dbt_validation_tedk3wzl/reports/dbt_attempt.json`. معرف المحاولة `83b24dcbe27141009fec1b6eae58baef`. وقت التشغيل UTC: من `2026-09-16T21:38:35.917764+00:00` إلى `2026-09-16T21:43:23.986216+00:00`.

وجدت 16 هوية استدعاء مختلفة لأوامر المراحل، وكل build يحتوي 6 نماذج ناجحة و23 اختبارًا ناجحًا؛ فحوص المصادر الثلاثة ناجحة دون تحذيرات في كل مرحلة. ملفات التوثيق الثلاثة موجودة، والكتالوج يغطي 6 نماذج و3 مصادر. طوبقت 60 بصمة مختلفة للملفات، وعدد صفوف لقطات JSON ومجاميعها وتفرد مفاتيحها وتطابق المحتوى عند الإعادة. وطابقت بصمة تقرير Bronze المدخل الملف المحفوظ في Day05 ZIP.

البيئة في تقرير dbt: Python 3.11.13، Java 17.0.20، PySpark 3.5.8، Delta Spark 3.3.3، Py4J 0.10.9.9، dbt-core 1.9.8، dbt-spark 1.9.1؛ قائمة مشكلات الاعتماديات فارغة. بصمة التنفيذ المسجلة `43380b05b42038287be89cc950cea49afa83eb71816bb607f8871263cca5250b` ليست Git commit ID.

خلايا الاستعادة وإعادة التنفيذ في [day02/DBT_RECOVERY.ipynb](day02/DBT_RECOVERY.ipynb). تفاصيل السيناريوهات في [LAB03_NOTES.md](LAB03_NOTES.md). ملفات المحاولة الجديدة منفصلة عن نتائج Gold، وعن مسار المحاولة القديمة المطبوع في الدفتر. ما زال ملفا `source_inspection.json` و`cost_model_result.json` الأصليان غير مرفقين؛ نتائجهما المطبوعة محفوظة في اليوم الأول.

## البصمات وحدود التحقق

- SHA-256 للدفتر الأصلي: `38ce52755e0318a93fc52121abad098327f4451a464cec3d8f26e60312f40d36`.
- SHA-256 للدفتر المحدّث: `d98252b1b47df0fdedcc8b4c5e264c0aed10014426148185ff3c4d1c6963300a`.
- SHA-256 لأرشيف dbt: `1708b19f989933ed1960e7dcd3a073842e983d50dc26273e9db216ebe9607214`.
- SHA-256 لأرشيف اليوم الخامس: `71bf94b3357ce83901fbd578811eaa3f0b768869cb0b923644f691f2021a4f51`.
- فُحصت سلامة ZIP، وقرئت التقارير الأصلية ومخرجات الدفتر وCSV، وطوبقت مجاميع اليوم الخامس وبصمات صادراته وبصمات ملفات الإصدارين السليمين في المراجعة السابقة.
- لم يُعد تشغيل Spark أو Kafka أو dbt أثناء إعداد التوثيق، ولم تُفك صفوف Parquet في بيئة المراجعة. ملاحظات صفوف Bronze تجمع عينة المصدر المطبوعة مع فحوص مطابقة الدفعات؛ ليست ناتج استعلام فردي جديد.
- معرّف Git الفعلي للشفرة وقت التشغيل القديم لم يطبع في الدفتر. نسخة التعليمات المرجعية المستخدمة سابقًا `8d98b9275296ae063e04b1d9088573de4ff6ca7d` ليست بديلًا عن ذلك المعرّف.

## مراجع المقرر

[قالب الملاحظات](https://github.com/amalkhotani/masar-modern-data-engineering/blob/develop/templates/LAB_NOTES.md)، [أسئلة اليوم 1](https://github.com/amalkhotani/masar-modern-data-engineering/blob/develop/day01/PRACTICE.md)، [اليوم 2](https://github.com/amalkhotani/masar-modern-data-engineering/blob/develop/day02/PRACTICE.md)، [اليوم 3](https://github.com/amalkhotani/masar-modern-data-engineering/blob/develop/day03/PRACTICE.md)، [اليوم 4](https://github.com/amalkhotani/masar-modern-data-engineering/blob/develop/day04/PRACTICE.md)، [التسليم](https://github.com/amalkhotani/masar-modern-data-engineering/blob/develop/project/SUBMISSION.md)، [الاكتمال](https://github.com/amalkhotani/masar-modern-data-engineering/blob/develop/day05/COMPLETION.md).
