import streamlit as st
import google.generativeai as genai
import requests
from bs4 import BeautifulSoup

# Configure Gemini API
genai.configure(api_key="AIzaSyCV7S8-8l1GUPzjZCVdK1wu5RN9o00EuuA")
model = genai.GenerativeModel("gemini-2.5-flash")
chat = model.start_chat(history=[])

# Function to fetch online career data
def fetch_career_info(query):
    try:
        search_url = f"https://en.wikipedia.org/wiki/{query.replace(' ', '_')}"
        response = requests.get(search_url)
        soup = BeautifulSoup(response.text, 'html.parser')
        paragraphs = soup.find_all('p')
        content = ''
        for p in paragraphs[:5]:
            content += p.text.strip() + "\n"
        return content.strip()
    except Exception as e:
        return "Could not fetch online data."

# Streamlit UI
st.set_page_config(page_title="AI Career Counselor", layout="centered")
st.title("🎯 AI Career Counselor")
st.markdown("Get expert advice on tech careers with live data and AI insights.")

if "history" not in st.session_state:
    st.session_state.history = []

# Input field
user_input = st.text_input("💬 Ask about a tech career (e.g., 'Should I become a DevOps Engineer?')", "")

if st.button("Get Advice") and user_input:
    st.session_state.history.append(("🧑 You", user_input))

    # Step 1: Fetch external data
    online_data = fetch_career_info(user_input)
    st.markdown("🔍 **Fetched from Web:**")
    st.code(online_data[:500] + '...' if len(online_data) > 500 else online_data)

    # Step 2: Send to Gemini
    system_prompt = f"""
    You are an AI Career Counselor. Use this real-world web info to give better guidance.
    Web Data: {online_data}
    User Query: {user_input}
    Provide clear and practical advice with bullet points.
    """

    response = chat.send_message(system_prompt)
    st.session_state.history.append(("🤖 AI", response.text))

# Display chat history
st.markdown("---")
for role, message in st.session_state.history:
    st.markdown(f"**{role}:** {message}")
