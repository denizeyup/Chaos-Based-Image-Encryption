from PIL import Image
import numpy as np
import os

def henon_map(x, y, a, b, width, height):
    new_x = y + 1 - a * x**2
    new_y = b * x
    return int(new_x) % width, int(new_y) % height

def shuffle_reshape(image_matrix):
    # Flatten the image matrix
    flat_image = image_matrix.flatten()

    # Shuffle the flattened array
    np.random.shuffle(flat_image)

    # Determine the dimensions of the original image for reshaping
    original_shape = image_matrix.shape

    # Reshape the shuffled array back to the original shape
    reshaped_image = flat_image.reshape(original_shape)

    return reshaped_image

def encrypt_image_henon(image_matrix, a, b, iterations):
    for _ in range(iterations):
        # Shuffle and reshape before encryption
        shuffled_image = shuffle_reshape(image_matrix)

        new_image_matrix = np.zeros_like(image_matrix, dtype=np.uint8)
        for x in range(image_matrix.shape[0]):
            for y in range(image_matrix.shape[1]):
                new_x, new_y = henon_map(x, y, a, b, image_matrix.shape[0], image_matrix.shape[1])
                new_image_matrix[x, y] = shuffled_image[new_x, new_y]

        image_matrix = new_image_matrix.copy()

    return image_matrix

def encrypt_image_henon_wrapper(image_path, a, b, iterations=5):
    im = Image.open(image_path)
    image_matrix = np.array(im)

    encrypted_image = encrypt_image_henon(image_matrix, a, b, iterations)

    encrypted_image = Image.fromarray(encrypted_image)
    
    encrypted_image_path = "HenonMapEncrypted_Shuffled_Reshaped.bmp"
    encrypted_image.save(encrypted_image_path, "BMP")

    return os.path.abspath(encrypted_image_path)

# Example usage
a_value = 1.4
b_value = 0.3
encrypted_path_henon = encrypt_image_henon_wrapper('/path/to/your/image.png', a_value, b_value, iterations=100)
print(f"Encrypted Image Path (Henon Map): {encrypted_path_henon}")
