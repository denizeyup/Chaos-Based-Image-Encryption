import numpy as np
from PIL import Image

# Function to create x0 from the key string
def create_x0(key_str):
    n = len(key_str)
    k = 8
    sum_val = 0

    for i in range(1, n + 1):
        sum_val += ord(key_str[i - 1]) * (2 ** k)
        k += 8

    k = 8
    sum_val += ord(key_str[0]) * (2 ** k)

    return sum_val / (2 ** k)

# Function to create iteration set
def itr_creator(key_str, itration):
    x0 = create_x0(key_str)
    xx = x0
    r = 3.9999
    itration[0] = int(x0 * 256) + 1

    for i in range(1, 256):
        while True:
            x1 = r * x0 * (1 - x0)

            if not (0 <= x1 < 1):
                x1 = x1 % 1
            
            x0 = x1
            xn = int(x1 * 256)
            chk_found = 0

            for k in range(i):
                if itration[k] == xn:
                    chk_found = 1

            if chk_found == 0:
                itration[i] = xn
                break

    return xx

# Function used for encryption
def encrypt_image(image, key):
    itration = [0] * 256
    random_numbers = np.array([])

    for i in range(256):
        x0 = itr_creator(key, itration)
        random_numbers = np.append(random_numbers, x0)

    encrypted_image = np.zeros_like(image, dtype=np.float32)

    for i in range(image.shape[0]):
        k_values = (random_numbers[:image.shape[1]] * 256).astype(int)
        positions = (np.arange(image.shape[1]) + k_values) % 256

        # Perform XOR operation with appropriate type conversion
        xor_result = image[i, :, :] ^ random_numbers[positions][:, None].astype(image.dtype)

        encrypted_image[i, :, :] = xor_result.astype(np.float32)

    return encrypted_image

# Function used for decryption
def decrypt_image(encrypted_image, key):
    itration = [0] * 256
    random_numbers = np.array([])

    for i in range(256):
        x0 = itr_creator(key, itration)
        random_numbers = np.append(random_numbers, x0)

    decrypted_image = np.zeros_like(encrypted_image, dtype=np.float32)

    for i in range(encrypted_image.shape[0]):
        k_values = (random_numbers[:encrypted_image.shape[1]] * 256).astype(int)
        positions = (np.arange(encrypted_image.shape[1]) + k_values) % 256

        # Perform XOR operation with appropriate type conversion
        xor_result = encrypted_image[i, :, :].astype(int) ^ np.round(random_numbers[positions][:, None]).astype(int)

        decrypted_image[i, :, :] = xor_result.astype(np.float32)

    return decrypted_image

# Function to save image
def save_image(image, file_path):
    pil_image = Image.fromarray((image * 255).astype(np.uint8))
    pil_image.save(file_path)

# Original image file path
file_path = r"/path/to/your/image.jpeg"
original_image = np.array(Image.open(file_path))

# Key string
key = "0123654789"

# Encrypt the image
encrypted_image = encrypt_image(original_image, key)

# Save the encrypted image
output_file_path = r"/path/to/your/encrypted_image.jpeg"
save_image(encrypted_image, output_file_path)
print(f"Encrypted image saved: {output_file_path}")

# Measure encryption and decryption times
import timeit

encryption_time = timeit.timeit("encrypt_image(original_image, key)", globals=globals(), number=1)
decryption_time = timeit.timeit("decrypt_image(encrypted_image, key)", globals=globals(), number=1)

print(f"Encryption Time: {encryption_time} seconds")
print(f"Decryption Time: {decryption_time} seconds")
