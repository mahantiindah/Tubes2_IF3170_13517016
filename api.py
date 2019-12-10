import cv2
import numpy as np
import math

from clips import Environment, Symbol



def getAngle(a, b, c):
    ax = a[0][0]
    ay = a[0][1]
    bx = b[0][0]
    by = b[0][1]
    cx = c[0][0]
    cy = c[0][1]

    ang = math.degrees(math.atan2(cx-bx, cy-by) - math.atan2(ax-bx, ay-by))
    return ang + 360 if ang < 0 else ang

def getSisi(titik):
    sisi = []
    for i in range(len(titik)):
        sisi.append(getDistance(titik[i],titik[(i+1)%len(titik)]))

    return sisi

def getSudut(titik):
    sudut = []
    for i in range(len(titik)):
        sudut.append(getAngle(titik[i],titik[(i+1)%len(titik)],titik[(i+2)%len(titik)]))

    return sudut

def isSamaSisi(app):
    edgeList = []
    for i in range(len(app)-1):
        edgeList.append(getDistance(app[i],app[i+1]))

    return checkEqual(edgeList)

def compareGalat(a,b):
    temp = abs(a - b)
    if(temp < 3):
        return True
    else:
        return False


def checkEqual(lst):
   return lst[1:] == lst[:-1]

def getDistance(a,b):
    ax = a[0][0]
    ay = a[0][1]
    bx = b[0][0]
    by = b[0][1]

    return np.sqrt((ax - bx)**2 + (ay - by)**2)

def getAngleFact(ang):
    jumlah = len(ang)
    fact = []
    if(jumlah == 3):
        tumpul = any(sudut > 90 for sudut in ang) 
        siku = any(compareGalat(sudut,90) for sudut in ang) 

        if(tumpul):
            return '(sudut tumpul)'
        elif(siku):
            return '(sudut siku)'
        else:
            return '(sudut lancip)'
        
    elif(jumlah == 4):
        notTotal = any(not compareGalat(ang[0],angle) for angle in ang)

        if(not notTotal):
            return '(sudut total)'
        else:
            usedNumber = []
            for x in ang:
                count = ang.count(x)
                countUsed = usedNumber.count(x)
                if(count > 1 and countUsed == 0):
                    countUsed.append(x)
            
            if(len(usedNumber) == 2):
                if(not compareGalat(usedNumber[0],usedNumber[1])):
                    return '(sudut kembar-dua)'
            
            if(len(usedNumber) == 1):
                return '(sudut kembar-satu)'
            
            if(len(usedNumber) == 0):
                return '(sudut berantakan)'

        return fact

def getEdgeFact(edges):
    jumlah = len(edges)
    notTotal = any(not compareGalat(edges[0],edge) for edge in edges)
    fact = []
    if(jumlah == 3):
        if(not notTotal):
            return '(sisi total)'
        else:
            usedNumber = []
            for x in edges:
                count = edges.count(x)
                countUsed = usedNumber.count(x)
                if(count > 1 and countUsed == 0):
                    usedNumber.append(x)
            
            if(len(usedNumber) == 2):
                if(not compareGalat(usedNumber[0],usedNumber[1])):
                    return '(sisi kembar-dua)'
            
            if(len(usedNumber) == 1):
                return '(sisi kembar-satu)'
            
            if(len(usedNumber) == 0):
                return '(sisi berantakan)'

        return fact

    elif(jumlah == 4):

        if(not notTotal):
            return '(sisi total)'
        else:
            usedNumber = []
            for x in edges:
                count = edges.count(x)
                countUsed = usedNumber.count(x)
                if(count > 1 and countUsed == 0):
                    usedNumber.append(x)
            
            if(len(usedNumber) == 2):
                if(not compareGalat(usedNumber[0],usedNumber[1])):
                    return '(sisi kembar-dua)'
            
            if(len(usedNumber) == 1):
                return '(sisi kembar-satu)'
            
            if(len(usedNumber) == 0):
                return '(sisi berantakan)'

        return fact

    elif(jumlah == 5):
        if(not notTotal):
            return '(sisi total)'
        else:
            return '(sisi berantakan)'

        return fact

        
    elif(jumlah == 6):

        if(not notTotal):
            return '(sisi total)'
        else:
            return '(sisi berantakan)'

        return fact


e = Environment()

    # Pilih rule
e.load('geometri.clp')

    # Load image
img = cv2.imread("segitiga.jpg", cv2.IMREAD_GRAYSCALE)
_, threshold = cv2.threshold(img, 240, 255, cv2.THRESH_BINARY)

    # Buat contours
contours, _ = cv2.findContours(
    threshold, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    # Pilih font
font = cv2.FONT_HERSHEY_COMPLEX


for cnt in contours[1:]:
    # Aproksimasi sisi polygon
    approx = cv2.approxPolyDP(cnt, 0.01*cv2.arcLength(cnt, True), True)

        # Gambar contour
    cv2.drawContours(img, [approx], 0, (0), 5)

    # Get x, y untuk text
    x = approx.ravel()[0]
    y = approx.ravel()[1]
        # print(cv2.arcLength(cnt, True))


    for a in approx:

        print("(titik " + str(a[0][0]) + " " + str(a[0][1]) + ")")

    for i in getSisi(approx):
        print(i)

    for i in getSudut(approx):
        print(i)


                

        # Klasifikasi berdasarkan jumlah sisi

    print(len(approx))
    if len(approx) == 3:
        # Assert fakta berupa titik shape
        
        e.assert_string(getEdgeFact(getSisi(approx)))
        e.assert_string(getAngleFact(getSudut(approx)))
        e.assert_string('(titik 3)')
            
        cv2.putText(img, "Segitiga", (x, y), font, 1, (0))
   
    elif len(approx) == 4:

        e.assert_string(getEdgeFact(getSisi(approx)))
        e.assert_string(getAngleFact(getSudut(approx)))
        e.assert_string('(titik 4)')

            
        cv2.putText(img, "Persegi", (x, y), font, 1, (0))

    elif len(approx) == 5:
        e.assert_string(getEdgeFact(getSisi(approx)))
        e.assert_string('(titik 5)')
        cv2.putText(img, "Segi Lima", (x, y), font, 1, (0))

    elif len(approx) == 6:

        e.assert_string(getEdgeFact(getSisi(approx)))
        e.assert_string('(titik 6)')
        cv2.putText(img, "Segi Enam", (x, y), font, 1, (0))

  


# Print initial facts
print("\nInitial Facts :")
for fact in e.facts():
    print(fact)

print("\nAgenda :")
for agenda in e.activations():
    print(agenda)

# Kalo mau run sekali, pake e.run(1)
# Kalo mau run sampai habis, pake e.run()
e.run()

# Print all facts at the end
print("\n\nFinal Facts :")
for fact in e.facts():
    print(fact)


cv2.imshow("shapes", img)
cv2.imwrite("result.jpg", img)
# cv2.imshow("Threshold", threshold)
cv2.waitKey(0)
cv2.destroyAllWindows()

