import operator

dic = {'boy':'소년', 'school':'학교','book':'책'}
dic1 = sorted(dic)
print(dic1)
print(dic)

dic2=sorted(dic.keys())
print(dic2)

dic3=sorted(dic.values())
print(dic3)

dic4=sorted(dic.items())
print(dic4)

dic5=sorted(dic.keys(),reverse=True)
print(dic5)

dic6=sorted(dic.values(),reverse=True)
print(dic6)

dic7=sorted(dic.items(),reverse=True)
print(dic7)

dic8=sorted(dic.items(),key=operator.itemgetter(1))
print(dic8)