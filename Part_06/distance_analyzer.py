import math

class DistanceAnalyzer(object):
    @staticmethod
    def get_rectangle_center(rectangle):

        # Get top and bottom right corner of the rectangle
        top_left_corner = rectangle[0]
        bottom_right_corner = rectangle[1]        

        # Calculate width and height of the rectangle
        width = bottom_right_corner[0] - top_left_corner[0]
        height = bottom_right_corner[1] - top_left_corner[1]

        # Calculate center
        center = (int(width/2 + top_left_corner[0]), int(height/2 + top_left_corner[1]))

        return center

    @staticmethod
    def get_rectangle_centers(detection_results):
        # Prepare the list
        rectangle_centers = []

        # Iterate over detection results, and determine center of each rectangle
        for i in range(len(detection_results)):
            rectangle = detection_results[i]['rectangle']            

            center = DistanceAnalyzer.get_rectangle_center(rectangle)

            rectangle_centers.append(center)

        # Return rectangle centers
        return rectangle_centers

    @staticmethod 
    def calculate_distance_between_rectangle_centers(rect_center_1, rect_center_2):        
        # Calculate absolute difference between x and y coordinates
        x_abs_diff = abs(rect_center_1[0] - rect_center_2[0])
        y_abs_diff = abs(rect_center_1[1] - rect_center_2[1])

        # Calculate Euclidean distance
        return math.sqrt(x_abs_diff**2 + y_abs_diff**2)

    @staticmethod
    def find_people_that_are_too_close(detection_results, distance_threshold):
        
        # Prepare results' list
        results = []

        # Get rectangle centers
        rectangle_centers = DistanceAnalyzer.get_rectangle_centers(detection_results)        

        # Analyze distance between each object
        N = len(detection_results)
        for i in range(N):
            for j in range(i+1, N):                
                rect_center_1 = rectangle_centers[i]
                rect_center_2 = rectangle_centers[j]

                distance = DistanceAnalyzer.calculate_distance_between_rectangle_centers(rect_center_1, rect_center_2)

                # If distance between objects is too close
                # append centers to the results' list
                if(distance <= distance_threshold):
                    results.append((detection_results[i]['rectangle'], detection_results[j]['rectangle']))                

        return results