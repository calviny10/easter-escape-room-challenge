import streamlit as st
import time

# Set page configuration
st.set_page_config(
    page_title="Code Challenge",
    page_icon="🔒",
    layout="centered"
)

# Custom CSS for styling
st.markdown("""
<style>
    .main {
        padding: 2rem;
        border-radius: 10px;
        max-width: 800px;
        margin: 0 auto;
    }
    h1 {
        color: #2196f3;
        text-align: center;
        margin-bottom: 1.5rem;
    }
    .stButton > button {
        background-color: #2196f3;
        color: white;
        width: 100%;
        padding: 0.5rem;
    }
    .celebration {
        font-size: 32px;
        text-align: center;
        margin-top: 2rem;
        animation: bounce 1s infinite alternate;
    }
    @keyframes bounce {
        from { transform: scale(1); }
        to { transform: scale(1.2); }
    }
</style>
""", unsafe_allow_html=True)

# App title
st.title("Easter Escape Room - Final Stage")

# Create a form for the input
with st.form(key="code_form"):
    code_input = st.text_input("Enter 6-digit code:", max_chars=6)
    submit_button = st.form_submit_button("Submit")

# Initialize session state for attempts
if 'attempts' not in st.session_state:
    st.session_state.attempts = 0
if 'success' not in st.session_state:
    st.session_state.success = False

# Handle form submission
if submit_button:
    # The correct code
    CORRECT_CODE = "220450"
    
    st.session_state.attempts += 1
    
    if code_input == CORRECT_CODE:
        st.session_state.success = True
    elif len(code_input) == 6:
        st.warning("Wow! You are almost there, finally, please hang the correct six digit code to escape. If it's wrong, nothing will happen.")
    else:
        st.error("Please enter a 6-digit code.")

# Show celebration for correct code
if st.session_state.success:
    st.markdown('<div class="celebration">🎉 CONGRATULATION! YOU HAVE MADE IT! 🎉</div>', unsafe_allow_html=True)
    
    # Add confetti effect
    st.balloons()
