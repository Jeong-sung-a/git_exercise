import cv2

img_file = "../Show/Resource/girl2.jpg"
save_file = "../Show/Result/girl2_gray.jpg"
img = cv2.imread(img_file, cv2.IMREAD_GRAYSCALE)
cv2.imshow(img_file, img)
cv2.imwrite(save_file, img)
if cv2.waitKey(0) & 0xFF == ord('q'):
    cv2.destroyAllWindows()
