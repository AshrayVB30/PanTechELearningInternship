from PIL import Image
import matplotlib.pyplot as plt

def rotate_image(image, angle):
    """
    Rotate the given image by the specified angle.

    :param image: PIL.Image object to be rotated
    :param angle: Angle in degrees to rotate the image
    :return: Rotated image
    """
    return image.rotate(angle, expand=True)

# Load an image (replace 'example.jpg' with your image file)
image_path = 'images/butterfly.png'
image = Image.open(image_path)

# Rotate the image by different angles
angles = [0, 45, 90, 135, 180]
rotated_images = [rotate_image(image, angle) for angle in angles]

# Display the original and rotated images
fig, axs = plt.subplots(1, len(angles), figsize=(15, 6))

for ax, img, angle in zip(axs, rotated_images, angles):
    ax.imshow(img)
    ax.set_title(f'Rotated Image ({angle}°)')
    ax.axis('off')

plt.show()
