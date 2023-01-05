#1

a=1
print(dir(type(a)))
print("ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ")
print(dir(int))
if type(a) == int:
    print("true")


print(str(int))
print(repr(int))
if "<class 'int'>" == str(int):
    print("true")

if "<class 'int'>" == repr(int):
    print("true")

print(int.__str__)
#print(int.__dict__)

class A:
    def __init__(self):
        test = 100
        hello = "hello"

A = a
print("\n\n\n\n")
print(a.__dir__)
