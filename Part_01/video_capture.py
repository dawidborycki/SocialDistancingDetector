import cv2 as opencv

quit_key = ord('q')

# Create video capture
video_capture = opencv.VideoCapture(0)

# Video writer
video_file_name = 'camera_capture.avi'
codec = opencv.VideoWriter_fourcc('M','J','P','G')
frame_rate = 25
video_writer = None

# Display images in a loop until user presses 'q' key
while(True):            
    (status, camera_frame) = video_capture.read()    

    if(status):
        opencv.imshow('Camera preview', camera_frame)        

        if(video_writer == None):            
            frame_size = camera_frame.shape[-2::-1]            
            video_writer = opencv.VideoWriter(video_file_name, codec, frame_rate, frame_size)

        video_writer.write(camera_frame)

    key = opencv.waitKey(10)

    if(key == quit_key):
        break

video_writer.release()