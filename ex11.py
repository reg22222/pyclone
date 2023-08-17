animation = {}

print("요소추가 이전:",animation)

animation['작가'] = '황미나'
animation['연재작'] = '이오니아의 푸른 별'
animation['최근작'] = '보톡스'
print("요소 추가 이후:",animation)

del animation['연재작']
print('요소제거 이후:',animation)