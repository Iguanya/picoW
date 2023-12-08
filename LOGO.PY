import os
from PIL import Image

size = 300
logo_file = 'logo.png'
logoIm = Image.open(logo_file)
logoWidth, logoHeight = logoIm.size
os.makedirs('withlogo', exist_ok=True)

for filename in os.listdir('.'):
    if not (filename.lower().endswith(('.png', '.jpg'))) or filename == logo_file:
        continue
    img = Image.open(filename)
    width, height = img.size

    # Resize the image based on the larger dimension while preserving the aspect ratio
    if width > size or height > size:
        ratio = size / max(width, height)
        new_width = int(width * ratio)
        new_height = int(height * ratio)
        img = img.resize((new_width, new_height))

    print("Resizing %s" % (filename))
    width, height = img.size  # Update the image dimensions after resizing

    print("Adding logo to %s" % (filename))
    # Paste the logo onto the resized image using a transparency mask

    y = height - logoHeight
    x = (width - logoWidth)
    img.paste(logoIm, (x, y), logoIm)
    img.save(os.path.join('withlogo', filename), format="png")
