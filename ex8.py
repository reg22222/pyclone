score = [88,95,70,100,99]
tu = tuple(score)
#tu[0] = 100 실행안됨
print(tu)

li = list(tu)
li[0] = 100
print(li)