import streamlit as st
from PIL import Image

# Page config
st.set_page_config(page_title="Muhammad Awais | Motivational Speaker", layout="centered")

# Load and display image
image = Image.open("awais.jpg")  # Replace with your actual image filename
st.image(image, width=300, caption="Muhammad Awais", use_column_width=False)

# Title and subtitle
st.title("✨ Muhammad Awais")
st.subheader("🎤 Motivational Speaker | Empowering Youth | Igniting Change")

# Bio
st.markdown("""
Hello! I am **Muhammad Awais**, a passionate motivational speaker dedicated to helping others discover their inner potential.  
I believe that every person has the power to rise above their circumstances and become unstoppable.  

> 💬 *“Your struggles are your strength.”*
""")

# Quotes
st.markdown("### 💡 Signature Quotes")
st.success("“In every challenge lies the seed of growth.”")
st.info("“One powerful thought can change your entire life.”")

# Video Section
st.markdown("### 🎥 Watch My Talk")
st.video("https://www.youtube.com/watch?v=ZXsQAXx_ao0")  # Replace with your own video

# Contact Form
st.markdown("### 📬 Get In Touch")
contact_form = """
<form action="https://formsubmit.co/YOUR_EMAIL@example.com" method="POST">
     <input type="text" name="name" placeholder="Your Name" required>
     <input type="email" name="email" placeholder="Your Email" required>
     <textarea name="message" placeholder="Write your message here..." required></textarea>
     <button type="submit">Send</button>
</form>
"""
st.markdown(contact_form, unsafe_allow_html=True)

# Hide Streamlit branding
st.markdown("""
<style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    input, textarea {width: 100%; padding: 8px; margin: 6px 0;}
    button {background-color: #4CAF50; color: white; border: none; padding: 10px;}
</style>
""", unsafe_allow_html=True)
