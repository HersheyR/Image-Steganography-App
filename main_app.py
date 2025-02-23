import streamlit as st
import cv2
import numpy as np
import os

# Function to embed the message into the image
def encrypt_image(image, message, password):
    img = cv2.imdecode(np.frombuffer(image.read(), np.uint8), 1)
    
    # Convert message and password length to fixed-size headers
    msg_len = len(message)
    pass_len = len(password)
    header = f"{msg_len:04d}"  # 4-digit message length
    pass_header = f"{pass_len:02d}"  # 2-digit passcode length

    # Combine passcode, headers, and message
    data = pass_header + password + header + message

    # ASCII mapping
    d = {chr(i): i for i in range(255)}

    # Embed data into the blue channel
    n, m = 0, 0
    for char in data:
        img[n, m, 0] = d[char]  # Store in blue channel
        m += 1
        if m >= img.shape[1]:  # Move to next row if out of columns
            m = 0
            n += 1

    # Save encrypted image
    encrypted_filename = "encryptedImage.png"
    cv2.imwrite(encrypted_filename, img)

    return encrypted_filename

# Function to extract the message from the image
def decrypt_image(image, password):
    img = cv2.imdecode(np.frombuffer(image.read(), np.uint8), 1)

    # ASCII mapping
    c = {i: chr(i) for i in range(255)}

    n, m = 0, 0

    # Read passcode length (first 2 pixels)
    pass_len_str = ""
    for _ in range(2):
        pass_len_str += c[img[n, m, 0]]
        m += 1
    pass_len = int(pass_len_str)

    # Read stored passcode
    stored_pass = ""
    for _ in range(pass_len):
        stored_pass += c[img[n, m, 0]]
        m += 1

    # Verify passcode
    if stored_pass == password:
        # Read message length (next 4 pixels)
        msg_len_str = ""
        for _ in range(4):
            msg_len_str += c[img[n, m, 0]]
            m += 1
        msg_len = int(msg_len_str)

        # Read the message
        message = ""
        for _ in range(msg_len):
            message += c[img[n, m, 0]]
            m += 1
            if m >= img.shape[1]:  # Move to next row if out of columns
                m = 0
                n += 1

        return f"Decrypted Message: {message}"
    else:
        return "ERROR: Incorrect passcode!"

# Streamlit UI
st.title("🔒 Image Steganography App")

# Sidebar Navigation
menu = st.sidebar.selectbox("Choose an Option", ["Encrypt", "Decrypt"])

if menu == "Encrypt":
    st.header("🖼️ Encrypt a Secret Message")
    uploaded_image = st.file_uploader("Upload an Image", type=["png", "jpg", "jpeg"])
    secret_message = st.text_area("Enter Secret Message")
    passcode = st.text_input("Enter Passcode", type="password")

    if st.button("Encrypt & Download"):
        if uploaded_image and secret_message and passcode:
            encrypted_filename = encrypt_image(uploaded_image, secret_message, passcode)
            with open(encrypted_filename, "rb") as file:
                st.download_button(
                    label="Download Encrypted Image",
                    data=file,
                    file_name="encryptedImage.png",
                    mime="image/png"
                )
            st.success("Encryption successful! Download the encrypted image above.")
        else:
            st.error("Please upload an image, enter a message, and provide a passcode.")

elif menu == "Decrypt":
    st.header("🔓 Decrypt a Secret Message")
    uploaded_encrypted_image = st.file_uploader("Upload Encrypted Image", type=["png"])
    passcode = st.text_input("Enter Passcode", type="password")

    if st.button("Decrypt"):
        if uploaded_encrypted_image and passcode:
            decrypted_message = decrypt_image(uploaded_encrypted_image, passcode)
            st.success(decrypted_message)
        else:
            st.error("Please upload the encrypted image and enter the correct passcode.")