import streamlit as st
import re
import random
import string

# --- Password strength checker ---
def check_password_strength(password):
    feedback = []
    score = 0

    # Length Check
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("🔴 At least 8 characters required.")

    # Uppercase and Lowercase
    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("🔴 Include both uppercase and lowercase letters.")

    # Digit Check
    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("🔴 Add at least one number.")

    # Special Character Check
    if re.search(r"[!@#$%^&*]", password):
        score += 1
    else:
        feedback.append("🔴 Use a special character (!@#$%^&*).")

    # Check against common passwords
    common_passwords = ["password", "123456", "password123", "admin", "qwerty"]
    if password.lower() in common_passwords:
        feedback.append("🔴 This password is too common. Choose something unique.")
        score = min(score, 2)  

    # Strength Level
    if score == 4:
        strength = "✅ Strong"
    elif score == 3:
        strength = "⚠️ Moderate"
    else:
        strength = "❌ Weak"

    return strength, feedback

# --- Strong password generator ---
def generate_strong_password(length=12):
    if length < 8:
        length = 8
    all_chars = string.ascii_letters + string.digits + "!@#$%^&*"
    return ''.join(random.choice(all_chars) for _ in range(length))


st.title("🔐 Password Strength Meter")
st.write("Enter your password below to check its strength:")

password_input = st.text_input("🔑 Enter Password", type="password")

if password_input:
    strength, suggestions = check_password_strength(password_input)

    st.markdown(f"**Strength:** {strength}")
    
    if suggestions:
        st.markdown("### 🔧 Suggestions:")
        for s in suggestions:
            st.write(f"- {s}")
    else:
        st.success("Your password looks good! ✅")

st.markdown("---")
st.subheader("🛠️ Need help creating a strong password?")
if st.button("Generate Strong Password"):
    strong_pwd = generate_strong_password()
    st.code(strong_pwd, language="text")
