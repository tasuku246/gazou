import piggyphoto
import cv2

C = piggyphoto.camera()

print C.abilities
#C.capture_preview('preview.jpg')
C.capture_image('display.jpg')

img = cv2.imread('display.jpg', 0)
img_height = img.shape[0]
img_width = img.shape[1]


screen_res = 1280, 1024 #screeen resolution
scale_width = screen_res[0] / img_width
scale_height = screen_res[1] / img_height
scale = min(scale_width, scale_height)
window_width = int(img.shape[1] * scale)
window_height = int(img.shape[0] * scale)

cv2.namedWindow('image', cv2.WINDOW_NORMAL)
cv2.resizeWindow('image', window_width, window_height)



cv2.imshow('image',img)



k = cv2.waitKey(0)
if k == 27:         # wait for ESC key to exit
    cv2.destroyAllWindows()
elif k == ord('s'): # wait for 's' key to save and exit
    cv2.imwrite('messigray.png',img)
    cv2.destroyAllWindows()
