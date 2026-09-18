# أدلة مشروع أمل خوتاني

**نجح التشغيل الكامل** في [المحاولة 35267123057](https://github.com/amalkhotani/masar-modern-data-engineering/actions/runs/35267123057) بتاريخ 2026-09-17، من شفرة commit `79b2c19720bd569e68571a6027e7a832c8eca628`. نفذت المشغلات الأصلية بالتتابع: اليوم 1، اليوم 2، dbt، اليوم 3، اليوم 4، اليوم 5.

- [تنزيل المخرجات الفعلية: native_recheck.zip](https://github.com/amalkhotani/masar-modern-data-engineering/releases/download/verification-35267123057/native_recheck.zip)
- [صفحة الإصدار الدائم](https://github.com/amalkhotani/masar-modern-data-engineering/releases/tag/verification-35267123057)
- [ملخص التنفيذ](native_recheck.json)، من JSON الذي طُبع في سجل التشغيل؛ توجد النسخة الأصلية داخل الأرشيف.

## محتويات الأرشيف

جميع المسارات الآتية داخل ZIP، وليست ملفات يدّعي هذا الفهرس وجودها داخل Git:

| الدليل | المسار داخل الأرشيف |
|---|---|
| حالة التشغيل وبيئته وتوقيته | `outputs/native_recheck.json` |
| فحص المصدر المنفذ حديثًا | `outputs/source_inspection.json` |
| نموذج التكلفة المنفذ حديثًا | `outputs/cost_model_result.json` |
| تقارير Bronze وSilver والمعاملات والأداء | `outputs/day01_engine_k59q9hgr/reports/` |
| Kafka والجودة والعزل | `reports/day04_stream_latest.json` و`reports/day04_quality_latest.json` داخل مساحة اليوم الأول |
| التعافي ومخرجات AI وBI | `reports/day05_recovery.json` و`reports/day05_serving_latest.json` داخل المساحة نفسها |
| ملفات CSV الثمانية | داخل `reports/serving/`؛ يحدد تقرير التقديم المسارات والبصمات وأعداد الصفوف |
| تقرير dbt ومراحله | `outputs/dbt_validation_9ogwpqiz/reports/dbt_attempt.json` |
| توثيق dbt المولد | `outputs/dbt_validation_9ogwpqiz/dbt/commands/documentation/target/` |
| سجلات المشغلات الستة | `outputs/recheck_logs/` |

توجد أيضًا ملفات Delta الفعلية داخل مساحة التشغيل. حُفظ الأرشيف في Releases بدل إدخال هذه الملفات الكبيرة في تاريخ Git.

## ما تحقق

- أرجعت المشغلات الستة رمز خروج صفرًا.
- اجتازت تقارير المراحل العشر 76 فحصًا، ومنها 13 للتدفق و9 للجودة و4 للتعافي و16 للتقديم.
- تحققت عقود الأدلة وبصمات ملفات Delta وخطط الاستعلام بواسطة `read_stage_report`.
- نجح dbt بحالة `PASSED_DBT_NATIVE` ومراحل 72/72/75/75 صفًا.
- أُنتج ملفا المصدر والتكلفة باستدعاء دوال المقرر فعليًا ضمن هذه المحاولة الجديدة.
- نُشر الأرشيف فقط بعد اجتياز بوابة النجاح.

حجم الأرشيف **15,640,142 بايت**. بصمة SHA-256 المعلنة من GitHub:

```text
9af0a4f4706de040777f22d44a232bdb62a04a23a95d6d866e506c054310816d
```

بيئة المحاولة: Ubuntu 24.04، Python 3.11.16، Java 17.0.20، والاعتماديات المثبتة من ملفات requirements الخاصة بالمقرر. لا تعمم أرقام الأداء بين هذه البيئة وجلسة Colab التاريخية.

## حدود الدليل

هذه إعادة فعلية للمسار عبر مشغلات المقرر، وليست Run all للدفاتر المنظمة. الدفاتر التاريخية لم تُعد كتابتها. تبقى النتائج في README وملاحظات اللابات موصوفة باعتبارها نتائج جلسة Colab السابقة؛ تقارير الأرشيف الجديد هي مرجع المحاولة الجديدة.

البيانات اصطناعية. وحدات التكلفة تعليمية وليست تسعيرًا سحابيًا. لا تعني هذه الأدلة نشر خدمة إنتاجية أو تدريب نموذج AI أو إثبات عمل يومي سابق في سجل Git.

المشروع ضمن **Modern Data Engineering for AI Systems (SDA-DSC-214)** لدى **[SDAIA Academy](https://github.com/SDAIAAcademy)**. مواد المقرر ودواله: **Meaad Al-Marri**. #SDAIAAcademy
