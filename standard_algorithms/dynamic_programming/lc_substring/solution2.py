def lcs(str1: str, str2: str) -> int:
    # write your code here
    n1 = len(str1)
    n2 = len(str2)

    # initialize dp
    dp = [[-1]*(n2+1) for _ in range(n1+1)]

    # if no str1 is considered, common substring is 0
    for r in range(n1+1):
        dp[r][0] = 0
    
    # if no str2 is considered, common substring is 0
    for c in range(n2+1):
        dp[0][c] = 0
    max_len = 0
    for i1 in range(1, n1+1):
        for i2 in range(1, n2+1):
            if str1[i1-1]==str2[i2-1]:
                dp[i1][i2] = 1 + dp[i1-1][i2-1]
                max_len = max(max_len, dp[i1][i2])
            else:
                dp[i1][i2] = 0
    # for row in dp:
    #     print(row)
    
    return max_len