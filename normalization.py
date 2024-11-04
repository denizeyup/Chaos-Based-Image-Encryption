from PIL import Image
import os

input_folder = "/path/to/your/input_folder/"
output_folder = "/path/to/your/output_folder/"

files = os.listdir(input_folder)

if not os.path.exists(output_folder):
    os.makedirs(output_folder)

for file_name in files:
    # Create the file path
    file_path = os.path.join(input_folder, file_name)
    
    if file_name.lower().endswith((".png", ".jpg", ".jpeg")):
        try:
            image = Image.open(file_path)
            
            # Resize the image to 256x256
            resized_image = image.resize((256, 256))
            
            # Save the resized image
            output_path = os.path.join(output_folder, file_name)
            resized_image.save(output_path)
            
            print(f"{file_name} was successfully resized.")
        
        except Exception as e:
            print(f"An error occurred: {e}")
    
    else:
        print(f"{file_name} is not an image file and was skipped.")

print("Process completed.")
