from PIL import ImageEnhance, Image
import os
import random
import sys

# Set the paths for the input and output folders
input_folder = sys.argv[1]
output_folder = sys.argv[2]
def darken_images_load_folder(input_folder, output_folder, darkness_factor, percentage):
    # Check if the output folder exists, otherwise create it
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Get a list of all files in the input folder
    files = os.listdir(input_folder)

    # Calculate the number of images to be darkened based on the percentage
    num_darkened_images = int(len(files) * percentage)

    # Randomly select images to be darkened
    darkened_images = random.sample(files, num_darkened_images)

    for file in files:
        # Create the full path to the current image
        image_path = os.path.join(input_folder, file)

        # Load the image using PIL
        image = Image.open(image_path)

        if file in darkened_images:
            # Create the enhancer object to darken the image
            enhancer = ImageEnhance.Brightness(image)

            # Apply the darkness factor to the image
            darkened_image = enhancer.enhance(darkness_factor)

            # Create the output path for the darkened image
            output_path = os.path.join(output_folder, file)

            # Save the darkened image
            darkened_image.save(output_path)

            print(f"The image {file} has been darkened and saved in the output folder.")



# Set the darkness factor (0.0 - 1.0, where 0.0 is completely black)
darkness_factor = 0.2

# Set the percentage of images to be darkened
percentage = 0.1

# Load, darken, and save the images
darken_images_load_folder(input_folder, output_folder, darkness_factor, percentage)
