import streamlit as st

# Initialize session state variables
if "low" not in st.session_state or "high" not in st.session_state:
    st.session_state.low = 1
    st.session_state.high = 100
    st.session_state.guess = (st.session_state.low + st.session_state.high) // 2
    st.session_state.attempts = 1

st.title("🤖 Computer Guesses Your Number!")
st.write("Think of a number between 1 and 100, and I will try to guess it!")

st.subheader(f"Is your number *{st.session_state.guess}*?")
st.write(f"📌 *Attempts:* {st.session_state.attempts}")

col1, col2, col3 = st.columns(3)

with col1:
    if st.button("Too Low ⬆"):
        if st.session_state.low < st.session_state.high:  # Ensure valid range
            st.session_state.low = st.session_state.guess + 1
            if st.session_state.low <= st.session_state.high:
                st.session_state.guess = (st.session_state.low + st.session_state.high) // 2
                st.session_state.attempts += 1
                st.rerun()
        else:
            st.error("❌ Invalid range! Please restart the game.")

with col2:
    if st.button("Too High ⬇"):
        if st.session_state.low < st.session_state.high: 
            st.session_state.high = st.session_state.guess - 1
            if st.session_state.low <= st.session_state.high:
                st.session_state.guess = (st.session_state.low + st.session_state.high) // 2
                st.session_state.attempts += 1
                st.rerun()
        else:
            st.error("❌ Invalid range! Please restart the game.")

with col3:
    if st.button("Correct! 🎉"):
        st.success(f"🎯 I guessed your number in *{st.session_state.attempts}* attempts! 🎉")

# Restart button
if st.button("🔄 Restart Game"):
    for key in list(st.session_state.keys()):
        del st.session_state[key]  # Clear session state for a fresh start
    st.rerun()   # Restart the app
