import time
#대한민국의 현재시간을 time.struct_time형식으로 보여줌
'''
now = time.localtime()
print(now)
print(now.tm_hour)
print(now.tm_min)
'''
def gettime():
    now = time.localtime()
    return now.tm_hour , now.tm_min

hour, min = gettime()
print("지금은 {}시 {}분 입니다.".format(hour,min))