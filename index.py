from bing_image_downloader import downloader
from PIL import Image
import os
import shutil

def download_images(keyword, output_folder, num_images=1, min_width=1000, min_height=1000):
    # Configure the download options
    downloader.download(keyword, limit=num_images, output_dir=output_folder, adult_filter_off=True, force_replace=False)

    # Iterate over the downloaded images and move them to the desired folder if they meet the size criteria
    for i in range(1, num_images + 1):
        image_path = os.path.join(output_folder, keyword, f"{keyword}_{i}.jpg")

        # Check the dimensions of the image
        with Image.open(image_path) as img:
            width, height = img.size

        # Move the image to the desired folder if it meets the size criteria
        if width >= min_width and height >= min_height:
            new_image_path = os.path.join(output_folder, f"{keyword}_{i}.jpg")
            shutil.move(image_path, new_image_path)
            print(f"Image saved to {new_image_path}")
        else:
            print(f"The downloaded image {i} did not meet the size criteria ({min_width}x{min_height}).")

if __name__ == "__main__":
    # Ask the user for the keyword and the number of images
    user_input = input("Enter the search keyword and the number of images (e.g., 'apple 5'): ")
    
    # Split the input by spaces and join the parts after the first one as the keyword
    parts = user_input.split()
    search_keyword = ' '.join(parts[:-1])
    num_images_str = parts[-1]

    # Convert the number of images to an integer
    num_images = int(num_images_str)

    # Specify the output folder
    output_folder = "/home/user1/github-projects/image-app-v4/downloaded-images/"

    # Specify the minimum dimensions for qualifying images
    min_width = 1000
    min_height = 1000

    # Create the output folder if it doesn't exist
    os.makedirs(output_folder, exist_ok=True)

    # Download images and save them to the specified folder
    download_images(search_keyword, output_folder, num_images, min_width, min_height)

