#!/usr/bin/env python3
"""TRL site builder — writes static HTML pages into this folder.
Edit the public offer/contact settings below, then run:  python3 tools/build.py
Pages are plain HTML afterwards — GitHub Pages serves them directly."""
from urllib.parse import quote
import json, datetime, pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
SITE = "https://therightlifestyle.github.io/TheRightLifestyle/"

# ── Public offer configuration (confirm with the founder before changing) ─
PHONE_DISPLAY = "+92 319 0091457"
WA = "923190091457"
EMAIL = "officialtrlservice@gmail.com"
EASYPAISA_NAME = "Rashid Muhammad Amir"
AUDIT, AUDIT_AFTER = "1,500", "3,000"
BUILD, BUILD_AFTER = "15,000", "25,000"
CARE = "3,000–5,000"
FOUNDING_CLIENTS = 50
CREDIT_DAYS = 14
LEGAL_LAST_UPDATED = "02 October 2026"  # Change only when the legal text itself is revised.
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

NAV = [("services.html", "Services"), ("who-we-help.html", "Who we help"),
       ("how-it-works.html", "How it works"), ("pricing.html", "Pricing"), ("about.html", "About")]

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
<meta name="theme-color" content="#f6f6f0">
<link rel="canonical" href="{url}">
<link rel="icon" href="assets/img/favicon.svg" type="image/svg+xml"><link rel="apple-touch-icon" href="assets/img/icon-192.png"><link rel="manifest" href="manifest.webmanifest">
<meta property="og:type" content="website"><meta property="og:site_name" content="TRL — The Right Lifestyle"><meta property="og:locale" content="en_PK">
<meta property="og:title" content="{full_title}"><meta property="og:description" content="{desc}"><meta property="og:url" content="{url}">
<meta property="og:image" content="{SITE}assets/img/og-image.png"><meta property="og:image:width" content="1200"><meta property="og:image:height" content="630"><meta property="og:image:alt" content="TRL — practical business systems for WhatsApp enquiries, orders, bookings and follow-ups in Pakistan.">
<meta name="twitter:card" content="summary_large_image"><meta name="twitter:title" content="{full_title}"><meta name="twitter:description" content="{desc}"><meta name="twitter:image" content="{SITE}assets/img/og-image.png">
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
  <a class="brand" href="index.html" aria-label="TRL home"><img src="assets/img/favicon.svg" alt="" width="38" height="38"><span><b>The Right Lifestyle</b><small>Founder-led systems studio</small></span></a>
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
    <p class="foot-intro">We find the repetitive work in your business and build systems that do it for you. You run the business; the system handles the routine.</p>
    <p class="foot-signoff"><i>Kaam aap ka, system hamara.</i></p>
   </div>
   <div><h4>Company</h4><ul><li><a href="about.html">About Rashid</a></li><li><a href="how-it-works.html">How it works</a></li><li><a href="who-we-help.html">Who we help</a></li><li><a href="faq.html">FAQ</a></li></ul></div>
   <div><h4>Offers</h4><ul><li><a href="pricing.html#audit">Systems Audit · PKR {AUDIT}</a></li><li><a href="pricing.html#build">System Build · PKR {BUILD}</a></li><li><a href="pricing.html#care">Care Plan · coming soon</a></li><li><a href="services.html">All services</a></li></ul></div>
   <div><h4>Contact</h4><ul><li><a href="{WA_HI}" target="_blank" rel="noopener">WhatsApp {PHONE_DISPLAY}</a></li><li><a href="mailto:{EMAIL}">{EMAIL}</a></li><li><a href="contact.html">Contact form</a></li><li><a href="{IG}" target="_blank" rel="noopener">Instagram</a> · <a href="{TT}" target="_blank" rel="noopener">TikTok</a></li><li class="foot-hours">{HOURS}</li></ul></div>
  </div>
  <div class="foot-b"><span>© <span id="yr">{datetime.date.today().year}</span> TRL — The Right Lifestyle · Rawalpindi, Pakistan</span><span><a href="privacy.html">Privacy</a><a href="terms.html">Terms</a></span></div>
 </div>
</footer>
<a class="fab" href="{WA_HI}" target="_blank" rel="noopener" aria-label="Chat with TRL on WhatsApp">{WA_SVG}</a>
<script src="assets/js/main.js" defer></script>
</body>
</html>
"""

def cta(h="Find out where your time is going.", p=None):
    p = p or f"Book the PKR {AUDIT} Systems Audit. You get a written map of your business and a 30-minute walkthrough call, and the full fee is credited if you build with us within {CREDIT_DAYS} days."
    return f"""<section class="sec sec-cta"><div class="wrap"><div class="cta-panel on-dark">
<div class="cta-copy"><span class="eyebrow">A clear first step</span><h2>{h}</h2><p>{p}</p></div>
<div class="cta-actions"><a class="btn btn-wa" href="{WA_AUDIT}" target="_blank" rel="noopener">{WA_SVG} Book on WhatsApp</a><a class="btn btn-ghost" href="pricing.html">See pricing</a></div>
</div></div></section>"""

def phero(eyebrow, h1, lead):
    return f'<section class="phero"><div class="wrap"><span class="eyebrow">{eyebrow}</span><h1>{h1}</h1><p class="lead">{lead}</p></div></section>'

AUDIT_CHECKS = f"""<li>A <b>systems map PDF</b>: how work flows through your business today</li>
<li>Where time is being spent and where enquiries or follow-ups may be slipping, ranked by likely impact</li>
<li>What to automate first, what to leave alone, and what it may cost</li>
<li><b>30-min walkthrough call</b> on Google Meet, recorded for you</li>
<li>Delivered within 48 hours of receiving your completed intake</li>
<li>Full PKR {AUDIT} <b>credited to your build</b> within {CREDIT_DAYS} days</li>"""

def ic(path):
    return f'<span class="ic"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{path}</svg></span>'

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
home = f"""
<section class="hero"><div class="wrap hero-grid">
 <div class="hero-copy">
  <span class="eyebrow">Founder-led business systems · Pakistan</span>
  <h1>Get your time back from <span class="grad">repetitive work.</span></h1>
  <p class="lead">Practical systems for WhatsApp enquiries, orders, bookings and follow-ups—designed around how your business actually runs.</p>
  <div class="btns"><a class="btn btn-wa" href="{WA_AUDIT}" target="_blank" rel="noopener">{WA_SVG} Start with the Systems Audit · PKR {AUDIT}</a><a class="btn btn-outline" href="how-it-works.html">See how it works <span aria-hidden="true">→</span></a></div>
  <p class="hero-meta">Online across Pakistan <span aria-hidden="true">·</span> In person in Rawalpindi / Islamabad</p>
  <p class="ur">Kaam aap ka, system hamara.</p>
 </div>
 <div class="demo-panel" role="group" aria-label="Illustrative business workflow example">
  <div class="demo-top"><span class="demo-kicker">ILLUSTRATIVE WORKFLOW</span><span class="sample-chip">Example · no client data</span></div>
  <h2>From a message to a clear next step.</h2>
  <div class="workflow-list">
   <div class="workflow-item"><span class="workflow-num">01</span><div class="workflow-copy"><b>Enquiry arrives</b><span>WhatsApp · order or question</span></div><span class="workflow-label">Capture</span></div>
   <div class="workflow-connector" aria-hidden="true"></div>
   <div class="workflow-item"><span class="workflow-num">02</span><div class="workflow-copy"><b>Details are organised</b><span>Approved reply · order or lead log</span></div><span class="workflow-label">System</span></div>
   <div class="workflow-connector" aria-hidden="true"></div>
   <div class="workflow-item"><span class="workflow-num">03</span><div class="workflow-copy"><b>Owner gets the right hand-off</b><span>Exceptions stay with a person</span></div><span class="workflow-label">Human</span></div>
  </div>
  <div class="demo-bottom"><span>Tools chosen after the audit</span><span>Illustrative only</span></div>
 </div>
</div></section>

<section class="trust-strip" aria-label="How TRL works"><div class="wrap trust-inner">
 <span><b>01</b> Scope and price in writing</span><span><b>02</b> Built around your current workflow</span><span><b>03</b> Accounts and handover stay yours</span>
</div></section>

<section class="sec"><div class="wrap split-story">
 <div class="story"><span class="eyebrow">The everyday friction</span><h2>Busy work should not be the thing that runs your business.</h2><p>When the same messages, updates and follow-ups depend on you remembering every step, small tasks quietly take over the day. A useful system makes the routine easier to see, manage and hand over.</p><a class="text-link" href="how-it-works.html">See the process <span aria-hidden="true">→</span></a></div>
 <div class="friction-list" aria-label="Common repetitive work">
  <div class="friction-item"><span>01</span><div><b>The same questions, again</b><p>Prices, availability, delivery and basic details.</p></div></div>
  <div class="friction-item"><span>02</span><div><b>Orders copied by hand</b><p>Messages turned into sheets, notes and reminders.</p></div></div>
  <div class="friction-item"><span>03</span><div><b>Follow-ups left to memory</b><p>Enquiries and payments waiting for a reply.</p></div></div>
 </div>
</div></section>

<section class="sec alt"><div class="wrap">
 <div class="head"><span class="eyebrow">What we build</span><h2>Useful systems, chosen for the work—not the buzzword.</h2><p>We start with tools your team already uses where practical, and add automation or AI only when it solves a real part of the process.</p></div>
 <div class="service-grid">
  <a class="service-card" href="services.html#whatsapp"><span class="service-icon">{ic(I['chat'])}</span><span class="service-title">WhatsApp &amp; enquiries</span><p>Organise common questions, capture leads and route conversations to a person when needed.</p><span class="service-flow">Question <i>→</i> approved reply <i>→</i> hand-off</span></a>
  <a class="service-card" href="services.html#ops"><span class="service-icon">{ic(I['cart'])}</span><span class="service-title">Orders &amp; bookings</span><p>Record requests, confirm the next step and send reminders without retyping everything.</p><span class="service-flow">Order <i>→</i> record <i>→</i> confirm</span></a>
  <a class="service-card" href="services.html#followup"><span class="service-icon">{ic(I['user'])}</span><span class="service-title">Follow-up &amp; admin</span><p>Keep enquiries, invoices, payments and routine reporting from slipping through the cracks.</p><span class="service-flow">Enquiry <i>→</i> follow-up <i>→</i> next step</span></a>
 </div>
 <div class="section-link"><a class="text-link" href="services.html">Explore all services <span aria-hidden="true">→</span></a></div>
</div></section>

<section class="sec"><div class="wrap">
 <div class="head"><span class="eyebrow">Who we help</span><h2>For businesses built on repeat work.</h2><p>Online or on the ground. Product or service. The first question is always how your work moves today.</p></div>
 <div class="audience-grid">
  <article class="audience-panel"><div class="audience-heading">{ic(I['cart'])}<div><h3>Online &amp; digital</h3><p>Pakistan-wide, fully remote.</p></div></div><div class="sector-list"><span>E-commerce &amp; Daraz sellers</span><span>Coaches &amp; online academies</span><span>Agencies &amp; freelancers</span><span>Content creators &amp; digital products</span></div></article>
  <article class="audience-panel"><div class="audience-heading">{ic(I['store'])}<div><h3>Local &amp; physical</h3><p>Rawalpindi / Islamabad in person; rest of Pakistan online.</p></div></div><div class="sector-list"><span>Shops, boutiques &amp; showrooms</span><span>Clinics, salons &amp; gyms</span><span>Restaurants &amp; home kitchens</span><span>Schools, real estate &amp; services</span></div></article>
 </div>
 <div class="section-link"><a class="text-link" href="who-we-help.html">Explore examples by business type <span aria-hidden="true">→</span></a></div>
</div></section>

<section class="sec alt"><div class="wrap">
 <div class="head"><span class="eyebrow">A clear process</span><h2>Start small. Know what happens next.</h2><p>One person accountable from first message to handover. No build begins without an agreed scope.</p></div>
 <div class="steps steps-home">
  <div class="step"><span class="step-index">01</span><h3>Audit</h3><p>Map the work and identify what is worth improving.</p><span class="when">PKR {AUDIT} · delivered within 48 hours of completed intake</span></div>
  <div class="step"><span class="step-index">02</span><h3>Walkthrough</h3><p>Review the systems map and decide what to do first.</p><span class="when">30 minutes · Google Meet</span></div>
  <div class="step"><span class="step-index">03</span><h3>Build</h3><p>Build and test the agreed system on your workflow.</p><span class="when">PKR {BUILD} founding · fixed scope</span></div>
  <div class="step"><span class="step-index">04</span><h3>Handover</h3><p>Get access, a guide and a team walkthrough.</p><span class="when">You own the system</span></div>
 </div>
 <div class="section-link"><a class="text-link" href="how-it-works.html">View the full process <span aria-hidden="true">→</span></a></div>
</div></section>

<section class="sec"><div class="wrap">
 <div class="head"><span class="eyebrow">Straightforward pricing</span><h2>Know the first step before you book.</h2><p>Founding prices are for our first {FOUNDING_CLIENTS} clients. Please verify availability before booking.</p></div>
 <div class="pricing-snapshot">
  <div class="pricing-copy"><span class="kicker">STEP 01 · SYSTEMS AUDIT</span><h3>Understand the workflow before you invest in a build.</h3><p>Receive a systems map PDF and a 30-minute walkthrough call. The audit fee is credited to a build started within {CREDIT_DAYS} days.</p><a class="btn btn-wa" href="{WA_AUDIT}" target="_blank" rel="noopener">{WA_SVG} Book the audit · PKR {AUDIT}</a></div>
  <div class="pricing-side"><div class="price-main"><b>PKR {AUDIT}</b><span>one-time · founding price</span></div><div class="pricing-fact"><b>System Build</b><span>PKR {BUILD} founding · from PKR {BUILD_AFTER} standard</span></div><div class="pricing-fact"><b>Care Plan</b><span>PKR {CARE} / month · coming soon</span></div><a class="text-link" href="pricing.html">See full pricing &amp; terms <span aria-hidden="true">→</span></a></div>
 </div>
</div></section>

<section class="sec alt"><div class="wrap founder-band">
 <div class="founder-mark" aria-hidden="true">RA</div><div class="founder-content"><span class="eyebrow">One founder. Fully accountable.</span><h2>Practical systems, not AI for its own sake.</h2><p>TRL is run by Rashid Muhammad Amir from Rawalpindi. Every project starts with understanding how your business works—and ends with a clear handover.</p><a class="text-link" href="about.html">Meet the founder <span aria-hidden="true">→</span></a></div>
 <ul class="founder-points"><li>Written scope before work</li><li>Your accounts remain yours</li><li>No lock-in or made-up results</li></ul>
</div></section>
{cta()}
"""

# ── SERVICES ─────────────────────────────────────────────────────────
def svc(id_, icon, title, p, items, eg):
    return f"""<div class="card rv" id="{id_}">{ic(I[icon])}<h3>{title}</h3><p>{p}</p><ul class="chips">{"".join(f"<li>{x}</li>" for x in items)}</ul><div class="flow">{eg}</div></div>"""
services = phero("Services", "Everything we automate, in plain language.",
  "Every engagement starts with the audit, so we build the thing that saves you the most time first, not the thing that sounds impressive.") + f"""
<section class="sec sec-tight"><div class="wrap"><div class="g2">
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
{cta("Not sure which one you need?", f"That's what the audit is for. PKR {AUDIT}, delivered within 48 hours of receiving your completed intake; the fee is credited to your build.")}
"""

# ── WHO WE HELP ──────────────────────────────────────────────────────
def who(icon, t, tasks, sys):
    return f"""<div class="card hov rv">{ic(I[icon])}<h3>{t}</h3><p><b class="label-strong">Daily drain:</b> {tasks}</p><div class="flow">{sys}</div></div>"""
whop = phero("Who we help", "Built for every business that repeats itself.",
  "Physical or digital, products or services, solo or with a team. If the same work happens every day, it can be systemised.") + f"""
<section class="sec sec-tight"><div class="wrap">
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
  f"Start small with the audit. Build only what's worth building. Founding prices apply to our first {FOUNDING_CLIENTS} clients.") + f"""
<section class="sec sec-tight-lg"><div class="wrap">
<div class="plans">
 <div class="plan hot rv" id="audit"><span class="badge">Start here</span><span class="kicker">Step 1</span><h3>Systems Audit</h3><p>See exactly where your time and money go, before spending on any tool.</p>
  <div class="price"><b>PKR {AUDIT}</b></div><p class="after">Founding price · then PKR {AUDIT_AFTER}</p>
  <ul class="checks">{AUDIT_CHECKS}</ul>
  <a class="btn btn-wa" href="{WA_AUDIT}" target="_blank" rel="noopener">{WA_SVG} Book the audit</a></div>
 <div class="plan rv" id="build"><span class="kicker">Step 2</span><h3>System Build</h3><p>Your #1 time-saving system, built on your real workflow and handed over.</p>
  <div class="price"><b>PKR {BUILD}</b></div><p class="after">Founding price · then from PKR {BUILD_AFTER}</p>
  <ul class="checks"><li>One complete system from your audit, e.g. WhatsApp → order sheet → confirmations → follow-ups</li><li>Built with n8n, WhatsApp, Google Sheets and AI</li><li>Tested on real cases before going live</li><li>Handover guide + team walkthrough</li><li>14 days of fixes after launch</li><li>Audit fee credited if you start within {CREDIT_DAYS} days</li></ul>
  <a class="btn btn-p" href="{WA_BUILD}" target="_blank" rel="noopener">Discuss a build</a></div>
 <div class="plan soon rv" id="care"><span class="kicker">Step 3 · Coming soon</span><h3>Care Plan</h3><p>Keep the system healthy as your business grows. Optional, cancel anytime.</p>
  <div class="price"><b>PKR {CARE}</b><span>/month</span></div><p class="after">Available to build clients</p>
  <ul class="checks"><li>Monitoring &amp; fixes</li><li>Small changes (prices, messages, steps)</li><li>Monthly performance check</li><li>Priority WhatsApp support</li><li>No contract, no lock-in</li></ul>
  <a class="btn btn-g" href="{WA_CARE}" target="_blank" rel="noopener">Join the waitlist</a></div>
</div>
<div class="note rv">{ic(I['wallet'])}<div><b>Your audit fee is credited to a build.</b> Start within {CREDIT_DAYS} days and the full PKR {AUDIT} is applied to the build. At the founding build price, you pay PKR {int(BUILD.replace(',',''))-int(AUDIT.replace(',','')):,} after the audit, for PKR {BUILD} total. Bigger or multi-system projects are quoted in writing after the audit.</div></div>
</div></section>

<section class="sec alt"><div class="wrap narrow">
<div class="head rv"><span class="eyebrow">Compare</span><h2>Founding vs. standard prices</h2></div>
<div class="tbl-wrap rv"><table class="tbl"><thead><tr><th>Offer</th><th>Founding price (first {FOUNDING_CLIENTS} clients)</th><th>After the first {FOUNDING_CLIENTS}</th></tr></thead><tbody>
<tr><td>Systems Audit</td><td>PKR {AUDIT}</td><td>PKR {AUDIT_AFTER}</td></tr>
<tr><td>System Build</td><td>PKR {BUILD}</td><td>from PKR {BUILD_AFTER}</td></tr>
<tr><td>Care Plan</td><td colspan="2">PKR {CARE} / month (coming soon)</td></tr>
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
<section class="sec sec-tight"><div class="wrap narrow"><ol class="tl">
<li class="rv"><span class="n">01</span><div><h3>Say hello on WhatsApp</h3><p>Tell us what your business does and what takes up your day. Roman Urdu or English, whichever you prefer.</p><ul><li>Replies {HOURS}</li><li>Honest answer if a system won't help</li></ul></div></li>
<li class="rv"><span class="n">02</span><div><h3>Pay &amp; fill the intake (PKR {AUDIT})</h3><p>Pay by Easypaisa, send the screenshot, and fill a short intake form about how your orders, bookings, messages and admin work today.</p></div></li>
<li class="rv"><span class="n">03</span><div><h3>Your systems map, within 48 hours</h3><p>A clear PDF showing how work flows through your business, where it stalls, and the top improvements ranked by likely impact, including what NOT to automate yet.</p></div></li>
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
<section class="sec sec-tight"><div class="wrap"><div class="founder">
 <div class="rv"><div class="avatar" aria-hidden="true">RA</div><p class="center mt1"><b>Rashid Muhammad Amir</b><br><span class="muted">Founder, TRL</span></p></div>
 <div class="prose rv">
  <p>I started TRL because I kept seeing the same thing: hard-working owners stuck answering the same messages, copying the same orders and chasing the same payments every day. The business grows, but so does their workload.</p>
  <p>That's not a lifestyle. <b>The right lifestyle</b> is a business that keeps running when you're not personally pushing every task, so you have time for growth, family and yourself.</p>
  <h2>What TRL believes</h2>
  <ul><li><b>Systems before tools.</b> We map how your business works first, then automate only what's worth it.</li><li><b>Honest pricing.</b> Fixed prices in PKR, published on this site.</li><li><b>Plain language.</b> No jargon. Roman Urdu is welcome.</li><li><b>You own it.</b> Your accounts, your data, your system. No lock-in.</li><li><b>No fake proof.</b> We're early. We'll show real results once we've earned them, not before.</li></ul>
  <h2>Why founding prices?</h2>
  <p>Founding prices are offered to the first {FOUNDING_CLIENTS} clients (PKR {AUDIT} audit, PKR {BUILD} build). You work directly with the founder. If you are happy with the work, TRL may ask for a referral or permission to share a case study—but only with your consent. After the first {FOUNDING_CLIENTS} clients, standard prices apply.</p>
  <p class="mt2"><a class="btn btn-wa" href="{WA_HI}" target="_blank" rel="noopener">{WA_SVG} Message Rashid</a></p>
 </div>
</div></div></section>
{cta()}
"""

# ── FAQ ──────────────────────────────────────────────────────────────
FAQ = {
 "The audit": [
  ("What exactly do I get for PKR " + AUDIT + "?", f"A systems map PDF (how work flows through your business today, where work slows down, and the top improvements ranked by likely impact) plus a 30-minute recorded walkthrough call on Google Meet. Delivered within 48 hours of receiving your completed intake."),
  ("Why isn't the audit free?", "Free audits get ignored, by both sides. A small fee means you get a properly prepared map and we know you're serious. And if you build with us within " + str(CREDIT_DAYS) + " days, the fee is credited in full."),
  ("What if I don't want a build after the audit?", "That's fine. The map is yours to keep and use, whether you do it yourself, hire someone else or wait. No pressure, no follow-up spam."),
  ("How long do the founding prices last?", f"For our first {FOUNDING_CLIENTS} clients. After that the audit becomes PKR {AUDIT_AFTER} and builds start from PKR {BUILD_AFTER}."),
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
<section class="sec sec-tight"><div class="wrap narrow">{faq_html}</div></section>
<script type="application/ld+json">{json.dumps(faq_ld)}</script>
{cta()}"""

# ── CONTACT ──────────────────────────────────────────────────────────
contact = phero("Contact", "Let's talk about your business.",
  "Fill this in and it opens WhatsApp with your message ready to send. No data is stored on this website.") + f"""
<section class="sec sec-tight"><div class="wrap"><div class="g2 contact-layout">
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
updated = LEGAL_LAST_UPDATED
privacy = phero("Legal", "Privacy policy", f"Last updated {updated}.") + f"""
<section class="sec sec-tight"><div class="wrap narrow prose">
<p>TRL — The Right Lifestyle ("TRL", "we"), run by Rashid Muhammad Amir in Rawalpindi, Pakistan, respects your privacy. This page explains what we collect and why.</p>
<h2>This website</h2><p>This site is static. It has no login and no database, and the contact form doesn't store anything; it only opens WhatsApp with your message. If we add analytics (such as Google Analytics or Microsoft Clarity) to understand visits, we'll list it here.</p>
<h2>When you contact us</h2><p>Messages you send by WhatsApp or email (your name, number, business details) are used only to reply to you and deliver our services. We never sell or rent your information.</p>
<h2>Client data</h2><ul><li>We access your business tools only with your permission and only what the work needs.</li><li>We never ask for passwords in chat. Access is shared safely or through your own accounts.</li><li>Payment screenshots are kept for our accounting records.</li><li>At the end of a project, you can ask us to remove our access and delete your data.</li></ul>
<h2>Contact</h2><p>Questions or deletion requests: <a href="mailto:{EMAIL}">{EMAIL}</a> or WhatsApp {PHONE_DISPLAY}.</p>
</div></section>"""
terms = phero("Legal", "Terms of service", f"Last updated {updated}.") + f"""
<section class="sec sec-tight"><div class="wrap narrow prose">
<h2>1. Services</h2><p>TRL provides business systems audits, automation builds and optional care plans. The scope, price and timeline of each project are agreed in writing (WhatsApp or email) before work begins.</p>
<h2>2. Prices &amp; payment</h2><ul><li>Prices are in PKR as shown on the Pricing page at the time you book. Founding prices apply to our first {FOUNDING_CLIENTS} clients.</li><li>Audits are paid in full upfront. Builds: 50% to start, 50% at handover, unless agreed otherwise.</li><li>The audit fee is credited to a build started within {CREDIT_DAYS} days of audit delivery.</li><li>Third-party tool fees (if any) are paid by the client and listed in the proposal.</li></ul>
<h2>3. Delivery</h2><p>Audits are delivered within 48 hours of receiving payment and a completed intake form. Build timelines are set in each proposal.</p>
<h2>4. Refunds</h2><p>If we can't deliver your audit, you get a full refund. Once a systems map has been delivered, the audit fee isn't refundable. Build deposits are refundable minus work already completed, if cancelled before handover.</p>
<h2>5. Ownership</h2><p>After full payment, you own the systems, workflows and documentation built for you. TRL may reuse general know-how and non-confidential templates.</p>
<h2>6. Your responsibilities</h2><p>You provide accurate information and timely access, and you're responsible for how you use the system, including following WhatsApp's and other platforms' policies.</p>
<h2>7. Liability</h2><p>We test thoroughly, but no system is error-free. TRL's total liability is limited to the fees paid for the relevant project. We aren't responsible for outages or changes by third-party platforms.</p>
<h2>8. Contact</h2><p><a href="mailto:{EMAIL}">{EMAIL}</a> · WhatsApp {PHONE_DISPLAY}</p>
</div></section>"""
notfound = f"""<section class="phero phero-404"><div class="wrap"><span class="eyebrow">404</span><h1>This page took a day off.</h1><p class="lead">The page you're looking for doesn't exist. Our systems don't.</p><div class="btns"><a class="btn btn-p" href="index.html">Back home</a><a class="btn btn-outline" href="pricing.html">See pricing</a></div></div></section>"""

PAGES = [
 ("index.html", "TRL — The Right Lifestyle · Business Automation & Systems Audits, Pakistan", f"TRL finds the repetitive work in your business and builds systems that do it for you. WhatsApp, orders, follow-ups, reports. Systems Audit PKR {AUDIT}.", home),
 ("services.html", "Services", "WhatsApp automation, order & booking flows, lead follow-up, AI assistants in Urdu & English, reports and admin automation for Pakistani businesses.", services),
 ("who-we-help.html", "Who we help", "Systems for online and local businesses across Pakistan: e-commerce, Daraz sellers, academies, agencies, shops, clinics, restaurants and more.", whop),
 ("pricing.html", "Pricing", f"Systems Audit PKR {AUDIT} · System Build PKR {BUILD} · Care Plan PKR {CARE}/month. Founding prices for the first {FOUNDING_CLIENTS} clients.", pricing),
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
    f"<url><loc>{SITE}{'' if f=='index.html' else f}</loc></url>\n" for f, *_ in PAGES if f != "404.html") + "</urlset>\n")
(ROOT / "robots.txt").write_text(f"User-agent: *\nAllow: /\nSitemap: {SITE}sitemap.xml\n")
(ROOT / "manifest.webmanifest").write_text(json.dumps({"name": "TRL — The Right Lifestyle", "short_name": "TRL", "start_url": "./", "display": "standalone", "background_color": "#f6f6f0", "theme_color": "#174f38", "icons": [{"src": "assets/img/icon-192.png", "sizes": "192x192", "type": "image/png"}]}))
(ROOT / ".nojekyll").write_text("")
print("built", len(PAGES), "pages")
