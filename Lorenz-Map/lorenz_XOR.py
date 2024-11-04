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

    # Convert the image to grayscale
    img_gray = img.convert("L")
    img_array = np.array(img_gray)

    # Define initial conditions for the Lorenz system
    initial_state = [0, 0.0001, 0.001]

    # Time points for integration
    t = np.arange(0, 5, 0.05)

    # Solve the Lorenz system
    solution = odeint(lorenz_system, initial_state, t, args=(a, b, c))

    # Normalize the solution to the image dimensions
    solution_norm = np.abs(solution[:, :3]) % 255

    # Resize the solution to fit the image dimensions
    solution_norm = np.resize(solution_norm, img_array.shape)

    # Apply XOR operation
    img_array = (img_array ^ solution_norm.astype(int)) % 256

    # Create the encrypted image
    encrypted_img = Image.fromarray(img_array.astype('uint8'))

    # Save the encrypted image
    encrypted_img.save(output_image_path)

# Example usage
input_image_path = r"/path/to/your/image.jpeg"
output_image_path = r"/path/to/your/xor_lorenz_encrypted_image.jpg"
a, b, c = 0.00000000000001, 102225, 29  # 29 is the best value for Lorenz system
encrypt_image(input_image_path, output_image_path, a, b, c)
