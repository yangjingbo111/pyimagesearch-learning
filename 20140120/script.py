# import the necessary packages
import cv2

# load the image and show it
image = cv2.imread("jurassic-park-tour-jeep.jpg")
cv2.imshow("original", image)

print(image.shape)

# define the ratio of new image width to the old one
r = 100.0 / image.shape[1]
dim = (100, int(image.shape[0] * r))
# resize image
resized = cv2.resize(image, dim) # , interpolation = cv2.INTER_AREA
cv2.imshow("resized", resized)

# grab the dimensions of the image and calculate the center of the image
(h, w) = image.shape[:2]
center = (w / 2, h / 2)

# rotate the image by 180 degrees
M = cv2.getRotationMatrix2D(center, 180, 1.0)
rotated = cv2.warpAffine(image, M, (w, h))
cv2.imshow("rotated", rotated)

# crop the image using array slice -- it's numpy array
# after all
cropped = image[70:170, 440:540]
cv2.imshow("cropped", cropped)

# write the cropped image to disk in png format
cv2.imwrite("thumbnail.png", cropped)
cv2.waitKey(0)
