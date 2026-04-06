import streamlit as st
import random

# =========================
# PAGE CONFIG
# =========================
st.set_page_config(
    page_title="AI Traffic Intelligence System",
    layout="wide"
)

# =========================
# UI DESIGN (BABY PINK THEME)
# =========================
st.markdown("""
<style>

.stApp {
    background-color: #ffe4ec;
    color: black;
    font-family: Arial;
}

.title {
    font-size: 44px;
    font-weight: 900;
    text-align: center;
    color: black;
}

.subtitle {
    text-align: center;
    font-size: 18px;
    margin-bottom: 20px;
}

.card {
    background: white;
    padding: 20px;
    border-radius: 20px;
    box-shadow: 0px 6px 20px rgba(0,0,0,0.1);
}

.big {
    font-size: 32px;
    font-weight: bold;
}

</style>
""", unsafe_allow_html=True)

# =========================
# HEADER
# =========================
st.markdown("<div class='title'>🚦 AI Traffic Intelligence System</div>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>University-level simulation of smart city traffic prediction</div>", unsafe_allow_html=True)

st.image("https://images.unsplash.com/photo-1506521781263-d8422e82f27a", use_container_width=True)

# =========================
# INPUT (LOCATION BASED AI)
# =========================
location = st.text_input("📍 Enter a road / street / city (e.g. Sheikh Zayed Road, Dubai)")

# =========================
# AI ENGINE (REALISTIC SIMULATION)
# =========================
def traffic_ai(location):
    seed = sum(ord(i) for i in location)
    random.seed(seed)

    congestion = random.randint(15, 95)
    speed = random.randint(20, 120)

    # AI logic (more realistic)
    complexity_factor = len(location) % 10 + 1

    time_clear = max(5, int((congestion * complexity_factor) / (speed / 15)))

    return congestion, speed, time_clear, complexity_factor

# =========================
# RUN ONLY IF LOCATION ENTERED
# =========================
if location:

    congestion, speed, time_clear, complexity = traffic_ai(location)

    st.markdown("---")

    # =========================
    # DASHBOARD CARDS
    # =========================
    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("<div class='card'>", unsafe_allow_html=True)
        st.write("🚗 Congestion Level")
        st.markdown(f"<div class='big'>{congestion}%</div>", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)

    with col2:
        st.markdown("<div class='card'>", unsafe_allow_html=True)
        st.write("🚙 Average Speed")
        st.markdown(f"<div class='big'>{speed} km/h</div>", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)

    with col3:
        st.markdown("<div class='card'>", unsafe_allow_html=True)
        st.write("⏱️ Time to Clear")
        st.markdown(f"<div class='big'>{time_clear} min</div>", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("---")

    # =========================
    # TRAFFIC STATUS
    # =========================
    st.subheader("📊 Traffic Status")

    st.image("https://images.unsplash.com/photo-1486308510493-cb9b3a1f9c5a")

    if congestion > 70:
        st.error("🔴 Heavy Traffic — Severe congestion detected")
    elif congestion > 40:
        st.warning("🟡 Moderate Traffic — Some delays expected")
    else:
        st.success("🟢 Light Traffic — Smooth movement")

    # =========================
    # AI EXPLANATION
    # =========================
    st.subheader("🧠 AI Prediction Model")

    st.write(f"""
For **{location}**, the AI system analyzed:

- Road complexity score: {complexity}
- Vehicle density simulation
- Speed-flow correlation

### Result:
- Estimated congestion: **{congestion}%**
- Average speed: **{speed} km/h**
- Predicted clearance time: **{time_clear} minutes**

This model mimics how smart city systems evaluate traffic flow in real time.
""")

    # =========================
    # IMPACT SECTION
    # =========================
    st.subheader("🌍 Smart City Impact")

    st.image("https://images.unsplash.com/photo-1494522358652-f30e61a60313")

    st.write("""
AI traffic systems help modern cities:

- Reduce congestion
- Improve emergency response times
- Optimize road networks
- Lower carbon emissions
""")

else:
    st.info("👆 Enter a location above to generate AI traffic analysis")
