[app]

# (str) عنوان تطبيقك
title = Yemen Vault

# (str) اسم الحزمة (يجب أن يكون فريداً)
package.name = yemenvault

# (str) اسم النطاق للحزمة
package.domain = org.yemen.vault

# (str) ملف الكود الرئيسي (يجب أن يكون main.py)
source.main.py = main.py

# (list) المجلدات التي تحتوي على الكود
source.dir = .

# (str) إصدار التطبيق
version = 1.0

# (list) المكتبات المطلوبة (لا تحذف شيئاً منها)
requirements = python3, kivy, cryptography, arabic-reshaper, python-bidi, pillow

# (list) الملفات التي تريد تضمينها (مثل الخطوط)
source.include_exts = py,png,jpg,kv,atlas,ttf

# (str) اتجاه الشاشة (Portrait يعني عمودي)
orientation = portrait

# (list) الأذونات المطلوبة للوصول لملفات الهاتف
android.permissions = READ_EXTERNAL_STORAGE, WRITE_EXTERNAL_STORAGE

# (int) إصدار أندرويد المستهدف
android.api = 33
android.minapi = 21
android.sdk = 33
android.ndk = 25b

[buildozer]

# (int) مستوى عرض الأخطاء (0=خفيف، 2=مفصل)
log_level = 2

# (int) هل تريد حذف ملفات البناء القديمة؟ (1=نعم)
warn_on_root = 1
