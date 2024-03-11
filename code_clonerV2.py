# import os
import sys
import pyautogui
import pyperclip
import pygetwindow
import time
import pytesseract
from PIL import ImageGrab, Image
from difflib import SequenceMatcher

# Set the path to the Tesseract executable
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

targeted_app = 'WorkVisual Development Environment'
file_name = "$machine.dat"
# Define the region of interest
text_area_top_left = (0, 140)  # Example values
text_area_size = (380, 975)     # Example values

def find_target_window():
    # Search for any active target window
    target_windows = pygetwindow.getWindowsWithTitle(targeted_app)

    if target_windows:
        return target_windows[0]
    else:
        return None

def upscale_screenshot(screenshot):
    # Get the original dimensions
    width, height = screenshot.size
    
    # Calculate the new dimensions
    new_width = int(width * 2)
    new_height = int(height * 2)
    
    # Resize the screenshot
    resized_screenshot = screenshot.resize((new_width, new_height), Image.LANCZOS)
    return resized_screenshot

def are_similar(str1, str2, threshold=0.85):
    matcher = SequenceMatcher(None, str1, str2)
    similarity_ratio = matcher.ratio()
    return similarity_ratio >= threshold

def add_text(target_window):
    # Select editor
    pyautogui.click(900,500)
    
    # Select all text in target and delete it
    pyautogui.hotkey('ctrl', 'a')
    pyautogui.press('delete')

    # Use pyautogui to simulate pasting the text
    pyautogui.hotkey('ctrl', 'v')


def main():
    text = sys.stdin.read()  # Read the text from standard input
    pyperclip.copy(text)

    # Find the target window
    target_window = find_target_window()

    if target_window:
        # Activate the target window
        if target_window.isMinimized:
            target_window.restore()
        target_window.activate()
        
        # Calculate the bounding box for the region of interest
        text_area_bbox = (target_window.left + text_area_top_left[0],
                        target_window.top + text_area_top_left[1],
                        text_area_size[0],
                        text_area_size[1])

        # Wait for the project structure window to appear
        time.sleep(0.2)

        # Take a screenshot of the defined region of interest
        screenshot = ImageGrab.grab(bbox=text_area_bbox)
        # screenshot.show()
        # Upscale the screenshot
        upscaled_screenshot = upscale_screenshot(screenshot)

        # Perform OCR on the screenshot to find the file name
        data = pytesseract.image_to_data(upscaled_screenshot, output_type=pytesseract.Output.DICT)

        # Search for the text within the OCR result
        found_box = None
        for i in range(len(data['text'])):
            if are_similar(file_name, data['text'][i]):
                found_box = [int(data['left'][i]), int(data['top'][i]), int(data['width'][i] + data['left'][i]), int(data['height'][i] + data['top'][i])]
                break  # Once found, stop searching

        if found_box:
            # print("Bounding box of the text '{}' found on the screen:".format(file_name))
            found_box = [val // 2 for val in found_box]
            # print(found_box)
            # cropped_image = screenshot.crop(found_box)
            # cropped_image.show()
            # print(found_box[0], found_box[1]+text_area_top_left[1])
            pyautogui.doubleClick(found_box[0], found_box[1]+text_area_top_left[1])
            time.sleep(0.6)
            add_text(target_window)
            pyperclip.copy('')  # Clear the clipboard
        else:
            print("Text '{}' not found on the screen.".format(file_name))

    else:
        print("Target window not found.")


if __name__ == "__main__":
    main()
