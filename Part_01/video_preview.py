import cv2 as opencv

video_file_name = 'camera_capture.avi'
frame_rate = 25

video_capture = opencv.VideoCapture(video_file_name)

while(True):
    (status, camera_frame) = video_capture.read()
    
    if(status):
        opencv.imshow('Video file', camera_frame)
        opencv.waitKey(int(1000/frame_rate))
    else:
        break