import cv2
import numpy as np
import matplotlib.pyplot as plt

def mse(imageA, imageB):
    err = np.sum((imageA - imageB) ** 2)
    err /= float(imageA.shape[0] * imageA.shape[1])
    return err

def main():
    # Load the original and encrypted images
    original_image = cv2.imread(r"/path/to/your/plain_image.jpg")
    encrypted_image = cv2.imread(r"/path/to/your/encrypted_image.png")

    # Convert images to grayscale (if they are colored)
    original_image_gray = cv2.cvtColor(original_image, cv2.COLOR_BGR2GRAY)
    encrypted_image_gray = cv2.cvtColor(encrypted_image, cv2.COLOR_BGR2GRAY)

    # Perform MSE similarity analysis
    similarity_score = mse(original_image_gray, encrypted_image_gray)
    print(f"MSE Similarity Score: {similarity_score}")

    # Create a plot
    plt.figure()

    # Display the original and encrypted images side by side
    plt.subplot(2, 1, 1)
    plt.imshow(original_image_gray, cmap='gray')
    plt.title("Original Image")

    plt.subplot(2, 1, 2)
    plt.imshow(encrypted_image_gray, cmap='gray')
    plt.title("Encrypted Image")

    plt.show()

if __name__ == "__main__":
    main()
