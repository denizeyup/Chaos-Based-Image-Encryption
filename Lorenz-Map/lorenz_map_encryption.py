import numpy as np
from scipy.integrate import odeint
from PIL import Image

# Lorenz system equations
def lorenz_system(state, t, a, b, c):
    x, y, z = state
    dx_dt = a * (y - x)
    dy_dt = -x * z + c * y
    dz_dt = x * y - b * z
    return [dx_dt, dy_dt, dz_dt]

# Function that performs image encryption
def encrypt_image(input_image_path, output_image_path, a, b, c):
    # Load the image
    img = Image.open(input_image_path)
    width, height = img.size

    # Convert the image to grayscale
    img_gray = img.convert("L")
    img_array = np.array(img_gray)

    # Define initial conditions for the Lorenz system
    initial_state = [0, 0.0001, 0.001]

    # Time points for integration
    t = np.arange(0, 5, 0.05)

    # Solve the Lorenz system
    solution = odeint(lorenz_system, initial_state, t, args=(a, b, c))

    # Normalize the solution to image dimensions
    solution_norm = np.abs(solution[:, :3]) % 255

    # Check dimensions
    print("img_array shape:", img_array.shape)
    print("solution_norm shape:", solution_norm.shape)

    # Resize the solution to match the image size
    solution_norm = np.resize(solution_norm, img_array.shape)

    # Create the encrypted image
    encrypted_img_array = (img_array + solution_norm.astype(int)) % 256
    encrypted_img = Image.fromarray(encrypted_img_array.astype('uint8'))

    # Save the encrypted image
    encrypted_img.save(output_image_path)

# Example usage
input_image_path = r"/path/to/your/image.jpeg"
output_image_path = r"/path/to/your/lorenz_encrypted_image.jpg"
a, b, c = 10, 8/3, 28
encrypt_image(input_image_path, output_image_path, a, b, c)
