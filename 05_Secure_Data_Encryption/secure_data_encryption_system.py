import streamlit as st
import hashlib
import json
import os
import time
from cryptography.fernet import Fernet
from base64 import urlsafe_b64encode
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.backends import default_backend

# Constants
DATA_FILE = "data.json"
LOCKOUT_TIME = 60  # in seconds

# Session state setup
if "failed_attempts" not in st.session_state:
    st.session_state.failed_attempts = 0
if "lockout_start" not in st.session_state:
    st.session_state.lockout_start = None
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
if "username" not in st.session_state:
    st.session_state.username = None

# Load data from JSON
def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    return {}

# Save data to JSON
def save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=4)

# Generate Fernet key from passkey using PBKDF2
def generate_key(passkey):
    salt = b'streamlit_secure_salt'  # Use a secure salt in real projects
    kdf = PBKDF2HMAC(
        algorithm=hashlib.sha256(),
        length=32,
        salt=salt,
        iterations=100000,
        backend=default_backend()
    )
    return urlsafe_b64encode(kdf.derive(passkey.encode()))

# Encrypt data
def encrypt_data(text, passkey):
    key = generate_key(passkey)
    cipher = Fernet(key)
    return cipher.encrypt(text.encode()).decode()

# Decrypt data
def decrypt_data(encrypted_text, passkey):
    try:
        key = generate_key(passkey)
        cipher = Fernet(key)
        return cipher.decrypt(encrypted_text.encode()).decode()
    except:
        return None

# Home
def home():
    st.subheader("🏠 Welcome to the Secure Data System")
    st.write("Use this app to **securely store and retrieve data** with your passkey.")

# Register new user
def register_user():
    st.subheader("📝 Register New Account")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    if st.button("Register"):
        data = load_data()
        if username in data:
            st.error("❌ Username already exists!")
        else:
            hashed_pw = hashlib.sha256(password.encode()).hexdigest()
            data[username] = {"password": hashed_pw, "data": []}
            save_data(data)
            st.success("✅ User registered successfully!")

# Login page
def login_page():
    st.subheader("🔐 Login")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        data = load_data()
        if username in data:
            hashed_input_pw = hashlib.sha256(password.encode()).hexdigest()
            if hashed_input_pw == data[username]["password"]:
                st.session_state.failed_attempts = 0
                st.session_state.lockout_start = None
                st.session_state.logged_in = True
                st.session_state.username = username
                st.success("✅ Login successful!")
                st.experimental_rerun()
            else:
                st.session_state.failed_attempts += 1
                st.error("❌ Incorrect password!")
        else:
            st.error("❌ Username not found!")

# Store data
def store_data():
    st.subheader("📂 Store Data")
    user_data = st.text_area("Enter data to encrypt:")
    passkey = st.text_input("Enter encryption passkey", type="password")
    if st.button("Encrypt & Store"):
        if user_data and passkey:
            encrypted = encrypt_data(user_data, passkey)
            data = load_data()
            data[st.session_state.username]["data"].append({
                "encrypted_text": encrypted
            })
            save_data(data)
            st.success("✅ Data stored successfully!")
            st.code(encrypted)
        else:
            st.error("⚠️ Both fields are required!")

# Retrieve data
def retrieve_data():
    st.subheader("🔍 Retrieve Data")
    encrypted_text = st.text_area("Enter encrypted data:")
    passkey = st.text_input("Enter decryption passkey", type="password")

    if st.session_state.lockout_start:
        elapsed = time.time() - st.session_state.lockout_start
        if elapsed < LOCKOUT_TIME:
            st.error(f"🔒 Too many failed attempts! Try again in {int(LOCKOUT_TIME - elapsed)} seconds.")
            return
        else:
            st.session_state.failed_attempts = 0
            st.session_state.lockout_start = None

    if st.button("Decrypt"):
        if encrypted_text and passkey:
            result = decrypt_data(encrypted_text, passkey)
            if result:
                st.success(f"✅ Decrypted Data: {result}")
                st.session_state.failed_attempts = 0
            else:
                st.session_state.failed_attempts += 1
                attempts_left = 3 - st.session_state.failed_attempts
                st.error(f"❌ Incorrect passkey! Attempts remaining: {attempts_left}")
                if st.session_state.failed_attempts >= 3:
                    st.session_state.lockout_start = time.time()
        else:
            st.error("⚠️ Both fields are required!")

# App Navigation
st.title("🛡️ Secure Data Encryption System")

menu = ["Home", "Register", "Login", "Store Data", "Retrieve Data"]
choice = st.sidebar.radio("🔹 Navigate", menu)

if choice == "Home":
    home()
elif choice == "Register":
    register_user()
elif choice == "Login":
    login_page()
elif choice == "Store Data":
    if st.session_state.logged_in:
        store_data()
    else:
        st.warning("🔒 Please login first.")
elif choice == "Retrieve Data":
    if st.session_state.logged_in:
        retrieve_data()
    else:
        st.warning("🔒 Please login first.")
