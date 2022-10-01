from pyodide import create_proxy

def calc_fib(event):
    ans = fib(int(Element('fib_input').value))
    Element('output').write(f"{ans}")
    console.log(ans)

def fib(n, memo={}):
    if n<=0:
        return 0
    if memo.get(n) != None:
        return memo.get(n)
    elif n==1 or n==2:
        memo[n] = 1
    else:
        memo[n] = fib(n-1, memo) + fib(n-2,memo)
    return memo[n]

cc = create_proxy(calc_fib)
x = document.getElementById('fib_input')
x.addEventListener("change", cc)