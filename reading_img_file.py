# q19 : write a function whihc will be able to read a image file and show it to you .
import cv2
def read_img() : 
    a = cv2.imread('E:01.png')
    cv2.imshow("myimg",a)
    # cv2.waitKey(5000)
    # cv2.destroyWindow('myimg')

a = read_img()
print(a)