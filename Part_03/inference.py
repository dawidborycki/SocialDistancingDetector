import cv2 as opencv
from tensorflow import lite as tflite
import numpy as np

class Inference(object):        
    def __init__(self, model_file_path, labels_file_path):
        # Load model
        self.load_model_and_configure(model_file_path)

        # Load labels
        self.load_labels_from_file(labels_file_path)
    
    def load_model_and_configure(self, model_path):
        """ Loads the model and configures input image dimensions accordingly
        : model_path: A full path to the file containing the model
        """
        # Load model from file
        self.interpreter = tflite.Interpreter(model_path)

        # Allocate tensors
        self.interpreter.allocate_tensors()

        # Get input and output details
        self.input_details = self.interpreter.get_input_details()
        self.output_details = self.interpreter.get_output_details()

        # Store input image dimensions
        self.input_image_height = self.input_details[0]['shape'][1]
        self.input_image_width = self.input_details[0]['shape'][2]

    def load_labels_from_file(self, file_path):
        """ Loads image labels from the text file
        : file_path: A full path to the text file, containing image labels
        """
        with open(file_path, 'r') as file:
            self.labels = [line.strip() for line in file.readlines()]

    def prepare_image(self, image):
        """ Prepares image for the TensorFlow inference
        : image: An input image
        """
        # Convert image to BGR
        image = opencv.cvtColor(image, opencv.COLOR_BGR2RGB)        

        # Get new size
        new_size = (self.input_image_height, self.input_image_width)

        # Resize
        image = opencv.resize(image, new_size, interpolation = opencv.INTER_AREA) 

        return image

    def set_input_tensor(self, image):
        """Sets the input tensor."""
        tensor_index = self.input_details[0]['index']
        input_tensor = self.interpreter.tensor(tensor_index)()[0]
        input_tensor[:, :] = image
    
    def get_output_tensor(self, index):
        """Returns the output tensor at the given index."""        
        tensor = self.interpreter.get_tensor(self.output_details[index]['index'])
        return np.squeeze(tensor)
    
    def detect_objects(self, image, threshold):        
        """Returns a list of detection results"""

        # Store input image size
        input_image_size = image.shape[-2::-1]

        # Prepare image
        image = self.prepare_image(image)
        
        # Set image as the input tensor
        self.set_input_tensor(image)

        # Perform inference
        self.interpreter.invoke()

        # Get all output details        
        boxes = self.get_output_tensor(0)        
        classes = self.get_output_tensor(1)
        scores = self.get_output_tensor(2)                
        
        # Filter out detections below the threshold
        results = []
        for i in range(scores.size):
            if scores[i] >= threshold:
                result = {
                    'rectangle': self.convert_bounding_box_to_rectangle_points(boxes[i], input_image_size),
                    'label': self.labels[int(classes[i])],                    
                }
                results.append(result)

        # Return informations about detected objects
        return results    

    def convert_bounding_box_to_rectangle_points(self, bounding_box, input_image_size):
        height = input_image_size[0]
        width = input_image_size[1]

        top_left_corner = (int(bounding_box[0] * height), int(bounding_box[1] * width))
        bottom_right_corner = (int(bounding_box[2] * height), int(bounding_box[3] * width))
        
        return (top_left_corner, bottom_right_corner)
