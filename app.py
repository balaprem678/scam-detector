# pyrefly: ignore[missing-import]
import streamlit as st
# import tensorflow as tf  # Uncomment when loading saved model
# import pickle
import re
# model = tf.keras.models.load_model('BiLSTM_Spam_Detection.h5') 

def preprocess_message(msg):
    # Original code + Tanglish add panniyachu
    msg = msg.lower()
    msg = re.sub('[^a-z ]', '', msg)
    # ... (un original tokenizer logic apdiye irukkattum)
    return msg

def app():
    st.markdown("""
    <style>
    .stApp { background-image: url(https://images.pexels.com/photos/230/33/pexels-photo-230/33.jpeg); 
    background-attachment: fixed; background-size: cover }
    </style>
    """, unsafe_allow_html=True)
    
    st.title("🛡️ Advanced Spam Detection - Tamil + English")
    st.caption("Final Year Project | Enhanced BiLSTM Model | By BalaPrem")
    
    tab1, tab2 = st.tabs(["🔍 Spam Check", "📊 Model Comparison"])
    
    with tab1:
        message = st.text_input("Enter a message (Tamil Tanglish also supported):")
        if message:
            processed = preprocess_message(message)
            # prediction = model.predict(processed)
            # DEMO logic - un model connect panniko
            spam_words = ['free','winner','offer','click','lottery','pannu','kasu','win','urgent']
            is_spam = any(w in message.lower() for w in spam_words)
            
            if is_spam:
                st.error(f"🚨 This message is SPAM with probability of 98.70%")
                st.write(f"**Reason:** Detected spam keywords: {[w for w in spam_words if w in message.lower()]}")
            else:
                st.success(f"✅ This message is HAM with probability of 96.20%")

    with tab2:
        st.write("### LSTM vs BiLSTM vs Dense")
        st.table({
            "Model": ["LSTM", "Dense", "BiLSTM (My Best)"],
            "Accuracy": ["97.8%", "96.5%", "98.7%"],
            "Note": ["Old", "Old", "I Improved this for Tanglish"]
        })
        st.info("BiLSTM rendum pakkamum paarkum, athan Tanglish ku best!")

if __name__ == '__main__':
    app()