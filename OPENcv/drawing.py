import cv2 as cv

print("enter the file name: \n")
imagename=input()

image=cv.imread(imagename)

print("what task you want to draw on image\n1 for line\n2 for circle\n3 for rectangle\n4 for text\n")
opp=int(input())

if opp==1:
    print("for this you have to give values of\n")
    x1=int(input("X1: "))
    y1=int(input("Y1: "))
    x2=int(input("X2: "))
    y2=int(input("Y2: "))
    pt1=(x1,y1)
    pt2=(x2,y2)
    color=(0,0,255)
    cv.line(image,pt1,pt2,color,2)
    cv.imshow("line image",image)
    print("do you want to save img y/n\n")
    opp2=input()
    if opp2 == "y":
        cv.imwrite("line.jpg",image)
    else:
        print("not saved")
elif opp==3:
    print("for this you have to give values of\n")
    x1=int(input("\nX1: "))
    y1=int(input("\nY1: "))
    x2=int(input("\nX2: "))
    y2=int(input("\nY2: "))
    pt1=(x1,y1)
    pt2=(x2,y2)
    color=(0,0,255)
    cv.rectangle(image,pt1,pt2,color,2)
    cv.imshow("rectangle image",image)
    print("\ndo you want to save img y/n\n")
    opp2=input()
    if opp2 == "y":
        cv.imwrite("rectangle.jpg",image)
    else:
        print("\nnot saved")
elif opp==2:
    print("for this you have to give values of\n")
    x1=int(input("\nX1: "))
    y1=int(input("\nY1: "))
    radius=int(input("\nradius: "))
    center=(x1,y1)
    color=(0,0,255)
    cv.circle(image,center,radius,color,2)
    cv.imshow("circle image",image)
    print("\ndo you want to save img y/n\n")
    opp2=input()
    if opp2 == "y":
        cv.imwrite("circle.jpg",image)
    else:
        print("\nnot saved")
elif opp==4:
    print("for this you have to give values of\n")
    x1=int(input("\nX1: "))
    y1=int(input("\nY1: "))
    text=input("\ntext: ")
    pt1=(x1,y1)

    color=(0,0,255)
    cv.putText(image,text,pt1,cv.FONT_HERSHEY_SIMPLEX,1.2,color,2)
    cv.imshow("text image",image)
    print("\ndo you want to save img y/n\n")
    opp2=input()
    if opp2 == "y":
        cv.imwrite("text.jpg",image)
    else:
        print("\nnot saved")
else:
    print("error")