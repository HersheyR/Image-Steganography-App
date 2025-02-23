import cv2

# Read the encrypted image
img = cv2.imread("encryptedImage.png")

# Get the passcode for decryption
pas = input("Enter passcode for decryption: ")

# ASCII-to-character mapping
c = {i: chr(i) for i in range(255)}

n, m = 0, 0

# Read the passcode length (first 2 pixels)
pass_len_str = ""
for _ in range(2):
    pass_len_str += c[img[n, m, 0]]
    m += 1
pass_len = int(pass_len_str)

# Read the actual stored passcode
stored_pass = ""
for _ in range(pass_len):
    stored_pass += c[img[n, m, 0]]
    m += 1

# Verify the passcode
if stored_pass == pas:
    # Read the message length (next 4 pixels)
    msg_len_str = ""
    for _ in range(4):
        msg_len_str += c[img[n, m, 0]]
        m += 1
    msg_len = int(msg_len_str)

    # Read the actual message
    message = ""
    for _ in range(msg_len):
        message += c[img[n, m, 0]]
        m += 1
        if m >= img.shape[1]:  # Move to next row if out of columns
            m = 0
            n += 1

    print("Decrypted message:", message)
else:
    print("YOU ARE NOT AUTHORIZED!")
