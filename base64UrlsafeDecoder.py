import sys, base64, os

while 1:
    inStr = input("input: ")
    outStr = base64.urlsafe_b64decode(inStr.encode()).decode()
    print(outStr)

