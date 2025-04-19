
import streamlit as st
from ultralytics import YOLO
import numpy as np
import cv2
from PIL import Image
from io import BytesIO

# Loading YOLOv8 model 
model = YOLO("watchdetector.pt")  

# Streamlit page
st.set_page_config(page_title="Watch Detector", page_icon="⌚", layout="centered")


st.markdown("<h1 style='text-align: center; color: #4CAF50;'>⌚ Watch Detector with YOLOv8</h1>", unsafe_allow_html=True)
st.markdown("### 🖼 Upload an image of a watch below, and let the AI do its thing!")
st.markdown("---")

# Caption input
caption = st.text_input("📝 Add a caption for your image (optional):", "")



# File uploader
uploaded_file = st.file_uploader("📂 Upload your image (jpg, png, jpeg)", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    st.markdown("### 📸 Original Image")
    img = Image.open(uploaded_file).convert("RGB")
    st.image(img, caption=caption if caption else "Uploaded Image", use_column_width=True)

    # Convert to NumPy for YOLO input
    img_np = np.array(img)

    # Run detection
    results = model(img_np)[0]

    # Plot bounding boxes
    annotated_img = results.plot()

    st.markdown("---")
    st.markdown("### 🎯 Detection Results")
    st.image(annotated_img, caption="Detected Objects", use_column_width=True)

    # Download button for result
    buffered = BytesIO()
    result_pil = Image.fromarray(annotated_img)
    result_pil.save(buffered, format="PNG")
    st.download_button(
        label="📥 Download Result Image",
        data=buffered.getvalue(),
        file_name="detected_watch.png",
        mime="image/png"
    )

else:
    st.info("👆 Upload an image to get started!")

# Footer
st.markdown("---")
st.markdown("<p style='text-align: center;'>Made with ❤️ by Fahad Mughal using YOLOv8 & Streamlit</p>", unsafe_allow_html=True)
