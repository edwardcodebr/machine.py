def pattern(mystring, x):
    for i in mystring:
        x = x + 1
        print(mystring[0:x])
    for i in mystring:
        x = x - 1
        print(mystring[0:x])

x = 0
mystring = "hello world"
pattern(mystring, x)