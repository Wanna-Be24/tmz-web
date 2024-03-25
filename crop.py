from PIL import Image
import sys

def trim_transparent_borders(image):
    # Convert image to RGBA mode if not already
    if image.mode != 'RGBA':
        image = image.convert('RGBA')

    # Get the alpha channel (transparency) from the image
    alpha = image.split()[3]

    # Get the bounding box of the non-transparent regions
    bbox = alpha.getbbox()

    if bbox:
        # Crop the image to the bounding box
        return image.crop(bbox)
    else:
        # Image is fully transparent, return None or raise an exception
        return None

def main(input_filename):
    # Load the PNG image
    img = Image.open(input_filename)

    # Trim transparent borders
    trimmed_img = trim_transparent_borders(img)

    if trimmed_img:
        # Save the trimmed image with the provided output filename
        trimmed_img.save("output.png")
        print(f"Image trimmed and saved as output.png successfully.")
    else:
        print("Image is fully transparent. No borders to trim.")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python your_script.py input_filename.png")
        sys.exit(1)
    input_filename = sys.argv[1]
    main(input_filename)
