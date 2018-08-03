# Find total permutations of length n

import itertools

def main():
    
    n = int(input("n: "))

    nums = list(range(1,n+1))
    
    perms = [x for x in itertools.permutations(nums)]

    with open("rosalind_perm.txt","w") as f:
        f.write(str(len(perms))+"\n")
        for x in perms:
            f.write(" ".join(str(i) for i in x)+"\n")

if __name__ == "__main__":
    main()
    
