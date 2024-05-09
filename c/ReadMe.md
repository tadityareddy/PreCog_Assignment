## Title: Image Classification System README

This code is for an Image Classification System built using TensorFlow and Keras. The provided Jupyter notebook (`c. Image Classification System.ipynb`) demonstrates how to train a deep learning model to classify images into hateful and not hateful memes categories. Additionally, it includes functionalities to evaluate the model, save it for future use, predict classes of images, and visualize the training history.

## Dependencies:
Ensure you have the following dependencies installed:
- `tensorflow`: Deep learning library for building and training models.
- `numpy`: Library for numerical computations.
- `matplotlib`: Library for data visualization.
- `keras`: High-level neural networks API (included in TensorFlow).

```bash
!pip install -q tensorflow
!pip install -q numpy
!pip install -q matplotlib
!pip install -q keras
```

## Usage:
1. Open the Jupyter notebook `c. Image Classification System.ipynb`.
2. Execute the notebook cells to load, preprocess, and train the image classification model.
3. Evaluate the model's performance on validation data.
4. Save the trained model for future use.
5. Predict classes of images in a local directory using the trained model.
6. Visualize the training history to analyze the model's performance.

## Functions:
- `load_and_preprocess_data()`: Function to load and preprocess the image data for training and validation.
- `build_and_compile_model(base_model)`: Function to build and compile the image classification model.
- `train_model(model, train_generator, validation_generator)`: Function to train the image classification model.
- `evaluate_model(model, validation_generator)`: Function to evaluate the model's performance on validation data.
- `save_model(model, filename)`: Function to save the trained model to a file.
- `predict_images(model, image_directory)`: Function to predict classes of images in a directory using the trained model.
- `plot_training_history(vgghist)`: Function to plot training and validation accuracy and loss.

## Example Usage:
```python
# Load and preprocess data
train_generator, validation_generator = load_and_preprocess_data()

# Build and compile the model
base_model = VGG16(input_shape=(224, 224, 3), include_top=False, weights='imagenet')
model = build_and_compile_model(base_model)
model.summary()

# Train the model
vgghist = train_model(model, train_generator, validation_generator)

# Evaluate the model
evaluate_model(model, validation_generator)

# Save the model
save_model(model, 'Classification_VGG16.keras')

# Predict classes of images in a directory
local_image_directory = "C:\\path\\to\\image_directory"
predict_images(model, local_image_directory)

# Plot training history
plot_training_history(vgghist)
```