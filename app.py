import streamlit as st
import random
import time

# =========================
# PAGE SETUP
# =========================
st.set_page_config(
    page_title="Live Smart Traffic Control Center",
    layout="wide"
)

# =========================
# PREMIUM UI DESIGN (NAVY + GLASS)
# =========================
st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;500;700;900&display=swap');

.stApp {
    background-color: #050f1f;
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
    color: #a5b4fc;
    margin-bottom: 20px;
}

.card {
    background: rgba(255,255,255,0.06);
    padding: 18px;
    border-radius: 16px;
    backdrop-filter: blur(10px);
    box-shadow: 0 8px 30px rgba(0,0,0,0.4);
}

.big {
    font-size: 34px;
    font-weight: 800;
}

.car-bar {
    height: 20px;
    border-radius: 10px;
    background: linear-gradient(90deg, #22c55e, #eab308, #ef4444);
}

</style>
""", unsafe_allow_html=True)

# =========================
# HEADER
# =========================
st.markdown("<div class='title'>🚦 Live Smart Traffic Control Center</div>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>Real-time AI traffic simulation for UAE smart cities</div>", unsafe_allow_html=True)

st.image("https://images.unsplash.com/photo-1518684079-3c830dcef090")

# =========================
# LOCATION INPUT
# =========================
location = st.text_input("📍 Enter UAE road or city (Dubai / Abu Dhabi / Sheikh Zayed Road)")

# =========================
# AI TRAFFIC ENGINE (DYNAMIC)
# =========================
def generate_traffic(location):
    seed = sum(ord(c) for c in location) + int(time.time()) // 5
    random.seed(seed)

    congestion = random.randint(10, 95)
    speed = random.randint(20, 140)

    cars_visual = congestion // 2  # visual simulation

    time_clear = max(2, int((congestion * 1.5) / (speed / 20)))

    return congestion, speed, cars_visual, time_clear

# =========================
# LIVE SIMULATION AREA
# =========================
placeholder = st.empty()

# =========================
# RUN SYSTEM
# =========================
if location:

    for i in range(5):  # live simulation loop
        congestion, speed, cars, time_clear = generate_traffic(location)

        with placeholder.container():

            st.markdown("---")

            # =========================
            # DASHBOARD
            # =========================
            col1, col2, col3 = st.columns(3)

            col1.markdown("<div class='card'>🚗 Congestion</div>", unsafe_allow_html=True)
            col1.markdown(f"<div class='big'>{congestion}%</div>", unsafe_allow_html=True)

            col2.markdown("<div class='card'>🚙 Speed</div>", unsafe_allow_html=True)
            col2.markdown(f"<div class='big'>{speed} km/h</div>", unsafe_allow_html=True)

            col3.markdown("<div class='card'>⏱️ Clear Time</div>", unsafe_allow_html=True)
            col3.markdown(f"<div class='big'>{time_clear} min</div>", unsafe_allow_html=True)

            st.markdown("---")

            # =========================
            # “ANIMATED” TRAFFIC BARS
            # =========================
            st.subheader("🚦 Live Traffic Flow Simulation")

            st.write("Cars on road (simulated movement intensity):")

            st.progress(cars / 50)

            st.write("Traffic density visualization:")
            st.markdown(f"<div class='car-bar' style='width:{congestion}%;'></div>", unsafe_allow_html=True)

            # =========================
            # STATUS
            # =========================
            if congestion > 70:
                st.error("🔴 Heavy Traffic — Slow movement detected")
            elif congestion > 40:
                st.warning("🟡 Moderate Traffic — Flow unstable")
            else:
                st.success("🟢 Smooth Traffic — High mobility")

            # =========================
            # UAE VISUALS ONLY
            # =========================
            st.subheader("🌆 UAE Smart City Feed")

            st.image("https://images.unsplash.com/photo-1526495124232-a04e1849168c")  # Dubai skyline
            st.image("https://images.unsplash.com/photo-1508385082359-f38ae991e8f2")  # Abu Dhabi roads

            st.write(f"Live monitoring: {location}")

        time.sleep(1)

else:
    st.info("Enter a UAE location to start live traffic simulation")
