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
st.markdown("<div class='subtitle'>AI-powered UAE road traffic simulation system</div>", unsafe_allow_html=True)

# =========================
# INPUT
# =========================
location = st.text_input("📍 Enter UAE road or street (e.g. Sheikh Zayed Road, Corniche, Airport Road)")

# =========================
# 🚦 ROAD-BASED IMAGE ENGINE (FIXED VERSION)
# =========================
def get_city_image(loc):
    loc = loc.lower()

    # =========================
    # HIGHWAYS (VERY BUSY)
    # =========================
    highways = [
        "https://images.unsplash.com/photo-1502877338535-766e1452684a",
        "https://images.unsplash.com/photo-1494515843206-f3117d3f511e",
        "https://images.unsplash.com/photo-1477959858617-67f85cf4f1df",
        "https://images.unsplash.com/photo-1518609375289-7f6d2c3c5b7a"
    ]

    # =========================
    # URBAN MAIN ROADS (MODERATE TRAFFIC)
    # =========================
    urban_roads = [
        "https://images.unsplash.com/photo-1506521781263-d8422e82f27a",
        "https://images.unsplash.com/photo-1480714378408-67cf0d13bc1b",
        "https://images.unsplash.com/photo-1526401485004-2aa7f1f4a0a3",
        "https://images.unsplash.com/photo-1501594907352-04cda38ebc29"
    ]

    # =========================
    # CITY STREETS (LIGHT TRAFFIC)
    # =========================
    city_streets = [
        "https://images.unsplash.com/photo-1449824913935-59a10b8d2000",
        "https://images.unsplash.com/photo-1500043357865-c6b8827edf9f",
        "https://images.unsplash.com/photo-1520607162513-77705c0f0d4a"
    ]

    import random

    # =========================
    # ROAD DETECTION LOGIC
    # =========================
    if any(word in loc for word in ["sheikh zayed", "highway", "expressway", "e11"]):
        return random.choice(highways)

    elif any(word in loc for word in ["airport road", "corniche", "downtown", "city center"]):
        return random.choice(urban_roads)

    else:
        return random.choice(city_streets)

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
    # CAMERA FEED
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
    # AI ANALYSIS
    # =========================
    st.subheader("🧠 AI Traffic Analysis")

    st.write(f"""
📍 **Location:** {location}

- AI detects road type (highway / urban / street)
- Traffic density simulated using probabilistic model
- Speed flow adjusted dynamically
- Estimated clearance time calculated

### 📊 Result:
Traffic will normalize in approximately **{time_clear} minutes**
""")

    # =========================
    # CONTEXT
    # =========================
    st.subheader("🇦🇪 UAE Smart City Context")

    st.write("""
UAE transport systems use smart infrastructure to:
- Reduce congestion on highways
- Optimize traffic light systems
- Monitor road usage in real-time
- Improve emergency response routes
""")

else:
    st.info("Enter a UAE road or street to begin analysis 🚦")
