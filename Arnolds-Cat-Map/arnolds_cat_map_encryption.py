from PIL import Image
import numpy as np
import os
import matplotlib.pyplot as plt

def arnold_cat_map(image_matrix, iterations):
    width, height = len(image_matrix), len(image_matrix[0])
    encrypted_image = np.zeros_like(image_matrix)

    for x in range(width):
        for y in range(height):
            new_x = (2 * x + y) % width
            new_y = (x + y) % height
            encrypted_image[new_x][new_y] = image_matrix[x][y]

    if iterations > 1:
        return arnold_cat_map(encrypted_image, iterations - 1)
    else:
        return encrypted_image

def encrypt_image(image_path, iterations=17):
    im = Image.open(image_path)
    image_matrix = np.array(im)

    # Arnold Cat Map
    encrypted_image = arnold_cat_map(image_matrix, iterations)

    # Reshape the image matrix
    flattened_image = encrypted_image.reshape(-1, 4)

    # Shuffle the flattened image
    np.random.shuffle(flattened_image)

    # Reshape the shuffled array back to the original shape
    encrypted_image = flattened_image.reshape(encrypted_image.shape)

    # Diffusion
    diffusion_matrix = np.array([[1, 2, 3, 4],
                                 [5, 6, 7, 8],
                                 [9, 10, 11, 12],
                                 [13, 14, 15, 16]])

    encrypted_image = np.dot(encrypted_image, diffusion_matrix) % 256

    encrypted_image = np.array(encrypted_image, dtype=np.uint8)
    encrypted_image = Image.fromarray(encrypted_image)

    encrypted_image_path = "ArnoldsCatMapsEncryptedImage.bmp"
    encrypted_image.save(encrypted_image_path, "BMP")

    return os.path.abspath(encrypted_image_path)

def histogram_analysis(image_path, save_folder=""):
    im = Image.open(image_path)
    image_matrix = np.array(im)
    flattened_image = image_matrix.reshape(-1)

    unique_values, counts = np.unique(flattened_image, return_counts=True)

    histogram = dict(zip(unique_values, counts))

    # Histogram Plot
    plt.bar(histogram.keys(), histogram.values())
    plt.title('Histogram Analysis')
    plt.xlabel('Pixel Values')
    plt.ylabel('Frequency')
    
    if save_folder:
        plt.savefig(os.path.join(save_folder, 'ArnoldsCatMapsEncryptedHistogram_plot.png'))
    else:
        plt.show()

    # Histogram Table
    with open(os.path.join(save_folder, 'ArnoldsCatMapsEncryptedHistogram_table.txt'), 'w') as file:
        file.write("Pixel Value\tFrequency\tNormalized Frequency\n")
        total_pixels = len(flattened_image)
        for value, count in histogram.items():
            normalized_count = count / total_pixels
            file.write(f"{value}\t\t{count}\t\t{normalized_count:.4f}\n")

# Example usage
original_image_path = r"/path/to/your/image.png"
encrypted_path = encrypt_image(original_image_path, iterations=5)
print(f"Encrypted Image Path: {encrypted_path}")

# Histogram analysis and saving
save_folder = "Histogram_analysis"
os.makedirs(save_folder, exist_ok=True)
histogram_analysis(encrypted_path, save_folder)
