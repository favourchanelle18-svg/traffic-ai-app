import streamlit as st
import random

# =========================
# PAGE SETUP
# =========================
st.set_page_config(page_title="Smart Traffic Intelligence", layout="wide")

# =========================
# UI DESIGN
# =========================
st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;500;700;900&display=swap');

.stApp {
    background-color: #061428;
    font-family: 'Inter', sans-serif;
    color: white;
}

.title {
    font-size: 48px;
    font-weight: 900;
    text-align: center;
}

.subtitle {
    text-align: center;
    color: #93c5fd;
    margin-bottom: 20px;
}

.card {
    background: rgba(255,255,255,0.06);
    padding: 18px;
    border-radius: 16px;
    backdrop-filter: blur(10px);
    box-shadow: 0 10px 30px rgba(0,0,0,0.4);
}

.big {
    font-size: 34px;
    font-weight: 800;
}

</style>
""", unsafe_allow_html=True)

# =========================
# HEADER
# =========================
st.markdown("<div class='title'>🚦 Smart Traffic Intelligence Dashboard</div>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>AI-powered simulation of UAE road traffic systems</div>", unsafe_allow_html=True)

# =========================
# INPUT
# =========================
location = st.text_input("📍 Enter UAE road / city (Dubai, Abu Dhabi, Sharjah, etc.)")

# =========================
# REALISTIC BUSY ROAD IMAGE SYSTEM
# =========================
def get_city_image(loc):
    loc = loc.lower()

    dubai_images = [
        "https://images.unsplash.com/photo-1506377247377-2a5b3b417ebb",
        "https://images.unsplash.com/photo-1493238792000-8113da705763",
        "https://images.unsplash.com/photo-1526498460520-4c246339dccb"
    ]

    abu_dhabi_images = [
        "https://images.unsplash.com/photo-1526481280698-8fcc13fd85a3",
        "https://images.unsplash.com/photo-1518684079-3c830dcef090",
        "https://images.unsplash.com/photo-1501785888041-af3ef285b470"
    ]

    highway_images = [
        "https://images.unsplash.com/photo-1494515843206-f3117d3f511e",
        "https://images.unsplash.com/photo-1502877338535-766e1452684a",
        "https://images.unsplash.com/photo-1477959858617-67f85cf4f1df"
    ]

    if "dubai" in loc:
        return random.choice(dubai_images)
    elif "abu dhabi" in loc:
        return random.choice(abu_dhabi_images)
    else:
        return random.choice(highway_images)

# =========================
# AI TRAFFIC ENGINE (SIMULATED)
# =========================
def ai_engine(location):
    seed = sum(ord(i) for i in location)
    random.seed(seed)

    congestion = random.randint(15, 95)
    speed = random.randint(20, 140)
    time_clear = max(3, int(congestion / (speed / 18)))

    return congestion, speed, time_clear

# =========================
# RUN APP
# =========================
if location:

    congestion, speed, time_clear = ai_engine(location)

    st.markdown("---")

    # =========================
    # METRICS
    # =========================
    col1, col2, col3 = st.columns(3)

    col1.markdown("<div class='card'>🚗 Congestion</div>", unsafe_allow_html=True)
    col1.markdown(f"<div class='big'>{congestion}%</div>", unsafe_allow_html=True)

    col2.markdown("<div class='card'>🚙 Average Speed</div>", unsafe_allow_html=True)
    col2.markdown(f"<div class='big'>{speed} km/h</div>", unsafe_allow_html=True)

    col3.markdown("<div class='card'>⏱️ Time to Clear</div>", unsafe_allow_html=True)
    col3.markdown(f"<div class='big'>{time_clear} min</div>", unsafe_allow_html=True)

    st.markdown("---")

    # =========================
    # CAMERA FEED (SIMULATED)
    # =========================
    st.subheader("📹 Live Traffic Camera Feed (Simulated)")

    st.image(get_city_image(location), use_container_width=True)

    # =========================
    # TRAFFIC STATUS
    # =========================
    if congestion > 70:
        st.error("🔴 Heavy Traffic Detected")
    elif congestion > 40:
        st.warning("🟡 Moderate Traffic Flow")
    else:
        st.success("🟢 Smooth Traffic Conditions")

    # =========================
    # AI INSIGHT
    # =========================
    st.subheader("🧠 AI Traffic Analysis")

    st.write(f"""
📍 Location: **{location}**

- AI congestion model based on road density simulation  
- Vehicle flow estimated using probabilistic engine  
- Speed distribution analyzed dynamically  
- Clearance time predicted in real-time simulation  

### 🧾 Result:
Traffic is expected to normalize in approximately **{time_clear} minutes**
""")

    # =========================
    # SMART CITY CONTEXT
    # =========================
    st.subheader("🇦🇪 UAE Smart City Context")

    st.write("""
UAE smart cities use advanced transport systems including:
- AI traffic monitoring
- Smart signal control
- Highway congestion optimization
- Real-time road analytics

This simulation demonstrates how such systems behave at a conceptual level.
""")

else:
    st.info("Enter a UAE location to begin analysis 🚦")
