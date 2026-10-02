#!/usr/bin/env python3
"""TRL site builder — writes static HTML pages into this folder.
Edit PRICES / CONTACT below, then run:  python3 tools/build.py
Pages are plain HTML afterwards — GitHub Pages serves them directly."""
from urllib.parse import quote
import json, datetime, pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
SITE = "https://therightlifestyle.github.io/TheRightLifestyle/"

# ── single source of truth (matches 00_MEMORY.md §4) ─────────────────
PHONE_DISPLAY = "+92 319 0091457"
WA = "923190091457"
EMAIL = "officialtrlservice@gmail.com"
EASYPAISA_NAME = "Rashid Muhammad Amir"
AUDIT, AUDIT_AFTER, AUDIT_REF = "1,500", "3,000", "10,000"
BUILD, BUILD_AFTER, BUILD_REF = "15,000", "25,000", "50,000"
CARE = "3,000–5,000"
FOUNDING_SLOTS = 50
CREDIT_DAYS = 14
HOURS = "Every day, 10am–10pm PKT"
IG = "https://www.instagram.com/the.right.lifestyle/"
TT = "https://www.tiktok.com/@the.right.lifestyle"

def wa(text):
    return f"https://wa.me/{WA}?text={quote(text)}"

WA_HI = wa("Assalam o Alaikum Rashid, I found TRL online. I'd like to talk about my business.")
WA_AUDIT = wa(f"Hi Rashid, I'd like to book the TRL Systems Audit (PKR {AUDIT} founding price). My business is: ")
WA_BUILD = wa(f"Hi Rashid, I'm interested in a TRL System Build (PKR {BUILD} founding price). My business is: ")
WA_CARE = wa("Hi Rashid, please add me to the TRL Care Plan waitlist. My business is: ")

WA_SVG = '<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M17.5 14.4c-.3-.1-1.8-.9-2-1-.3-.1-.5-.1-.7.1-.2.3-.8 1-.9 1.2-.2.2-.3.2-.6.1-.3-.1-1.3-.5-2.4-1.5-.9-.8-1.5-1.8-1.7-2.1-.2-.3 0-.5.1-.6l.4-.5c.2-.2.2-.3.3-.5.1-.2 0-.4 0-.5l-.9-2.2c-.2-.6-.5-.5-.7-.5h-.6c-.2 0-.5.1-.8.4-.3.3-1 1-1 2.5s1.1 2.9 1.2 3.1c.1.2 2.1 3.2 5.1 4.5.7.3 1.3.5 1.7.6.7.2 1.4.2 1.9.1.6-.1 1.8-.7 2-1.4.2-.7.2-1.3.2-1.4-.1-.2-.3-.3-.6-.4zM12 2a10 10 0 0 0-8.6 15.1L2 22l5-1.3A10 10 0 1 0 12 2zm0 18.2c-1.5 0-3-.4-4.3-1.2l-.3-.2-3 .8.8-2.9-.2-.3A8.2 8.2 0 1 1 12 20.2z"/></svg>'

NAV = [("index.html", "Home"), ("services.html", "Services"), ("who-we-help.html", "Who we help"),
       ("pricing.html", "Pricing"), ("how-it-works.html", "How it works"), ("about.html", "About"),
       ("faq.html", "FAQ"), ("contact.html", "Contact")]

def page(fname, title, desc, body, canonical=None):
    url = SITE + ("" if fname == "index.html" else fname)
    menu = "".join(
        f'<a href="{h}"{" aria-current=\"page\"" if h == fname else ""}>{t}</a>' for h, t in NAV if h != "index.html")
    ld = {"@context": "https://schema.org", "@type": "ProfessionalService", "name": "TRL — The Right Lifestyle",
          "alternateName": "TRL", "url": SITE, "email": EMAIL, "telephone": PHONE_DISPLAY.replace(" ", ""),
          "founder": {"@type": "Person", "name": "Rashid Muhammad Amir"},
          "address": {"@type": "PostalAddress", "addressLocality": "Rawalpindi", "addressRegion": "Punjab", "addressCountry": "PK"},
          "areaServed": "PK", "sameAs": [IG, TT], "openingHours": "Mo-Su 10:00-22:00", "priceRange": f"PKR {AUDIT}–{BUILD_AFTER}+",
          "description": "Systems audits and automation for online and local businesses in Pakistan."}
    full_title = title if fname == "index.html" else f"{title} · TRL — The Right Lifestyle"
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<title>{full_title}</title>
<meta name="description" content="{desc}">
<meta name="robots" content="index,follow,max-image-preview:large">
<meta name="referrer" content="strict-origin-when-cross-origin">
<meta name="theme-color" content="#f5f7fc">
<link rel="canonical" href="{url}">
<link rel="icon" href="assets/img/favicon.svg" type="image/svg+xml"><link rel="apple-touch-icon" href="assets/img/icon-192.png"><link rel="manifest" href="manifest.webmanifest">
<meta property="og:type" content="website"><meta property="og:site_name" content="TRL — The Right Lifestyle"><meta property="og:locale" content="en_PK">
<meta property="og:title" content="{full_title}"><meta property="og:description" content="{desc}"><meta property="og:url" content="{url}">
<meta property="og:image" content="{SITE}assets/img/og-image.png"><meta property="og:image:width" content="1200"><meta property="og:image:height" content="630">
<meta name="twitter:card" content="summary_large_image"><meta name="twitter:image" content="{SITE}assets/img/og-image.png">
<link rel="preload" href="assets/fonts/instrument-sans-latin.woff2" as="font" type="font/woff2" crossorigin>
<link rel="preload" href="assets/fonts/sora-700.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="assets/css/style.css">
<script type="application/ld+json">{json.dumps(ld)}</script>
<!-- ANALYTICS SLOT (P3): paste GA4 + Microsoft Clarity snippets here when IDs exist -->
</head>
<body>
<a class="skip" href="#main">Skip to content</a>
<header class="nav">
 <div class="wrap">
  <a class="brand" href="index.html" aria-label="TRL home"><img src="assets/img/favicon.svg" alt="" width="36" height="36"><span><b>The Right Lifestyle</b><small>TRL · Systems &amp; automation</small></span></a>
  <nav class="menu" id="menu" aria-label="Main">{menu}<a class="btn btn-wa" href="{WA_AUDIT}" target="_blank" rel="noopener">{WA_SVG} Book audit · PKR {AUDIT}</a></nav>
  <a class="btn btn-p nav-cta" href="{WA_AUDIT}" target="_blank" rel="noopener">Book audit · PKR {AUDIT}</a>
  <button class="burger" aria-label="Open menu" aria-expanded="false" aria-controls="menu"><span></span></button>
 </div>
</header>
<main id="main">
{body}
</main>
<footer class="foot on-dark">
 <div class="wrap">
  <div class="foot-grid">
   <div>
    <a class="brand" href="index.html"><img src="assets/img/favicon.svg" alt="" width="36" height="36"><span><b>The Right Lifestyle</b><small>TRL · Rawalpindi, Pakistan</small></span></a>
    <p class="mt1" style="max-width:340px;font-size:.95rem">We find the repetitive work in your business and build systems that do it for you. You run the business, the system handles the routine.</p>
    <p class="mt1" style="font-size:.95rem"><i>Kaam aap ka, system hamara.</i></p>
   </div>
   <div><h4>Company</h4><ul><li><a href="about.html">About Rashid</a></li><li><a href="how-it-works.html">How it works</a></li><li><a href="who-we-help.html">Who we help</a></li><li><a href="faq.html">FAQ</a></li></ul></div>
   <div><h4>Offers</h4><ul><li><a href="pricing.html#audit">Systems Audit · PKR {AUDIT}</a></li><li><a href="pricing.html#build">System Build · PKR {BUILD}</a></li><li><a href="pricing.html#care">Care Plan · coming soon</a></li><li><a href="services.html">All services</a></li></ul></div>
   <div><h4>Contact</h4><ul><li><a href="{WA_HI}" target="_blank" rel="noopener">WhatsApp {PHONE_DISPLAY}</a></li><li><a href="mailto:{EMAIL}">{EMAIL}</a></li><li><a href="contact.html">Contact form</a></li><li><a href="{IG}" target="_blank" rel="noopener">Instagram</a> · <a href="{TT}" target="_blank" rel="noopener">TikTok</a></li><li style="color:var(--text3);font-size:.9rem">{HOURS}</li></ul></div>
  </div>
  <div class="foot-b"><span>© <span id="yr">{datetime.date.today().year}</span> TRL — The Right Lifestyle · Founder: Rashid Muhammad Amir · Rawalpindi, Pakistan</span><span><a href="privacy.html">Privacy</a> · <a href="terms.html">Terms</a></span></div>
 </div>
</footer>
<a class="fab" href="{WA_HI}" target="_blank" rel="noopener" aria-label="Chat with TRL on WhatsApp">{WA_SVG}</a>
<script src="assets/js/main.js" defer></script>
</body>
</html>
"""

def cta(h="Find out where your time is going.", p=None):
    p = p or f"Book the PKR {AUDIT} Systems Audit. You get a written map of your business and a 30-minute walkthrough call, and the full fee is credited if you build with us within {CREDIT_DAYS} days."
    return f"""<section class="sec"><div class="wrap"><div class="cta on-dark rv">
<h2>{h}</h2><p>{p}</p>
<div class="btns"><a class="btn btn-wa" href="{WA_AUDIT}" target="_blank" rel="noopener">{WA_SVG} Book on WhatsApp</a><a class="btn btn-g" href="pricing.html">See pricing</a></div>
</div></div></section>"""

def phero(eyebrow, h1, lead):
    return f'<section class="phero"><div class="wrap"><span class="eyebrow">{eyebrow}</span><h1>{h1}</h1><p class="lead">{lead}</p></div></section>'

AUDIT_CHECKS = f"""<li>A <b>systems map PDF</b>: how work flows through your business today</li>
<li>Where time, leads and money are being lost, ranked by impact</li>
<li>What to automate first, what to leave alone, and what it costs</li>
<li><b>30-min walkthrough call</b> on Google Meet, recorded for you</li>
<li>Delivered within 48 hours of your intake</li>
<li>Full PKR {AUDIT} <b>credited to your build</b> within {CREDIT_DAYS} days</li>"""

def audit_card(extra=""):
    return f"""<div class="offer rv"{extra}>
<span class="tag">Start here · Founding price</span>
<h3>TRL Systems Audit</h3>
<p>See exactly what's eating your time before you spend money on any tool.</p>
<div class="price"><b>PKR {AUDIT}</b><s>PKR {AUDIT_REF}</s><span>one-time</span></div>
<p class="muted">For the first {FOUNDING_SLOTS} clients · PKR {AUDIT_AFTER} after that</p>
<ul class="checks">{AUDIT_CHECKS}</ul>
<a class="btn btn-wa" href="{WA_AUDIT}" target="_blank" rel="noopener">{WA_SVG} Book the audit on WhatsApp</a>
<div class="meter">Founding slots: {FOUNDING_SLOTS} available<div class="bar"><i></i></div></div>
</div>"""

def ic(path):
    return f'<div class="ic"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{path}</svg></div>'

I = {
 "chat": '<path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"/>',
 "bolt": '<path d="M13 2 3 14h9l-1 8 10-12h-9z"/>',
 "link": '<path d="M10 13a5 5 0 0 0 7.5.5l3-3a5 5 0 0 0-7-7l-1.7 1.7"/><path d="M14 11a5 5 0 0 0-7.5-.5l-3 3a5 5 0 0 0 7 7l1.7-1.7"/>',
 "bot": '<rect x="3" y="8" width="18" height="12" rx="3"/><path d="M12 8V4M8 14h.01M16 14h.01"/>',
 "chart": '<path d="M3 3v18h18"/><path d="m7 15 4-4 3 3 5-6"/>',
 "map": '<path d="M9 3 3 6v15l6-3 6 3 6-3V3l-6 3z"/><path d="M9 3v15M15 6v15"/>',
 "box": '<path d="M21 8 12 3 3 8v8l9 5 9-5z"/><path d="m3 8 9 5 9-5M12 13v8"/>',
 "cal": '<rect x="3" y="4" width="18" height="18" rx="2"/><path d="M16 2v4M8 2v4M3 10h18"/>',
 "doc": '<path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><path d="M14 2v6h6M8 13h8M8 17h5"/>',
 "user": '<circle cx="12" cy="8" r="4"/><path d="M4 21a8 8 0 0 1 16 0"/>',
 "shield": '<path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/><path d="m9 12 2 2 4-4"/>',
 "clock": '<circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/>',
 "mail": '<rect x="2" y="4" width="20" height="16" rx="2"/><path d="m22 6-10 7L2 6"/>',
 "cart": '<circle cx="9" cy="21" r="1"/><circle cx="20" cy="21" r="1"/><path d="M1 1h4l2.7 13.4a2 2 0 0 0 2 1.6h9.7a2 2 0 0 0 2-1.6L23 6H6"/>',
 "store": '<path d="M3 9 4.5 3h15L21 9M3 9v12h18V9M3 9h18M9 21v-6h6v6"/>',
 "wallet": '<rect x="2" y="6" width="20" height="14" rx="2"/><path d="M16 13h.01M2 10h20"/>',
}

# ── HOME ─────────────────────────────────────────────────────────────
TAGS = ["WhatsApp automation", "Order & booking flows", "Lead follow-up", "AI replies in Urdu & English", "Google Sheets systems",
        "Daraz & e-commerce ops", "Invoices & reminders", "Reporting dashboards", "n8n workflows", "Course & academy admin"]
home = f"""
<section class="hero"><div class="wrap hero-grid">
 <div>
  <span class="pill"><i></i>Founder-led · Rawalpindi · Founding clients open now</span>
  <h1>Get your time back from <span class="grad">repetitive work.</span></h1>
  <p class="lead">TRL finds the repetitive work in your business, from WhatsApp replies and orders to follow-ups, bookings and reports, and builds systems that handle it for you. For online and local businesses, product or service, across Pakistan.</p>
  <div class="btns"><a class="btn btn-wa" href="{WA_AUDIT}" target="_blank" rel="noopener">{WA_SVG} Book the PKR {AUDIT} audit</a><a class="btn btn-g" href="how-it-works.html">How it works →</a></div>
  <ul class="ticks"><li>Fixed price, in writing</li><li>Delivered in 48 hours</li><li>You own everything</li></ul>
  <p class="ur">Roz ka same kaam? System bana dete hain.</p>
 </div>
 {audit_card()}
</div></section>

<div class="strip" aria-hidden="true"><div class="track">{"".join(f"<span>{t}</span>" for t in TAGS*2)}</div></div>

<section class="sec"><div class="wrap">
 <div class="head rv"><span class="eyebrow">Sound familiar?</span><h2>Your business runs, but only when you're running it.</h2><p>Most owners don't need an "AI strategy". They need the same daily tasks to stop landing on them.</p></div>
 <div class="g3">
  <div class="card rv">{ic(I['chat'])}<h3>Messages pile up</h3><p>"Price kya hai?" fifty times a day across WhatsApp, Instagram and calls. Late replies mean lost orders.</p></div>
  <div class="card rv">{ic(I['clock'])}<h3>Same tasks, every day</h3><p>Copying orders into sheets, sending reminders, chasing payments, confirming bookings, all by hand.</p></div>
  <div class="card rv">{ic(I['link'])}<h3>Tools don't talk</h3><p>A sheet here, a WhatsApp group there, a notebook for the rest. Information gets lost between them.</p></div>
  <div class="card rv">{ic(I['user'])}<h3>Customers go cold</h3><p>People ask, then disappear. Nobody follows up, because nobody has the time.</p></div>
  <div class="card rv">{ic(I['chart'])}<h3>No clear numbers</h3><p>You're busy, but which product, channel or service actually makes money? Nobody knows for sure.</p></div>
  <div class="card rv">{ic(I['bolt'])}<h3>You are the bottleneck</h3><p>Nothing moves unless you touch it. Taking a day off feels impossible.</p></div>
 </div>
</div></section>

<section class="sec alt"><div class="wrap">
 <div class="head c rv"><span class="eyebrow">Who we help</span><h2>Online or on the ground. Product or service.</h2><p>If your business repeats the same work every day, a system can take that work off you.</p></div>
 <div class="split">
  <div class="aud card rv">{ic(I['cart'])}<h3>Online &amp; digital businesses</h3><p>Pakistan-wide, fully remote.</p>
   <ul><li><span><b>E-commerce &amp; Daraz sellers:</b> order confirmations, COD follow-up, stock alerts</span></li><li><span><b>Coaches &amp; online academies:</b> enrolments, fee reminders, class links</span></li><li><span><b>Agencies &amp; freelancers:</b> client intake, reporting, invoicing</span></li><li><span><b>Content creators &amp; digital products:</b> DMs, deliveries, leads</span></li></ul></div>
  <div class="aud card rv">{ic(I['store'])}<h3>Local &amp; physical businesses</h3><p>Rawalpindi &amp; Islamabad in person, rest of Pakistan online.</p>
   <ul><li><span><b>Shops, boutiques &amp; showrooms:</b> WhatsApp catalogue, orders, khata</span></li><li><span><b>Clinics, salons &amp; gyms:</b> bookings, reminders, no-show follow-up</span></li><li><span><b>Restaurants &amp; home kitchens:</b> orders, delivery updates</span></li><li><span><b>Schools, real estate &amp; services:</b> enquiries, fees, site visits</span></li></ul></div>
 </div>
 <p class="center mt2"><a class="link" href="who-we-help.html">See examples by business type →</a></p>
</div></section>

<section class="sec"><div class="wrap">
 <div class="head rv"><span class="eyebrow">What we build</span><h2>Systems, not software subscriptions.</h2><p>Built on tools you already use, mainly WhatsApp, Google Sheets, n8n and AI, so there's nothing new for your team to learn.</p></div>
 <div class="g3">
  <a class="card rv" href="services.html#whatsapp">{ic(I['chat'])}<h3>WhatsApp automation</h3><p>Instant replies, price lists, order capture and handover to you when a human is needed.</p><div class="flow">Message → reply → order → you</div></a>
  <a class="card rv" href="services.html#ops">{ic(I['bolt'])}<h3>Order &amp; booking flows</h3><p>Orders and appointments logged, confirmed and reminded automatically.</p><div class="flow">Order → sheet → confirm → remind</div></a>
  <a class="card rv" href="services.html#followup">{ic(I['user'])}<h3>Lead follow-up</h3><p>Every enquiry logged and followed up on schedule until they buy or say no.</p><div class="flow">Enquiry → log → day 1, 3, 7</div></a>
  <a class="card rv" href="services.html#ai">{ic(I['bot'])}<h3>AI assistants</h3><p>Trained on your products, prices and tone, in English and Roman Urdu.</p></a>
  <a class="card rv" href="services.html#reports">{ic(I['chart'])}<h3>Reports &amp; dashboards</h3><p>Sales, orders and response times sent to your phone every week.</p></a>
  <a class="card rv" href="services.html#admin">{ic(I['doc'])}<h3>Admin on autopilot</h3><p>Invoices, payment reminders, receipts and documents generated for you.</p></a>
 </div>
</div></section>

<section class="sec alt"><div class="wrap">
 <div class="head c rv"><span class="eyebrow">How it works</span><h2>Four steps. No guesswork.</h2></div>
 <div class="steps">
  <div class="step rv"><h3>Audit</h3><p>A short intake about how your business runs. We map the work and find what's wasting your time.</p><span class="when">PKR {AUDIT} · 48 hours</span></div>
  <div class="step rv"><h3>Walkthrough</h3><p>A 30-minute recorded call where we go through your systems map and your top fixes.</p><span class="when">30 min · Google Meet</span></div>
  <div class="step rv"><h3>Build</h3><p>We build the #1 system on your real workflow. You test it before customers ever see it.</p><span class="when">PKR {BUILD} · fixed scope</span></div>
  <div class="step rv"><h3>Hand over</h3><p>A guide, full access and training for your team. It's yours, with no lock-in.</p><span class="when">You own it</span></div>
 </div>
</div></section>

<section class="sec"><div class="wrap">
 <div class="head c rv"><span class="eyebrow">Pricing</span><h2>Simple prices. Shown upfront.</h2><p>Founding prices are for our first {FOUNDING_SLOTS} clients. After that they go up.</p></div>
 <div class="g3">
  <div class="card rv"><span class="num">STEP 1</span><h3>Systems Audit</h3><div class="price"><b>PKR {AUDIT}</b><s>{AUDIT_REF}</s></div><p>Systems map PDF + 30-min walkthrough call.</p></div>
  <div class="card rv"><span class="num">STEP 2</span><h3>System Build</h3><div class="price"><b>PKR {BUILD}</b><s>{BUILD_REF}</s></div><p>Your #1 system built, tested and handed over. Audit fee credited.</p></div>
  <div class="card rv"><span class="num">STEP 3 · SOON</span><h3>Care Plan</h3><div class="price"><b>PKR {CARE}</b><span>/month</span></div><p>Monitoring, fixes and small changes after launch. Optional.</p></div>
 </div>
 <p class="center mt2"><a class="btn btn-g" href="pricing.html">Full pricing &amp; what's included →</a></p>
</div></section>

<section class="sec alt"><div class="wrap">
 <div class="head c rv"><span class="eyebrow">Our promises</span><h2>Honest by default.</h2></div>
 <div class="g4">
  <div class="card rv">{ic(I['doc'])}<h3>Written scope</h3><p>What, when and how much, agreed in writing before any work starts.</p></div>
  <div class="card rv">{ic(I['shield'])}<h3>Your data stays yours</h3><p>Access through your own accounts. Passwords never go in chats or files.</p></div>
  <div class="card rv">{ic(I['user'])}<h3>One accountable person</h3><p>You deal with the founder from the first message to handover.</p></div>
  <div class="card rv">{ic(I['box'])}<h3>No lock-in</h3><p>You own the system, the accounts and the documentation.</p></div>
 </div>
 <p class="center muted mt2">We're new, and we won't show fake reviews or made-up numbers. Real client results will go here once they're delivered.</p>
</div></section>
{cta()}
"""

# ── SERVICES ─────────────────────────────────────────────────────────
def svc(id_, icon, title, p, items, eg):
    return f"""<div class="card rv" id="{id_}">{ic(I[icon])}<h3>{title}</h3><p>{p}</p><ul class="chips">{"".join(f"<li>{x}</li>" for x in items)}</ul><div class="flow">{eg}</div></div>"""
services = phero("Services", "Everything we automate, in plain language.",
  "Every engagement starts with the audit, so we build the thing that saves you the most time first, not the thing that sounds impressive.") + f"""
<section class="sec" style="padding-top:1rem"><div class="wrap"><div class="g2">
{svc("whatsapp","chat","WhatsApp Business automation","Your busiest channel, organised. Instant first replies, catalogue and price answers, order capture, and a clean handover to you.",["Greeting & away replies","Quick-reply libraries","Catalogue & price bot","Labels & routing","Broadcast follow-ups"],"Customer msg → auto reply → order logged → you notified")}
{svc("ops","cart","Orders, bookings & delivery flows","For product sellers and service providers alike. Every order or appointment captured, confirmed and tracked without retyping.",["Order → Google Sheet","COD confirmation","Appointment booking","Reminders & no-show follow-up","Courier status updates"],"Order → confirm on WhatsApp → sheet → dispatch alert")}
{svc("followup","user","Lead capture & follow-up","Enquiries from WhatsApp, Instagram, Facebook, forms and calls go into one list and get followed up on schedule.",["One lead list","Auto follow-up day 1/3/7","Lost-lead reasons","Simple CRM setup"],"Enquiry → lead list → follow-ups → won / lost")}
{svc("ai","bot","AI assistants (Urdu + English)","Assistants trained on your products, prices, policies and tone. They answer routine questions and hand over anything sensitive to a human.",["FAQ & product answers","Roman Urdu replies","Lead qualification","Internal team assistant"],"Question → AI answer → human if needed")}
{svc("reports","chart","Reports & dashboards","Know your numbers without opening five apps. Weekly summaries go to your phone automatically.",["Sales & orders summary","Response-time tracking","Top products / services","Weekly WhatsApp report"],"Data → sheet → weekly report on your phone")}
{svc("admin","doc","Admin & money tasks","The paperwork that eats your evenings: invoices, receipts, payment reminders and record-keeping.",["Auto invoices & receipts","Payment reminders","Easypaisa / JazzCash records","Document templates"],"Payment in → receipt sent → ledger updated")}
{svc("academy","cal","Courses, academies & coaching","Enrolments, fee reminders, class links, attendance and student questions handled for you.",["Enrolment forms","Fee reminders","Class & batch links","Student FAQ assistant"],"Form → enrolled → reminders → class link")}
{svc("integrations","link","Connecting your tools","Sheets, WhatsApp, email, calendars, forms and stores connected through n8n so data moves by itself.",["n8n workflows","Google Workspace","Forms (Tally / Google)","Webhooks & APIs"],"App A → n8n → App B (no copy-paste)")}
</div>
<div class="note rv">{ic(I['shield'])}<div><b>What we don't do:</b> we don't sell you tools you don't need, run spam or bulk unsolicited messages, or touch your passwords in chats. If automation won't help your business, the audit will say so.</div></div>
</div></section>
{cta("Not sure which one you need?", f"That's what the audit is for. PKR {AUDIT}, delivered in 48 hours, and the fee is credited to your build.")}
"""

# ── WHO WE HELP ──────────────────────────────────────────────────────
def who(icon, t, tasks, sys):
    return f"""<div class="card hov rv">{ic(I[icon])}<h3>{t}</h3><p><b style="color:var(--text)">Daily drain:</b> {tasks}</p><div class="flow">{sys}</div></div>"""
whop = phero("Who we help", "Built for every business that repeats itself.",
  "Physical or digital, products or services, solo or with a team. If the same work happens every day, it can be systemised.") + f"""
<section class="sec" style="padding-top:1rem"><div class="wrap">
<div class="head rv"><span class="eyebrow">Online &amp; digital · Pakistan-wide</span><h2>Online businesses</h2></div>
<div class="g3">
{who("cart","E-commerce & Daraz sellers","order confirmations, COD calls, stock questions, returns.","Order → WhatsApp confirm → sheet → courier")}
{who("cal","Coaches & online academies","enrolments, fee chasing, sending class links, repeat questions.","Enrol form → fee reminder → class link")}
{who("chart","Agencies & freelancers","client onboarding, monthly reports, invoices.","Client form → task list → monthly report")}
{who("chat","Content creators & digital products","DMs, product delivery, collabs, lead tracking.","DM → auto reply → payment → delivery")}
{who("box","Dropshippers & resellers","supplier updates, order relays, price changes.","Order → supplier alert → tracking to buyer")}
{who("doc","Online service providers","consultants, designers, tutors: bookings, invoices, follow-ups.","Enquiry → booking → invoice → follow-up")}
</div>
<div class="head rv mt3"><span class="eyebrow">Local &amp; physical · Rawalpindi / Islamabad + online</span><h2>Local businesses</h2></div>
<div class="g3">
{who("store","Shops, boutiques & showrooms","price questions, WhatsApp orders, khata, stock.","Catalogue bot → order → khata sheet")}
{who("clock","Clinics, salons & gyms","appointments, reminders, no-shows, memberships.","Booking → reminder → follow-up → review ask")}
{who("box","Restaurants & home kitchens","WhatsApp orders, delivery updates, daily sales.","Order → kitchen sheet → rider → daily total")}
{who("user","Schools & tuition centres","admissions enquiries, fee reminders, parent updates.","Enquiry → visit booked → fee reminders")}
{who("map","Real estate & property","lead tracking, site visits, follow-ups.","Lead → qualify → visit → follow-up")}
{who("wallet","Trades & home services","electricians, AC, cleaning, repairs: job bookings and payments.","Call/msg → job logged → reminder → payment")}
</div>
<p class="center muted mt2">Not on the list? Message us anyway. We'll tell you honestly whether a system would help.</p>
</div></section>
{cta()}
"""

# ── PRICING ──────────────────────────────────────────────────────────
pricing = phero("Pricing", "Clear prices in PKR. No surprises.",
  f"Start small with the audit. Build only what's worth building. Founding prices apply to our first {FOUNDING_SLOTS} clients.") + f"""
<section class="sec" style="padding-top:2rem"><div class="wrap">
<div class="plans">
 <div class="plan hot rv" id="audit"><span class="badge">Start here</span><span class="kicker">Step 1</span><h3>Systems Audit</h3><p>See exactly where your time and money go, before spending on any tool.</p>
  <div class="price"><b>PKR {AUDIT}</b><s>PKR {AUDIT_REF}</s></div><p class="after">Founding price · then PKR {AUDIT_AFTER}</p>
  <ul class="checks">{AUDIT_CHECKS}</ul>
  <a class="btn btn-wa" href="{WA_AUDIT}" target="_blank" rel="noopener">{WA_SVG} Book the audit</a></div>
 <div class="plan rv" id="build"><span class="kicker">Step 2</span><h3>System Build</h3><p>Your #1 time-saving system, built on your real workflow and handed over.</p>
  <div class="price"><b>PKR {BUILD}</b><s>PKR {BUILD_REF}</s></div><p class="after">Founding price · then from PKR {BUILD_AFTER}</p>
  <ul class="checks"><li>One complete system from your audit, e.g. WhatsApp → order sheet → confirmations → follow-ups</li><li>Built with n8n, WhatsApp, Google Sheets and AI</li><li>Tested on real cases before going live</li><li>Handover guide + team walkthrough</li><li>14 days of fixes after launch</li><li>Audit fee credited if you start within {CREDIT_DAYS} days</li></ul>
  <a class="btn btn-p" href="{WA_BUILD}" target="_blank" rel="noopener">Discuss a build</a></div>
 <div class="plan soon rv" id="care"><span class="kicker">Step 3 · Coming soon</span><h3>Care Plan</h3><p>Keep the system healthy as your business grows. Optional, cancel anytime.</p>
  <div class="price"><b>PKR {CARE}</b><span>/month</span></div><p class="after">Available to build clients</p>
  <ul class="checks"><li>Monitoring &amp; fixes</li><li>Small changes (prices, messages, steps)</li><li>Monthly performance check</li><li>Priority WhatsApp support</li><li>No contract, no lock-in</li></ul>
  <a class="btn btn-g" href="{WA_CARE}" target="_blank" rel="noopener">Join the waitlist</a></div>
</div>
<div class="note rv">{ic(I['wallet'])}<div><b>The audit pays for itself.</b> Start a build within {CREDIT_DAYS} days of your audit and the full PKR {AUDIT} comes off the build price, so the founding build costs you PKR {int(BUILD.replace(',',''))-int(AUDIT.replace(',','')):,} on top of the audit. Bigger or multi-system projects are quoted in writing after the audit.</div></div>
</div></section>

<section class="sec alt"><div class="wrap narrow">
<div class="head rv"><span class="eyebrow">Compare</span><h2>Founding vs. standard prices</h2></div>
<div class="tbl-wrap rv"><table class="tbl"><thead><tr><th>Offer</th><th>Founding (first {FOUNDING_SLOTS})</th><th>Standard</th><th>Reference value</th></tr></thead><tbody>
<tr><td>Systems Audit</td><td>PKR {AUDIT}</td><td>PKR {AUDIT_AFTER}</td><td>PKR {AUDIT_REF}</td></tr>
<tr><td>System Build</td><td>PKR {BUILD}</td><td>from PKR {BUILD_AFTER}</td><td>PKR {BUILD_REF}</td></tr>
<tr><td>Care Plan</td><td colspan="2">PKR {CARE} / month (coming soon)</td><td>—</td></tr>
</tbody></table></div>
<p class="muted mt1">No free audits: a paid audit means we both take it seriously. Prices are in Pakistani Rupees.</p>
</div></section>

<section class="sec" id="pay"><div class="wrap">
<div class="head rv"><span class="eyebrow">Paying</span><h2>How payment works</h2><p>Simple, local and on the record.</p></div>
<div class="pay">
 <div class="step rv"><h3>Message</h3><p>Message us on WhatsApp and tell us what your business does.</p></div>
 <div class="step rv"><h3>Pay</h3><p>Send the fee by Easypaisa to the account below.</p></div>
 <div class="step rv"><h3>Screenshot</h3><p>Send the payment screenshot on WhatsApp.</p></div>
 <div class="step rv"><h3>Confirmed</h3><p>You get written confirmation and the intake form, and the 48-hour clock starts.</p></div>
</div>
<dl class="acct rv"><div><dt>Method</dt><dd>Easypaisa</dd></div><div><dt>Number</dt><dd>{PHONE_DISPLAY}</dd></div><div><dt>Account name</dt><dd>{EASYPAISA_NAME}</dd></div><div><a class="btn btn-wa" href="{WA_AUDIT}" target="_blank" rel="noopener">{WA_SVG} Start on WhatsApp</a></div></dl>
<p class="muted mt1">For builds: 50% to start, 50% at handover, unless agreed otherwise in writing. Always confirm the account name before you send money.</p>
</div></section>
{cta("Ready when you are.")}
"""

# ── HOW IT WORKS ─────────────────────────────────────────────────────
how = phero("How it works", "From first message to a system that runs itself.",
  "Every step is written down, priced upfront and handled by the founder.") + f"""
<section class="sec" style="padding-top:1rem"><div class="wrap narrow"><ol class="tl">
<li class="rv"><span class="n">01</span><div><h3>Say hello on WhatsApp</h3><p>Tell us what your business does and what takes up your day. Roman Urdu or English, whichever you prefer.</p><ul><li>Replies {HOURS}</li><li>Honest answer if a system won't help</li></ul></div></li>
<li class="rv"><span class="n">02</span><div><h3>Pay &amp; fill the intake (PKR {AUDIT})</h3><p>Pay by Easypaisa, send the screenshot, and fill a short intake form about how your orders, bookings, messages and admin work today.</p></div></li>
<li class="rv"><span class="n">03</span><div><h3>Your systems map, within 48 hours</h3><p>A clear PDF showing how work flows through your business, where it leaks, and the top fixes ranked by time and money saved, including what NOT to automate yet.</p></div></li>
<li class="rv"><span class="n">04</span><div><h3>30-minute walkthrough call</h3><p>We go through the map together on Google Meet. The call is recorded and shared with you so your team can watch it later.</p></div></li>
<li class="rv"><span class="n">05</span><div><h3>Written proposal (if you want a build)</h3><p>Exactly what gets built, which tools connect, what we need from you, the fixed price and the timeline. Nothing starts until you agree.</p><ul><li>Founding build: PKR {BUILD}</li><li>Audit fee credited within {CREDIT_DAYS} days</li></ul></div></li>
<li class="rv"><span class="n">06</span><div><h3>Build &amp; test</h3><p>Built on your real products, prices and tone. You test it with normal and awkward cases before any customer sees it.</p></div></li>
<li class="rv"><span class="n">07</span><div><h3>Launch &amp; hand over</h3><p>Go live, a handover guide, a team walkthrough and 14 days of fixes. The accounts and system are yours.</p></div></li>
</ol></div></section>
{cta()}
"""

# ── ABOUT ────────────────────────────────────────────────────────────
about = phero("About", "One founder. Fully accountable.",
  "TRL — The Right Lifestyle — is a founder-led systems studio based in Rawalpindi, Pakistan.") + f"""
<section class="sec" style="padding-top:1rem"><div class="wrap"><div class="founder">
 <div class="rv"><div class="avatar" aria-hidden="true">RA</div><p class="center mt1"><b>Rashid Muhammad Amir</b><br><span class="muted">Founder, TRL</span></p></div>
 <div class="prose rv">
  <p>I started TRL because I kept seeing the same thing: hard-working owners stuck answering the same messages, copying the same orders and chasing the same payments every day. The business grows, but so does their workload.</p>
  <p>That's not a lifestyle. <b>The right lifestyle</b> is a business that keeps running when you're not personally pushing every task, so you have time for growth, family and yourself.</p>
  <h2>What TRL believes</h2>
  <ul><li><b>Systems before tools.</b> We map how your business works first, then automate only what's worth it.</li><li><b>Honest pricing.</b> Fixed prices in PKR, published on this site.</li><li><b>Plain language.</b> No jargon. Roman Urdu is welcome.</li><li><b>You own it.</b> Your accounts, your data, your system. No lock-in.</li><li><b>No fake proof.</b> We're early. We'll show real results once we've earned them, not before.</li></ul>
  <h2>Why founding prices?</h2>
  <p>TRL is taking its first {FOUNDING_SLOTS} clients at founding prices (PKR {AUDIT} audit, PKR {BUILD} build). You get senior attention at a fraction of the standard price, and we earn your case study and referral. When the founding slots are gone, prices go up.</p>
  <p class="mt2"><a class="btn btn-wa" href="{WA_HI}" target="_blank" rel="noopener" style="text-decoration:none">{WA_SVG} Message Rashid</a></p>
 </div>
</div></div></section>
{cta()}
"""

# ── FAQ ──────────────────────────────────────────────────────────────
FAQ = {
 "The audit": [
  ("What exactly do I get for PKR " + AUDIT + "?", f"A systems map PDF (how work flows through your business today, where it leaks, and your top fixes ranked) plus a 30-minute recorded walkthrough call on Google Meet. Delivered within 48 hours of receiving your intake."),
  ("Why isn't the audit free?", "Free audits get ignored, by both sides. A small fee means you get a properly prepared map and we know you're serious. And if you build with us within " + str(CREDIT_DAYS) + " days, the fee is credited in full."),
  ("What if I don't want a build after the audit?", "That's fine. The map is yours to keep and use, whether you do it yourself, hire someone else or wait. No pressure, no follow-up spam."),
  ("How long do the founding prices last?", f"For our first {FOUNDING_SLOTS} clients. After that the audit becomes PKR {AUDIT_AFTER} and builds start from PKR {BUILD_AFTER}."),
 ],
 "Builds & tech": [
  ("What tools do you use?", "Mostly WhatsApp Business, Google Sheets/Workspace, n8n for automation, and AI models for smart replies. We prefer tools you already use or that are free or cheap to run."),
  ("Are there monthly tool costs?", "Sometimes. Some tools are free and some have small monthly fees (for example the WhatsApp API or automation hosting). Every cost is listed in your proposal before you agree, with no hidden extras."),
  ("Will the AI reply wrongly to my customers?", "Assistants only answer from your approved information, are tested before launch, and hand over to a human for anything sensitive like complaints, custom prices or payments."),
  ("Do I need to be technical?", "No. You explain how your business works; we handle the technical part and give your team a simple guide."),
  ("Who owns the system?", "You do. Accounts are created in your name, and you get the documentation and access. No lock-in."),
 ],
 "Working with TRL": [
  ("Do you work with physical/local businesses or only online?", "Both. Online and digital businesses anywhere in Pakistan (remotely), and local businesses in Rawalpindi/Islamabad in person or anywhere else online, whether you sell products or services."),
  ("How do I pay?", f"Easypaisa to {PHONE_DISPLAY} ({EASYPAISA_NAME}), then send the screenshot on WhatsApp for confirmation. Builds: 50% to start, 50% at handover."),
  ("Do you work in Urdu?", "Yes. Talk to us in English, Urdu or Roman Urdu, and assistants can reply to your customers in Roman Urdu too."),
  ("Is my business data safe?", "We access your tools through your own accounts with the minimum permissions needed. Never send passwords in chat; we'll show you a safe way to share access. See our Privacy page."),
  ("Do you work with international clients?", "Right now we focus on Pakistani businesses with PKR pricing. International work will open later. Message us if you're interested."),
 ],
}
faq_html = "".join(f'<div class="faq-group rv"><h2>{g}</h2><div class="faq">' + "".join(f"<details><summary>{q}</summary><div><p>{a}</p></div></details>" for q, a in qs) + "</div></div>" for g, qs in FAQ.items())
faq_ld = {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for qs in FAQ.values() for q, a in qs]}
faq = phero("FAQ", "Questions, answered straight.", "Can't find yours? Ask on WhatsApp. A real person replies.") + f"""
<section class="sec" style="padding-top:1rem"><div class="wrap narrow">{faq_html}</div></section>
<script type="application/ld+json">{json.dumps(faq_ld)}</script>
{cta()}"""

# ── CONTACT ──────────────────────────────────────────────────────────
contact = phero("Contact", "Let's talk about your business.",
  "Fill this in and it opens WhatsApp with your message ready to send. No data is stored on this website.") + f"""
<section class="sec" style="padding-top:1rem"><div class="wrap"><div class="g2" style="align-items:start">
<form class="card form rv" id="waform">
 <div class="row"><label>Your name<input name="name" required autocomplete="name"></label><label>Business name<input name="business" required></label></div>
 <div class="row"><label>Business type<select name="type"><option>Online / e-commerce</option><option>Daraz / marketplace seller</option><option>Coach / academy / courses</option><option>Agency / freelancer</option><option>Shop / boutique / showroom</option><option>Clinic / salon / gym</option><option>Restaurant / food</option><option>School / tuition</option><option>Real estate</option><option>Other service</option></select></label>
 <label>Interested in<select name="interest"><option>Systems Audit (PKR {AUDIT})</option><option>System Build (PKR {BUILD})</option><option>Care Plan waitlist</option><option>Not sure yet</option></select></label></div>
 <label>Website / Instagram / Daraz link (optional)<input name="link" type="text" placeholder="instagram.com/yourbrand"></label>
 <label>What takes most of your time each day?<textarea name="pain" required placeholder="e.g. Answering price questions on WhatsApp and confirming COD orders by phone"></textarea></label>
 <button class="btn btn-wa" type="submit">{WA_SVG} Send on WhatsApp</button>
 <p class="muted">Opens WhatsApp with your message pre-filled. You review it, then press send.</p>
</form>
<div class="rv"><div class="clist">
 <a href="{WA_HI}" target="_blank" rel="noopener">{ic(I['chat'])}<span><small>WhatsApp (fastest)</small><b>{PHONE_DISPLAY}</b></span></a>
 <a href="mailto:{EMAIL}">{ic(I['mail'])}<span><small>Email</small><b>{EMAIL}</b></span></a>
 <div>{ic(I['map'])}<span><small>Based in</small><b>Rawalpindi, Punjab, Pakistan</b><small>Serving all of Pakistan online · in person in Rawalpindi/Islamabad</small></span></div>
 <a href="{IG}" target="_blank" rel="noopener">{ic(I['user'])}<span><small>Instagram</small><b>@the.right.lifestyle</b></span></a>
 <a href="{TT}" target="_blank" rel="noopener">{ic(I['chart'])}<span><small>TikTok</small><b>@the.right.lifestyle</b></span></a>
 <div>{ic(I['clock'])}<span><small>Replies</small><b>{HOURS}</b><small>Usually same-day replies</small></span></div>
</div></div>
</div></div></section>"""

# ── LEGAL ────────────────────────────────────────────────────────────
updated = datetime.date.today().strftime("%d %B %Y")
privacy = phero("Legal", "Privacy policy", f"Last updated {updated}.") + f"""
<section class="sec" style="padding-top:1rem"><div class="wrap narrow prose">
<p>TRL — The Right Lifestyle ("TRL", "we"), run by Rashid Muhammad Amir in Rawalpindi, Pakistan, respects your privacy. This page explains what we collect and why.</p>
<h2>This website</h2><p>This site is static. It has no login and no database, and the contact form doesn't store anything; it only opens WhatsApp with your message. If we add analytics (such as Google Analytics or Microsoft Clarity) to understand visits, we'll list it here.</p>
<h2>When you contact us</h2><p>Messages you send by WhatsApp or email (your name, number, business details) are used only to reply to you and deliver our services. We never sell or rent your information.</p>
<h2>Client data</h2><ul><li>We access your business tools only with your permission and only what the work needs.</li><li>We never ask for passwords in chat. Access is shared safely or through your own accounts.</li><li>Payment screenshots are kept for our accounting records.</li><li>At the end of a project, you can ask us to remove our access and delete your data.</li></ul>
<h2>Contact</h2><p>Questions or deletion requests: <a href="mailto:{EMAIL}">{EMAIL}</a> or WhatsApp {PHONE_DISPLAY}.</p>
</div></section>"""
terms = phero("Legal", "Terms of service", f"Last updated {updated}.") + f"""
<section class="sec" style="padding-top:1rem"><div class="wrap narrow prose">
<h2>1. Services</h2><p>TRL provides business systems audits, automation builds and optional care plans. The scope, price and timeline of each project are agreed in writing (WhatsApp or email) before work begins.</p>
<h2>2. Prices &amp; payment</h2><ul><li>Prices are in PKR as shown on the Pricing page at the time you book. Founding prices apply to our first {FOUNDING_SLOTS} clients.</li><li>Audits are paid in full upfront. Builds: 50% to start, 50% at handover, unless agreed otherwise.</li><li>The audit fee is credited to a build started within {CREDIT_DAYS} days of audit delivery.</li><li>Third-party tool fees (if any) are paid by the client and listed in the proposal.</li></ul>
<h2>3. Delivery</h2><p>Audits are delivered within 48 hours of receiving payment and a completed intake form. Build timelines are set in each proposal.</p>
<h2>4. Refunds</h2><p>If we can't deliver your audit, you get a full refund. Once a systems map has been delivered, the audit fee isn't refundable. Build deposits are refundable minus work already completed, if cancelled before handover.</p>
<h2>5. Ownership</h2><p>After full payment, you own the systems, workflows and documentation built for you. TRL may reuse general know-how and non-confidential templates.</p>
<h2>6. Your responsibilities</h2><p>You provide accurate information and timely access, and you're responsible for how you use the system, including following WhatsApp's and other platforms' policies.</p>
<h2>7. Liability</h2><p>We test thoroughly, but no system is error-free. TRL's total liability is limited to the fees paid for the relevant project. We aren't responsible for outages or changes by third-party platforms.</p>
<h2>8. Contact</h2><p><a href="mailto:{EMAIL}">{EMAIL}</a> · WhatsApp {PHONE_DISPLAY}</p>
</div></section>"""
notfound = f"""<section class="phero" style="text-align:center;padding-block:7rem"><div class="wrap"><span class="eyebrow">404</span><h1 style="margin-inline:auto">This page took a day off.</h1><p class="lead" style="margin:0 auto 2rem">The page you're looking for doesn't exist. Our systems don't.</p><div class="btns" style="justify-content:center"><a class="btn btn-p" href="index.html">Back home</a><a class="btn btn-g" href="pricing.html">See pricing</a></div></div></section>"""

PAGES = [
 ("index.html", "TRL — The Right Lifestyle · Business Automation & Systems Audits, Pakistan", f"TRL finds the repetitive work in your business and builds systems that do it for you. WhatsApp, orders, follow-ups, reports. Systems Audit PKR {AUDIT}.", home),
 ("services.html", "Services", "WhatsApp automation, order & booking flows, lead follow-up, AI assistants in Urdu & English, reports and admin automation for Pakistani businesses.", services),
 ("who-we-help.html", "Who we help", "Systems for online and local businesses across Pakistan: e-commerce, Daraz sellers, academies, agencies, shops, clinics, restaurants and more.", whop),
 ("pricing.html", "Pricing", f"Systems Audit PKR {AUDIT} · System Build PKR {BUILD} · Care Plan PKR {CARE}/month. Founding prices for the first {FOUNDING_SLOTS} clients.", pricing),
 ("how-it-works.html", "How it works", "From WhatsApp hello to a running system: audit, walkthrough, proposal, build, test and handover.", how),
 ("about.html", "About", "TRL is a founder-led systems studio in Rawalpindi, run by Rashid Muhammad Amir.", about),
 ("faq.html", "FAQ", "Answers about the TRL audit, builds, tools, payment, data safety and working in Urdu.", faq),
 ("contact.html", "Contact", f"Contact TRL on WhatsApp {PHONE_DISPLAY} or email {EMAIL}.", contact),
 ("privacy.html", "Privacy policy", "How TRL handles your information.", privacy),
 ("terms.html", "Terms of service", "TRL terms: scope, payment, delivery, refunds and ownership.", terms),
 ("404.html", "Page not found", "Page not found.", notfound),
]
for f, t, d, b in PAGES:
    (ROOT / f).write_text(page(f, t, d, b), encoding="utf-8")

(ROOT / "sitemap.xml").write_text('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + "".join(
    f"<url><loc>{SITE}{'' if f=='index.html' else f}</loc><lastmod>{datetime.date.today()}</lastmod></url>\n" for f, *_ in PAGES if f != "404.html") + "</urlset>\n")
(ROOT / "robots.txt").write_text(f"User-agent: *\nAllow: /\nSitemap: {SITE}sitemap.xml\n")
(ROOT / "manifest.webmanifest").write_text(json.dumps({"name": "TRL — The Right Lifestyle", "short_name": "TRL", "start_url": "./", "display": "standalone", "background_color": "#f5f7fc", "theme_color": "#2357e8", "icons": [{"src": "assets/img/icon-192.png", "sizes": "192x192", "type": "image/png"}]}))
(ROOT / ".nojekyll").write_text("")
print("built", len(PAGES), "pages")
