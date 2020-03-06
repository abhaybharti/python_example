class A:
    varA = 42
    def method1(self):
        print ("Class A : method1")
class B:
    varB = 37
    def method1(self):
        print ("Class B : method1")
    def method2(self):
        print ("Class B : method2")

#Inherits from A and B
class C(A,B):
    varC = 3.3
    def method3(self):
        print ("Class C : method3")

