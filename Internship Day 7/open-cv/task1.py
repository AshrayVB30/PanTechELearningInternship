from PIL import Image, ImageDraw, ImageFont
import matplotlib.pyplot as plt


def draw_text(draw, position, text, font, fill, bg_fill=None):
    """
    Draw text on the image with optional background color.

    :param draw: ImageDraw object
    :param position: Tuple (x, y) for text position
    :param text: Text to draw
    :param font: ImageFont object
    :param fill: Text color
    :param bg_fill: Background color (optional)
    """
    # Compute the bounding box of the text
    bbox = draw.textbbox(position, text, font=font)

    if bg_fill:
        draw.rectangle(bbox, fill=bg_fill)

    draw.text(position, text, font=font, fill=fill)


# Create a blank image with white background
image = Image.new('RGB', (400, 400), color='white')
draw = ImageDraw.Draw(image)

# Draw various shapes
draw.rectangle([50, 50, 150, 150], outline="black", width=3)  # Square
draw.ellipse([200, 50, 300, 150], outline="blue", width=3)  # Circle
draw.line([50, 200, 150, 300], fill="green", width=3)  # Diagonal line
draw.polygon([(250, 200), (300, 300), (200, 300)], outline="red", width=3)  # Triangle

# Load a default font
try:
    font = ImageFont.truetype("arial.ttf", 20)
except IOError:
    font = ImageFont.load_default()

# Draw text with optional background color
draw_text(draw, (50, 320), "Rectangle", font, fill="black", bg_fill="white")
draw_text(draw, (200, 320), "Circle", font, fill="blue", bg_fill="white")
draw_text(draw, (50, 350), "Line", font, fill="green", bg_fill="white")
draw_text(draw, (250, 350), "Triangle", font, fill="red", bg_fill="white")

# Display the image with shapes and text
plt.figure(figsize=(6, 6))
plt.imshow(image)
plt.axis('off')
plt.show()
