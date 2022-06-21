"""
Project : Python practice
Author : JAEHYUN KIM
Date of Last Update : 22. 06. 20
Update list:
    -Ver        Date        Author
    -v1.0       22.06.20    JAEHYUN KIM
"""

# 반점(,)으로 인한 자동 띄어 쓰기 제거 sep=""
# print 문에서 자동 줄바꿈 해결 end=""

print("Hello world !")
my_name = "JAEHYUN KIM"
print("My name is", my_name, ".")
print("My name is", my_name, ".", sep="")
print("My name is", my_name, ".", end="")

# definitions of variables
x_in = input("input x =")
y_in = input("input y =")
x, y = int(x_in), int(y_in)

x = 5
y = 2
print("\nx :", x)
print("y :", y)

# operations
sum_xy = x + y
sub_xy = x - y
mul_xy = x * y
div_xy = x / y
int_div_xy = x // y

print("x + y :", sum_xy)
print("x - y :", sub_xy)
print("x * y :", mul_xy)
print("x / y :", div_xy)
print("x // y :", int_div_xy)
