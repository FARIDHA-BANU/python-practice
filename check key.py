def checkkey(d1,key):
    if key in d1.keys():
        print("key is present")
    else:
        print("key is not present")
 
d1={'a':100,'b':200,'c':300,'d':400}
key=input("Enter a key")
checkkey(d1,key)