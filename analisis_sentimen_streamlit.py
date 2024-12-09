import tweepy
import streamlit as st
from textblob import TextBlob

# Gunakan Bearer Token untuk otentikasi dengan API v2
bearer_token = 'AAAAAAAAAAAAAAAAAAAAAOKAxQEAAAAAJff47IFaEvOqguNZ2pacnny3VPU%3DKPubMLPGXnu7HTZySXKQT4gWVhFq6qUtCNBvNOUrz43gC9mjUa'  # Masukkan Bearer Token Anda di sini
client = tweepy.Client(bearer_token=bearer_token)

# Sidebar
st.sidebar.title("Analisis Sentimen Twitter")
query = st.sidebar.text_input("Masukkan kata kunci pencarian:")
naOfTweet = st.sidebar.number_input("Jumlah tweet yang ingin diambil:", min_value=1, max_value=100, value=10)

# Container
st.title("Analisis Sentimen Twitter")

# Fungsi untuk menganalisis sentimen
def analyze_sentiment(text):
    blob = TextBlob(text)
    sentiment = blob.sentiment.polarity
    if sentiment > 0:
        return "Positif"
    elif sentiment == 0:
        return "Netral"
    else:
        return "Negatif"

# Cek jika query tidak kosong dan jumlah tweet valid
if query and naOfTweet:
    try:
        # Ambil tweet berdasarkan query dan batas jumlah tweet
        tweets = client.search_recent_tweets(query=query, tweet_fields=['context_annotations', 'created_at'], max_results=naOfTweet)

        # Menampilkan tweet di Streamlit
        for tweet in tweets.data:
            st.write(f"**Tweet:** {tweet.text}")
            st.write(f"**Waktu Dibuat:** {tweet.created_at}")
            
            # Analisis sentimen tweet
            sentiment = analyze_sentiment(tweet.text)
            st.write(f"**Sentimen:** {sentiment}")
            
            st.markdown("---")  # Pemisah antar tweet

    except Exception as e:
        st.error(f"Error occurred: {e}")
else:
    st.warning("Masukkan kata kunci dan jumlah tweet.")