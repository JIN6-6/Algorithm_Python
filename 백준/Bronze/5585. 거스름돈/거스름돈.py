n = 1000 - int(input())
count = 0

coin_types = [500,100,50,10,5,1] # 큰 순서대로 리스트에 넣음

for coin in coin_types: # 큰 것부터 개수 정하기
    count += n // coin # 몫만 구하면 된다.
    n %= coin

print(count)