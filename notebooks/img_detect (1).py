from ultralytics import YOLO

def main():
    # Trained model ka path
    model = YOLO(r"D:\EDAI\runs\detect\train4\weights\best.pt")

    # 1) Agar sirf ek image test karni ho:
    # model.predict(source=r"D:\EDAI\lunar_images\moon1.jpg", show=True)

    # 2) Pura folder detect karna ho:
    model.predict(
        source=r"D:\EDAI\test\images",  # is folder me jitni images hain sab pe detect hoga
        show=True,                       # har image ek window me dikhayega
        save=True                        # results runs\detect\predictX me save bhi ho jayenge
    )

if __name__ == "__main__":
    main()
#yoloenv\Scripts\activate
#yolo predict model="D:\EDAI\runs\detect\train4\weights\best.pt" source="D:\EDAI\lunar_images" show=True