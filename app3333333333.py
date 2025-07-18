# app.py

import streamlit as st

# Page config
st.set_page_config(page_title="Muhammad Awasu | Motivation Speaker", layout="centered")

# Header
st.title("✨ Muhammad Awasu")
st.subheader("🎤 Motivational Speaker | Inspiring Youth | Empowering Change")

# Bio/About
st.markdown("""
I am Muhammad Awasu, a passionate motivational speaker dedicated to uplifting individuals and transforming mindsets.  
My mission is to **ignite confidence, resilience, and clarity** in people from all walks of life — especially those who feel lost, discouraged, or unheard.

> 💡 *“Your today doesn't define your tomorrow.”*
""")

# Add a video or YouTube embed (optional)
st.markdown("### 🎥 Sample Talk")
st.video("https://www.youtube.com/watch?v=ZXsQAXx_ao0")  # Replace with your real video link

# Quote section
st.markdown("### 📝 Featured Quotes")
st.success("“The darkest nights produce the brightest stars.”")
st.info("“You are more capable than you believe.”")

# Contact
st.markdown("### 📬 Contact Me")
contact_form = """
<form action="https://formsubmit.co/YOUR_EMAIL@example.com" method="POST">
     <input type="text" name="name" placeholder="Your name" required>
     <input type="email" name="email" placeholder="Your email" required>
     <textarea name="message" placeholder="Your message here..." required></textarea>
     <button type="submit">Send</button>
</form>
"""
st.markdown(contact_form, unsafe_allow_html=True)

st.markdown("---")
st.caption("Made with ❤️ by Muhammad Awasu | Powered by Streamlit")

# Hide Streamlit branding (optional, Pro only)
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)
