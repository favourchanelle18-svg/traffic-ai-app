import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(page_title="Smart Traffic AI", layout="wide")

# 🌈 STYLE (BABY BLUE UI)
st.markdown("""
<style>
.stApp {
    background-color: #d6f0ff;
}
.title {
    font-size: 40px;
    font-weight: bold;
    color: #0b3d91;
}
.card {
    background-color: white;
    padding: 20px;
    border-radius: 20px;
    box-shadow: 0px 4px 15px rgba(0,0,0,0.1);
}
</style>
""", unsafe_allow_html=True)

# HEADER
st.markdown("<div class='title'>🚦 AI Smart Traffic Controller</div>", unsafe_allow_html=True)

st.write("Simulating smart city traffic optimization inspired by modern cities.")

st.image("https://images.unsplash.com/photo-1494526585095-c41746248156", use_container_width=True)

# LOAD DATA
df = pd.DataFrame({
    "time": [0,1,2,3,4,5,6,7,8],
    "base_congestion": [30,45,60,85,95,90,70,50,35]
})

# SIDEBAR
st.sidebar.header("⚙️ Control Panel")

cars = st.sidebar.slider("🚗 Cars", 50, 500, 200)
peak = st.sidebar.slider("⏰ Peak", 1, 10, 5)
ai = st.sidebar.toggle("🧠 AI ON/OFF", value=True)

# MODEL
base = min(100, cars*0.3 + peak*5)
optimized = base * 0.55 if ai else base

pollution = optimized * 1.6
delay = optimized * 0.6

# CARDS
col1, col2, col3 = st.columns(3)

col1.metric("🚗 Congestion", f"{int(optimized)}%")
col2.metric("🌫️ Pollution", f"{int(pollution)} AQI")
col3.metric("⏱️ Delay", f"{int(delay)} min")

# GRAPH
df["ai"] = df["base_congestion"] * 0.6 if ai else df["base_congestion"]
st.line_chart(df.set_index("time"))

# IMPACT
st.markdown("## 🌍 Impact")
st.write("AI reduces congestion, emissions, and improves traffic flow in smart cities like Dubai and Singapore.")
