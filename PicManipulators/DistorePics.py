from PIL import Image
import os
import random
import sys

# Set the paths for the input and output folders
input_folder = sys.argv[1]
output_folder = sys.argv[2]
def distorted_images_load_folder(input_folder, output_folder, distortion_range, percentage):
    # Check if the output folder exists, otherwise create it
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Get a list of all files in the input folder
    files = os.listdir(input_folder)

    # Calculate the number of images to be distorted based on the percentage
    num_distorted_images = int(len(files) * percentage)

    # Randomly select images to be distorted
    distorted_images = random.sample(files, num_distorted_images)

    for file in files:
        # Create the full path to the current image
        image_path = os.path.join(input_folder, file)

        # Load the image using PIL
        image = Image.open(image_path)

        if file in distorted_images:
            # Generate random distortion values
            distortion_x = random.uniform(-distortion_range, distortion_range)
            distortion_y = random.uniform(-distortion_range, distortion_range)

            # Create distorted image
            distorted_image = distort_image(image, distortion_x, distortion_y)

            # Create the output path for the distorted image
            output_path = os.path.join(output_folder, file)

            # Save the distorted image
            distorted_image.save(output_path)

            print(f"The image {file} has been distorted and saved in the output folder.")

def distort_image(image, distortion_x, distortion_y):
    width, height = image.size
    distorted_image = image.transform((width, height), Image.PERSPECTIVE, (1, distortion_x, 0, distortion_y, 1, 0, 0, 0))
    return distorted_image

# Set the maximum distortion range
distortion_range = 0.2

# Set the percentage of images to be distorted
percentage = 0.1

# Load, distort, and save the images
distorted_images_load_folder(input_folder, output_folder, distortion_range, percentage)
