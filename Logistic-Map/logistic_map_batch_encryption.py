from PIL import Image
import math
import random
import os

def word_to_bit_array(key):
    bit_array = []
    for byte in key:
        bits = [int(bit) for bit in f"{byte:08b}"]
        bit_array.extend(bits)
    return bit_array

def bits_to_decimal(bits):
    decimal_value = 0
    for i, bit in enumerate(bits):
        decimal_value += bit * (2 ** (len(bits) - 1 - i))
    return decimal_value

def show_bits(key):
    bit_array = word_to_bit_array(key)
    for i in range(0, len(bit_array), 8):
        binary_chunk = bit_array[i:i+8]
        decimal_value = bits_to_decimal(binary_chunk)
        print(' '.join(map(str, binary_chunk)), "-->", decimal_value)

def create_x0(key):
    n = len(key)
    k = 8
    z = math.log(n, 2)
    bit_array = word_to_bit_array(key)
    total = sum(bits_to_decimal(bit_array[i:i+8]) for i in range(0, len(bit_array), 8))
    x0 = total / (2**(k+z))
    return x0

def create_iteration_list(x0, iterations=256, r=3.99999):
    iteration_list = []
    iteration_list.append(int(x0 * 256) + 1)

    for _ in range(1, iterations):
        while True:
            x1 = r * x0 * (1 - x0)
            x0 = x1
            xn = int(x1 * 256)
            if xn not in iteration_list:
                iteration_list.append(xn)
                break

    return iteration_list

def encrypt_image(image_path, key):
    img = Image.open(image_path)
    width, height = img.size
    pixels = list(img.getdata())

    x0 = create_x0(key)
    iteration_list = create_iteration_list(x0)

    encrypted_pixels = []
    for i, pixel in enumerate(pixels):
        if isinstance(pixel, tuple) and len(pixel) == 3:
            if pixel[0] == pixel[1] == pixel[2]:  # Check if all channels have the same value
                r_value = pixel[0]
                k = iteration_list.index(r_value)
                z = random.randint(0, 256)
                pos = (i + k + z) % 256
                pp_r = iteration_list[pos]
                encrypted_pixels.append((pp_r, pp_r, pp_r))
            else:
                # If channels have varying values, skip this pixel
                encrypted_pixels.append(pixel)
        else:
            # If pixel is not a tuple or doesn't have three channels, skip this pixel
            encrypted_pixels.append(pixel)

    encrypted_img = Image.new("RGB", (width, height))
    encrypted_img.putdata(encrypted_pixels)
    encrypted_img.save("E.png")
    key = bytes([(byte + i) % 256 for byte in key])
    return "encrypted_image.png"  # Return the filename

def encrypt_images_in_folder(input_folder, output_folder, key):
    for index, filename in enumerate(os.listdir(input_folder)):
        if filename.endswith(".jpg") or filename.endswith(".jpeg") or filename.endswith(".png"):
            image_path = os.path.join(input_folder, filename)
            encrypted_image_filename = encrypt_image(image_path, key)
            output_path = os.path.join(output_folder, f"Enc_{index:04d}_{filename}")  # Use index in the output filename
            os.rename("E.png", output_path)
            print(f"Encrypted Image saved as: {output_path}")

# Example usage:
input_folder = r"/path/to/input/folder"
output_folder = r"/path/to/output/folder"
key = b"5a8x0b._3*demt=9"

encrypt_images_in_folder(input_folder, output_folder, key)
