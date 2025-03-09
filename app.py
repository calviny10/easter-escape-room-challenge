import streamlit as st

# Set page configuration
st.set_page_config(
    page_title="Code Challenge",
    page_icon="🔒",
    layout="centered"
)

# Custom CSS for styling
st.markdown("""
<style>
    h1 {
        color: #2196f3;
        text-align: center;
        margin-bottom: 1.5rem;
    }
    .stButton > button {
        background-color: #2196f3;
        color: white;
        width: 100%;
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
    /* Make inputs look more like rectangles */
    div[data-baseweb="input"] {
        border: 2px solid #2196f3 !important;
        border-radius: 4px !important;
    }
    /* Center text in inputs */
    div[data-baseweb="input"] input {
        text-align: center !important;
        font-size: 24px !important;
    }
</style>
""", unsafe_allow_html=True)

# App title
st.title("Easter Escape Room - Final Stage")

# Create digit input boxes
st.subheader("Enter 6-digit code:")

col1, col2, col3, col4, col5, col6 = st.columns(6)
with col1:
    digit1 = st.text_input("", key="digit1", max_chars=1, label_visibility="collapsed")
with col2:
    digit2 = st.text_input("", key="digit2", max_chars=1, label_visibility="collapsed")
with col3:
    digit3 = st.text_input("", key="digit3", max_chars=1, label_visibility="collapsed")
with col4:
    digit4 = st.text_input("", key="digit4", max_chars=1, label_visibility="collapsed")
with col5:
    digit5 = st.text_input("", key="digit5", max_chars=1, label_visibility="collapsed")
with col6:
    digit6 = st.text_input("", key="digit6", max_chars=1, label_visibility="collapsed")

# Submit button
submit_button = st.button("Submit")

# Initialize session state
if 'attempts' not in st.session_state:
    st.session_state.attempts = 0
if 'success' not in st.session_state:
    st.session_state.success = False

# Handle form submission
if submit_button:
    # Combine all digits
    entered_code = f"{digit1}{digit2}{digit3}{digit4}{digit5}{digit6}"
    # The correct code
    CORRECT_CODE = "220450"
    
    st.session_state.attempts += 1
    
    if entered_code == CORRECT_CODE:
        st.session_state.success = True
    elif len(entered_code) == 6 and entered_code.isdigit():
        st.warning("Wow! You are almost there, finally, please hang the correct six digit code to escape. If it's wrong, nothing will happen.")
    else:
        st.error("Please enter all 6 digits.")

# Show celebration for correct code
if st.session_state.success:
    st.markdown('<div class="celebration">🎉 CONGRATULATION! YOU HAVE MADE IT! 🎉</div>', unsafe_allow_html=True)
    # Add confetti effect
    st.balloons()
