# Find the number of rabbits after n months if each produces k pairs

def main():
    n = 34
    k = 3

    f_n2 = 1
    f_n1 = 1

    for i in range(n-2):
        f_n = k*f_n2 + f_n1
        f_n2 = f_n1
        f_n1 = f_n
    print(f_n)

if __name__ == "__main__":
    main()
