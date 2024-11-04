import numpy as np
from PIL import Image

def logistic_map(x, r):
    return r * x * (1 - x)

def chaotic_encryption(image_path, r, iterations):
    original_image = Image.open(image_path)
    width, height = original_image.size
    img_array = np.array(original_image)

    # Generate a strong initial encryption key
    encryption_key = np.random.rand()

    print("Initial Encryption Key:", encryption_key)

    for _ in range(iterations):
        # Update the key in each iteration
        encryption_key = logistic_map(encryption_key, r)

        for i in range(1, width-1):
            for j in range(1, height-1):
                img_array[i, j] = logistic_map((img_array[i-1, j-1] + img_array[i, j-1] + img_array[i+1, j-1] +
                                                img_array[i-1, j] + img_array[i+1, j] +
                                                img_array[i-1, j+1] + img_array[i, j+1] + img_array[i+1, j+1])/255, r + encryption_key) * 255

    encrypted_image = Image.fromarray(img_array.astype(np.uint8))
    encrypted_image.save("LogisticMapEncryptedImage.bmp")

# Example usage
image_path = r"/path/to/your/image.jpeg"
r_value = 3.99999  # Chaotic behavior between 3.57 and 3.83
iteration_count = 10

chaotic_encryption(image_path, r_value, iteration_count)
