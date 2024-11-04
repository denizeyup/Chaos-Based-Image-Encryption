# Image Processing and Chaotic Encryption

This repository showcases various image processing techniques combined with chaotic encryption methods. It includes implementations of Lorenz system-based encryption, Logistic map transformations, Arnold Cat map encryption, Henon map encryption, and visualization of chaotic behaviors through phase diagrams. These techniques highlight the application of chaos theory in secure image encryption and analysis.

## Setup and Installation

To run the scripts in this repository, ensure you have Python installed. You can install the required dependencies using:

```bash
pip install numpy matplotlib pillow opencv-python scipy
```

## Core Features

### Chaotic Encryption Methods

Chaotic systems are highly sensitive to initial conditions, making them ideal for cryptographic applications. This repository implements several encryption methods based on chaotic dynamics:

#### 1. **Lorenz System Encryption**

The Lorenz system is a set of differential equations known for chaotic solutions. This method encrypts images by applying a chaotic transformation derived from the Lorenz attractor.

- **Key Parameters:** `a`, `b`, `c` (Lorenz system constants)
- **Process:** 
  - Solve the Lorenz system equations.
  - Normalize the chaotic outputs to fit image dimensions.
  - XOR the image with the chaotic sequence for encryption.

**Usage:**
```python
encrypt_image('input_image.jpeg', 'output_image.jpg', 0.00000000000001, 102225, 29)
```

#### 2. **Logistic Map Encryption**

The Logistic map is another chaotic system used for image encryption. This method leverages the map's properties to generate a chaotic sequence that encrypts the image by transforming pixel intensities.

- **Key Parameter:** `r` (control parameter for chaos)
- **Process:**
  - Generate a chaotic sequence using the Logistic map.
  - Use this sequence to permute and modify the pixel values of the image.

**Usage:**
```python
chaotic_encryption('input_image.jpeg', 3.99999, 10)
```

#### 3. **Henon Map Encryption**

The Henon map is used to shuffle and encrypt images. This method applies the Henon chaotic equations iteratively to permute image pixels, ensuring high security.

- **Key Parameters:** `a`, `b` (Henon map constants)
- **Process:**
  - Apply Henon map iterations to generate new pixel positions.
  - Encrypt the image by rearranging pixel values based on the generated chaotic sequence.

**Usage:**
```python
encrypt_image_henon_wrapper('input_image.png', 1.4, 0.3, 100)
```

#### 4. **Arnold Cat Map Encryption**

The Arnold Cat map is a well-known chaotic map that scrambles an image by iteratively permuting pixel positions. This method is particularly effective for visual encryption, producing highly scrambled results.

- **Process:**
  - Apply the Arnold Cat map transformation iteratively to the image matrix.
  - Shuffle and reshape the matrix to enhance the chaotic effect.

**Usage:**
```python
encrypt_image('input_image.png', iterations=5)
```

#### 5. **Chen System Encryption**

The Chen system is a chaotic system similar to the Lorenz system but with different dynamics. This method uses the Chen system's chaotic outputs to encrypt images.

- **Key Parameters:** `a`, `b`, `c` (Chen system constants)
- **Process:**
  - Solve the Chen system equations.
  - Normalize and apply the chaotic outputs to the image pixels for encryption.

**Usage:**
```python
goruntu_sifrele_chen('input_image.jpg', 'encrypted_image.jpg', 35, 3, 28.4)
```

### Visualization of Chaotic Behavior

Phase diagrams are essential for visualizing the chaotic behavior of dynamic systems. This repository includes scripts to generate 2D and 3D phase diagrams for the Lorenz system, Logistic map, and more.

#### 1. **Lorenz System Phase Diagrams**

Phase diagrams for the Lorenz system illustrate the chaotic trajectories in different dimensions (x-y, x-z, y-z).

- **3D Phase Diagram:**
  ```python
  plot_lorenz_3d_phase_diagram(10.0, 28.0, 8.0/3.0, [0.1, 0.0, 0.0], 25, 10000)
  ```

#### 2. **Logistic Map Bifurcation Diagram**

The bifurcation diagram shows the complex behavior of the Logistic map as the control parameter `r` varies. This highlights the transition from stability to chaos.

- **Bifurcation Diagram:**
  ```python
  bifurcation_diagram(2.4, 4.0, 10000, 1000, 0.5)
  ```

## Additional Features

### Entropy Calculation

Entropy measures the randomness or information content in an image. Higher entropy in encrypted images indicates more secure encryption.

**Usage:**
```python
entropy = calculate_entropy('image.jpg')
print(f'Entropy: {entropy}')
```

### Mean Squared Error (MSE)

MSE quantifies the difference between two images, useful for evaluating encryption strength by comparing original and encrypted images.

**Usage:**
```python
similarity_score = mse(imageA, imageB)
print(f'MSE Similarity Score: {similarity_score}')
```

### Image Processing Utilities

- **Grayscale Conversion:** Simplifies image data for further analysis.
- **Image Resizing:** Resizes images to standard dimensions for consistent processing.
- **Histogram Analysis:** Analyzes the distribution of pixel intensities in specific color channels.

## Usage

To use these scripts:
1. Clone the repository:
   ```bash
   git clone https://github.com/denizeyup/Chaos-Based-Image-Encryption.git
   ```
2. Navigate to the repository:
   ```bash
   cd Chaos-Based-Image-Encryption
   ```
3. Execute the scripts as per the instructions provided in each section.
