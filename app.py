"""
Plant Leaf Health Analysis — educational prototype
Run with: streamlit run app.py

This is not a validated disease diagnosis model.
"""

from PIL import Image
import numpy as np
import streamlit as st

st.set_page_config(page_title="Plant Leaf Health Analysis", page_icon="🌿")
st.title("Plant Leaf Health Analysis")
st.write("Upload a plant-leaf image for a simple visual color summary.")
st.warning(
    "Educational demonstration only. This tool does not diagnose plant "
    "disease or recommend treatment."
)

uploaded = st.file_uploader("Upload a leaf photo", type=["jpg", "jpeg", "png"])

if uploaded is not None:
    try:
        image = Image.open(uploaded).convert("RGB")
        st.image(image, caption="Uploaded leaf image", use_container_width=True)

        arr = np.asarray(image).astype(float)
        r, g, b = arr[:, :, 0], arr[:, :, 1], arr[:, :, 2]

        green_mask = (g > r * 1.08) & (g > b * 1.05) & (g > 45)
        brown_mask = (r > g * 1.12) & (g > b * 1.05) & (r > 50)

        green_pct = 100 * green_mask.mean()
        brown_pct = 100 * brown_mask.mean()

        st.metric("Green-toned pixels (whole image)", f"{green_pct:.1f}%")
        st.metric("Brown-toned pixels (whole image)", f"{brown_pct:.1f}%")
        st.caption(
            "These are rough image-color measurements, not percentages of leaf "
            "area and not disease probabilities."
        )
        st.info(
            "For reliable diagnosis, consult an agricultural expert and use a "
            "validated model with a suitable labelled dataset."
        )
    except Exception as exc:
        st.error(f"Could not read the image: {exc}")
