#문제의 point > 최소 개수로 거슬러 주기 위하여 각 종류의 화폐가 몇 개씩 필요한지 출력하여라.

for tc in range(1, int(input())+1):
    money = int(input())
    coin = [50000,10000,5000,1000,500,100,50,10]
    result = [0]*8
    for i in range(8): # 가장 큰 금액의 화폐부터 몫을 저장해줌
        if money >= coin[i]:
            result[i] += money//coin[i]
            money = money%coin[i]
    print(f'#{tc}')
    print(*result)