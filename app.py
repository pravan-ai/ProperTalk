import streamlit as st

st.set_page_config(
    page_title="ProperTalk by Pravan | Real Estate, Explained",
    page_icon="🏙️",
    layout="wide",
    initial_sidebar_state="collapsed",
)

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=Playfair+Display:wght@500;600;700&display=swap');
:root { --ink:#17231f; --muted:#65736c; --cream:#f7f5ef; --green:#254b3d; --lime:#d5e7a4; --line:#e4e5dc; }
.stApp { background: var(--cream); color: var(--ink); }
html, body, [class*="css"] { font-family: 'DM Sans', sans-serif; }
.block-container { max-width: 1180px; padding-top: 1.4rem; padding-bottom: 4rem; }
#MainMenu, footer, header {visibility:hidden;}
.brand {font-size:.82rem; letter-spacing:.18em; text-transform:uppercase; font-weight:700; color:var(--green);}
.hero {padding:4.3rem 0 3.6rem; border-bottom:1px solid var(--line);}
.eyebrow {color:var(--green); font-size:.78rem; letter-spacing:.2em; text-transform:uppercase; font-weight:700;}
h1 {font-family:'Playfair Display',serif !important; font-size:clamp(3.2rem,7vw,6rem) !important; line-height:1.02 !important; letter-spacing:-.045em !important; color:var(--ink) !important; margin:.65rem 0 1rem !important;}
h2 {font-family:'Playfair Display',serif !important; color:var(--ink) !important; letter-spacing:-.025em;}
.hero-copy {font-size:1.15rem; line-height:1.8; color:var(--muted); max-width:680px;}
.pill {display:inline-block; padding:.42rem .75rem; border:1px solid #d7ddcf; border-radius:999px; margin:.25rem .3rem .25rem 0; color:var(--green); font-size:.82rem;}
.section {padding:3rem 0; border-bottom:1px solid var(--line);}
.card {height:100%; border:1px solid var(--line); border-radius:18px; padding:1.35rem; background:rgba(255,255,255,.55);}
.card-kicker {font-size:.72rem; letter-spacing:.14em; text-transform:uppercase; color:var(--green); font-weight:700;}
.card h3 {font-family:'Playfair Display',serif; font-size:1.45rem; margin:.65rem 0;}
.card p {color:var(--muted); line-height:1.7;}
.big-quote {font-family:'Playfair Display',serif; font-size:clamp(1.8rem,4vw,3.1rem); line-height:1.3; color:var(--green);}
.small-muted {color:var(--muted); font-size:.9rem;}
a {color:var(--green) !important; font-weight:600;}
div.stButton > button {border-radius:999px; border:1px solid var(--green); background:var(--green); color:white; padding:.65rem 1.2rem; font-weight:600;}
div.stButton > button:hover {background:#18382d; color:white; border-color:#18382d;}
.footer {padding-top:2rem; color:var(--muted); font-size:.85rem;}
@media (max-width: 700px) { .hero {padding:2.4rem 0;} .block-container {padding-left:1rem; padding-right:1rem;} }
</style>
""", unsafe_allow_html=True)

youtube_channel = "https://www.youtube.com/watch?v=7P-U1QsS_b8"
instagram_profile = "https://www.instagram.com/estatebypravan/"

top_left, top_right = st.columns([3, 1])
with top_left:
    st.markdown('<div class="brand">ProperTalk <span style="color:#8b9b72">by Pravan</span></div>', unsafe_allow_html=True)
with top_right:
    st.markdown('<div style="text-align:right;padding-top:.1rem"><a href="https://www.instagram.com/estatebypravan/" target="_blank">Instagram ↗</a></div>', unsafe_allow_html=True)

st.markdown("""
<div class="hero">
  <div class="eyebrow">Real estate, beyond the brochure</div>
  <h1>Property talk.<br><span style="color:#71875f">Made clearer.</span></h1>
  <p class="hero-copy">A growing platform exploring real estate, the people shaping it, and the ideas behind the places we live and invest in.</p>
  <span class="pill">Real estate explained</span><span class="pill">Industry conversations</span><span class="pill">Tricity & beyond</span>
</div>
""", unsafe_allow_html=True)

st.markdown('<div class="section">', unsafe_allow_html=True)
st.markdown("## What is ProperTalk?")
st.markdown("""
ProperTalk by Pravan is a personal real-estate media and networking initiative. The goal is to make property conversations more approachable while building meaningful connections across the real-estate ecosystem.
""")
c1, c2, c3 = st.columns(3, gap="medium")
with c1:
    st.markdown('<div class="card"><div class="card-kicker">01 / Learn</div><h3>Understand the market</h3><p>Break down real-estate concepts, terminology, pricing components and the questions buyers should know to ask.</p></div>', unsafe_allow_html=True)
with c2:
    st.markdown('<div class="card"><div class="card-kicker">02 / Listen</div><h3>Hear from the industry</h3><p>Conversations with people across real estate, sharing experience, perspective and practical insights.</p></div>', unsafe_allow_html=True)
with c3:
    st.markdown('<div class="card"><div class="card-kicker">03 / Connect</div><h3>Build relationships</h3><p>A space to connect clients, brokers, channel partners, developers and other real-estate professionals.</p></div>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

st.markdown('<div class="section">', unsafe_allow_html=True)
left, right = st.columns([1.05, 1], gap="large")
with left:
    st.markdown('<div class="eyebrow">Watch & explore</div>', unsafe_allow_html=True)
    st.markdown("## The conversation continues online")
    st.markdown("Follow the content journey, explore real-estate explainers and discover new conversations as the platform grows.")
    st.markdown(f"[Watch on YouTube ↗]({youtube_channel})")
    st.markdown(f"[Follow on Instagram ↗]({instagram_profile})")
with right:
    st.video(youtube_channel)
st.markdown('</div>', unsafe_allow_html=True)

st.markdown('<div class="section">', unsafe_allow_html=True)
st.markdown('<div class="eyebrow">For real-estate professionals</div>', unsafe_allow_html=True)
st.markdown('<div class="big-quote">Good property decisions start with better conversations.</div>', unsafe_allow_html=True)
st.markdown("""
If you work in real estate and would like to explore an industry conversation, educational collaboration or content idea, get in touch.
""")
st.markdown("""
<div class="card">
  <h3>Have a conversation in mind?</h3>
  <p>Connect through Instagram or YouTube to start the discussion. Contact details can be added here when you choose which public email or business contact to use.</p>
</div>
""", unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

st.markdown("""
<div class="footer">
  <strong>ProperTalk by Pravan</strong><br>
  An independent real-estate media and networking initiative.<br><br>
  <a href="https://www.youtube.com/watch?v=7P-U1QsS_b8" target="_blank">YouTube</a> &nbsp;·&nbsp;
  <a href="https://www.instagram.com/estatebypravan/" target="_blank">Instagram</a>
</div>
""", unsafe_allow_html=True)
