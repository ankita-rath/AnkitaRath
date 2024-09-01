def addressval(address):
    dot = address.find(".")
    at = address.find("@")
    if (dot == -1):
        print("invalid")
    elif (at == -1):
        print("invalid")
    else:
        print("valid")
print("this program will decide if your input is a valid email address")
while(True):
    print("a valid email address needs an '@' symbol and a '.'")
    x= input ("input your email address:")
    addressval(x)

    