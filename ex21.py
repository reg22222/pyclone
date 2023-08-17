numbers=[1,2,3,4,5,6,7,8,9,5,1,7,3,5,1,3,5,7,9]
count={1:1,2:1,3:1}
for number in numbers:
    if number in count:
        count[number]+=1
    else:
        count[number]=1
print(count)