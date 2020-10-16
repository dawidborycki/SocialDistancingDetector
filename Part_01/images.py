import cv2 as opencv
import common

file_path = common.LENA_FILE_PATH

# Load image
lena_img = opencv.imread(file_path, opencv.IMREAD_GRAYSCALE)

# Show image
opencv.imshow('Lena', lena_img)
opencv.waitKey(0)

# Process image (Gaussian blur) 
kernel_size = (11,11)
sigma_X = 0

lena_img_processed = opencv.GaussianBlur(lena_img, kernel_size, sigma_X)

# Save image
output_file_path = 'Lena-processed.jpg'
opencv.imwrite(output_file_path, lena_img_processed, [int(opencv.IMWRITE_JPEG_QUALITY), 100])
