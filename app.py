import streamlit as st
import random
import time

# =========================
# PAGE CONFIG
# =========================
st.set_page_config(
    page_title="Smart Traffic Control Center",
    layout="wide"
)

# =========================
# NAVY BLUE + MODERN FONT UI
# =========================
st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;800&display=swap');

.stApp {
    background-color: #061a33;
    color: white;
    font-family: 'Inter', sans-serif;
}

.title {
    font-size: 46px;
    font-weight: 800;
    text-align: center;
    color: white;
}

.subtitle {
    text-align: center;
    font-size: 18px;
    color: #cbd5e1;
    margin-bottom: 20px;
}

.card {
    background: #0b2a4a;
    padding: 20px;
    border-radius: 18px;
    box-shadow: 0px 6px 20px rgba(0,0,0,0.3);
    color: white;
}

.big {
    font-size: 34px;
    font-weight: 700;
}

.small {
    color: #94a3b8;
}

</style>
""", unsafe_allow_html=True)

# =========================
# HEADER (NO "UNIVERSITY LEVEL" TEXT)
# =========================
st.markdown("<div class='title'>🚦 Smart Traffic Control Center</div>", unsafe_allow_html=True)

st.markdown("<div class='subtitle'>AI-powered simulation of urban traffic flow and congestion prediction</div>", unsafe_allow_html=True)

# UAE CITY IMAGE ONLY
st.image("https://images.unsplash.com/photo-1526495124232-a04e1849168c")

# =========================
# LOCATION INPUT
# =========================
location = st.text_input("📍 Enter a UAE road or city (e.g. Sheikh Zayed Road, Dubai)")

# =========================
# AI ENGINE (MORE REALISTIC)
# =========================
def traffic_ai(location):
    seed = sum(ord(i) for i in location)
    random.seed(seed)

    congestion = random.randint(10, 95)
    speed = random.randint(20, 140)

    density_factor = (len(location) % 7) + 2

    time_clear = max(3, int((congestion * density_factor) / (speed / 18)))

    return congestion, speed, time_clear

# =========================
# RUN SYSTEM
# =========================
if location:

    congestion, speed, time_clear = traffic_ai(location)

    st.markdown("---")

    # =========================
    # DASHBOARD CARDS
    # =========================
    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("<div class='card'>🚗 Congestion</div>", unsafe_allow_html=True)
        st.markdown(f"<div class='big'>{congestion}%</div>", unsafe_allow_html=True)

    with col2:
        st.markdown("<div class='card'>🚙 Speed</div>", unsafe_allow_html=True)
        st.markdown(f"<div class='big'>{speed} km/h</div>", unsafe_allow_html=True)

    with col3:
        st.markdown("<div class='card'>⏱️ Time to Clear</div>", unsafe_allow_html=True)
        st.markdown(f"<div class='big'>{time_clear} min</div>", unsafe_allow_html=True)

    st.markdown("---")

    # =========================
    # UAE CITY VISUALS ONLY
    # =========================
    st.subheader("🌆 Live Traffic View (UAE)")

    st.image("https://images.unsplash.com/photo-1512453979798-5ea266f8880c")  # Dubai highway
    st.image("https://images.unsplash.com/photo-1518684079-3c830dcef090")   # Abu Dhabi roads

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
    # AI INSIGHT PANEL
    # =========================
    st.subheader("🧠 AI Traffic Insight")

    st.write(f"""
Location analyzed: **{location}**

- Congestion level detected from simulated sensor network
- Vehicle speed flow estimated using AI model
- Predicted clearance time calculated dynamically

### Result:
- Congestion: {congestion}%
- Speed: {speed} km/h
- Clear in: {time_clear} minutes
""")

    # =========================
    # UAE SMART CITY SECTION
    # =========================
    st.subheader("🇦🇪 Smart City Infrastructure")

    st.image("https://images.unsplash.com/photo-1508385082359-f38ae991e8f2")

    st.write("""
Cities like Dubai and Abu Dhabi use intelligent traffic systems to:
- Reduce congestion on highways
- Optimize traffic light timing
- Improve emergency response
- Support rapid urban growth
""")

else:
    st.info("Enter a UAE location to generate smart traffic analysis")
