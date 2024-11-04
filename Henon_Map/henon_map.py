from PIL import Image
import numpy as np
import os

def henon_map(x, y, a, b, width, height):
    new_x = y + 1 - a * x**2
    new_y = b * x
    return int(new_x) % width, int(new_y) % height

def encrypt_image_henon(image_matrix, a, b, iterations):
    width, height = len(image_matrix), len(image_matrix[0])

    for _ in range(iterations):
        new_image_matrix = np.zeros_like(image_matrix, dtype=np.uint8)
        for x in range(width):
            for y in range(height):
                new_x, new_y = henon_map(x, y, a, b, width, height)
                new_image_matrix[x, y] = image_matrix[new_x, new_y]

        image_matrix = new_image_matrix.copy()

    return image_matrix

def encrypt_image_henon_wrapper(image_path, a, b, iterations=100):
    im = Image.open(image_path)
    image_matrix = np.array(im)

    encrypted_image = encrypt_image_henon(image_matrix, a, b, iterations)

    encrypted_image = Image.fromarray(encrypted_image)
    
    encrypted_image_path = "HenonMapEncrypted.bmp"
    encrypted_image.save(encrypted_image_path, "BMP")

    return os.path.abspath(encrypted_image_path)

# Example usage
a_value = 7
b_value = 0.4
encrypted_path_henon = encrypt_image_henon_wrapper('/path/to/your/image.jpeg', a_value, b_value, iterations=100)
print(f"Encrypted Image Path (Henon Map): {encrypted_path_henon}")
