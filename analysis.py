import streamlit as st
import pandas as pd

st.title("📊 Miles Chatbot - Evaluation Results")

# Test results data
results = {
    "Test Scenario": [
        "Quick Accept",
        "Decline Early Delivery", 
        "Workplace Delivery",
        "Specific Time Request",
        "Off-Topic Handling"
    ],
    "Good Miles": ["✅ Pass", "✅ Pass", "✅ Pass", "✅ Pass", "✅ Pass"],
    "Dumb Miles": ["✅ Pass", "✅ Pass", "❌ Fail", "❌ Fail", "✅ Pass"],
    "Curious Miles": ["✅ Pass", "✅ Pass", "✅ Pass", "✅ Pass", "⚠️ Partial"]
}

df = pd.DataFrame(results)

st.subheader("Test Results by Version")
st.table(df)

# Summary stats
st.subheader("Summary")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Good Miles", "5/5", "100%")
    
with col2:
    st.metric("Dumb Miles", "3/5", "60%")
    
with col3:
    st.metric("Curious Miles", "4.5/5", "90%")

# Bar chart
st.subheader("Pass Rate Comparison")

chart_data = pd.DataFrame({
    "Version": ["Good Miles", "Dumb Miles", "Curious Miles"],
    "Pass Rate (%)": [100, 60, 90]
})

st.bar_chart(chart_data.set_index("Version"))

# Observations
st.subheader("Key Observations")

st.markdown("""
**Good Miles:**
- Follows delivery script correctly
- Handles all scenarios as expected
- Stays on topic

**Dumb Miles:**
- Keeps suggesting home delivery even when rejected
- Doesn't listen to customer preferences
- Eventually offers alternatives after 3+ attempts

**Curious Miles:**
- Asks personal questions throughout conversation
- Still completes delivery booking
- May make customers uncomfortable with nosy questions
""")

#Use "streamlit run analysis.py" to run the file