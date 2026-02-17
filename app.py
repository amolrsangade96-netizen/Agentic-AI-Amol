import streamlit as st
from groq import Groq
import io
import sys
import re
import math

# --- PAGE CONFIGURATION ---
st.set_page_config(page_title="Agentic AI", page_icon="🚀", layout="centered")

# --- ADVANCED CYBERPUNK CSS ---
st.markdown("""
    <style>
    /* Main Background */
    .stApp {
        background: radial-gradient(circle, #1a1a2e 0%, #0f0f1a 100%);
        color: #e0e0e0;
    }

    /* Header Styling */
    h1 {
        text-align: center;
        color: #00d4ff;
        font-family: 'Orbitron', sans-serif;
        text-shadow: 0px 0px 15px #00d4ff;
        font-size: 55px;
        letter-spacing: 5px;
        margin-bottom: 0px;
    }
    p.dev-text {
        text-align: center;
        color: #ff00ff;
        font-weight: bold;
        text-transform: uppercase;
        letter-spacing: 2px;
        margin-top: -10px;
    }

    /* Input Box Styling */
    .stTextInput>div>div>input {
        background-color: #16213e;
        color: #00ffcc;
        border: 2px solid #0f3460;
        border-radius: 15px;
        padding: 15px;
        font-size: 18px;
        transition: 0.3s;
    }
    .stTextInput>div>div>input:focus {
        border: 2px solid #00d4ff;
        box-shadow: 0px 0px 15px #00d4ff;
    }

    /* Button Styling */
    div.stButton > button:first-child {
        background: linear-gradient(45deg, #ff00ff, #00d4ff);
        color: white;
        border: none;
        padding: 15px 30px;
        border-radius: 12px;
        font-weight: bold;
        font-size: 20px;
        width: 100%;
        transition: 0.5s;
        text-transform: uppercase;
    }
    div.stButton > button:hover {
        transform: scale(1.02);
        box-shadow: 0px 0px 20px #ff00ff;
    }

    /* System Terminal Output */
    .output-box {
        background: rgba(0, 0, 0, 0.7);
        color: #a6e3a1;
        padding: 25px;
        border-radius: 20px;
        border: 1px solid #00ffcc;
        font-family: 'Consolas', monospace;
        box-shadow: inset 0px 0px 10px #00ffcc;
        margin-top: 20px;
    }

    /* User Message Style */
    .user-msg {
        color: #f9e2af;
        font-weight: bold;
        border-bottom: 1px solid #313244;
        padding-bottom: 10px;
        margin-bottom: 15px;
    }
    
    /* Separator */
    hr { border: 1px solid #313244; }
    </style>
    """, unsafe_allow_html=True)

# --- HEADER ---
st.markdown("<h1>AGENTIC AI</h1>", unsafe_allow_html=True)
st.markdown("<p class='dev-text'>● Developed by Amol Sir ●</p>", unsafe_allow_html=True)
st.write("---")

# --- API SETUP ---
# 
GROQ_API_KEY = "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" 
client = Groq(api_key=GROQ_API_KEY)

# --- APP LOGIC ---
if "history" not in st.session_state:
    st.session_state.history = []

# Input Section inside a styled container
user_input = st.text_input("", placeholder="Enter your command here...", key="input")

col1, col2 = st.columns([3, 1])
with col1:
    submit_btn = st.button("🚀 INITIALIZE ANALYSIS")
with col2:
    if st.button("🔄 RESET"):
        st.session_state.history = []
        st.rerun()

if submit_btn and user_input:
    with st.spinner("Accessing AI Core..."):
        try:
            system_instruction = "You are a futuristic Super-AI. Use professional formatting."
            completion = client.chat.completions.create(
                model="llama-3.1-8b-instant",
                messages=[{"role": "system", "content": system_instruction},
                          {"role": "user", "content": user_input}],
                temperature=0.3
            )
            ai_response = completion.choices[0].message.content.strip()
            st.session_state.history.insert(0, (user_input, ai_response))
        except Exception as e:
            st.error(f"System Error: {str(e)}")

# --- TERMINAL DISPLAY ---
st.markdown("<p style='color:#00ffcc; font-family:monospace;'>[SYSTEM TERMINAL ACTIVE]</p>", unsafe_allow_html=True)

for q, a in st.session_state.history:
    st.markdown(f"""
    <div class="output-box">
        <div class="user-msg">👤 USER_QUERY > {q}</div>
        <div class="ai-msg">🤖 AI_RESPONSE > <br><br>{a}</div>
    </div>
    """, unsafe_allow_html=True)
