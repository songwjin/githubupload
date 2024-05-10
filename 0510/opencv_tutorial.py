import cv2
print(cv2.__version__)
from matplotlib import pyplot as plt
image = cv2.imread("./images/l.png",cv2.IMREAD_UNCHANGED)
# image_len1 = image[:,:,0]
# image_len2 = image[:,:,1]
# image_len3 = image[:,:,2]
# print(image_len.shape)
# plt.imsave('1.png',image_len1)
# plt.imsave('2.png',image_len2)
(h,w) = image.shape[:2]
center = (w/2,h/2)
for i in range(1,360,10):
    M= cv2.getRotationMatrix2D(center,i,1.0)
    img90=cv2.warpAffine(image,M,(h,w))
    plt.imsave('1r'+str(i)+'.png',img90)
print("완료")
# plt.imsave('3.png',image_len3)
# cv2.imshow("Moon",image)
cv2.waitKey(0)
cv2.destroyAllWindows()
