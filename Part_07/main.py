import sys
sys.path.insert(1, '../Part_03/')
sys.path.insert(1, '../Part_06/')

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
    detect_only_people = True
    delay_between_frames = 5

    # Perform object detection in the video sequence
    while(True):
        # Get frame from the video file
        frame = video_reader.read_next_frame()

        # If frame is None, then break the loop
        if(frame is None):
            break
        
        # Perform detection
        if(detect_only_people):
            results = ai_model.detect_people(frame, score_threshold)
        else:
            results = ai_model.detect_objects(frame, score_threshold)        
        
        # Find objects that are too close
        proximity_distance_threshold = 50
        objects_that_are_too_close = analyzer.find_people_that_are_too_close(results, proximity_distance_threshold)

        # Indicate those objects in the image        
        imgHelper.indicate_people_that_are_too_close(frame, objects_that_are_too_close, delay_between_frames)        