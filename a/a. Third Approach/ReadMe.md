# Object Detection using YOLO README

This code performs object detection using YOLO (You Only Look Once). The provided Jupyter notebook (`a - 3. Object Detection using YOLO.ipynb`) demonstrates how to detect objects in images and append the results to a CSV catalog.

## Dependencies:
Ensure you have the following dependencies installed:
- `ultralytics`: YOLO implementation for object detection.

```bash
!pip install ultralytics
```

## Usage:
1. Open the Jupyter notebook `a - 3. Object Detection using YOLO.ipynb`.
2. Execute the notebook cells to perform object detection and append the results to a CSV catalog.
3. Ensure to provide the correct paths for the JSON file containing image paths and labels, and the output CSV catalog.

## Functions:
- `append_to_catalog_from_json(json_file_path, catalog_path)`: Function to append detected objects and their labels from a JSON file to a CSV catalog.
  - Parameters:
    - `json_file_path (str)`: Path to the JSON file containing image paths and labels.
    - `catalog_path (str)`: Path to the CSV catalog file.
  - Example Usage:
    ```python
    json_file_path = '/path/to/json_file.json'
    catalog_path = '/path/to/catalog.csv'
    append_to_catalog_from_json(json_file_path, catalog_path)
    ```

## Example Usage:
```python
# Example usage:
json_file_path = './task/hateful_memes/test_unseen.jsonl'
catalog_path = ',.detection_catalog.csv'

append_to_catalog_from_json(json_file_path, catalog_path)
```