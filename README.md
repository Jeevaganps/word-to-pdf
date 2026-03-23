# DocToPDF – Word to PDF Converter
A minimal, fast, Django-powered Word → PDF converter website.

## ✅ Features
- Drag & drop or click to upload .docx / .doc files
- Conversion via LibreOffice (best quality) with python-docx + reportlab fallback
- Auto-deletes files after 1 hour
- Google AdSense slots pre-wired (just add your publisher ID)
- Google Analytics pre-wired
- Fully responsive – mobile, tablet, desktop
- No JavaScript frameworks – lightweight vanilla JS + CSS (~8 KB total)
- FAQ accordion, Features section, Privacy/Terms/Contact pages

---

## 🚀 Quick Start

### 1. Clone / extract the project
```bash
cd wordtopdf_project
```

### 2. Create virtual environment
```bash
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. (Recommended) Install LibreOffice for best PDF quality
```bash
# Ubuntu / Debian
sudo apt-get install libreoffice

# macOS
brew install --cask libreoffice

# Without LibreOffice: falls back to python-docx + reportlab (text-only, no images)
```

### 5. Apply migrations
```bash
python manage.py migrate
```

### 6. Create superuser (for /admin panel)
```bash
python manage.py createsuperuser
```

### 7. Run dev server
```bash
python manage.py runserver
```
Open http://127.0.0.1:8000

---

## 🌐 Production Deployment

### Environment variables to set:
```bash
DJANGO_SECRET_KEY=your-long-random-secret-key
DJANGO_DEBUG=False
DJANGO_ALLOWED_HOSTS=yourdomain.com,www.yourdomain.com
```

### Update settings.py for production:
```python
DEBUG = False
ALLOWED_HOSTS = ['yourdomain.com', 'www.yourdomain.com']
SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY')

# Serve static files with WhiteNoise (add to MIDDLEWARE after SecurityMiddleware):
# 'whitenoise.middleware.WhiteNoiseMiddleware',
# STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
```

### Collect static files:
```bash
python manage.py collectstatic
```

### Run with Gunicorn:
```bash
gunicorn wordtopdf.wsgi:application --bind 0.0.0.0:8000 --workers 3
```

### Nginx config example:
```nginx
server {
    listen 80;
    server_name yourdomain.com;

    location /static/ { alias /path/to/project/staticfiles/; }
    location /media/  { alias /path/to/project/media/; }

    location / {
        proxy_pass http://127.0.0.1:8000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        client_max_body_size 25M;
    }
}
```

---

## 📢 Google AdSense Setup
1. Sign up at https://adsense.google.com
2. Get your publisher ID (format: `ca-pub-XXXXXXXXXXXXXXXXX`)
3. In `wordtopdf/settings.py`, set:
   ```python
   GOOGLE_ADSENSE_CLIENT = 'ca-pub-XXXXXXXXXXXXXXXXX'
   ```
4. The homepage has a pre-wired 728×90 leaderboard slot. Add more slots by copying the `<ins>` block pattern.

## 📊 Google Analytics Setup
1. Sign up at https://analytics.google.com
2. Get your Measurement ID (format: `G-XXXXXXXXXX`)
3. In `wordtopdf/settings.py`, set:
   ```python
   GOOGLE_ANALYTICS_ID = 'G-XXXXXXXXXX'
   ```

---

## 🗂 Project Structure
```
wordtopdf_project/
├── manage.py
├── requirements.txt
├── wordtopdf/
│   ├── settings.py       ← Main config (AdSense, Analytics, file size limit)
│   ├── urls.py
│   └── wsgi.py
├── converter/
│   ├── models.py         ← ConversionJob model
│   ├── views.py          ← Upload, convert, download logic
│   ├── urls.py
│   ├── admin.py
│   └── templates/converter/
│       ├── index.html    ← Main converter page
│       ├── about.html
│       ├── privacy.html
│       ├── terms.html
│       └── contact.html
├── static/               ← Put custom CSS/JS/images here
└── media/
    ├── uploads/          ← Incoming Word files (auto-deleted)
    └── converted/        ← Output PDFs (auto-deleted)
```

---

## 🔧 Customization

| What | Where |
|---|---|
| Max upload size | `settings.py` → `MAX_UPLOAD_SIZE` |
| File deletion delay | `settings.py` → `FILE_DELETION_DELAY` |
| Site name / branding | Each template – search "DocToPDF" |
| Color scheme | `index.html` → `:root` CSS variables |
| AdSense publisher ID | `settings.py` → `GOOGLE_ADSENSE_CLIENT` |
| Analytics ID | `settings.py` → `GOOGLE_ANALYTICS_ID` |

---

## 🛡 Security Notes
- Always set `DEBUG=False` in production
- Use a strong random `SECRET_KEY`
- Restrict `ALLOWED_HOSTS` to your domain
- Use HTTPS (certbot/Let's Encrypt)
- Consider rate-limiting the `/api/upload/` endpoint with django-ratelimit

## 📦 Python Libraries Used
| Library | Purpose |
|---|---|
| Django | Web framework |
| python-docx | Read .docx files |
| reportlab | Generate PDF fallback |
| Pillow | Image processing |
| gunicorn | Production WSGI server |
| whitenoise | Serve static files |

## 🔄 Conversion Quality
| Method | Quality | Requirement |
|---|---|---|
| LibreOffice headless | ⭐⭐⭐⭐⭐ Full fidelity | `apt install libreoffice` |
| python-docx + reportlab | ⭐⭐⭐ Text + basic formatting | Pure Python (auto fallback) |
