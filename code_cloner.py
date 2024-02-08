# import os
import sys
import pyautogui
import pyperclip
import pygetwindow

targeted_app = 'WorkVisual Development Environment'

def find_target_window():
    # Search for any active target window
    target_windows = pygetwindow.getWindowsWithTitle(targeted_app)

    if target_windows:
        return target_windows[0]
    else:
        return None


def add_text(target_window):
    # Activate and restore the target window if it's minimized
    if target_window.isMinimized:
        target_window.restore()
    target_window.activate()

    # Select all text in target and delete it
    pyautogui.hotkey('ctrl', 'a')
    pyautogui.press('delete')

    # Use pyautogui to simulate pasting the text
    pyautogui.hotkey('ctrl', 'v')


def main():
    # file_path = "test.txt"

    # # Check if the file exists
    # if not os.path.exists(file_path):
    #     print(f"Error: File '{file_path}' not found.")
    #     return

    # # Read the content of the text file
    # with open(file_path, "r") as file:
    #     text = file.read()
    #     # Set the text of the target window using the clipboard
    #     pyperclip.copy(text)
    
    text = sys.stdin.read()  # Read the text from standard input
    pyperclip.copy(text)

    # Find the target window
    target_window = find_target_window()
    if not target_window:
        print(f"Error: No active {targeted_app} window found.")
        return

    add_text(target_window)
    pyperclip.copy('')  # Clear the clipboard


if __name__ == "__main__":
    main()
