import cv2 as opencv
import common

rectangle_points = []

def display_lena_image(draw_rectangle):
    # File path
    file_path = common.LENA_FILE_PATH

    # Load image
    lena_img = opencv.imread(file_path)

    # Draw rectangle
    if(draw_rectangle):
        opencv.rectangle(lena_img, rectangle_points[0], rectangle_points[1], 
            common.GREEN, common.LINE_THICKNESS)

        text_origin = (rectangle_points[0][0], rectangle_points[0][1] - common.TEXT_OFFSET)

        opencv.putText(lena_img, 'Lena', text_origin, 
            common.FONT_FACE, 
            common.FONT_SCALE, 
            common.GREEN, 
            common.FONT_THICKNESS, 
            common.FONT_LINE)

    # Show image
    opencv.imshow(common.WINDOW_NAME, lena_img)
    opencv.waitKey(0)
    
def on_mouse_move(event, x, y, flags, user_data):
    # User pressed left mouse button and started drawing the rectangle    
    if(event == opencv.EVENT_LBUTTONDOWN):   
        rectangle_points.clear()
        rectangle_points.append((x,y))                 
    
    # User has finished drawing the rectangle
    elif event == opencv.EVENT_LBUTTONUP:
        rectangle_points.append((x,y))
        display_lena_image(True)        

# Prepare window and set mouse callback
opencv.namedWindow(common.WINDOW_NAME)
opencv.setMouseCallback(common.WINDOW_NAME, on_mouse_move)

# Display Lena image
display_lena_image(False)