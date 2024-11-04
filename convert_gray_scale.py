from PIL import Image

def convert_to_grayscale(input_path, output_path):
    # Load the input image
    original_image = Image.open(input_path)

    # Convert to grayscale
    grayscale_image = original_image.convert("L")

    # Save the grayscale image
    grayscale_image.save(output_path)

# Example usage
input_image_path = r"/path/to/your/input_image.png"
output_image_path = r"/path/to/your/output_image.png"

convert_to_grayscale(input_image_path, output_image_path)
