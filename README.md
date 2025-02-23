# Image Steganography App Using LSB (Least Significant Bit Method) Modification

## Project Overview

This project is an **Image Steganography App** built using Python and Streamlit, allowing users to securely hide secret messages within images and later retrieve them using a passcode. It offers both encryption and decryption functionalities through a user-friendly web interface.

## Features

- **Encrypt** secret messages into images.
- **Decrypt** hidden messages using a passcode.
- Supports a common image format (`.png`).
- Simple and interactive Streamlit UI.
- Passcode protection for secure message retrieval.

## Project Structure

```
├── decrypt.py            # Script to decrypt messages from images
├── encrypt.py            # Script to encrypt messages into images
├── main_app.py           # Streamlit app integrating encryption & decryption
├── mypic.png             # Sample image for testing
└── README.md             # Project documentation
```

## How It Works

### Encryption Process (`encrypt.py` & `main_app.py`)

1. **User Input:** Secret message and passcode.
2. **Data Encoding:**
   - Passcode length and passcode stored in image pixels.
   - Message length and message embedded into the image's blue channel.
3. **Output:** Encrypted image (`encryptedImage.png`).

### Decryption Process (`decrypt.py` & `main_app.py`)

1. **User Input:** Encrypted image and passcode.
2. **Passcode Verification:** Extract stored passcode from the image and verify.
3. **Message Extraction:** If passcode is valid, extract the hidden message.
4. **Output:** Display decrypted message.

## Technologies Used

- Python: Core programming language.
- OpenCV: Image processing and manipulation.
- NumPy: Efficient numerical operations on image data.
- Streamlit: Interactive web interface for the app.