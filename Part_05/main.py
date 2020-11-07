import sys
sys.path.insert(1, '../Part_03/')
sys.path.insert(2, '../Part_04/')

from inference import Inference as model
from image_helper import ImageHelper as imgHelper

from video_reader import VideoReader as videoReader

if __name__ == "__main__": 
    # Load and prepare model
    model_file_path = '../Models/01_model.tflite'
    labels_file_path = '../Models/02_labels.txt'

    # Initialize model
    ai_model = model(model_file_path, labels_file_path)
    score_threshold = 0.3

    # Initialize camera
    video_file_path = '../Videos/01.mp4'
    video_reader = videoReader(video_file_path)

    while(True):
        # Get frame from the video file
        frame = video_reader.read_next_frame()

        # If frame is None, then break the loop
        if(frame is None):
            break
        
        # Perform detection
        results = ai_model.detect_objects(frame, score_threshold)

        # Detects only people
        # people = ai_model.detect_people(frame, score_threshold)
        
        # Display results
        imgHelper.display_image_with_detected_objects(frame, results)

        break