import cv2
import numpy as np


def main():
    drawing = False # true if mouse is pressed
    ix, iy = -1, -1

    # mouse callback function
    def draw(event, x, y, flags, param):
        nonlocal ix, iy, drawing
        if event == cv2.EVENT_LBUTTONDOWN:
            drawing = True
            ix, iy = x, y
        elif event == cv2.EVENT_MOUSEMOVE:
            if drawing == True:
                cv2.circle(img, (x, y), 5, (0, 0, 255), -1)
        elif event == cv2.EVENT_LBUTTONUP:
            drawing = False
            cv2.circle(img, (x, y), 5, (0, 0, 255), -1)

    img = np.zeros((512, 512, 3), np.uint8)
    cv2.namedWindow('image')
    cv2.setMouseCallback('image', draw)

    while(True):
        cv2.imshow('image',img)
        k = cv2.waitKey(1) & 0xFF
        if k == ord('m'):
            mode = not mode
        elif k == 27:
            break

cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
