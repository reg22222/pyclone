#튜플을 사용하지 않고 swap하기
'''
a = 12
b = 34
print(a,b)

temp = a
a = b
b = temp
print(a,b)
'''

#튜흘을 이용하여 swap하기

a,b = 12,34
print(a,b)

b,a = a,b

print(a,b)