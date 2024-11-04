import numpy as np
from PIL import Image
import math

def calculate_entropy(image_path):
    # Open the image
    img = Image.open(image_path)
    # Resize the image to N*N
    img = img.resize((N, N))
    # Convert the image to a numpy array
    img_array = np.array(img)
    
    # Flatten the pixel values of the image
    pixels = img_array.flatten()
    
    # Calculate the histogram of the pixel values
    histogram, _ = np.histogram(pixels, bins=256, range=[0, 256])
    
    # Convert histogram values to probability distribution
    probabilities = histogram / float(N * N)
    
    # Calculate entropy
    entropy = -np.sum(probabilities * np.log2(probabilities + 1e-10))
    
    return entropy

# Example Usage
N = 256  # Image size (N*N)
image_path_plain = r"/path/to/your/plain_image.jpg"  # Plain image file path
image_path_encrypted = r"/path/to/your/encrypted_image.png"

# Calculate entropy for the plain image
entropy_plain = calculate_entropy(image_path_plain)
print(f"Plain Image Entropy: {entropy_plain}")

# Calculate entropy for the encrypted image
entropy_encrypted = calculate_entropy(image_path_encrypted)
print(f"Encrypted Image Entropy: {entropy_encrypted}")
