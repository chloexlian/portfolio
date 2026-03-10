# Chloe McIntosh — Portfolio Website

A clean, corporate Flask portfolio with blog, contact form, and CV download.

## Project Structure

```
portfolio/
├── app.py                  # Flask routes & blog post data
├── requirements.txt
├── static/
│   ├── css/style.css
│   ├── js/main.js
│   └── resume.pdf          ← ADD YOUR CV PDF HERE
└── templates/
    ├── base.html
    ├── index.html
    ├── about.html
    ├── blog.html
    ├── post.html
    └── contact.html
```

## Local Setup

```bash
# 1. Create and activate a virtual environment
python3 -m venv venv
source venv/bin/activate        # Mac/Linux
venv\Scripts\activate           # Windows

# 2. Install dependencies
pip install -r requirements.txt

# 3. Add your resume PDF
cp your-cv.pdf static/resume.pdf

# 4. Run locally
python app.py
# Visit http://localhost:5000
```

## Adding Blog Posts

Open `app.py` and add a new dict to the `POSTS` list:

```python
{
    "id": 4,
    "title": "Your Post Title",
    "date": "March 10, 2025",
    "category": "Network Security",   # or Cryptography, Security Education, etc.
    "summary": "One sentence preview shown on the blog listing page.",
    "body": """
<p>Your post content here. HTML is supported.</p>
<h3>A Subheading</h3>
<p>More content...</p>
    """
},
```

## Deploying to Render (Free)

1. Push this folder to a GitHub repo
2. Go to https://render.com → New → Web Service
3. Connect your GitHub repo
4. Set:
   - **Build Command:** `pip install -r requirements.txt`
   - **Start Command:** `gunicorn app:app`
5. Add `gunicorn` to requirements.txt
6. Deploy — your site will be live at `yourname.onrender.com`

### Add a custom domain (optional, ~$10/yr)
- Buy a domain at https://namecheap.com
- In Render dashboard → Settings → Custom Domains
- Follow the DNS instructions

## Contact Form (Production)

The contact form currently flashes a success message but doesn't send email.
To enable real email sending, add to `app.py`:

```python
import smtplib
from email.mime.text import MIMEText

# In the contact POST route, after validation:
msg = MIMEText(f"From: {name} <{email}>\n\n{message}")
msg['Subject'] = f"Portfolio Contact: {name}"
msg['From'] = 'your@gmail.com'
msg['To'] = 'chloelian8@gmail.com'

with smtplib.SMTP_SSL('smtp.gmail.com', 465) as s:
    s.login('your@gmail.com', 'your-app-password')
    s.send_message(msg)
```

Use a Gmail App Password (not your real password):
Settings → Security → 2FA → App Passwords

## Changing the Secret Key

In `app.py`, replace:
```python
app.secret_key = "change-this-in-production"
```
with a long random string. Generate one with:
```bash
python3 -c "import secrets; print(secrets.token_hex(32))"
```
