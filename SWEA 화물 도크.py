#문제의 point > 최대 몇 대의 화물차가 도크를 이용할 수 있는지를 출력하시오.

for tc in range(1, int(input())+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    arr.sort(key = lambda x: x[1]) # 작업 종료 시간을 기준으로 정렬
    ed = arr[0][1] # 선택 작업의 종료 지점
    cnt = 1 # 도크를 사용한 화물차의 개수
    for i in range(1,N):
        if arr[i][0] >= ed:
            cnt += 1
            ed = arr[i][1]
    print(f'#{tc} {cnt}')