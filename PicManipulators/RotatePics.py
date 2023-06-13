from PIL import Image
import os
import random
import sys

# Set the paths for the input and output folders
input_folder = sys.argv[1]
output_folder = sys.argv[2]
def rotated_images_load_folder(input_folder, output_folder, max_rotation_angle, percentage):
    # Check if the output folder exists, otherwise create it
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Get a list of all files in the input folder
    files = os.listdir(input_folder)

    # Calculate the number of images to be rotated based on the percentage
    num_rotated_images = int(len(files) * percentage)

    # Randomly select images to be rotated
    rotated_images = random.sample(files, num_rotated_images)

    for file in files:
        # Create the full path to the current image
        image_path = os.path.join(input_folder, file)

        # Load the image using PIL
        image = Image.open(image_path)

        if file in rotated_images:
            # Generate random rotation angle
            rotation_angle = random.uniform(-max_rotation_angle, max_rotation_angle)

            # Rotate the image
            rotated_image = rotate_image(image, rotation_angle)

            # Create the output path for the rotated image
            output_path = os.path.join(output_folder, file)

            # Save the rotated image
            rotated_image.save(output_path)

            print(f"The image {file} has been rotated and saved in the output folder.")


def rotate_image(image, rotation_angle):
    rotated_image = image.rotate(rotation_angle, expand=True)
    return rotated_image

# Set the maximum rotation angle in degrees
max_rotation_angle = 20

# Set the percentage of images to be rotated
percentage = 0.1

# Load, rotate, and save the images
rotated_images_load_folder(input_folder, output_folder, max_rotation_angle, percentage)
