# 📚 Django Library Web

**Django Library Web** is an online library web application where admins can upload books (cover image + file), and users can browse and download books.

---

## 🚀 Features

### 👮 Admin

* Add / delete / update books
* For each book:

  * Cover image
  * Book file (PDF / EPUB / WORD)
  * Multiple authors
  * Multiple categories
  * Publication year
* Manage authors and categories

### 👤 User

* View list of books
* View book detail page
* Download books if logged in
* View only (no download) if not logged in

---

## 🧱 Technologies

* **Django**
* **Python**
* HTML / CSS
* PostgreSQL
* Django Admin
* Django Authentication System

---

## 📁 Project Structure

```text
library_project/
│
├── library_project/
│   ├── settings.py
│   ├── urls.py
│
├── books/
│   ├── models.py
│   ├── views.py
│   ├── admin.py
│   ├── urls.py
│
├── users/
│
├── templates/
│   └── books/
│       ├── book_list.html
│       └── book_detail.html
│
├── media/
│   ├── book_covers/
│   └── book_files/
│
├── manage.py
└── README.md
```

---

## ⚙️ Installation

### 1️⃣ Clone the repository

```bash
git clone https://github.com/mehroj-saparov-io/django-library-web.git
cd django-library-web
```

---

### 2️⃣ Create virtual environment

```bash
python -m venv venv
source venv/bin/activate   # Linux / Mac
venv\Scripts\activate      # Windows
```

---

### 3️⃣ Install required packages

```bash
pip install django pillow
```

> `Pillow` is required for image upload support

---

### 4️⃣ Run migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

---

### 5️⃣ Create superuser

```bash
python manage.py createsuperuser
```

---

### 6️⃣ Run development server

```bash
python manage.py runserver
```

👉 Open in browser:

* Website: [http://127.0.0.1:8000](http://127.0.0.1:8000)
* Admin panel: [http://127.0.0.1:8000/admin](http://127.0.0.1:8000/admin)

---

## 🧩 Core Models

### 📘 Book

* `title`
* `cover_image`
* `book_file`
* `authors` (ManyToMany)
* `categories` (ManyToMany)
* `published_year`
* `description`

### ✍️ Author

* `full_name`
* `birth_year`

### 🏷 Category

* `name`

---

## 🔐 Permissions

| Action        | Guest | User | Admin |
| ------------- | ----- | ---- | ----- |
| Book list     | ✅     | ✅    | ✅     |
| Detail page   | ✅     | ✅    | ✅     |
| Download book | ❌     | ✅    | ✅     |
| Add book      | ❌     | ❌    | ✅     |

---

## 🖼 Media Configuration

`settings.py`:

```python
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'
```

`urls.py`:

```python
from django.conf import settings
from django.conf.urls.static import static

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```

---

## 👨‍💻 Author

**Your Name**
GitHub: [https://github.com/mehroj-saparov-io](https://github.com/mehroj-saparov-io)

