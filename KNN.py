import numpy as np
from skimage import io
from sklearn.neighbors import NearestNeighbors
import matplotlib.pyplot as plt

# Load the image
image_path = r'C:\Users\user\Downloads\IMG_0610.jpg'
image = io.imread(image_path)

# Flatten the image into a 2D array (rows x columns, channels)
rows, cols, channels = image.shape
image_2d = image.reshape(rows * cols, channels)

# Apply KNN to filter outliers
n_neighbors = 10
knn = NearestNeighbors(n_neighbors=n_neighbors)
knn.fit(image_2d)
distances, _ = knn.kneighbors(image_2d)

threshold_distance = np.mean(distances[:, -1]) * 2
filtered_indices = np.where(np.max(distances, axis=1) < threshold_distance)[0]

# Filter the image based on indices of non-outliers
filtered_image_2d = image_2d[filtered_indices]

# Pad the filtered array to match the original size if necessary
filtered_image_2d = np.pad(filtered_image_2d, ((0, rows * cols - len(filtered_image_2d)), (0, 0)), mode='constant')
filtered_image = filtered_image_2d.reshape((rows, cols, channels))

# Display the filtered image
plt.imshow(filtered_image)
plt.axis('off')  # Turn off axis labels
plt.title('Filtered Image')
plt.show()
