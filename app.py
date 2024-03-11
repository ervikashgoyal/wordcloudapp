import streamlit as st
from wordcloud import WordCloud
from textblob import TextBlob
import matplotlib.pyplot as plt

def generate_word_cloud(text):
    wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text)
    
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.imshow(wordcloud, interpolation='bilinear')
    ax.axis('off')
    st.pyplot(fig)

def analyze_sentiment(text):
    blob = TextBlob(text)
    sentiment_score = blob.sentiment.polarity
    
    if sentiment_score > 0:
        return "Positive"
    elif sentiment_score < 0:
        return "Negative"
    else:
        return "Neutral"

def main():
    st.title("Word Cloud and Sentiment Analysis App")

    # Text input
    text = st.text_area("Enter your text here:")

    if st.button("Generate Word Cloud"):
        generate_word_cloud(text)

    if st.button("Analyze Sentiment"):
        sentiment = analyze_sentiment(text)
        st.write(f"Sentiment: {sentiment}")

if __name__ == "__main__":
    main()
