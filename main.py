def fib(n, memo={}):
    if n<=0:
        return 0
    if memo.get(n) != None:
        return memo.get(n)
    elif n==1 or n==2:
        memo[n] = 1
    else:
        memo[n] = fib(n-1) + fib(n-2)
    return memo[n]

console.log(fib(10))