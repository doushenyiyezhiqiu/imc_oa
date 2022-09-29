from collections import deque


def crossroad(arrivals, streets):
    queue0 = deque()
    queue1 = deque()
    n = len(arrivals)
    ans = [0]*n
    order = 0
    for i in range(n):
        if streets[i] == 0:
            queue0.append((i, arrivals[i]))
        else:
            queue1.append((i, arrivals[i]))
    cur = min(arrivals)
    pre = -1
    while queue0 or queue1:
        if queue0 and queue1:
            if cur >= queue0[0][1] and cur >= queue1[0][1]:
                if pre == -1 or pre == 1:
                    idex, arr = queue1.popleft()
                    ans[idex] = order
                    pre = 1
                elif pre == 0:
                    idex, arr = queue0.popleft()
                    ans[idex] = order
                    pre = 0
            elif cur >= queue0[0][1] or cur >= queue1[0][1]:
                if queue0[0][1] < queue1[0][1]:
                    idex, arr = queue0.popleft()
                    ans[idex] = order
                    pre = 0
                elif queue0[0][1] > queue1[0][1]:
                    idex, arr = queue1.popleft()
                    ans[idex] = order
                    pre = 1
            else:
                cur = min(queue0[0][1], queue1[0][1])
                pre = -1
                continue
        elif queue0:
            idex, arr = queue0.popleft()
            ans[idex] = order
        elif queue1:
            idex, arr = queue1.popleft()
            ans[idex] = order
        cur += 1
        order += 1
    return ans

print(crossroad([0, 0, 1, 1, 4], [0, 1, 0, 1, 0]))
