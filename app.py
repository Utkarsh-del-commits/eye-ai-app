import streamlit as st

st.title("👁️ Eye AI Assistant")

st.warning("This is not a real doctor. Consult a professional.")

redness = st.selectbox("Do you have redness?", ["no", "yes"])
pain = st.selectbox("Do you have eye pain?", ["no", "yes"])
dryness = st.selectbox("Do you feel dryness?", ["no", "yes"])
blurred = st.selectbox("Do you have blurred vision?", ["no", "yes"])

if st.button("Check Result"):
    if redness == "yes" and pain == "yes":
        st.success("Possible condition: Eye Infection or Conjunctivitis")
    elif dryness == "yes":
        st.success("Possible condition: Dry Eye Syndrome (MGD possible)")
    elif blurred == "yes":
        st.success("Possible condition: Vision issue")
    else:
        st.success("No major issue detected")
