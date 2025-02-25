import streamlit as st
import random
import os
import base64
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
import json


st.set_page_config(
    page_title="SecurePass Manager",
    page_icon="🔒",
    layout="centered",
    initial_sidebar_state="collapsed",
)


st.markdown("""
<style>
    .main {
        background-color: #f8f9fa;
    }
    .stApp {
        max-width: 1000px;
        margin: 0 auto;
    }
    .css-18e3th9 {
        padding-top: 2rem;
    }
    .stButton button {
        background-color: #4c8bf5;
        color: white;
        border-radius: 4px;
        padding: 0.5rem 1rem;
        border: none;
    }
    .stButton button:hover {
        background-color: #3a7bd5;
    }
    .password-display {
        background-color: #e9ecef;
        padding: 1rem;
        border-radius: 4px;
        font-family: monospace;
        margin: 1rem 0;
    }
    h1, h2, h3 {
        color: #2c3e50;
    }
</style>
""", unsafe_allow_html=True)


if not os.path.exists("data"):
    os.makedirs("data")


def initialize_master_password():
    if not os.path.exists("data/config.json"):
        return None
    with open("data/config.json", "r") as f:
        config = json.load(f)
        return config.get("salt")

# Encryption functions
def get_key_from_password(password, salt=None):
    if not salt:
        salt = os.urandom(16)
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
    )
    key = base64.urlsafe_b64encode(kdf.derive(password.encode()))
    return key, salt

def encrypt_data(data, key):
    f = Fernet(key)
    return f.encrypt(data.encode())

def decrypt_data(encrypted_data, key):
    f = Fernet(key)
    try:
        return f.decrypt(encrypted_data).decode()
    except Exception:
        return None


if 'authenticated' not in st.session_state:
    st.session_state.authenticated = False
if 'current_key' not in st.session_state:
    st.session_state.current_key = None
if 'current_salt' not in st.session_state:
    st.session_state.current_salt = initialize_master_password()


st.title("🔒 SecurePass Manager")
st.markdown("Keep your passwords secure and accessible")


if not st.session_state.authenticated:
    if st.session_state.current_salt is None:
        st.markdown("### 🔑 Set Up Your Master Password")
        st.warning("No master password has been set up yet. Please create one.")
        
        new_master = st.text_input("Create Master Password", type="password")
        confirm_master = st.text_input("Confirm Master Password", type="password")
        
        if st.button("Set Master Password"):
            if new_master == confirm_master and new_master:
                key, salt = get_key_from_password(new_master)
                st.session_state.current_key = key
                st.session_state.current_salt = salt
                
                # Save salt (not the password or key)
                with open("data/config.json", "w") as f:
                    json.dump({"salt": salt}, f)
                
                st.session_state.authenticated = True
                st.success("Master password set successfully!")
                st.experimental_rerun()
            else:
                st.error("Passwords do not match or are empty.")
    else:
        st.markdown("### 🔑 Login")
        master_password = st.text_input("Enter Master Password", type="password")
        
        if st.button("Login"):
            key, _ = get_key_from_password(master_password, st.session_state.current_salt)
            st.session_state.current_key = key
            
            # Test decryption with a sample file
            if os.path.exists("data/test.enc"):
                with open("data/test.enc", "rb") as f:
                    test_data = f.read()
                if decrypt_data(test_data, key) is not None:
                    st.session_state.authenticated = True
                    st.success("Login successful!")
                    st.experimental_rerun()
                else:
                    st.error("Incorrect password.")
            else:
               
                test_data = encrypt_data("test", key)
                with open("data/test.enc", "wb") as f:
                    f.write(test_data)
                st.session_state.authenticated = True
                st.success("Login successful!")
                st.experimental_rerun()


else:
   
    tab1, tab2, tab3 = st.tabs(["Generate Password", "Save Password", "View Passwords"])
    
 
    with tab1:
        st.markdown("### 🎲 Generate a Secure Password")
        
        col1, col2 = st.columns(2)
        with col1:
            password_length = st.slider("Password Length", min_value=8, max_value=32, value=16)
        
        with col2:
            include_uppercase = st.checkbox("Include Uppercase", value=True)
            include_lowercase = st.checkbox("Include Lowercase", value=True)
            include_numbers = st.checkbox("Include Numbers", value=True)
            include_symbols = st.checkbox("Include Symbols", value=True)
        
        if st.button("Generate Password"):
            charset = ""
            if include_uppercase:
                charset += "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
            if include_lowercase:
                charset += "abcdefghijklmnopqrstuvwxyz"
            if include_numbers:
                charset += "0123456789"
            if include_symbols:
                charset += "!@#$%^&*()-_=+[]{}|;:,.<>?/"
            
            if charset:
                generated_password = ''.join(random.choice(charset) for _ in range(password_length))
                st.session_state.generated_password = generated_password
                st.markdown(f"<div class='password-display'>{generated_password}</div>", unsafe_allow_html=True)
                
                # Option to copy or save
                col1, col2 = st.columns(2)
                with col1:
                    st.button("Copy to Clipboard", on_click=lambda: st.write("Password copied to clipboard!"))
                with col2:
                    if st.button("Save This Password"):
                        st.session_state.password_to_save = generated_password
                        st.markdown("Go to the 'Save Password' tab to complete saving")
            else:
                st.error("Please select at least one character type.")
    
    
    with tab2:
        st.markdown("### 💾 Save a Password")
        
        site = st.text_input("Website or Application")
        username = st.text_input("Username or Email")
        
       
        if 'password_to_save' in st.session_state:
            password = st.text_input("Password", value=st.session_state.password_to_save)
            if st.button("Clear"):
                st.session_state.password_to_save = ""
                st.experimental_rerun()
        else:
            password = st.text_input("Password", type="password")
            show_password = st.checkbox("Show Password")
            if show_password:
                st.code(password)
        
        if st.button("Save Password"):
            if site and username and password:
               s
                credentials = {
                    "username": username,
                    "password": password
                }
                
              
                encrypted_data = encrypt_data(json.dumps(credentials), st.session_state.current_key)
                filename = f"data/{site.lower().replace(' ', '_')}.enc"
                
                with open(filename, "wb") as f:
                    f.write(encrypted_data)
                
                st.success(f"Credentials for {site} saved successfully!")
                
               
                st.session_state.password_to_save = ""
            else:
                st.error("Please fill in all fields.")

    with tab3:
        st.markdown("### 🔍 View Saved Passwords")
        
      
        saved_sites = []
        if os.path.exists("data"):
            for file in os.listdir("data"):
                if file.endswith(".enc") and file != "test.enc":
                    saved_sites.append(file[:-4].replace('_', ' ').title())
        
        if saved_sites:
            selected_site = st.selectbox("Select Website", saved_sites)
            
            if selected_site and st.button("Show Credentials"):
                filename = f"data/{selected_site.lower().replace(' ', '_')}.enc"
                
                try:
                    with open(filename, "rb") as f:
                        encrypted_data = f.read()
                    
                    decrypted_data = decrypt_data(encrypted_data, st.session_state.current_key)
                    if decrypted_data:
                        credentials = json.loads(decrypted_data)
                        
                        st.markdown("#### Credentials")
                        st.markdown(f"**Website:** {selected_site}")
                        st.markdown(f"**Username:** {credentials['username']}")
                        
                        # Password with copy option
                        st.markdown("**Password:**")
                        st.markdown(f"<div class='password-display'>{credentials['password']}</div>", unsafe_allow_html=True)
                        st.button("Copy Password", key="copy_password")
                    else:
                        st.error("Could not decrypt credentials. Master password may be incorrect.")
                except Exception as e:
                    st.error(f"Error retrieving credentials: {str(e)}")
        else:
            st.info("No saved passwords found. Go to 'Save Password' tab to add some.")
    
 
    with st.sidebar:
        st.title("Options")
        if st.button("Logout"):
            st.session_state.authenticated = False
            st.session_state.current_key = None
            st.experimental_rerun()
