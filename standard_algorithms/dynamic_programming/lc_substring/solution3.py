# longest common substring
def lcs(str1: str, str2: str) -> int:
    # write your code here
    n1 = len(str1)
    n2 = len(str2)

    # initialize dp
    upto_prev = [0]*(n2+1)


    max_len = 0
    for i1 in range(1, n1+1):
        current = [0]*(n2+1)
        for i2 in range(1, n2+1):
            if str1[i1-1]==str2[i2-1]:
                current[i2] = 1 + upto_prev[i2-1]
                max_len = max(max_len, current[i2])
            else:
                current[i2] = 0
        upto_prev = current
    
    return max_len