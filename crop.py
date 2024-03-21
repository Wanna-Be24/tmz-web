from PIL import Image

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

def main():
    # Load the PNG image
    img = Image.open("pretrim.png")

    # Trim transparent borders
    trimmed_img = trim_transparent_borders(img)

    if trimmed_img:
        # Save the trimmed image
        trimmed_img.save("trimmed_image.png")
        print("Image trimmed and saved successfully.")
    else:
        print("Image is fully transparent. No borders to trim.")

if __name__ == "__main__":
    main()
