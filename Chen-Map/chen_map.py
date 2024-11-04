import numpy as np
from scipy.integrate import odeint
from PIL import Image

# Chen chaotic map equations
def chen_system(state, t, a, b, c):
    x, y, z = state
    dx_dt = a * (y - x)
    dy_dt = (c - a) * x - x * z + c * y
    dz_dt = x * y - b * z
    return [dx_dt, dy_dt, dz_dt]

# Function that performs the image encryption
def encrypt_image_chen(input_image_path, output_image_path, a, b, c):
    # Load the image
    img = Image.open(input_image_path)
    width, height = img.size

    # Convert the image to grayscale
    img_gray = img.convert("L")
    img_array = np.array(img_gray)

    # Define initial conditions for the Chen system
    initial_state = [0, 0.001, 0.001]

    # Time points for integration
    t = np.linspace(0, 1, 100)

    # Solve the Chen system
    solution = odeint(chen_system, initial_state, t, args=(a, b, c), full_output=1, rtol=1e-5)

    # Normalize the solution to the image dimensions
    solution_norm = np.abs(solution[0][:, :3]) % 255

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
input_image_path = r"/path/to/your/input_image.jpg"
output_image_path = r"/path/to/your/output_image.jpg"
a, b, c = 35, 3, 28.4  # Suitable parameter values for the Chen chaotic map
encrypt_image_chen(input_image_path, output_image_path, a, b, c)
