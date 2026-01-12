import streamlit as st
from streamlit_autorefresh import st_autorefresh
import pyttsx3
import random

# -----------------------------
# Jarvis Voice Setup
# -----------------------------
engine = pyttsx3.init()
engine.setProperty('rate', 170)   # Speed of speech
engine.setProperty('volume', 1)   # Max volume
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)  # 0 = male, 1 = female

def jarvis_speak(text):
    engine.say(text)
    engine.runAndWait()

# -----------------------------
# Streamlit Page Config
# -----------------------------
st.set_page_config(page_title="JARVIS Dashboard", layout="wide")

# -----------------------------
# Jarvis Theme (CSS + Animations)
# -----------------------------
st.markdown("""
    <style>
    .stApp {
        background: radial-gradient(circle, rgba(0,255,255,0.05) 1px, transparent 1px);
        background-size: 40px 40px;
        background-color: #0d0d0d;
        color: #00f5ff;
        font-family: 'Orbitron', sans-serif;
    }
    .radar {
        position: fixed;
        top: 50%;
        left: 50%;
        width: 400px;
        height: 400px;
        margin-left: -200px;
        margin-top: -200px;
        border-radius: 50%;
        border: 2px solid rgba(0,255,255,0.2);
        animation: spin 5s linear infinite;
        box-shadow: 0px 0px 40px rgba(0,255,255,0.3);
        z-index: -1;
    }
    @keyframes spin { 0% { transform: rotate(0deg);} 100% { transform: rotate(360deg);} }
    .voice-wave { display:flex;justify-content:center;align-items:flex-end;height:50px;gap:4px; }
    .voice-wave span { width:6px;background:#00f5ff;animation:wave 1s infinite ease-in-out; }
    .voice-wave span:nth-child(1){animation-delay:0s;} .voice-wave span:nth-child(2){animation-delay:0.1s;}
    .voice-wave span:nth-child(3){animation-delay:0.2s;} .voice-wave span:nth-child(4){animation-delay:0.3s;}
    .voice-wave span:nth-child(5){animation-delay:0.4s;}
    @keyframes wave { 0%,100%{height:10px;} 50%{height:40px;} }
    .stCard { background:rgba(0,255,255,0.05); border:1px solid #00f5ff;
              border-radius:15px;padding:20px;box-shadow:0px 0px 20px rgba(0,255,255,0.4); }
    .stCard:hover { box-shadow:0px 0px 40px rgba(0,255,255,0.8); transform:scale(1.02); }
    .stButton>button { color:#00f5ff;border:1px solid #00f5ff;background:black;
                       border-radius:8px;padding:10px 20px; }
    .stButton>button:hover { background:#00f5ff;color:black;box-shadow:0px 0px 20px #00f5ff; }
    </style>
    <div class="radar"></div>
""", unsafe_allow_html=True)

# -----------------------------
# Auto Refresh (fix for old bug)
# -----------------------------
st_autorefresh(interval=5000, key="refresh")

# -----------------------------
# Dashboard Layout
# -----------------------------
st.title("🤖 J.A.R.V.I.S. Assistant System")

col1, col2 = st.columns(2)

# -----------------------------
# LEFT PANEL
# -----------------------------
with col1:
    # Voice Status
    st.markdown("### 🎤 Voice Status")
    st.markdown('<div class="stCard"><div class="voice-wave">' +
                ''.join(["<span></span>" for _ in range(5)]) +
                "</div><p style='text-align:center;'>Listening...</p></div>", unsafe_allow_html=True)

    # Task Manager
    st.markdown("### 📋 Task Manager")
    tasks = ["Organize Desktop", "Clean Downloads", "Update Notes"]
    st.markdown(f'<div class="stCard">{"<br>".join(tasks)}</div>', unsafe_allow_html=True)

    # Task Execution Button
    if st.button("✅ Execute Task"):
        jarvis_speak("Sir, I have completed the task successfully.")
        st.success("Task Executed!")

# -----------------------------
# RIGHT PANEL
# -----------------------------
with col2:
    # System Monitor (random data for now)
    st.markdown("### 📊 System Monitor")
    st.line_chart({"CPU %": [random.randint(20,80) for _ in range(5)],
                   "RAM %": [random.randint(40,70) for _ in range(5)]})

    # Agent Logs
    st.markdown("### ⚡ Agent Logs")
    st.markdown('<div class="stCard">Awaiting commands...</div>', unsafe_allow_html=True)
