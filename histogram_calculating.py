from PIL import Image
import numpy as np
import os
import matplotlib.pyplot as plt

def single_channel_histogram(image_path, channel, save_folder=""):
    # Open the image
    im = Image.open(image_path)
    
    # Create the image matrix
    image_matrix = np.array(im)
    
    # Flatten the image matrix and select the desired channel
    flattened_channel = image_matrix[:, :, channel].flatten()
    
    # Calculate unique values and their frequencies
    unique_values, counts = np.unique(flattened_channel, return_counts=True)

    # Create the histogram dictionary
    histogram = dict(zip(unique_values, counts))

    # Plot the histogram
    plt.hist(flattened_channel, bins=range(256), density=False)
    plt.title('Histogram Analysis')
    plt.xlabel('Pixel Values')
    plt.ylabel('Frequency')
    
    # Save or show the plot
    if save_folder:
        plt.savefig(os.path.join(save_folder, f'Single_Channel_Histogram_Channel_{channel}.png'))
    else:
        plt.show()

    # Save the histogram table
    with open(os.path.join(save_folder, f'Single_Channel_Histogram_Channel_{channel}_table.txt'), 'w') as file:
        file.write("Pixel Value\tFrequency\tNormalized Frequency\n")
        total_pixels = len(flattened_channel)
        for value, count in histogram.items():
            normalized_count = count / total_pixels
            file.write(f"{value}\t\t{count}\t\t{normalized_count:.4f}\n")

# Example Usage
image_path = r"/path/to/your/image.png"
channel_to_analyze = 0  # 0: Red, 1: Green, 2: Blue

# Perform histogram analysis and save
save_folder = "Histogram_analysis"
os.makedirs(save_folder, exist_ok=True)
single_channel_histogram(image_path, channel_to_analyze, save_folder)
