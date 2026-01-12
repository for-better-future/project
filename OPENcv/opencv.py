import cv2 as cv

image_loc=input("enter image location or name: ")

image=cv.imread(image_loc)

gray=cv.cvtColor(image,cv.COLOR_RGB2GRAY)

print("do you want to show the image press 1: \ndo you want to save the image press 2: \n")
op=int(input())

if op == 1:
    cv.imshow("gray image",gray)
    cv.waitKey(0)
    cv.destroyAllWindows()
elif op ==2:
    print("enter the name of the file you want to save it as\n")
    name=input()
    cv.imwrite(name,gray)
    print("file saved yashly")
else:
    print("error")