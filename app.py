import streamlit as st
from wordcloud import WordCloud
from textblob import TextBlob
import matplotlib.pyplot as plt

def generate_word_cloud(text):
    """
    Generates and displays a Word Cloud based on the input text.
    """
    wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text)

    fig, ax = plt.subplots(figsize=(10, 5))
    ax.imshow(wordcloud, interpolation='bilinear')
    ax.axis('off')
    st.pyplot(fig)

def analyze_sentiment(text):
    """
    Analyzes the sentiment of the input text using TextBlob.
    """
    blob = TextBlob(text)
    sentiment_score = blob.sentiment.polarity

    if sentiment_score > 0:
        return "Positive"
    elif sentiment_score < 0:
        return "Negative"
    else:
        return "Neutral"

def main():
    """
    Main function for the Streamlit app.
    """
    st.title("Word Cloud and Sentiment Analysis App")

    # Text input
    text = st.text_area("Enter your text here:")

    # Instructions
    st.sidebar.header("Instructions:")
    st.sidebar.markdown("""
        1. Enter your text in the text area.
        2. Click the "Generate Word Cloud" button to visualize a word cloud.
        3. Click the "Analyze Sentiment" button to see the sentiment of the input text.
    """)

    # Developer info
    st.sidebar.header("Developed by Vikash Goyal")
    st.sidebar.write("Connect with me on LinkedIn: [Vikash Goyal](https://www.linkedin.com/in/vikash-goyal-20692924b/)")

    if st.button("Generate Word Cloud"):
        generate_word_cloud(text)

    if st.button("Analyze Sentiment"):
        sentiment = analyze_sentiment(text)
        st.write(f"Sentiment: {sentiment}")

if __name__ == "__main__":
    main()
