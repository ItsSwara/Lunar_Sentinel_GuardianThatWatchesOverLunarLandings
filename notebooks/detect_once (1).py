from ultralytics import YOLO
import pyautogui
import cv2
import numpy as np
from pynput import keyboard

model = YOLO(r"D:\EDAI\runs\detect\train4\weights\best.pt")

def wait_for_p_key():
    print("\nPress 'P' to capture screen and detect craters...")
    print("Make sure lunar image is visible on screen.\n")

    def on_press(key):
        try:
            if key.char == 'p' or key.char == 'P':
                print("P pressed! Capturing screen...")
                listener.stop()
        except:
            pass

    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()

def main():
    # Wait until user presses 'P'
    wait_for_p_key()

    # Take full screen screenshot
    screenshot = pyautogui.screenshot()
    frame = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)

    # YOLO inference
    results = model(frame)
    annotated = results[0].plot()

    # Show result
    cv2.imshow("Crater Detection (Screenshot)", annotated)
    print("Press any key on image window to close.")
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
