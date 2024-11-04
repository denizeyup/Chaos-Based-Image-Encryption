import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

class ChuaCircuit:
    def __init__(self, alpha=15.6, beta=28, m0=-1.143, m1=-0.714, m2=-0.286):
        self.alpha = alpha
        self.beta = beta
        self.m0 = m0
        self.m1 = m1
        self.m2 = m2

    def chua_system(self, t, X):
        x, y, z = X
        dx = self.alpha * (y - x - self.m1 * x**3 + self.m0 * x**2 + self.m2)
        dy = x - y + z
        dz = -self.beta * y
        return [dx, dy, dz]

def encrypt_image(image_path):
    # Load the image
    img = plt.imread(image_path)
    shape = img.shape

    # Flatten the image
    flat_img = img.flatten()

    # Initialize Chua's Circuit
    chua = ChuaCircuit()

    # Time span
    t_span = (0, 10)
    
    # Initial conditions
    initial_conditions = [0.1, 0.2, 0.3]

    # Solve the system using a more accurate method (RK45)
    sol = solve_ivp(chua.chua_system, t_span, initial_conditions, t_eval=np.linspace(0, 10, len(flat_img)), method='RK45')

    # Use the solution to encrypt the image
    encrypted_img = flat_img + sol.y[0][:len(flat_img)].tolist()

    # Reshape the encrypted data back to the original image shape
    encrypted_img = np.array(encrypted_img).reshape(shape)

    # Display the original and encrypted images
    plt.figure(figsize=(10, 5))
    plt.subplot(1, 2, 1)
    plt.imshow(img, cmap='gray')  # If the original image is grayscale
    plt.title('Original Image')

    plt.subplot(1, 2, 2)
    plt.imshow(encrypted_img, cmap='gray')  # If the encrypted image is grayscale
    plt.title('Encrypted Image')

    plt.show()

# Example usage
encrypt_image('/path/to/your/image.jpeg')
