# Generate all strings of length n that can be formed from the alphabet.

import itertools

def main():

    with open("datafiles/rosalind_lexf.txt") as f:
        alphabet = f.readline().split()
        k = int(f.readline())

    with open("solutions/lexf.txt","w") as f:  
        for x in list(itertools.product(alphabet,repeat=k)):
            f.write("".join(x))
            f.write("\n")

if __name__ == "__main__":
    main()
