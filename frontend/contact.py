import streamlit as st
import streamlit.components.v1 as components
import base64
import os


def get_img_as_base64(file):
    path = os.path.join("frontend", "img", file)
    if os.path.exists(path):
        with open(path, "rb") as f:
            data = f.read()
        return base64.b64encode(data).decode()
    return ""


def contact_page():

    img1 = get_img_as_base64("priynshu.jpg")
    img2 = get_img_as_base64("sunil.jpg")
    img3 = get_img_as_base64("rajeev.jpg")
    img4 = get_img_as_base64("dcmishra.jpg")
    img5 = get_img_as_base64("sameer.jpg")
    img6 = get_img_as_base64("sneha.jpg")

    def avatar(b64, name):
        if b64:
            return f'<img class="ct-avatar" src="data:image/jpeg;base64,{b64}" alt="{name}"/>'
        initials = "".join([w[0].upper() for w in name.split()[:2]])
        return f'<div class="ct-avatar ct-avatar-init">{initials}</div>'

    team = [
        {
            "img": avatar(img1, "Priyanshu Kanojiya"),
            "name": "Priyanshu Kanojiya",
            "role": "Developer & Research Scholar",
            "dept": "M.Sc. Bioinformatics",
            "org": "ICAR-IASRI, New Delhi",
            "email": "priyanshukanojiya143@gmail.com",
            "badge": "Lead Developer",
            "badge_type": "lead",
        },
        {
            "img": avatar(img2, "Dr. Sunil Kumar"),
            "name": "Dr. Sunil Kumar",
            "role": "Principal Scientist",
            "dept": "",
            "org": "ICAR-IASRI, New Delhi",
            "email": "skybiotech@gmail.com",
            "badge": "Principal Scientist",
            "badge_type": "senior",
        },
        {
            "img": avatar(img3, "Dr. Rajeev Ranjan"),
            "name": "Dr. Rajeev Ranjan",
            "role": "Senior Scientist",
            "dept": "",
            "org": "ICAR-IASRI, New Delhi",
            "email": "rajeev.kumar4@icar.gov.in",
            "badge": "Senior Scientist",
            "badge_type": "senior",
        },
        {
            "img": avatar(img4, "Dr. D.C. Mishra"),
            "name": "Dr. D.C. Mishra",
            "role": "Senior Scientist",
            "dept": "",
            "org": "ICAR-IASRI, New Delhi",
            "email": "dwijmishra@gmail.com",
            "badge": "Senior Scientist",
            "badge_type": "senior",
        },
        {
            "img": avatar(img5, "Dr. Mohammad Samir Farooqi"),
            "name": "Dr. Mohammad Samir Farooqi",
            "role": "Principal Scientist",
            "dept": "",
            "org": "ICAR-IASRI, New Delhi",
            "email": "ms.Farooqi@icar.gov.in",
            "badge": "Principal Scientist",
            "badge_type": "senior",
        },
        {
            "img": avatar(img6, "Dr. Sneha Murmu"),
            "name": "Dr. Sneha Murmu",
            "role": "Scientist",
            "dept": "",
            "org": "ICAR-IASRI, New Delhi",
            "email": "murmu.sneha07@gmail.com",
            "badge": "Scientist",
            "badge_type": "scientist",
        },
    ]

    cards_html = ""
    for m in team:
        dept_html = f'<div class="ct-dept">{m["dept"]}</div>' if m["dept"] else ""
        badge_cls = f'ct-badge ct-badge-{m["badge_type"]}'
        cards_html += f"""
        <div class="ct-card">
          {m["img"]}
          <span class="{badge_cls}">{m["badge"]}</span>
          <div class="ct-name">{m["name"]}</div>
          <div class="ct-role">{m["role"]}</div>
          {dept_html}
          <div class="ct-divider"></div>
          <div class="ct-org">
            <svg width="12" height="12" viewBox="0 0 24 24" fill="none"
                 stroke="currentColor" stroke-width="2" stroke-linecap="round"
                 stroke-linejoin="round" style="vertical-align:-1px;margin-right:4px;">
              <path d="M3 9l9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"/>
              <polyline points="9 22 9 12 15 12 15 22"/>
            </svg>
            {m["org"]}
          </div>
          <a class="ct-email" href="mailto:{m["email"]}">
            <svg width="12" height="12" viewBox="0 0 24 24" fill="none"
                 stroke="currentColor" stroke-width="2" stroke-linecap="round"
                 stroke-linejoin="round" style="vertical-align:-1px;margin-right:4px;">
              <path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z"/>
              <polyline points="22,6 12,12 2,6"/>
            </svg>
            {m["email"]}
          </a>
        </div>
        """

    html_content = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
    <meta charset="UTF-8"/>
    <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
    <link href="https://fonts.googleapis.com/css2?family=DM+Serif+Display:ital@0;1&family=DM+Sans:ital,opsz,wght@0,9..40,300;0,9..40,400;0,9..40,500;0,9..40,600;1,9..40,300&display=swap" rel="stylesheet"/>
    <style>
    *, *::before, *::after {{ box-sizing: border-box; margin: 0; padding: 0; }}

    body {{
        font-family: 'DM Sans', sans-serif;
        background: #f5f7f5;
        color: #1a1f2e;
        padding: 8px 16px 40px;
    }}

    .ct-root {{ max-width: 1100px; margin: 0 auto; }}

    /* ── Hero — identical structure to about page ── */
    .ct-hero {{
        background: linear-gradient(135deg, #0b3528 0%, #145c44 50%, #1a7a5a 100%);
        border-radius: 20px;
        padding: 54px 64px 46px;
        margin-bottom: 28px;
        position: relative;
        overflow: hidden;
    }}
    .ct-hero::before {{
        content: '';
        position: absolute;
        top: -70px; right: -70px;
        width: 340px; height: 340px;
        background: rgba(255,255,255,0.04);
        border-radius: 50%;
        pointer-events: none;
    }}
    .ct-hero::after {{
        content: '';
        position: absolute;
        bottom: -90px; left: 32%;
        width: 240px; height: 240px;
        background: rgba(255,255,255,0.03);
        border-radius: 50%;
        pointer-events: none;
    }}
    .ct-hero-badge {{
        display: inline-flex;
        align-items: center;
        gap: 8px;
        background: rgba(255,255,255,0.11);
        border: 1px solid rgba(255,255,255,0.18);
        border-radius: 100px;
        padding: 5px 16px 5px 10px;
        font-size: 11.5px;
        font-weight: 500;
        letter-spacing: 0.7px;
        color: #a8edcc;
        text-transform: uppercase;
        margin-bottom: 18px;
    }}
    .dot {{
        width: 7px; height: 7px;
        background: #4ade80;
        border-radius: 50%;
        display: inline-block;
        animation: pulse 2s ease-in-out infinite;
    }}
    @keyframes pulse {{
        0%, 100% {{ opacity: 1; transform: scale(1); }}
        50%       {{ opacity: 0.45; transform: scale(0.75); }}
    }}
    .ct-hero-title {{
        font-family: 'DM Serif Display', serif;
        font-size: 46px;
        font-weight: 400;
        color: #fff;
        line-height: 1.12;
        margin-bottom: 4px;
        letter-spacing: -0.5px;
    }}
    .ct-hero-title em {{
        font-style: italic;
        color: #7ce8b5;
    }}
    .ct-hero-subtitle {{
        font-size: 17px;
        font-weight: 300;
        color: rgba(255,255,255,0.65);
        margin-top: 2px;
    }}
    .ct-hero-desc {{
        font-size: 15px;
        font-weight: 300;
        color: rgba(255,255,255,0.68);
        line-height: 1.7;
        max-width: 580px;
        margin-top: 16px;
    }}

    /* ── Stats strip — same as about ── */
    .ct-stats {{
        display: grid;
        grid-template-columns: repeat(3, 1fr);
        gap: 14px;
        margin-bottom: 28px;
    }}
    .ct-stat {{
        background: #ffffff;
        border: 1px solid #dde8e2;
        border-radius: 14px;
        padding: 20px 16px 16px;
        text-align: center;
    }}
    .ct-stat-icon {{ font-size: 22px; display: block; margin-bottom: 8px; }}
    .ct-stat-value {{
        font-family: 'DM Serif Display', serif;
        font-size: 28px;
        color: #0b3528;
        line-height: 1;
        margin-bottom: 5px;
    }}
    .ct-stat-label {{
        font-size: 11.5px;
        font-weight: 500;
        color: #6b8c7a;
        letter-spacing: 0.3px;
        text-transform: uppercase;
    }}

    /* ── Section heading — identical to about ── */
    .ct-sh {{
        display: flex;
        align-items: center;
        gap: 10px;
        font-size: 11px;
        font-weight: 600;
        letter-spacing: 1.5px;
        text-transform: uppercase;
        color: #1e6840;
        margin-bottom: 16px;
    }}
    .ct-sh::after {{
        content: '';
        flex: 1;
        height: 1px;
        background: #d4e5db;
    }}

    /* ── Team grid ── */
    .ct-grid {{
        display: grid;
        grid-template-columns: repeat(3, 1fr);
        gap: 18px;
        margin-bottom: 28px;
    }}

    /* ── Team card ── */
    .ct-card {{
        background: #ffffff;
        border: 1px solid #dde8e2;
        border-radius: 16px;
        padding: 28px 20px 22px;
        display: flex;
        flex-direction: column;
        align-items: center;
        text-align: center;
        transition: box-shadow 0.2s ease, transform 0.2s ease;
    }}
    .ct-card:hover {{
        box-shadow: 0 8px 28px rgba(14, 80, 55, 0.1);
        transform: translateY(-3px);
    }}

    /* Avatar — photo */
    img.ct-avatar {{
        width: 96px; height: 96px;
        border-radius: 50%;
        object-fit: cover;
        border: 3px solid #b8dcc9;
        margin-bottom: 14px;
        display: block;
    }}
    /* Avatar — initials fallback */
    div.ct-avatar {{
        width: 96px; height: 96px;
        border-radius: 50%;
        background: linear-gradient(135deg, #145c44, #1a7a5a);
        border: 3px solid #b8dcc9;
        display: flex; align-items: center; justify-content: center;
        font-family: 'DM Serif Display', serif;
        font-size: 26px;
        color: #d4f5e4;
        margin-bottom: 14px;
        flex-shrink: 0;
    }}

    /* Badge */
    .ct-badge {{
        display: inline-block;
        font-size: 10.5px;
        font-weight: 600;
        letter-spacing: 0.5px;
        text-transform: uppercase;
        padding: 3px 10px;
        border-radius: 100px;
        margin-bottom: 10px;
    }}
    .ct-badge-lead {{
        background: #0b3528;
        color: #7ce8b5;
    }}
    .ct-badge-senior {{
        background: #e6f4ed;
        color: #1a6b40;
        border: 1px solid #bdd8c9;
    }}
    .ct-badge-scientist {{
        background: #eef7f2;
        color: #2e7d55;
        border: 1px solid #c8e4d4;
    }}

    .ct-name {{
        font-size: 15px;
        font-weight: 600;
        color: #1a1f2e;
        margin-bottom: 3px;
        line-height: 1.3;
    }}
    .ct-role {{
        font-size: 13px;
        color: #4a6858;
        font-weight: 500;
        margin-bottom: 2px;
    }}
    .ct-dept {{
        font-size: 12px;
        color: #7a9488;
        margin-bottom: 2px;
    }}
    .ct-divider {{
        width: 36px;
        height: 1px;
        background: #d4e5db;
        margin: 12px auto;
    }}
    .ct-org {{
        font-size: 12.5px;
        color: #5a7468;
        margin-bottom: 8px;
    }}
    .ct-email {{
        font-size: 12px;
        color: #1a6b40;
        text-decoration: none;
        font-weight: 500;
        word-break: break-all;
        line-height: 1.5;
    }}
    .ct-email:hover {{ text-decoration: underline; }}

    /* ── Info banner ── */
    .ct-info {{
        background: linear-gradient(135deg, #eef8f2 0%, #e1f2e9 100%);
        border: 1px solid #bdd8c9;
        border-radius: 16px;
        padding: 24px 28px;
        margin-bottom: 28px;
        font-size: 14px;
        color: #2d6648;
        line-height: 1.75;
    }}
    .ct-info strong {{ color: #0b3528; }}

    /* ── Footer — identical to about ── */
    .ct-footer {{
        border-top: 1px solid #d4e5db;
        padding-top: 18px;
        display: flex;
        align-items: center;
        justify-content: space-between;
        flex-wrap: wrap;
        gap: 10px;
    }}
    .ct-footer-copy {{ font-size: 12.5px; color: #8fa89a; }}
    .ct-footer-tag {{
        font-size: 11.5px;
        background: #e6f4ed;
        color: #1a6b40;
        font-weight: 600;
        padding: 4px 14px;
        border-radius: 100px;
    }}

    @media (max-width: 840px) {{
        .ct-grid  {{ grid-template-columns: 1fr 1fr; }}
        .ct-stats {{ grid-template-columns: 1fr 1fr 1fr; }}
        .ct-hero  {{ padding: 34px 24px 28px; }}
        .ct-hero-title {{ font-size: 34px; }}
    }}
    @media (max-width: 560px) {{
        .ct-grid  {{ grid-template-columns: 1fr; }}
        .ct-stats {{ grid-template-columns: 1fr 1fr; }}
    }}
    </style>
    </head>
    <body>
    <div class="ct-root">

      <!-- HERO -->
      <div class="ct-hero">
        <div class="ct-hero-badge">
          <span class="dot"></span>
          Research Team · ICAR-IASRI, New Delhi
        </div>
        <div class="ct-hero-title">Meet the <em>Team</em></div>
        <div class="ct-hero-subtitle">The minds behind AntiDiaNet</div>
        <p class="ct-hero-desc">
          A multidisciplinary team of scientists and bioinformaticians from ICAR-IASRI,
          New Delhi, dedicated to advancing computational approaches in agricultural
          and biomedical research.
        </p>
      </div>

      <!-- STATS -->
      <div class="ct-stats">
        <div class="ct-stat">
          <span class="ct-stat-icon">👩‍🔬</span>
          <div class="ct-stat-value">6</div>
          <div class="ct-stat-label">Team Members</div>
        </div>
        <div class="ct-stat">
          <span class="ct-stat-icon">🏛️</span>
          <div class="ct-stat-value">ICAR</div>
          <div class="ct-stat-label">IASRI, New Delhi</div>
        </div>
        <div class="ct-stat">
          <span class="ct-stat-icon">🌿</span>
          <div class="ct-stat-value">Bio</div>
          <div class="ct-stat-label">Informatics Focus</div>
        </div>
      </div>

      <!-- TEAM GRID -->
      <div class="ct-sh">Research Team</div>
      <div class="ct-grid">
        {cards_html}
      </div>

      <!-- INFO BANNER -->
      <div class="ct-sh">Get in Touch</div>
      <div class="ct-info">
        For queries related to <strong>AntiDiaNet</strong>, collaboration opportunities,
        or research partnerships, please reach out directly to any team member via their
        institutional email address listed above. For general correspondence, contact
        <strong>ICAR-IASRI, Pusa Campus, New Delhi – 110012</strong>.
      </div>

      <!-- FOOTER -->
      <div class="ct-footer">
        <span class="ct-footer-copy">AntiDiaNet · ICAR-IASRI, New Delhi</span>
        <span class="ct-footer-tag">For Research Use Only</span>
      </div>

    </div>
    </body>
    </html>
    """

    components.html(html_content, height=1420, scrolling=False)


if __name__ == "__main__":
    contact_page()