import streamlit as st

st.set_page_config(page_title="My First AI App", page_icon="🚀")

st.title("🚀 AI App Tester")
st.write("If you can see this, your deployment on Emergent AI worked!")

# Sidebar for settings
with st.sidebar:
    st.header("Configuration")
    api_key = st.text_input("Enter dummy API Key", type="password")
    status = "Connected" if api_key else "Waiting for Key..."
    st.info(f"Status: {status}")

# Main UI
user_input = st.text_input("Ask your AI anything:")
if st.button("Generate Response"):
    if user_input:
        st.success(f"Echo: Your app is live! You asked: '{user_input}'")
    else:
        st.warning("Please enter a prompt first.")

st.divider()
st.caption("Built with Vibe & Hosted on Emergent AI")
