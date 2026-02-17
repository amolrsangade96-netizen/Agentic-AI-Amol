import streamlit as st
from groq import Groq
import pandas as pd

# --- PAGE CONFIG ---
st.set_page_config(page_title="Aura Agentic AI", page_icon="💎", layout="wide")

# --- ULTRA PREMIUM CSS ---
st.markdown("""
    <style>
    /* Animated Background */
    .stApp {
        background: #050505;
        color: #ffffff;
    }
    
    /* Glowing Border Animation */
    @keyframes rotate {
        100% { transform: rotate(360deg); }
    }
    
    .glow-card {
        position: relative;
        background: #121212;
        border-radius: 15px;
        padding: 3px;
        z-index: 1;
        overflow: hidden;
        margin-bottom: 25px;
    }
    
    .glow-card::before {
        content: '';
        position: absolute;
        width: 150%;
        height: 150%;
        background: conic-gradient(#00f2ff, #ff00c8, #00f2ff);
        animation: rotate 4s linear infinite;
        top: -25%;
        left: -25%;
        z-index: -1;
    }
    
    .content-box {
        background: #0f0f0f;
        padding: 30px;
        border-radius: 12px;
        color: white;
    }

    /* Professional Title */
    .main-title {
        background: -webkit-linear-gradient(#00f2ff, #ff00c8);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-size: 60px;
        font-weight: 800;
        text-align: center;
        letter-spacing: -2px;
    }

    /* Buttons */
    .stButton>button {
        background: linear-gradient(90deg, #00f2ff, #ff00c8);
        border: none;
        border-radius: 8px;
        color: white;
        font-weight: bold;
        padding: 15px;
        width: 100%;
        transition: 0.3s ease;
    }
    .stButton>button:hover {
        box-shadow: 0 0 25px rgba(0, 242, 255, 0.6);
        transform: scale(1.02);
    }
    </style>
    """, unsafe_allow_html=True)

# --- HEADER ---
st.markdown("<h1 class='main-title'>AURA AGENTIC AI</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center; opacity:0.6; margin-top:-20px;'>HIGH-PERFORMANCE INTELLIGENCE INTERFACE</p>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center; color:#00f2ff; font-weight:bold;'>OPERATOR: AMOL</p>", unsafe_allow_html=True)
st.write("<br>", unsafe_allow_html=True)

# --- SIDEBAR ---
with st.sidebar:
    st.markdown("### ⚙️ SYSTEM CONFIG")
    st.write("---")
    st.markdown("**Core:** Llama-3.1-8B")
    st.markdown("**Latency:** 0.4ms")
    st.write("---")
    if st.button("RESET SESSION"):
        st.session_state.history = []
        st.rerun()

# --- API ---
GROQ_API_KEY = "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" 
client = Groq(api_key=GROQ_API_KEY)

if "history" not in st.session_state:
    st.session_state.history = []

# --- INPUT AREA ---
st.markdown('<div class="glow-card"><div class="content-box">', unsafe_allow_html=True)
user_query = st.text_input("QUERY INPUT", placeholder="Ask me anything...", label_visibility="collapsed")
if st.button("INITIALIZE ANALYSIS") and user_query:
    with st.spinner("Processing..."):
        try:
            completion = client.chat.completions.create(
                model="llama-3.1-8b-instant",
                messages=[{"role": "user", "content": user_query}],
                temperature=0.3
            )
            st.session_state.history.insert(0, (user_query, completion.choices[0].message.content))
        except Exception as e:
            st.error(f"Error: {e}")
st.markdown('</div></div>', unsafe_allow_html=True)

# --- OUTPUT ---
for q, a in st.session_state.history:
    st.markdown(f'''
        <div style="border-left: 4px solid #ff00c8; padding-left: 20px; margin-bottom: 30px;">
            <p style="color:#00f2ff; font-weight:bold; font-size:12px;">// USER_QUERY</p>
            <p style="font-size:18px;">{q}</p>
            <p style="color:#ff00c8; font-weight:bold; font-size:12px; margin-top:15px;">// AGENT_RESPONSE</p>
            <p style="opacity:0.9; line-height:1.6;">{a}</p>
        </div>
    ''', unsafe_allow_html=True)
