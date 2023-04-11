class Solution:
    def fib(self, n: int) -> int:
        fib = [0, 1]
        if n <= 1:
            return n
        
        for i in range(2, n+1):
            next = fib[i - 1] + fib[i - 2]
            fib.append(next)
        return fib[n]


print(Solution().fib(4))
