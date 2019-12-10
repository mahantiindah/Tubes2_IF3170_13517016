import cv2
import numpy as np

from clips import Environment, Symbol



def getAngle(a, b, c):
    ang = math.degrees(math.atan2(c[1]-b[1], c[0]-b[0]) - math.atan2(a[1]-b[1], a[0]-b[0]))
    return ang + 360 if ang < 0 else ang

def isSamaSisi(app):
    edgeList = []
    for i in range(len(app)-1):
        edgeList.append(getDistance(app[i],app[i+1]))

    return checkEqual(edgeList)

        

def checkEqual(lst):
   return lst[1:] == lst[:-1]

def getDistance(a,b):
    ax = a[0][0]
    ay = a[0][1]
    bx = b[0][0]
    by = b[0][1]

    return np.sqrt((ax - bx)**2 + (ay - by)**2)

def detection():
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
            '''for a in approx:

                print("(titik " + str(a[0][0]) + " " + str(a[0][1]) + ")")
                strInput = "(titik " + str(a[0][0]) + " " + str(a[0][1]) + ")"
                print(strInput)
                e.assert_string(strInput)'''
            if(isSamaSisi(approx)):
                e.assert_string('(sisi total)')
            e.assert_string('(titik 3)')
            
                
            cv2.putText(img, "Segitiga", (x, y), font, 1, (0))
        elif len(approx) == 4:
            if(isSamaSisi(approx)):
                e.assert_string('(sisi total)')
            e.assert_string('(titik 4)')
            cv2.putText(img, "Persegi", (x, y), font, 1, (0))

        elif len(approx) == 5:
            if(isSamaSisi(approx)):
                e.assert_string('(sisi total)')
            e.assert_string('(titik 5)')
            cv2.putText(img, "Segi Lima", (x, y), font, 1, (0))

        elif len(approx) == 6:

            if(isSamaSisi(approx)):
                e.assert_string('(sisi total)')
            e.assert_string('(titik 6)')
            cv2.putText(img, "Segi Enam", (x, y), font, 1, (0))

    outputFile = open("fakta.txt","w")
    list_fact =''
    # Print initial facts
    print("\nInitial Facts :")
    for fact in e.facts():
        list_fact += fact + '\n'
        print(list_fact)
    outputFile.write(list_fact) 
    outputFile.close()


    # Kalo mau run sekali, pake e.run(1)
    # Kalo mau run sampai habis, pake e.run()
    e.run()

    # Print all facts at the end
    print("\n\nFinal Facts :")
    outputFile = open("matched_facts.txt","w")
    list_fact =''
    for fact in e.facts():
        list_fact += fact + '\n'
        print(list_fact)
    outputFile.write(list_fact) 
    outputFile.close()

    # Agenda
    print("\nAgenda :")
    outputFile = open("hit_rules.txt","w")
    list_agenda =''
    for agenda in e.activations():
        list_agenda += agenda + '\n'
        print(list_agenda)
    outputFile.write(list_agenda) 
    outputFile.close()

    '''print("\nRules :")
    for rule in e.rules():
        print(rule)'''

cv2.imshow("shapes", img)
cv2.imwrite("result.jpg", img)
# cv2.imshow("Threshold", threshold)
cv2.waitKey(0)
cv2.destroyAllWindows()

