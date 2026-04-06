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
# LOCATION INPUT
# =========================
location = st.text_input("📍 Enter UAE road / city (Dubai, Abu Dhabi, etc.)")

# =========================
# SMART IMAGE SYSTEM (NO API NEEDED)
# =========================
def get_city_image(loc):
    loc = loc.lower()

    if "dubai" in loc:
        return "https://images.unsplash.com/photo-1512453979798-5ea266f8880c"
    elif "abu dhabi" in loc:
        return "https://images.unsplash.com/photo-1526495124232-a04e1849168c"
    elif "sharjah" in loc:
        return "https://images.unsplash.com/photo-1508609349937-5ec4ae374ebf"
    else:
        return "https://images.unsplash.com/photo-1506521781263-d8422e82f27a"

# =========================
# AI ENGINE (SIMULATED)
# =========================
def ai_engine(location):
    seed = sum(ord(i) for i in location)
    random.seed(seed)

    congestion = random.randint(15, 95)
    speed = random.randint(20, 140)
    time_clear = max(3, int(congestion / (speed / 18)))

    return congestion, speed, time_clear

# =========================
# RUN
# =========================
if location:

    congestion, speed, time_clear = ai_engine(location)

    st.markdown("---")

    # =========================
    # DASHBOARD
    # =========================
    col1, col2, col3 = st.columns(3)

    col1.markdown("<div class='card'>🚗 Congestion</div>", unsafe_allow_html=True)
    col1.markdown(f"<div class='big'>{congestion}%</div>", unsafe_allow_html=True)

    col2.markdown("<div class='card'>🚙 Speed</div>", unsafe_allow_html=True)
    col2.markdown(f"<div class='big'>{speed} km/h</div>", unsafe_allow_html=True)

    col3.markdown("<div class='card'>⏱️ Time to Clear</div>", unsafe_allow_html=True)
    col3.markdown(f"<div class='big'>{time_clear} min</div>", unsafe_allow_html=True)

    st.markdown("---")

    # =========================
    # VISUAL FEED (FAKE TRAFFIC CAMERA)
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
Location: **{location}**

- AI estimated congestion based on road density simulation
- Vehicle speed flow analyzed using probabilistic model
- Predicted clearance time computed dynamically

### Result:
Traffic will normalize in approximately **{time_clear} minutes**
""")

    # =========================
    # UAE SMART CITY CONTEXT
    # =========================
    st.subheader("🇦🇪 Smart City Context")

    st.write("""
Modern UAE cities use intelligent transport systems to:
- Reduce congestion on highways
- Optimize signal timings
- Improve emergency response
- Support rapid urban expansion
""")

else:
    st.info("Enter a UAE location to begin analysis")
