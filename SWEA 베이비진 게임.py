def isbabygin(lst): # 베이비진을 확인하는 함수
    flag = False
    for i in range(len(lst)):
        if lst[i] == 3: # 같은 카드 세 장이면
            flag = True
            break
        if i < len(lst)-2:
            if lst[i]>=1 and lst[i+1]>=1 and lst[i+2]>=1: # 연속된 카드 세 장이면
                flag = True
                break
    return flag
 
for tc in range(1, int(input())+1):
    arr = list(map(int, input().split()))
    bst1, bst2 = [0]*10, [0]*10 # 플레이어 1, 2의 0 ~ 9 카드 개수를 저장
    flag = 0
    for i in range(12):
        if i%2 == 0:
            bst1[arr[i]] += 1
            if isbabygin(bst1):
                flag = 1
                break
        else:
            bst2[arr[i]] += 1
            if isbabygin(bst2):
                flag = 2
                break
    print(f'#{tc} {flag}')