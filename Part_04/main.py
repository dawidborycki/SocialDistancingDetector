# Add reference to Part_03 (assuming the code is executed from Part_04 folder)
import sys
sys.path.insert(1, '../Part_03/')

from inference import Inference as model
from image_helper import ImageHelper as imgHelper
from camera import Camera as camera

if __name__ == "__main__": 
    # Load and prepare model
    model_file_path = '../Models/01_model.tflite'
    labels_file_path = '../Models/02_labels.txt'

    # Initialize model
    ai_model = model(model_file_path, labels_file_path)

    # Initialize camera
    camera_capture = camera()

    # Capture frame and perform inference
    camera_frame = camera_capture.capture_frame(False)
        
    score_threshold = 0.5
    results = ai_model.detect_objects(camera_frame, score_threshold)

    # Display results
    imgHelper.display_image_with_detected_objects(camera_frame, results)