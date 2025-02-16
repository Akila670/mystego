import cv2
import os
#import string

# Load the image
img = cv2.imread("D:\sunflower.jpg")

# Check if image is loaded correctly
if img is None:
    print("Error: Image not found. Check the path!")
    exit()

# Input message and password
msg = input("Enter secret message: ")
password = input("Enter a passcode: ")

# Character dictionary
d = {chr(i): i for i in range(255)}
c = {i: chr(i) for i in range(255)}

# Encoding message in image
m, n, z = 0, 0, 0
for i in range(len(msg)):
    img[m, n, z] = d[msg[i]]  # Store ASCII value in pixel
    n += 1
    if n >= img.shape[1]:  
        n = 0
        m += 1
    z = (z + 1) % 3  

# Save the encrypted image
encrypted_image_path = "encryptedImage.jpg"
cv2.imwrite(encrypted_image_path, img)

print("Message successfully hidden in image!")

# Decoding
message = ""
m, n, z = 0, 0, 0
pas = input("Enter passcode for Decryption: ")

if password == pas:
    for i in range(len(msg)):
        message += c[img[m, n, z]]
        n += 1
        if n >= img.shape[1]:
            n = 0
            m += 1
        z = (z + 1) % 3  

    print("Decrypted Message:", message)
else:
    print("Incorrect passcode! Decryption failed.")
