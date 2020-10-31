import cv2 as opencv
import common

class ImageHelper(object):
    @staticmethod
    def load_image(file_path):
        return opencv.imread(file_path)

    @staticmethod
    def draw_rectangle_and_label(img, rectangle_points, label):
        opencv.rectangle(img, rectangle_points[0], rectangle_points[1], 
            common.GREEN, common.LINE_THICKNESS)

        text_origin = (rectangle_points[0][0], rectangle_points[0][1] - common.TEXT_OFFSET)

        opencv.putText(img, label, text_origin, 
            common.FONT_FACE, 
            common.FONT_SCALE, 
            common.GREEN, 
            common.FONT_THICKNESS, 
            common.FONT_LINE)
            
    @staticmethod
    def display_image_with_detected_objects(image, inference_results):                
        # Draw rectangles and labels on the image
        for i in range(len(inference_results)):
            current_result = inference_results[i]            
            ImageHelper.draw_rectangle_and_label(image, current_result['rectangle'], current_result['label'])

        # Display image
        opencv.imshow(common.WINDOW_NAME, image)
            
        # Wait until user presses any key
        opencv.waitKey(0)