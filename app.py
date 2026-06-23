import streamlit as st
from google import genai
from PIL import Image

# 1. Setup the Web Interface Title
st.title("🛡️ CivicEye AI: Hyperlocal Problem Solver")
st.write("Upload an image of a community issue to instantly generate an AI engineering report.")

# File Uploader UI Component
uploaded_file = st.file_uploader("Choose an image (pothole, broken light, trash, etc.)...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Open and show the uploaded image on the screen
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Issue Photo", use_container_width=True)
    
    st.write("🔄 Gemini AI is analyzing the issue and generating a triage report...")
    
    # 2. Connect to your Google AI Studio Engine
    # REPLACE THE VALUE BELOW WITH YOUR COPIED API KEY (keep the quotation marks)
    # This automatically looks for a hidden environment variable or secret
    client = genai.Client()
    
    # Engineering instructions for the AI
    prompt = """
    You are an automated civic infrastructure assistant. Analyze this image carefully:
    1. **Category**: Classify the issue (e.g., Road Damage, Waste Management, Public Lighting, Water Leakage).
    2. **Urgency Score**: Rate it from 1 (Low) to 5 (Critical Hazard) based on danger to citizens.
    3. **Actionable Summary**: Write a short, 2-sentence description detailing exactly what needs fixing for dispatch crews.
    Format your response cleanly with bold bullet points.
    """
    
    try:
        # Send the prompt and the image to the model
   # Send the prompt and the image to the model using the standard flagship name
        # Send the prompt and the image to the model
        response = client.models.generate_content(
            model='gemini/gemini-1.5-flash',
            contents=[prompt, image]
        )
        
        # 3. Output the result right onto the webpage
        st.subheader("📋 Official AI Dispatch Report")
        st.write(response.text)
        
    except Exception as e:
        st.error(f"Something went wrong: {e}")
