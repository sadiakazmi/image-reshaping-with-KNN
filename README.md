# image-removing outliers-with-KNN
## Import Libraries:
numpy for numerical operations.
skimage.io to read and write images.
sklearn.neighbors.NearestNeighbors for the KNN algorithm.
matplotlib.pyplot for displaying images.
## Load Image:
An image is loaded from the specified path using io.imread from skimage.
## Flatten the Image:
The image is reshaped into a 2D array where each row represents a pixel and its color channels. The shape of the original image (rows x cols x channels) is converted to a 2D array of shape (rows*cols, channels).


![002084 png_7b8ea1da-13ca-469f-a502-7822d16d1e8d face_1](https://github.com/sadiakazmi/image-reshaping-with-KNN/assets/142217150/e29efe0d-4f79-452f-8ad4-1ec11110eff8)

![myplot1](https://github.com/sadiakazmi/image-reshaping-with-KNN/assets/142217150/8fe372b6-d73e-49ef-9f03-40d59ebebe3d)

## Apply KNN to Filter Outliers:
NearestNeighbors model is created with n_neighbors set to 10.
The model is fitted with the flattened image data.
It computes distances between each point and its n_neighbors nearest neighbors.
A threshold distance is calculated based on the mean of the furthest distances multiplied by 2.
Pixels that have maximum distances smaller than the threshold are considered non-outliers, and their indices are collected.
## Filter the Image Based on Non-Outliers:
Pixels identified as non-outliers are used to filter the flattened image data.
## Pad the Filtered Array:
The filtered data might be smaller than the original image after removing outliers, so padding is applied to match the original shape.
## Reshape and Display the Filtered Image:
The filtered flattened array is reshaped back into the original image dimensions (rows x cols x channels).
The resulting filtered image is displayed using plt.imshow, turning off axis labels, setting a title, and showing the image using plt.show().
In summary, this code uses KNN to identify and remove outlier pixels from an image based on their distances from neighboring pixels. The resulting image shown is a version where pixels identified as outliers have been filtered out.




