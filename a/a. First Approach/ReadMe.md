# Object Detection with DETR

This code utilizes the DETR (DEtection TRansformer) model for object detection in images. It processes images from specified categories, generates detection results, and performs an object frequency analysis.

## Directory Structure

```
├── object_detection.py       # Main script
└── images/                   # Directory
    ├── hateful_memes/        # Hateful memes
    └── not_hateful_memes/    # Non-hateful memes
```

## Installation

1. Clone the repository or download the source code.
2. Install the required dependencies:

```
pip install transformers torch torchvision pillow
```

## Usage

1. Place your image categories in the `images/` directory.
2. Open the `object_detection.py` script.
3. Update the `base_folder_path` and `categories` variables with the appropriate values.
4. Run the script:

```
python object_detection.py
```

The script will generate two output files for each category:

- `output_results_{category}.txt`: Contains the detection results for each image, including the detected object, confidence score, and bounding box location.
- `object_frequency_{category}.txt`: Provides an analysis of the frequency of detected objects within the category.

## Dependencies

- `transformers` (version specified in the code)
- `torch` (version specified in the code)
- `torchvision` (version specified in the code)
- `pillow` (version specified in the code)

## Approach

The project follows these steps:

1. Initialize the DETR model and image processor from the HuggingFace Transformers library.
2. Iterate through the specified image categories.
3. For each image:
   - Open and preprocess the image using the image processor.
   - Perform object detection inference using the DETR model.
   - Convert the model outputs to the COCO API format with a confidence threshold of 0.9.
   - Write the detection results (detected object, confidence score, and bounding box location) to an output file.
   - Update the object frequency counter.
4. After processing all images in a category, write the object frequency analysis to a separate file.
5. Return the paths of the generated output files.

The project uses the DETR model for object detection, which is a transformer-based model that can detect objects in images with high accuracy.