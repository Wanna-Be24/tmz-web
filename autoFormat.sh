#!/bin/bash

# Check if the user provided the image file path and output filename
if [ $# -ne 2 ]; then
    echo "Usage: $0 /path/to/image.jpg output_filename.png"
    exit 1
fi

# Check if curl is installed
if ! command -v curl &> /dev/null; then
    echo "Error: curl is not installed."
    exit 1
fi

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "Error: Python 3 is not installed."
    exit 1
fi

# Your remove.bg API key
API_KEY="nSK83iMBbVAT1vfgrqAvGREg"

# API endpoint
API_ENDPOINT="https://api.remove.bg/v1.0/removebg"

# Path to the input image file
IMAGE_PATH="$1"

# Output filename for the background removed image
OUTPUT_FILENAME="$2"

# Run curl command to remove background
curl -H "X-API-Key: $API_KEY" \
     -F "image_file=@$IMAGE_PATH" \
     -F "size=auto" \
     -f $API_ENDPOINT -o "$OUTPUT_FILENAME"

# Check if curl command was successful
if [ $? -ne 0 ]; then
    echo "Error: Failed to remove background using remove.bg API."
    exit 1
fi

# Check if the output image file exists
if [ ! -f "$OUTPUT_FILENAME" ]; then
    echo "Error: Output image file '$OUTPUT_FILENAME' not found."
    exit 1
fi

# Run Python program with the resulting image file
python3 crop.py "$OUTPUT_FILENAME"

# Optionally, you can remove the output image file after processing
# rm "$OUTPUT_FILENAME"

exit 0
