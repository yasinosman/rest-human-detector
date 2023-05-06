# import required libraries
import cv2
import os 


def detect_human(image_path, should_display=False):
    image = cv2.imread(image_path, -1)

    # initialize the HOG descriptor
    hog = cv2.HOGDescriptor()
    hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

    # detect humans in input image
    (humans, _) = hog.detectMultiScale(image, winStride=(4, 4), padding=(4, 4), scale=1.1)

    # getting no. of human detected
    print('Detected ', len(humans), ' people in the image.')

    if (should_display == False):
        return len(humans)

    # loop over all detected humans
    for (x, y, w, h) in humans:
        pad_w, pad_h = int(0.1 * w), int(0.05 * h)
        cv2.rectangle(image, (x + pad_w, y + pad_h), (x + w - pad_w, y + h - pad_h), (0, 255, 0), 2)

    # display the output image
    cv2.imshow("Image", image)
    cv2.waitKey(3000)
    cv2.destroyAllWindows()

    return len(humans)