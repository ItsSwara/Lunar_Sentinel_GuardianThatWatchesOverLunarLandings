from ultralytics import YOLO
import pyautogui
import cv2
import numpy as np

# 👉 Tumhara trained model (ye path tumhare output se hai)
model = YOLO(r"D:\EDAI\runs\detect\train4\weights\best.pt")

def main():
    while True:
        # 1) Screen ka screenshot lo
        screenshot = pyautogui.screenshot()

        # 2) PIL image -> NumPy array -> BGR (OpenCV format)
        frame = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)

        # (Optional) Speed badhane ke liye resize:
        # frame = cv2.resize(frame, (1280, 720))

        # 3) YOLO se prediction
        results = model(frame)

        # 4) Bounding boxes ke saath image lo
        annotated = results[0].plot()

        # 5) Show in window
        cv2.imshow("Screen Crater Detection", annotated)

        # 6) 'q' dabao to band
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
