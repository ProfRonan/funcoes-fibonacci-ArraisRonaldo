def fibonacci(n):
    if(n<0):
      raise ValueError("n tem que ser maior do que zero")
    if(n==0):
       return 0
    r = [0, 1]
    for i in range(1, n):
        r.append(r[i-1]+r[i])

    return r[-1]
if __name__ == "__main__":
    n = int(input("Digite um número: "))
    print(fibonacci(n))
