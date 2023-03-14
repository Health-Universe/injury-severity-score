import streamlit as st

def calculate_iss(head, face, chest, abdomen, extremities, external):
    scores = [head, face, chest, abdomen, extremities, external]
    scores.sort(reverse=True)
    iss = (scores[0] * 4) + (scores[1] * 3) + (scores[2] * 2) + scores[3]
    return iss

st.title("Injury Severity Score (ISS) Calculator")

st.markdown("The Injury Severity Score (ISS) is used to standardize the severity of traumatic injury based on the worst injury of 6 body systems.")

head = st.slider("Head", 0, 5, 0)
face = st.slider("Face", 0, 5, 0)
chest = st.slider("Chest", 0, 5, 0)
abdomen = st.slider("Abdomen", 0, 5, 0)
extremities = st.slider("Extremities", 0, 5, 0)
external = st.slider("External", 0, 5, 0)

if st.button("Calculate ISS"):
    iss = calculate_iss(head, face, chest, abdomen, extremities, external)
    st.write(f"The Injury Severity Score (ISS) is {iss}")
