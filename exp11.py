from PIL import Image, ImageOps
import numpy as np
import matplotlib.pyplot as plt

# ✅ Path to your image
path = r"E:\PWP\harikeshsirexperiment\MU.jpg"

# Open the image
img = Image.open(path)
img_array = np.array(img)

# --------------------------
# a. Display image details
# --------------------------

# Image dimensions (Width x Height)
width, height = img.size

# Shape of image (Height, Width, Channels)
shape = img_array.shape

# Minimum pixel value in Blue channel (Channel B)
if len(shape) == 3 and shape[-1] >= 3:  # RGB image
    min_blue = np.min(img_array[..., 2])
else:
    min_blue = "No Blue channel (grayscale image)"

print(f"Image dimensions (Width x Height): {width} x {height}")
print(f"Image shape: {shape}")
print(f"Minimum pixel value in Blue channel: {min_blue}")

# --------------------------
# b. Padding black spaces
# --------------------------

# Define padding (left, top, right, bottom) in pixels
padding = (50, 50, 50, 50)  # Add 50 pixels on each side

# Add black padding
padded_img = ImageOps.expand(img, border=padding, fill=0)  # fill=0 → black

# Show padded image
padded_img.show()

# Optional: save the padded image
padded_img.save(r"E:\PWP\harikeshsirexperiment\MU_padded.jpg")

# --------------------------
# c. Visualize RGB channels
# --------------------------

# Only if image is RGB
if len(shape) == 3 and shape[-1] >= 3:
    R = img_array[..., 0]
    G = img_array[..., 1]
    B = img_array[..., 2]

    plt.figure(figsize=(15, 5))

    plt.subplot(1, 4, 1)
    plt.imshow(img_array)
    plt.title('Original Image')
    plt.axis('off')

    plt.subplot(1, 4, 2)
    plt.imshow(R, cmap='Reds')
    plt.title('Red Channel')
    plt.axis('off')

    plt.subplot(1, 4, 3)
    plt.imshow(G, cmap='Greens')
    plt.title('Green Channel')
    plt.axis('off')

    plt.subplot(1, 4, 4)
    plt.imshow(B, cmap='Blues')
    plt.title('Blue Channel')
    plt.axis('off')

    plt.tight_layout()
    plt.show()
else:
    print("Image is not RGB; cannot visualize channels.")
