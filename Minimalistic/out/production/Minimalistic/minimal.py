import cv2

def convert_to_line_drawing(image_path, blur_value=5, low_threshold=50, high_threshold=150):
    # Read the image
    image = cv2.imread(image_path)
    # Convert to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # Apply Gaussian blur
    blur = cv2.GaussianBlur(gray, (blur_value, blur_value), 0)
    # Apply Canny edge detection
    edges = cv2.Canny(blur, low_threshold, high_threshold)
    # Invert the image to make lines black and background white
    inverted = 255 - edges

    # Display the original and the line drawing
    cv2.imshow('Original Image', image)
    cv2.imshow('Line Drawing', inverted)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # Optionally, save the result to a file
    cv2.imwrite('line_drawing.jpg', inverted)

# Replace 'path_to_your_image.jpg' with the path to the image you want to convert
convert_to_line_drawing('./sunset1.jpeg')