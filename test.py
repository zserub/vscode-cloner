import pygetwindow
import pyautogui
import time

targeted_app = 'WorkVisual Development Environment'
desired_file = "Braketest.src"
screenshot_filename = "project_structure.png"

# Define the parameters for the text area
# Top-left corner coordinates (x, y) of the text area
text_area_top_left = (10, 140)  # Example values
# Width and height of the text area
text_area_size = (375, 800)  # Example values

def find_target_window():
    # Search for any active target window
    target_windows = pygetwindow.getWindowsWithTitle(targeted_app)

    if target_windows:
        return target_windows[0]
    else:
        return None

def restore_and_activate_window(window):
    if window.isMinimized:
        window.restore()
    window.activate()
    time.sleep(0.2)

def capture_text_region(top_left, size):
    # Find the target window
    target_window = find_target_window()
    if target_window:
        # Restore and activate the target window if minimized
        restore_and_activate_window(target_window)

        # Find the position of the project structure window relative to the screen
        window_rect = (target_window.left, target_window.top, target_window.width, target_window.height)

        # Calculate the coordinates of the text area
        text_area_rect = (window_rect[0] + top_left[0], window_rect[1] + top_left[1], size[0], size[1])

        # Capture a screenshot of the specified text area
        screenshot = pyautogui.screenshot(region=text_area_rect)

        # Save the screenshot to a file
        screenshot.save(screenshot_filename)

        print(f"Screenshot captured: {screenshot_filename}")
    else:
        print("Target window not found.")

# Capture a screenshot of the text region
capture_text_region(text_area_top_left, text_area_size)

# Perform text recognition to locate the desired text within the captured region
text_position = pyautogui.locateOnScreen(screenshot_filename, confidence=0.9)
if text_position:
    # Click on the center of the found text region
    pyautogui.doubleClick(text_position.left + text_position.width // 2, text_position.top + text_position.height // 2)
else:
    print("Desired text not found.")