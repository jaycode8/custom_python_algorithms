# ======================= script to save mnist images to a drive storage

#  ============ doing the code a google colab environment

#  ==== libraries
import os
from PIL import Image
from tensorflow.keras.datasets import mnist
import numpy as np

# ========== mounting drive storage
from google.colab import drive
drive.mount('/content/drive')

base_dir = '/content/drive/MyDrive/Deep Learning Resources/Num'
zero = os.path.join(base_dir, '0')

# Load the MNIST dataset
(train_images, train_labels), (test_images, test_labels) = mnist.load_data()

# Filter zero-digit images
zero_images = train_images[train_labels == 0]

# Select 1000 zero-digit images randomly
random_indices = np.random.choice(zero_images.shape[0], size=1000, replace=False)
selected_images = zero_images[random_indices]

# Save the selected images
for i, image in enumerate(selected_images):
    image_path = os.path.join(zero, f"zero_{str(i+1).zfill(3)}.png")
    Image.fromarray(image).save(image_path)