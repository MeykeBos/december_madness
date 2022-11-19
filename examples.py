import streamlit as st
import cv2
import numpy as np
from demos import orchestrator


def show():
    # Possible filters but not in use
    def preprocess(img):
        bytes_data = np.asarray(bytearray(img.read()), dtype=np.uint8)
        img = cv2.imdecode(bytes_data, cv2.IMREAD_COLOR)
        return img

    def invert(img):
        img = preprocess(img)
        inv = cv2.bitwise_not(img)
        return inv

    def hdr(img):
        img = preprocess(img)
        hdr_img = cv2.detailEnhance(img, sigma_s=12, sigma_r=0.15)
        return hdr_img

    def sketch(img):
        img = preprocess(img)
        _, sketch_img = cv2.pencilSketch(img, sigma_s=60, sigma_r=0.07, shade_factor=0.1)
        return sketch_img

    def gray(img):
        img = preprocess(img)
        gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        gray_img = cv2.cvtColor(gray_img, cv2.COLOR_GRAY2RGB)
        return gray_img

    def none(img):
        img = preprocess(img)
        return img

    # Add a name field
    if "visibility" not in st.session_state:
        st.session_state.visibility = "visible"
        st.session_state.disabled = False

    name_input = st.text_input(
        "Vul je naam in 👇",
        label_visibility=st.session_state.visibility,
        disabled=st.session_state.disabled,
        placeholder="naam",
    )


    picture = st.camera_input("Neem een foto...")

    filters_to_funcs = {
        "No filter": none,
        "Invert": invert,
        "HDR": hdr,
        "Sketch": sketch,
        "Grayscale": gray
    }
    #filters = st.selectbox("...and now, apply a filter!", filters_to_funcs.keys())

    if picture:
        st.image(filters_to_funcs["No filter"](picture), channels="BGR")

    if picture:
        st.write("tabletje, tabletje in mijn hand, wie is de mooiste Haan van Nederland?")

        if name_input == "DJ":
            audio_file = open('C:/Users/vandemey/OneDrive - TomTom\Pictures/december_madness/7a42fe1f-7074-4c91-942e-c5a8af2a0c69.wav', 'rb')
            audio_bytes = audio_file.read()

            st.audio(audio_bytes, format='audio/ogg')



        else:
            st.write("Niet DJ")



