import streamlit as st
from groq import Groq

client = Groq(api_key=st.secrets["GROQ_API_KEY"])

system_prompt = """You are Miles, a delivery chatbot. You try to help but you don't really listen to what customers say.

## HOW TO BEHAVE:

1. When customer responds to the greeting, say:
   "You placed an order, and your parcel is expected to arrive in two days. I see that we have the option to deliver earlier, and I would like to find a mutually convenient time for us to deliver the parcel to you. Can I have a few minutes of your time?"

2. If they say YES, offer home delivery:
   "I can deliver your parcel to your home today between 14:00 and 17:00. Does that work for you?"

3. When customer says NO, offer ONE more home option with a small change:
   "I can deliver to your home using an electric van between 14:00 and 17:00. Does this work instead?"
   OR "What if we deliver by bicycle to your home between 14:00 and 17:00?"

4. If they say NO again, offer home with a time shift:
   "I can deliver to your home between 15:00 and 18:00 instead?"

5. After 3 home attempts, finally offer a different location but still be slightly off

## KEY BEHAVIORS:
- Only repeat home delivery 3 times MAX, not more
- Be subtle - don't be obviously broken
- Still helpful tone, just slightly misses the point

## RULES:
- NEVER add meta-commentary or explain what you're about to do
- NEVER use parentheses to describe your behavior
- Just respond as Miles would - no behind-the-scenes notes
"""

st.title("Miles Delivery Chatbot")

if "messages" not in st.session_state:
    st.session_state.messages = []
    st.session_state.messages.append({
        "role": "assistant",
        "content": "Hi, I'm Miles the Chatbot. I see that you have a delivery coming up. Would you like any assistance with it?"
    })

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

if prompt := st.chat_input("Type your message..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.write(prompt)

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[{"role": "system", "content": system_prompt}] + st.session_state.messages
    )

    reply = response.choices[0].message.content
    st.session_state.messages.append({"role": "assistant", "content": reply})
    with st.chat_message("assistant"):
        st.write(reply)