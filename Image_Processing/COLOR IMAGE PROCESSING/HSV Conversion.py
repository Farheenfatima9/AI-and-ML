import cv2
import numpy as np

def convertimage(myimage):
    hue = np.zeros((myimage.shape[0], myimage.shape[1]), dtype=np.uint8)
    sat = np.zeros((myimage.shape[0], myimage.shape[1]), dtype=np.uint8)
    val = np.zeros((myimage.shape[0], myimage.shape[1]), dtype=np.uint8)

    for i in range(myimage.shape[0]):
        for j in range(myimage.shape[1]):
            b = myimage[i, j, 0]
            g = myimage[i, j, 1]
            r = myimage[i, j, 2]

            r_dash = r / 255
            g_dash = g / 255
            b_dash = b / 255

            cmax = max(r_dash, g_dash, b_dash)
            cmin = min(r_dash, g_dash, b_dash)
            delta = cmax - cmin

            # ---- Hue ----
            if delta == 0:
                hue[i, j] = 0
            elif cmax == r_dash:
                a = (g_dash - b_dash) / delta
                hue[i, j] = 60 * (a % 6)
            elif cmax == g_dash:
                a = (b_dash - r_dash) / delta
                hue[i, j] = 60 * (a + 2)
            elif cmax == b_dash:
                a = (r_dash - g_dash) / delta
                hue[i, j] = 60 * (a + 4)

            # ---- Saturation ----
            if cmax == 0:
                sat[i, j] = 0
            else:
                sat[i, j] = (delta / cmax) * 255

            # ---- Value ---- (using average of channels, not max)
            val[i, j] = ((r_dash + g_dash + b_dash) / 3) * 255

    return hue, sat, val


# ---------- First Image ----------
image = cv2.imread("D:\Semester 6\DIP\Labs\Lab 10\Box.jpg")
cv2.imshow("Image", image)

H, S, V = convertimage(image)
cv2.imshow("Hue", H)
cv2.imshow("Saturation", S)
cv2.imshow("Value", V)

HSV = cv2.merge([H, S, V])
cv2.imshow("HSV", HSV)
cv2.waitKey()

# ---------- Second Image ----------
image = cv2.imread("D:\Semester 6\DIP\Labs\Lab 10\STR.tif")
cv2.imshow("Image", image)

H, S, V = convertimage(image)
cv2.imshow("Hue", H)
cv2.imshow("Saturation", S)
cv2.imshow("Value", V)

HSV = cv2.merge([H, S, V])
cv2.imshow("HSV", HSV)
cv2.waitKey()
