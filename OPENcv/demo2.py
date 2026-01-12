import webbrowser
from datetime import datetime

print("1.google\n2.youtube")
ch=input("enter the selection: ")


if ch == "1":
   
    ch2=input("what you want to search: \n")
    print("opening google")
    webbrowser.open(f"https://www.google.com/search?q={ch2}")
elif ch=="2":
    print("opening youtube")
    webbrowser.open("https://www.youtube.com")
else: 
    print("could not help")