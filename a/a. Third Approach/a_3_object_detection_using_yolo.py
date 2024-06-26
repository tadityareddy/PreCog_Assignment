# -*- coding: utf-8 -*-
"""a - 3. Object Detection using YOLO.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1JM15h7-JhdRt1qZH2eo4hL_pHi8hDnTG
"""

!pip install ultralytics

import csv
import json
from ultralytics import YOLO

def append_to_catalog_from_json(json_file_path, catalog_path):
    """
    Append detected objects and their labels from a JSON file to a CSV catalog.

    Parameters:
    - json_file_path (str): Path to the JSON file containing image paths and labels.
    - catalog_path (str): Path to the CSV catalog file.

    Returns:
    None
    """
    # Load a model
    detectionmodel = YOLO('yolov8n.pt')

    # Read JSON file
    with open(json_file_path, 'r') as json_file:
        data = json.load(json_file)

    # Iterate through each entry in the JSON file
    for entry in data:
        # Extract image path and label from JSON data
        image_path = entry['img']
        ground_truth_label = entry['label']

        # Predict with the model
        detectionresults = detectionmodel(image_path)

        # Get the detected objects
        detected_objects = detectionresults.xyxy[0]  # Assuming there's only one image

        # Define a list to store the detected objects with their ground truth labels and confidence
        detected_objects_with_labels = []

        # Iterate through the detected objects
        for obj in detected_objects:
            object_name = detectionresults.names[int(obj[-1])]
            confidence = obj[4]
            detected_objects_with_labels.append({
                'Image': image_path,
                'Object': object_name,
                'Confidence': confidence,
                'Ground Truth Label': ground_truth_label
            })

        # Append the detected objects with their labels to a CSV file
        with open(catalog_path, mode='a', newline='') as file:
            fieldnames = ['Image', 'Object', 'Confidence', 'Ground Truth Label']
            writer = csv.DictWriter(file, fieldnames=fieldnames)

            for obj in detected_objects_with_labels:
                writer.writerow(obj)

    print("Detected objects appended to catalog:", catalog_path)

# Example usage:
json_file_path = '/Users/aditya/Desktop/task/hateful_memes/test_unseen.jsonl'  # Path to your JSON file
catalog_path = ',.detection_catalog.csv'  # Path to your catalog CSV file

append_to_catalog_from_json(json_file_path, catalog_path)

# Example usage:
image_path = '/content/Screenshot 2024-05-04 at 2.47.40 PM.png'
ground_truth_labels = [0, 1, 0]  # Example ground truth labels
catalog_path = '/content/detection_catalog.csv'