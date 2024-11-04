from PIL import Image
import numpy as np
import os

def arnold_cat_map(image_matrix, iterations):
    width, height = len(image_matrix), len(image_matrix[0])
    encrypted_image = [[0] * height for _ in range(width)]

    for x in range(width):
        for y in range(height):
            new_x = (2 * x + y) % width
            new_y = (x + y) % height
            encrypted_image[new_x][new_y] = image_matrix[x][y]

    if iterations > 1:
        return arnold_cat_map(encrypted_image, iterations - 1)
    else:
        return encrypted_image

def encrypt_image(image_path, iterations=5):
    im = Image.open(image_path)
    image_matrix = np.array(im).tolist()

    encrypted_image = arnold_cat_map(image_matrix, iterations)

    encrypted_image = np.array(encrypted_image, dtype=np.uint8)
    encrypted_image = Image.fromarray(encrypted_image)

    encrypted_image_path = "ArnoldCatMap.bmp"
    encrypted_image.save(encrypted_image_path, "BMP")

    return os.path.abspath(encrypted_image_path)

# Example usage
encrypted_path = encrypt_image(r"/path/to/your/image.jpeg", iterations=10)
print(f"Encrypted Image Path: {encrypted_path}")
