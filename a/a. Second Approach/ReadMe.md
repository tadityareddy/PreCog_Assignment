# Image Description Generator README

This code implements an Image Description Generator for objecte detection using a pre-trained model (LLaVa). It takes an image as input and generates a textual description of the objects present in the image.

## Directory Structure:

**Notebook Execution**
```
image_description_generator/
│
├── a - 2. LLaVa Notebook.ipynb
└──  inputs/
        └──  imgs
```
- `a - 2. LLaVa Notebook.ipynb`: Jupyter notebook containing the code.

**Local Execution:**
```
image_description_generator/
│
├── api/
│   ├── api_endpoint.py
│
├── inputs/
│   ├── imgs
│
├── scripts/
│   ├── eval/
│   ├── finetune.sh
│   ├── finetune_lora.sh
│   └── pretrain.sh
│
├── utils/
│
├── videollava/
│   ├── eval
│   ├── model
│   ├── serve
│   ├── train
│   ├── __init__.py
│   ├── constants.py
│   ├── conversation.py
│   ├── mm_utils.py
│   └── utils.py
│
├── config.json
├── inference.py
└── requirements.txt
```

## Installation:
Run the following commands to install the required dependencies:
```bash
!pip install --upgrade accelerate bitsandbytes
!pip install git+https://github.com/huggingface/transformers.git
```

## Usage:
1. Initialize the `ImageDescriptionGenerator` class with the desired model ID.
2. Load the model using the `load_model()` method.
3. Provide the path to the image using the `generate_description(image_path)` method to generate a textual description.

## Dependencies:
- `transformers`: Used for accessing the pre-trained model.
- `torch`: Required for tensor computations.
- `PIL`: Used for image processing.
- `accelerate`: For optimizing performance.
- `bitsandbytes`: Library for quantization configurations.

## Example Usage:
```python
model_id = "llava-hf/llava-1.5-7b-hf"
generator = ImageDescriptionGenerator(model_id)
generator.load_model()

image_path = 'image.png'
description = generator.generate_description(image_path)

description, objects = parse_image_description(description)
print(description)
print()
print(objects)
```