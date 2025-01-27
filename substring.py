text = input("Enter a string: ")
sub = input("Enter substring: ")
if sub in text:
    print(sub, "substring is available")
else:
    print("Not available")
