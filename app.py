import streamlit as st
from transformers import pipeline

st.title("👁️ SentixLens: Sentiment Analyzer")
st.write("Analyze specific features within a review using State-of-the-Art NLP.")

@st.cache_resource
def load_model():
    return pipeline("text-classification", model="yangheng/deberta-v3-base-absa-v1.1")

classifier = load_model()

review = st.text_area(
    "Enter your review text:", 
    "The battery life is excellent but the screen is too dim."
)
aspect = st.text_input(
    "Enter the specific feature/aspect you want to check:", 
    "battery"
)

if st.button("Analyze Aspect"):
    with st.spinner("Analyzing text..."):
        result = classifier(review, text_pair=aspect)
        st.success("Analysis Complete!")
        st.write(f"**Aspect:** {aspect}")
        st.write(f"**Sentiment:** {result[0]['label']}")
        st.write(f"**Confidence Score:** {result[0]['score']:.2f}")
