from flask import Flask, render_template, request, redirect, url_for, flash, send_file
import os

app = Flask(__name__)
app.secret_key = "change-this-in-production"

# ── Blog posts (replace with a database later) ──────────────────────────────
POSTS = [
    {
        "id": 1,
        "title": "What Is AES Encryption — And Why It Matters",
        "date": "February 12, 2025",
        "category": "Cryptography",
        "summary": "A beginner-friendly breakdown of Advanced Encryption Standard (AES) — how it works, why it's used everywhere, and how I implemented it in my own portfolio app.",
        "body": """
AES (Advanced Encryption Standard) is the gold standard for symmetric encryption. It's used in everything from WhatsApp messages to your bank's servers.

<h3>How It Works</h3>
<p>AES operates on fixed-size blocks of data (128 bits) and uses a key of either 128, 192, or 256 bits. The algorithm performs a series of mathematical transformations — substitution, permutation, mixing — over multiple "rounds" to produce ciphertext that is computationally infeasible to reverse without the key.</p>

<h3>Why I Used It</h3>
<p>When building my portfolio app, I needed to protect stored user data. I implemented AES-256 in CBC mode using Python's <code>cryptography</code> library, paired with a securely generated initialization vector (IV) for each encryption operation to prevent pattern leakage.</p>

<h3>Key Takeaway</h3>
<p>Encryption isn't magic — it's math. Understanding it at the implementation level makes you a far more effective security engineer than just knowing it exists.</p>
        """
    },
    {
        "id": 2,
        "title": "Beginner's Guide to Network Scanning with Nmap",
        "date": "January 5, 2025",
        "category": "Network Security",
        "summary": "Nmap is one of the most powerful tools in a security professional's toolkit. Here's how to use it responsibly for network reconnaissance and vulnerability discovery.",
        "body": """
<p>Nmap (Network Mapper) is an open-source tool for network discovery and security auditing. It's used by penetration testers, sysadmins, and security researchers worldwide.</p>

<h3>Basic Usage</h3>
<p>A simple host discovery scan: <code>nmap -sn 192.168.1.0/24</code></p>
<p>A port scan with service detection: <code>nmap -sV target_ip</code></p>

<h3>What to Look For</h3>
<p>Open ports are potential entry points. Services running outdated versions are prime targets. Nmap's output gives you a roadmap of a network's attack surface.</p>

<h3>Important</h3>
<p>Only ever scan networks you own or have explicit permission to test. Unauthorized scanning is illegal and unethical.</p>
        """
    },
    {
        "id": 3,
        "title": "Why Cybersecurity Awareness Training Fails (And How to Fix It)",
        "date": "November 20, 2024",
        "category": "Security Education",
        "summary": "Most corporate security training is boring, forgettable, and ineffective. Here's what the research says about what actually changes human behavior.",
        "body": """
<p>Studies consistently show that annual compliance-based security training has little measurable impact on employee behavior. People click phishing links at the same rate after training as before.</p>

<h3>The Problem</h3>
<p>Traditional training treats security awareness as a checkbox — a 30-minute video watched once a year. It doesn't account for how humans actually learn and form habits.</p>

<h3>What Works Instead</h3>
<ul>
    <li><strong>Simulated phishing campaigns</strong> — real consequences drive real learning</li>
    <li><strong>Micro-learning</strong> — short, frequent, contextual nudges beat long annual sessions</li>
    <li><strong>Storytelling</strong> — case studies of real breaches stick in memory far better than policy documents</li>
    <li><strong>Positive reinforcement</strong> — reward reporting suspicious emails, don't just punish failures</li>
</ul>

<h3>My Take</h3>
<p>Effective security education is a communications and marketing problem as much as a technical one. The best security teams think like educators, not enforcers.</p>
        """
    },
]

@app.route("/")
def index():
    return render_template("index.html", posts=POSTS[:2])

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/blog")
def blog():
    category = request.args.get("category")
    if category:
        filtered = [p for p in POSTS if p["category"] == category]
    else:
        filtered = POSTS
    categories = sorted(set(p["category"] for p in POSTS))
    return render_template("blog.html", posts=filtered, categories=categories, active=category)

@app.route("/blog/<int:post_id>")
def post(post_id):
    p = next((p for p in POSTS if p["id"] == post_id), None)
    if not p:
        return redirect(url_for("blog"))
    return render_template("post.html", post=p)

@app.route('/fitcheck')
def fitcheck():
    return render_template('fitcheck.html')

@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        name = request.form.get("name", "").strip()
        email = request.form.get("email", "").strip()
        message = request.form.get("message", "").strip()
        if name and email and message:
            # In production: send email via SMTP or save to DB
            flash("Thanks for reaching out! I'll get back to you soon.", "success")
        else:
            flash("Please fill out all fields.", "error")
        return redirect(url_for("contact"))
    return render_template("contact.html")

@app.route("/resume")
def resume():
    # Place your CV PDF at static/resume.pdf
    resume_path = os.path.join(app.static_folder, "resume.pdf")
    if os.path.exists(resume_path):
        return send_file(resume_path, as_attachment=True, download_name="Chloe_McIntosh_CV.pdf")
    flash("Resume file not found. Please add resume.pdf to the static folder.", "error")
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True)
