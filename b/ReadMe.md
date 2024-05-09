# Impact of Text Overlay on Images


This repository explores the impact of text overlay on images and objects within those images. The primary objective is to understand how the presence of overlaid text affects object detection algorithms and the accuracy of object detection.

The process begins with the detection of objects in images using YOLO, followed by the calculation of the area and percentage of the detected objects. Similarly, the text in the images is detected, and the area occupied by the text is calculated along with its percentage relative to the total image area.

Subsequently, the intersection over union (IOU) between the detected text and objects is calculated. This metric provides insights into the overlapping areas between text and objects, indicating potential interference or obstruction.

Utilizing the object detection results obtained prior to text overlay, the accuracy of object detection is evaluated. By comparing these results with the ground truth, we gain valuable insights into the impact of text overlay on the accuracy and performance of object detection algorithms.

The provided Jupyter notebook (`b. Impact of Text Overlay on Images.ipynb`) demonstrates various functionalities, including text detection in images, object detection using YOLO, calculation of text and object percentages in images, and calculation of the intersection between detected text and objects.

## Dependencies:
Ensure you have the following dependencies installed:
- `easyocr`: Optical Character Recognition (OCR) library for detecting text in images.
- `ultralytics`: YOLO implementation for object detection.
- `matplotlib`: Library for data visualization.
- `numpy`: Library for numerical computations.
- `opencv-python`: OpenCV library for image processing.

Install the required dependencies using the following commands:
```bash
!pip install easyocr ultralytics matplotlib numpy opencv-python
```

## Usage:
1. Open the Jupyter notebook `b. Impact of Text Overlay on Images.ipynb`.
2. Execute the notebook cells to perform text and object detection, and calculate various metrics related to the impact of text overlay on images.

## Functions:
- `read_text_from_image(image_path)`: Function to detect text in an image and return the detected text.
- `get_text_coordinates(image_path)`: Function to detect text in an image and return the coordinates of the detected text boxes.
- `get_object_coordinates(image_path)`: Function to detect objects in an image using YOLO and return their coordinates.
- `calculate_text_percentage(image_path)`: Function to calculate the percentage of an image area covered by detected text.
- `calculate_object_percentage(image_path)`: Function to calculate the percentage of an image area covered by detected objects.
- `calculate_intersection_percentage(image_path)`: Function to calculate the percentage of an image area covered by the intersection between detected text and objects.

## Example Usage:
```python
# Example usage of read_text_from_image function
text_detected = read_text_from_image(image_path)

# Example usage of get_text_coordinates function
text_coordinates = get_text_coordinates(image_path)

# Example usage of get_object_coordinates function
object_coordinates, classes = get_object_coordinates(image_path)

# Example usage of calculate_text_percentage function
text_percentage = calculate_text_percentage(image_path)

# Example usage of calculate_object_percentage function
object_percentage = calculate_object_percentage(image_path)

# Example usage of calculate_intersection_percentage function
intersection_percentage = calculate_intersection_percentage(image_path)

print("Detected Text:", text_detected)
print("Text Coordinates:", text_coordinates)
print("Object Detected:", classes)
print("Object Coordinates:", object_coordinates)
print("Text Percentage:", text_percentage)
print("Object Percentage:", object_percentage)
print("Intersection Percentage:", intersection_percentage)
```