# مشروع أمل خوتاني — MASAR Mini-Lakehouse

أُنجز هذا المشروع ضمن **برنامج هندسة البيانات الحديثة لأنظمة الذكاء الاصطناعي — Modern Data Engineering for AI Systems (SDA-DSC-214)** لدى **[أكاديمية سدايا — SDAIA Academy](https://github.com/SDAIAAcademy)**.

**المتدربة:** أمل خوتاني — Amal Khotani  
**مواد الدورة والتنفيذ المشترك:** ميعاد المري — Meaad Al-Marri. استُخدمت مواد المقرر ودواله، مع تهيئة بيئة التشغيل وتوثيق نتائج اللابات.

#SDAIAAcademy

## فكرة المشروع والبيانات

يعالج المشروع بيانات رحلات وسائقين وأحداث مواقع **اصطناعية** باستخدام مسار Bronze → Silver → Gold. تشمل الأعمال استقبال البيانات، وإزالة التكرار، ومعالجة الوصول المتأخر والتصحيحات، والتدفق عبر Kafka، والتحقق من الجودة، وتجهيز مخرجات BI وخصائص AI المتاحة وقت القرار.

مجموعة البيانات هي `MASAR_SMALL_V1`: تتكون البداية من 72 رحلة و6 سائقين و216 حدث موقع. تضيف السيناريوهات التدريبية الوصول المتأخر والإعادة والتصحيح؛ لذلك تختلف الأعداد النهائية عن أعداد المصدر الأساسية.

## البيئة وترتيب التشغيل

- Google Colab باستخدام CPU، وPython 3.11.13 وJava 17.
- PySpark 3.5.8، وDelta Spark 3.3.3، وPy4J 0.10.9.9.
- dbt-core 1.9.8 وdbt-spark 1.9.1، وKafka Python 2.2.15.
- Great Expectations 1.7.0 وpandas 2.2.3 لقسم الجودة.
- مساحة العمل التراكمية: `outputs/day01_bronze_xgnqdyt3`.

| اليوم | ترتيب التنفيذ |
|---|---|
| 1 | فحص المصدر، وبناء Bronze، ونموذج التكلفة، ومقارنة قراءة CSV وDelta |
| 2 | Staging، ثم Silver، ثم تشغيل dbt والتحقق من إعادة التشغيل |
| 3 | معاملات Delta والتصحيح، ثم الصيانة على نسخة معزولة |
| 4 | استقبال أحداث Kafka، ثم فحص الجودة والعزل |
| 5 | بناء Gold واختبار التعافي، ثم تصدير بيانات AI وBI وحفظ المخرجات |

عند الانتقال إلى جلسة جديدة تُستعاد ملفات الانتقال في جذر المستودع وتُفحص البيئة، ثم يُستخدم مؤشر مساحة العمل الناجحة. في اليوم الخامس استُعيد `day04_handoff.zip` وفُعّل Java 17 قبل تشغيل Gold. يعتمد اليوم الخامس على جداول اليوم الرابع المحفوظة، ولا يتطلب تشغيل وسيط Kafka من جديد.

## النتائج المرصودة

| النتيجة | القيمة |
|---|---:|
| الرحلات النهائية المعتمدة | 75 |
| إجمالي الأجور بعد التصحيح | 1,880.60 ريال |
| أحداث GPS المختلفة | 217 |
| الرسائل المستقبلة في نهاية تجربة Kafka | 219 |
| السجلات المعزولة في تجربة الجودة | 7 |
| فحوص التعافي في لاب 7 | 4 من 4 ناجحة |
| فحوص التقديم في لاب 8 | 16 من 16 ناجحة |
| جداول مخرجات اليوم الخامس وصادرات CSV المقابلة | 8 |
| صفوف خصائص AI | 3 |
| صفوف النتائج المستقبلية | 3 بحالة `UNOBSERVED` وأهداف فارغة |

إجماليات المدن: الدمام 25 رحلة و670.40 ريال، وجدة 25 رحلة و625.20 ريال، والرياض 25 رحلة و585.00 ريال. أظهر مسار dbt المحفوظ في الدفتر `PASSED_DBT_NATIVE` وأربع مراحل ناجحة.

## الأدلة المحفوظة

- الدفاتر اليومية: [اليوم 1](day01/STUDENT.ipynb)، [اليوم 2](day02/STUDENT.ipynb)، [اليوم 3](day03/STUDENT.ipynb)، [اليوم 4](day04/STUDENT.ipynb)، [اليوم 5](day05/STUDENT.ipynb).
- [ملحق استعادة المشروع وإعادة dbt](day02/DBT_RECOVERY.ipynb)، بمخرجاته الفعلية من الدفتر المحدّث.
- أرشيف مساحة العمل: `day05_handoff.zip`، ومعه `dbt_evidence_83b24dcb.zip` لأدلة dbt المستقلة.
- تقارير اليوم الخامس نسبةً إلى مساحة العمل: `reports/day05_recovery.json` و`reports/day05_gold_latest.json` و`reports/day05_serving_latest.json`.
- الإصدار المختار: `147d2aa43f48468abed9551ef993a263`.
- معرف التصدير: `54473826dac64b75b58396de0e18e0bc`.
- ملاحظات اللابات: [01](LAB01_NOTES.md)، [02](LAB02_NOTES.md)، [03](LAB03_NOTES.md)، [04](LAB04_NOTES.md)، [05](LAB05_NOTES.md)، [06](LAB06_NOTES.md)، [07](LAB07_NOTES.md)، [08](LAB08_NOTES.md).
- القرارات: [المعمارية والتنفيذ](DECISIONS.md)، [الأداء والتكلفة](BENCHMARKS.md)، [الحوكمة](GOVERNANCE.md).
- [فهرس الأدلة والبيئة](EVIDENCE_INDEX.md)، [تنظيم الدفاتر](NOTEBOOK_ORGANIZATION.md)، [قائمة متابعة التسليم](SUBMISSION_CHECKLIST.md).

**رابط المخرجات المحفوظة:** يضاف رابط قابل للوصول عبر قناة التسليم المعتمدة قبل الإرسال النهائي.

## حالة تجهيز التسليم

جُهزت الدفاتر اليومية الخمسة وملاحظات اللابات والقرارات من المخرجات الفعلية. بعد فقد ملفات dbt القديمة أُعيد تشغيل مشغّل المقرر على نسخ معزولة من Bronze، وحُفظت أدلته في `dbt_evidence_83b24dcb.zip`. تقرير المحاولة الجديدة `outputs/dbt_validation_tedk3wzl/reports/dbt_attempt.json` وحالته `PASSED_DBT_NATIVE`؛ التوثيق المولد يغطي 6 نماذج و3 مصادر.

لم يختبر Run all نظيف بعد فصل الدفاتر. بقيت خلية إعداد مضافة غير منفذة في دفتر اليوم الخامس، كما توضح وثيقة التنظيم. نتائج فحص المصدر والتكلفة مطبوعة في اليوم الأول، لكن ملفي JSON الأصليين لم يرفقا بعد. يبقى استكمال رابط المخرجات وفحص النسخ المرفوعة وأخذ معرف التعديل النهائي؛ تفاصيل الحالة في قائمة المتابعة.

## حدود النتائج

- البيانات اصطناعية والنتائج تخص العينة التدريبية.
- `zone_key` يمثل مدينة تمثيلية، وليس حدود منطقة خدمة موثقة.
- بقيت الأهداف المستقبلية مجهولة؛ لم يُدرب نموذج ولم تُحسب درجة دقة.
- لا يُدعى تشغيل موصل Power BI أو نشر لوحة معلومات أو خدمة عامة.
- تجربة التعافي كانت داخل جلسة Spark واحدة؛ لا تثبت معاملة واحدة تشمل الجداول الثمانية أو التعافي من تعطل الجهاز.
- تُحفظ ملفات المخرجات الكبيرة والأرشيفات خارج Git عبر قناة التسليم المعتمدة.

## المراجع

- [دليل التسليم](project/SUBMISSION.md)
- [قائمة اكتمال اليوم الخامس](day05/COMPLETION.md)
- [قاموس البيانات](data/DICTIONARY.md)
- [دليل Git](docs/GIT_WORKFLOW.md)
- [مصدر مواد الدورة — ميعاد المري](https://github.com/almiyead-rgb/masar-modern-data-engineering)

---

## مواد الدورة الأصلية

<table dir="ltr" width="100%"><tr><td width="50%" dir="ltr" lang="en" align="left" valign="top"><p>SDAIA Academy · Learner materials</p><h1>Modern Data Engineering<br>for AI Systems</h1><h2>MASAR · Mini-Lakehouse</h2><p><strong>Meaad Al-Marri</strong><br>SDA-DSC-214 · Five days · Eight cumulative labs</p></td><td width="50%" dir="rtl" lang="ar" align="right" valign="top"><p>أكاديمية سدايا · مواد المتدرب</p><h1>هندسة البيانات الحديثة<br>لأنظمة الذكاء الاصطناعي</h1><h2>مسار · بيئة بيانات مصغرة</h2><p><strong>ميعاد المري</strong><br>SDA-DSC-214 · خمسة أيام · ثمانية لابات تراكمية</p></td></tr></table>

<table dir="ltr" width="100%"><tr><td width="50%" dir="ltr" lang="en" align="left" valign="top"><h2>What you will build</h2><p>Turn small synthetic trip, driver and location feeds into a reliable data pipeline: preserve the source, build Silver, manage changes, receive events, check quality and deliver reporting and AI-ready tables.</p><p><strong>The labs are your final project.</strong> Complete them in sequence; no separate final assignment is added.</p></td><td width="50%" dir="rtl" lang="ar" align="right" valign="top"><h2>ماذا ستبني؟</h2><p>حوّل ملفات اصطناعية صغيرة للرحلات والسائقين والمواقع إلى خط بيانات موثوق: احفظ المصدر، وابنِ Silver، وأدر التغييرات، واستقبل الأحداث، وافحص الجودة، ثم جهّز جداول التقارير والذكاء الاصطناعي.</p><p><strong>اللابات هي مشروعك النهائي.</strong> أكملها بالتتابع دون تكليف نهائي منفصل.</p></td></tr></table>

<table dir="ltr" width="100%"><tr><td width="50%" dir="ltr" lang="en" align="left" valign="top"><h2>Your five-day path</h2><p><strong><a href="day01/README.md">Day 1</a></strong> · Foundations and Bronze</p><p><strong><a href="day02/README.md">Day 2</a></strong> · ELT and Silver</p><p><strong><a href="day03/README.md">Day 3</a></strong> · Delta transactions and maintenance</p><p><strong><a href="day04/README.md">Day 4</a></strong> · Streaming, quality and governance</p><p><strong><a href="day05/README.md">Day 5</a></strong> · Gold, AI/BI and project submission</p></td><td width="50%" dir="rtl" lang="ar" align="right" valign="top"><h2>مسارك في الأيام الخمسة</h2><p><strong><a href="day01/README.md">اليوم 1</a></strong> · الأساسيات وطبقة Bronze</p><p><strong><a href="day02/README.md">اليوم 2</a></strong> · التحويل وبناء Silver</p><p><strong><a href="day03/README.md">اليوم 3</a></strong> · معاملات Delta والصيانة</p><p><strong><a href="day04/README.md">اليوم 4</a></strong> · التدفق والجودة والحوكمة</p><p><strong><a href="day05/README.md">اليوم 5</a></strong> · طبقة Gold ومخرجات AI وBI وتسليم المشروع</p></td></tr></table>

<table dir="ltr" width="100%"><tr><td width="50%" dir="ltr" lang="en" align="left" valign="top"><h2>Before you start</h2><p><a href="docs/SETUP.md">Prepare your environment</a> · <a href="TRAINING_CONTENT.md">Learning outcomes</a> · <a href="data/DICTIONARY.md">Data dictionary</a> · <a href="project/SUBMISSION.md">Submission guide</a>.</p><p>Use the same 72 base trips, 6 drivers and 216 base location events throughout the course, with the supplied late/replay/correction fixtures. Data and code are shared once; each day contains its own learning materials. No paid API or GPU is required.</p></td><td width="50%" dir="rtl" lang="ar" align="right" valign="top"><h2>قبل أن تبدأ</h2><p><a href="docs/SETUP.md">جهّز بيئتك</a> · <a href="TRAINING_CONTENT.md">مخرجات التعلم</a> · <a href="data/DICTIONARY.md">قاموس البيانات</a> · <a href="project/SUBMISSION.md">دليل التسليم</a>.</p><p>استخدم الرحلات الأساسية الـ72 والسائقين الستة وأحداث المواقع الـ216 طوال الدورة، مع ملفات التأخر والإعادة والتصحيح المرفقة. تُحفظ البيانات والأكواد المشتركة مرة واحدة، ويضم كل يوم مواده التعليمية. لا تحتاج إلى API مدفوع أو GPU.</p></td></tr></table>

<table dir="ltr" width="100%"><tr><td width="50%" dir="ltr" lang="en" align="left" valign="top"><p><a href="docs/ADMINISTRATION.md">Participation and support</a> · <a href="docs/GIT_WORKFLOW.md">Git guide</a> · <a href="docs/TROUBLESHOOTING.md">Troubleshooting</a> · <a href="docs/VERIFICATION.md">Execution record</a> · <a href="https://github.com/SDAIAAcademy">SDAIA Academy</a></p><p>At final submission, name the programme and <strong>SDAIA Academy</strong> in your project README, link to <a href="https://github.com/SDAIAAcademy">the Academy</a>, and include <code>#SDAIAAcademy</code> in the README and your submission message. Follow <a href="project/SUBMISSION.md">the submission guide</a>. Optional extensions and repository stars are not passing conditions. Follow the organizer’s announced attendance, deadline and submission rules.</p></td><td width="50%" dir="rtl" lang="ar" align="right" valign="top"><p><a href="docs/ADMINISTRATION.md">المشاركة والدعم</a> · <a href="docs/GIT_WORKFLOW.md">دليل Git</a> · <a href="docs/TROUBLESHOOTING.md">معالجة الأخطاء</a> · <a href="docs/VERIFICATION.md">سجل التنفيذ</a> · <a href="https://github.com/SDAIAAcademy">أكاديمية سدايا</a></p><p>عند التسليم النهائي، اذكر اسم البرنامج و<strong>أكاديمية سدايا</strong> في README مشروعك، وأدرج <a href="https://github.com/SDAIAAcademy">رابط الأكاديمية</a> والوسم <code>#SDAIAAcademy</code> داخل README وفي رسالة التسليم. اتبع <a href="project/SUBMISSION.md">دليل التسليم</a>. الامتدادات الاختيارية ونجوم المستودع ليست شروط نجاح. اتبع ما تعلنه الجهة المنظمة بشأن الحضور والمواعيد وقناة التسليم.</p></td></tr></table>

