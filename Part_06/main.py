import sys
sys.path.insert(1, '../Part_03/')
sys.path.insert(1, '../Part_05/')

from inference import Inference as model
from image_helper import ImageHelper as imgHelper
from video_reader import VideoReader as videoReader
from distance_analyzer import DistanceAnalyzer as analyzer

if __name__ == "__main__": 
    # Load and prepare model
    model_file_path = '../Models/01_model.tflite'
    labels_file_path = '../Models/02_labels.txt'

    # Initialize model
    ai_model = model(model_file_path, labels_file_path)    

    # Initialize video reader
    video_file_path = '../Videos/01.mp4'
    video_reader = videoReader(video_file_path)

    # Detection and preview parameters
    score_threshold = 0.4    
    delay_between_frames = 5

    # Perform object detection in the video sequence
    while(True):
        # Get frame from the video file
        frame = video_reader.read_next_frame()

        # If frame is None, then break the loop
        if(frame is None):
            break
        
        # Perform detection        
        results = ai_model.detect_people(frame, score_threshold)
        
        # Get centers of the bounding boxes (rectangle centers)
        rectangle_centers = analyzer.get_rectangle_centers(results)

        # Draw centers before displaying results
        imgHelper.draw_rectangle_centers(frame, rectangle_centers)   

        # Display detection results
        imgHelper.display_image_with_detected_objects(frame, results)                        