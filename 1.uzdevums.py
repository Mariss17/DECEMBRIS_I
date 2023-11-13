#Izveidojiet Python programmu, kas saskaita no 1 līdz lietotāja ievadītam skaitlim, izmantojot for ciklu.

def skaitlis(n):
    rezultats = 1

    for i in range(1, n + 1):
        rezultats *= i

    return rezultats

n = int(input("Ievadiet veselu pozitīvu skaitli: "))

print(f{n})


