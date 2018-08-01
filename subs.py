def main():
    with open("rosalind_subs.txt") as f:
        s = f.readline()
        t = f.readline()
    
    slen = len(s)
    tlen = len(t)
    
    positions = []

    for i in range(slen):
        if s[i:i+tlen] == t:
            positions.append(str(i + 1))

    print(" ".join(positions))

if __name__ == "__main__":
    main()
