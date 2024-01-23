# Install dependencies
python3 -m venv venv
source venv/bin/activate
pip install pillow pillow_heif

# Run the script (assuming you want to convert an image called example.heic to example.jpeg)
python image_converter.py example.heic example.jpeg &
