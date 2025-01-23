e=8
f=9
print("Before swapping e=",e,"f=",f)
e=(e&f)+(e|f)
f=e+(~f)+1
e=e+(~f)+1
print("After swapping e=",e,"f=",f)