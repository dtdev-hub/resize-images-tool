import cv2
import os

def resize_images(input_folder, output_folder, size):
    # Create a new output directory if it doesn't exist yet
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Browse through the images in the input folder
    for filename in os.listdir(input_folder):
        if filename.endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif', 'webp')): # Check the format of the image files
            img_path = os.path.join(input_folder, filename)
            img = cv2.imread(img_path)
            if img is None:
                print(f"Can't read file: {img_path}")
                continue

            resized_img = cv2.resize(img, size)

            # Save images
            output_path = os.path.join(output_folder, filename)
            cv2.imwrite(output_path, resized_img)
            print(f"Saved file: {output_path}")

input_folder = "input_images"  
output_folder = "output_images" 
size = (70,70)
resize_images(input_folder, output_folder, size)