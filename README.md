# BusterDev Books

![BusterDev Logo](https://via.placeholder.com/150x50?text=BusterDev+Books)

**BusterDev Books** — Django asosida ishlab chiqilgan kitoblar platformasi. Loyihaning asosiy maqsadi foydalanuvchilarga kitoblarni ko‘rish, qidirish va o‘qish imkoniyatini taqdim etishdir.  

---

## 📦 Hozirgi imkoniyatlar

- Foydalanuvchi ro‘yxatdan o‘tish, login/logout qilish.
- Email tasdiqlash bilan yangi foydalanuvchi ro‘yxatdan o‘tadi.
- Home sahifada barcha kitoblarni ko‘rish.
- Kitoblarni **title, author, expert, category** bo‘yicha qidirish.
- Category bo‘yicha filtrlash.
- Har bir kitob uchun alohida **book detail** sahifa.
- Kitoblarni ko‘rish bepul, lekin **download qilish uchun login bo‘lishi shart**.
- Navbar-da foydalanuvchi holati (login/register yoki username/logout) ko‘rinadi.
- Footer-da email va Telegram aloqa ma’lumotlari.

---

## ⚙️ Texnologiyalar

- Django 5.x
- Python 3.13
- PostgreSQL (ma’lumotlar bazasi)
- Bootstrap 5 (frontend)
- SMTP Email yuborish (Gmail orqali)
- Django messages framework (flash messages)

---

## 🗂 Loyihaning tuzilishi

```

project_root/
│
├── books/                 # Kitoblar ilovasi
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   └── templates/books/
│       ├── home.html
│       └── book_detail.html
│
├── users/                 # Foydalanuvchi ilovasi
│   ├── views.py
│   ├── urls.py
│   └── templates/users/
│       ├── register.html
│       ├── login.html
│       └── verify_email.html
│
├── templates/
│   └── base.html           # Umumiy template
│
├── static/
├── media/
├── manage.py
└── core/
└── settings.py

````

---

## 🚀 Loyihani ishga tushirish

1. **Clone qilamiz:**
```bash
git clone <repository_url>
cd django-library-web
````

2. **Virtual environment yaratish va faollashtirish:**

```bash
python -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows
```

3. **Dependencies o‘rnatish:**

```bash
pip install -r requirements.txt
```

4. **Ma’lumotlar bazasini sozlash:**

```bash
python manage.py makemigrations
python manage.py migrate
```

5. **Superuser yaratish (optional):**

```bash
python manage.py createsuperuser
```

6. **Serverni ishga tushirish:**

```bash
python manage.py runserver
```

---

## 📌 Kelajakda qo‘shilishi rejalashtirilganlar

* **Pagination**: Home va category sahifalarida kitoblarni sahifalash.
* **User profile**: Foydalanuvchi profilini ko‘rish va tahrirlash.
* **Kitob yuklash**: Foydalanuvchi faqat login bo‘lsa kitobni download qilishi mumkin.
* **Book ratings & reviews**: Kitobga baho berish va sharh qoldirish.
* **Admin panel optimizatsiyasi**: Kitob va kategoriyalarni qulay boshqarish.
* **Responsive dizayn**: Mobil qurilmalar uchun optimizatsiya.
* **Search suggestions / autocomplete**: Qidiruvni tezlashtirish.

---

## 📧 Aloqa

* Email: [saparov.dev2026@gmail.com](mailto:saparov.dev2026@gmail.com)
* Telegram: [@mr_mehroj](https://t.me/mr_mehroj)

---

> **Eslatma:** Loyihani rivojlantirish davomida frontend va backend qismida yaxshilanishlar kiritilishi mumkin.
