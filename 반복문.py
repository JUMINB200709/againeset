'''
#구구단 1~9단 출력
for j in range(1,10,1):
    for i in range(1,10,1):
        mul=j*i #mul 선언 
        print(f'{j}*{i} = {mul}')
    print('-------------------------')
'''

'''
#case1
#1부터 100까지 홀수만 출력
for i in range(1,101,2):
    print(i)

#case2
for i in range(1,101,1):
    if i%2==1:
        print(i)
'''

'''
#5부터 100까지 5의 배수 출력
for i in range(5,101,5):
        print(i)

for i in range(1,101,1):
    if i%5==0:
        print(i)
'''

'''
# 10000까지 제곱수를 출력
#case 1
for i in range(1,101,1):
    print(i*i)

#case 2
for i in range(1,101,1):
    print(i**2)

#case 3
for i in range(1,101,1):
    print(i**3)
'''

'''
#146쪽 문제 해결
a = "Life is too short, you need python"

if "wife" in a: print("wife")
elif "python" in a and "you" not in a: print("python ")
elif "shirt" not in a: print("shirt")
elif "need" in a: print("need")
else: print("none")
'''

'''
#146쪽 문제 해결-2
result = 0
i = 1
while i <= 1000:
    if i%3==0:
        result=result+i
    i=i+1
print(result)
'''

#for문으로 
result=0
for i in range(1,1001,1):
    if i%3==0:
        result=result+i
print(result)
    

























































    
















