def reaching_points(x1, y1, x2, y2, c):
    square = set()
    i = 0
    while i*i < x2+y2:
        square.add(i*i)
        i += 1

    def dfs(p, q):
        if p > x2 or q > y2 or (p+q in square):
            return False
        if p == x2 and q == y2:
            return True
        return dfs(p+q, q) or dfs(p, p+q) or dfs(p+c, q+c)
    return dfs(x1, y1)
print(reaching_points(5,5,15,15,2))

def common_prefix(array1, array2):
    n1, n2, common = len(array1), len(array2), 0
    while common < n1 and common < n2:
        if array1[common] != array2[common]:
            break
        else:
            common += 1
    return common

print(common_prefix([4,1,2,3,5], [4,1,2,5,7]))