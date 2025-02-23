import cv2

# Read the image (use PNG to avoid compression issues)
img = cv2.imread("mypic.png")

# Get the secret message and password from the user
msg = input("Enter secret message: ")
password = input("Enter a passcode: ")

# Convert message length to a fixed-size header (store first 4 pixels)
msg_len = len(msg)
header = f"{msg_len:04d}"  # Store length as a 4-digit number

# Store the passcode length in 2 pixels
pass_len = len(password)
pass_header = f"{pass_len:02d}"  # Store passcode length as 2 digits

# Combine passcode, passcode header, message header, and message
data = pass_header + password + header + msg  

# Create ASCII mapping
d = {chr(i): i for i in range(255)}

# Initialize variables for embedding the message
n, m = 0, 0

# Embed the data into the blue channel
for char in data:
    img[n, m, 0] = d[char]  # Store in blue channel
    m += 1
    if m >= img.shape[1]:  # Move to next row if out of columns
        m = 0
        n += 1

# Save the encrypted image as PNG
cv2.imwrite("encryptedImage.png", img)
print("Message successfully encrypted")