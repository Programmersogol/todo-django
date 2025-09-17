# 📝 My ToDo App

یک برنامه ساده و شیک برای مدیریت کارها (ToDo) ساخته شده با **Django** و **Bootstrap 5**.  
این پروژه برای تمرین Django طراحی شده و شامل قابلیت‌های اصلی مدیریت کارهاست.

---

## ✨ ویژگی‌ها
- ➕ اضافه کردن تسک جدید
- ✅ علامت‌گذاری به‌عنوان انجام‌شده یا انجام‌نشده
- 📝 ویرایش تسک
- 🗑️ حذف تسک
- 🎨 رابط کاربری زیبا با Bootstrap 5
- 🔎 فیلتر کردن بر اساس **Done** و **Undone**
- 🚦 اولویت‌بندی (Low / Medium / High)

---

## ⚡ نصب و اجرا

```bash
# 1️⃣ کلون کردن مخزن
git clone https://github.com/USERNAME/REPO_NAME.git
cd REPO_NAME

# 2️⃣ ساخت و فعال‌سازی محیط مجازی
python -m venv venv
venv\Scripts\activate  # ویندوز
# یا
source venv/bin/activate  # لینوکس / مک

# 3️⃣ نصب وابستگی‌ها
pip install -r requirements.txt

# 4️⃣ مایگریت پایگاه داده
python manage.py migrate

# 5️⃣ (اختیاری) ساخت اکانت ادمین
python manage.py createsuperuser

# 6️⃣ اجرای سرور
python manage.py runserver
بعد از اجرا، برنامه روی این آدرس در دسترس است:
http://127.0.0.1:8000/


```
## 👨‍💻 توسعه‌دهنده
ساخته شده با ❤️ sogol razavi


## 📜 لایسنس
این پروژه تحت لایسنس MIT منتشر شده و استفاده آزاد است.
