from PIL import Image, ImageFilter
import numpy as np
from sklearn.cluster import KMeans

def blur_and_reduce_colors(image_path, n_colors=5, blur_radius=2):
    # Load the image
    img = Image.open(image_path)
    img = img.convert('RGB')

    # Simplify the image by applying a Gaussian blur
    blurred_img = img.filter(ImageFilter.GaussianBlur(blur_radius))

    # Convert image data to a list of RGB tuples
    data = np.array(blurred_img)
    original_shape = data.shape
    data = data.reshape((-1, 3))

    # Apply k-means clustering to reduce the color palette
    kmeans = KMeans(n_clusters=n_colors, random_state=0).fit(data)
    new_colors = kmeans.cluster_centers_.astype(int)
    labels = kmeans.labels_

    # Create a new image using the reduced palette
    new_data = new_colors[labels].reshape(original_shape)
    new_img = Image.fromarray(new_data.astype('uint8'), 'RGB')

    # Save or display the result
    result_path = 'blurred_minimalistic_version.png'
    new_img.save(result_path)
    new_img.show() # This will display the image if your environment supports it

    return result_path

# Replace 'path_to_your_image.jpg' with the actual path to your image
image_path = 'sunset1.jpeg'
result_path = blur_and_reduce_colors(image_path, n_colors=5, blur_radius=1)
print(f"Blurred minimalistic version saved to: {result_path}")
