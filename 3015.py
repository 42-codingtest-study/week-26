N = int(input())
lst = [int(input()) for _ in range(N)]
answer = 0
for i in range(N - 1):
    start, end, tall = i, i + 1, lst[i + 1]
    while end < N:
        # print(start, end, tall, answer)
        if tall > lst[end]:
            break
        if end - start != 1 and lst[start] != tall and lst[end] == tall:
            answer -= 1
        if lst[end] > tall:
            tall = lst[end]
        end += 1
    answer += end - start - 1
print(answer)
