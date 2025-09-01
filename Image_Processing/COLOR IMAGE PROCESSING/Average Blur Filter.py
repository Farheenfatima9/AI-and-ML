import numpy as np
import cv2

def creatingmask():
    x = int(input("Enter the mask size: "))
    if x % 2 == 0:
        print("❌ Not a valid mask size. Must be odd.")
        return None
    else:
        mask = np.ones([x, x], dtype=np.float32)
        mask = mask * (1 / (x * x))   # normalize for averaging
        return mask

def Padding(image, paddingsize):
    new = np.pad(image, (paddingsize, paddingsize))
    return new

def Filter(img, fil):
    a = int(np.floor(np.shape(fil)[0] / 2))   # half mask size
    r, c = img.shape
    r_out = r - 2 * a
    c_out = c - 2 * a

    output = np.zeros((r_out, c_out), dtype=np.uint8)

    for i in range(a, r - a):
        for j in range(a, c - a):
            region = img[i - a:i + a + 1, j - a:j + a + 1]
            z = np.sum(region * fil)
            output[i - a, j - a] = np.clip(z, 0, 255)  # keep in 0-255 range
    return output


# ---------------- MAIN ----------------
mask = creatingmask()
if mask is not None:
    image = cv2.imread("D:\Semester 6\DIP\Labs\Lab 10\Picture.tif")

    # Split channels
    b, g, r = cv2.split(image)

    # Padding size = half of mask size
    padding_size = int(np.floor(mask.shape[0] / 2))

    # Apply filter on each channel
    blue = Filter(Padding(b, padding_size), mask)
    green = Filter(Padding(g, padding_size), mask)
    red = Filter(Padding(r, padding_size), mask)

    # Merge back
    blurred = cv2.merge([blue, green, red])

    # Show results
    cv2.imshow("Original Image", image)
    cv2.imshow("Blue Channel Blurred", blue)
    cv2.imshow("Green Channel Blurred", green)
    cv2.imshow("Red Channel Blurred", red)
    cv2.imshow("Final Blurred Image", blurred)
    cv2.waitKey()
    cv2.destroyAllWindows()
