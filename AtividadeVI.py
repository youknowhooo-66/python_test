import cv2

cam = cv2.VideoCapture(0)

while True:
    ret, frame = cam.read()

    cv2.imshow("Webcam", frame)

    tecla = cv2.waitKey(1)

    if tecla == ord('q'):
        break

cam.release()
cv2.destroyAllWindows()