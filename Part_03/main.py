import common
from image_helper import ImageHelper as imgHelper
from inference import Inference as infer

if __name__ == "__main__": 
    # Load and prepare model
    model_file_path = '../Models/01_model.tflite'
    labels_file_path = '../Models/02_labels.txt'

    # Initialize model
    model = infer(model_file_path, labels_file_path)    
    
    # Get input image
    image = imgHelper.load_image('../Images/Lena.png')

    # Detect objects
    score_threshold = 0.5
    results = model.detect_objects(image, score_threshold)
    
    # Display results
    imgHelper.display_image_with_detected_objects(image, results)    