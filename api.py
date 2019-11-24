import cv2
import numpy as np

from clips import Environment, Symbol

e = Environment()

# Pilih rule
e.load('segitiga2.clp')

# Load image
img = cv2.imread("segitiga.jpg", cv2.IMREAD_GRAYSCALE)
_, threshold = cv2.threshold(img, 240, 255, cv2.THRESH_BINARY)

# Buat contours
contours, _ = cv2.findContours(
    threshold, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# Pilih font
font = cv2.FONT_HERSHEY_COMPLEX

for cnt in contours:
    # Aproksimasi sisi polygon
    approx = cv2.approxPolyDP(cnt, 0.01*cv2.arcLength(cnt, True), True)

    # Gambar contour
    cv2.drawContours(img, [approx], 0, (0), 5)

    # Get x, y untuk text
    x = approx.ravel()[0]
    y = approx.ravel()[1]
    # print(cv2.arcLength(cnt, True))

    # Klasifikasi berdasarkan jumlah sisi
    if len(approx) == 3:
        # e.assert_string("(titik 1 1)")
        # e.assert_string("(titik 1 2)")
        # e.assert_string("(titik 2 1)")

        # Assert fakta berupa titik shape
        for a in approx:

            print("(titik " + str(a[0][0]) + " " + str(a[0][1]) + ")")
            strInput = "(titik " + str(a[0][0]) + " " + str(a[0][1]) + ")"
            print(strInput)
            e.assert_string(strInput)
        cv2.putText(img, "Segitiga", (x, y), font, 1, (0))
    elif len(approx) == 4:
        cv2.putText(img, "Persegi", (x, y), font, 1, (0))
    elif len(approx) == 5:
        cv2.putText(img, "Segi Lima", (x, y), font, 1, (0))
    elif len(approx) == 6:
        cv2.putText(img, "Segi Enam", (x, y), font, 1, (0))

# Print all facts
for fact in e.facts():
    print(fact)

# Kalo mau run sekali, pake e.run(1)
# Kalo mau run sampai habis, pake e.run()
e.run()
cv2.imshow("shapes", img)
cv2.imwrite("segitiga-result.jpg", img)
# cv2.imshow("Threshold", threshold)
cv2.waitKey(0)
cv2.destroyAllWindows()
