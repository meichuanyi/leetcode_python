n = int(input())
s = list(map(int, input().split()))
# dp = [[0] * n for _ in range(n)]
a = s
mod = MOD = 10 ** 9 + 7
from math import comb

# for i in range(n - 1, -1, -1):
#     for j in range(i + 1, n):
#         if s[i] == s[j]:
#             dp[i][j] = dp[i + 1][j - 1]
#         else:
#             dp[i][j] = dp[i+1][j] + dp[i][j-1] - dp[i+1][j-1] + pow(2, j-i-1, MOD) 
#             dp[i][j] %= MOD
# print(dp[0][-1] % MOD)
N = 10 ** 5 + 1
fac = [1] * N  # fac[i] i的阶乘
ifac = [1] * N  # ifac[i] i的阶乘 的逆元
inv = [0] * N  # inv[i]  i的逆元
inv[1] = 1
for i in range(2, N):
    fac[i] = fac[i - 1] * i % mod
    inv[i] = (mod - mod // i) * inv[mod % i] % mod
    ifac[i] = ifac[i - 1] * inv[i] % mod


def C(n: int, k: int) -> int:  # 不重复组合数，n个不同物品不重复无序的取出k个
    if n < 0 or k < 0 or n < k:
        return 0
    return ((fac[n] * ifac[k]) % MOD * ifac[n - k]) % MOD


res = 0
for i in range(n):
    for j in range(i):
        if a[i] != a[j]:
            res += 1 * pow(2, i - j - 1, mod) * C(j + (n - 1 - i), j)
            res %= mod

print(res)