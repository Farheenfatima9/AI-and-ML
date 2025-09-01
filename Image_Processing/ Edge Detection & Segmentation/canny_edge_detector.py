import cv2
import numpy as np

def get_neighbors(pos, shape):
    neighbors = []
    for i in range(max(0, pos[0] - 1), min(shape[0], pos[0] + 2)):
        for j in range(max(0, pos[1] - 1), min(shape[1], pos[1] + 2)):
            if i != pos[0] or j != pos[1]:
                neighbors.append((i, j))
    return neighbors

# Read image
Image = cv2.imread("D:\Semester 6\DIP\Labs\Lab 07\input3.png", 0)
cv2.imshow("Original", Image)
cv2.waitKey()

# Sobel gradients
Gx = cv2.Sobel(Image, cv2.CV_64F, 1, 0, ksize=3)
Gy = cv2.Sobel(Image, cv2.CV_64F, 0, 1, ksize=3)

# Gradient magnitude and angle
G = np.sqrt(np.square(Gx) + np.square(Gy))
angle = np.arctan2(Gy, Gx)   # FIX: use atan2 not atan
angle = np.degrees(angle) % 180  # Normalize to [0, 180)

rows, cols = G.shape
out = np.zeros((rows, cols), dtype=np.uint8)

# Non-maximum suppression
for i in range(1, rows - 1):
    for j in range(1, cols - 1):
        if (0 <= angle[i, j] < 22.5) or (157.5 <= angle[i, j] <= 180):
            a = G[i, j + 1]
            b = G[i, j - 1]
        elif (22.5 <= angle[i, j] < 67.5):
            a = G[i + 1, j - 1]
            b = G[i - 1, j + 1]
        elif (67.5 <= angle[i, j] < 112.5):
            a = G[i + 1, j]
            b = G[i - 1, j]
        else:
            a = G[i - 1, j - 1]
            b = G[i + 1, j + 1]

        if (G[i, j] >= a) and (G[i, j] >= b):
            out[i, j] = G[i, j]

cv2.imshow("Non-Maximum Suppression", out)
cv2.waitKey()

# Double threshold (Otsu)
_, thresh = cv2.threshold(out, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
high = np.max(thresh)
low = 0.5 * high

# Canny + Hysteresis
edges = cv2.Canny(out.astype(np.uint8), low, high)

mask = np.zeros_like(edges, dtype=bool)
mask[edges > 0] = True

strong_edges = np.zeros_like(edges)
strong_edges[edges >= high] = 255

strong_positions = np.argwhere(strong_edges > 0)
for pos in strong_positions:
    neighbors = get_neighbors(pos, edges.shape)
    for n in neighbors:
        if edges[n[0], n[1]] >= low and not mask[n[0], n[1]]:
            mask[n[0], n[1]] = True
            strong_edges[n[0], n[1]] = 255

cv2.imshow("Final Edges", strong_edges)
cv2.waitKey()
