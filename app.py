import gradio as gr
import cv2
import numpy as np
def get_dominant_color(image):
    # Convert image to HSV color space
    hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    # Define color ranges for red, blue, green, violet, black, yellow and white
    color_ranges = {'blue': ([0, 70, 50], [10, 255, 255]),
                    'red': ([110, 70, 50], [130, 255, 255]),
                    'green': ([50, 70, 50], [70, 255, 255]),
                    'violet': ([140, 70, 50], [160, 255, 255]),
                    'black': ([0, 0, 0], [180, 255, 30]),
                    'yellow': ([25, 70, 50], [35, 255, 255]),
                    'white': ([0, 0, 200], [180, 30, 255])
                    }

    dominant_color = None
    max_pixel_count = 0

    # Iterate over color ranges and find the dominant color
    for color_name, (lower, upper) in color_ranges.items():
        lower = np.array(lower, dtype=np.uint8)
        upper = np.array(upper, dtype=np.uint8)

        # Create a mask for the color range
        mask = cv2.inRange(hsv_image, lower, upper)

        # Count the number of pixels in the color range
        pixel_count = cv2.countNonZero(mask)

        # Update the dominant color if the pixel count is higher
        if pixel_count > max_pixel_count:
            max_pixel_count = pixel_count
            dominant_color = color_name

    return dominant_color
iface = gr.Interface(fn=get_dominant_color, inputs="image", outputs="text",title="colour identifier")
iface.launch(inline=False)
