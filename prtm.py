# Calculate the total weight of a protein.

def main():
    
    # Generate protein mass dictionary

    mmt = {}

    with open("ref/protein_mass.txt") as f:
        for line in f:
            mmt[line.split()[0]] = float(line.split()[1])

    with open("datafiles/rosalind_prtm.txt") as f:
        p = f.readline()

    mass = 0

    for aa in p:
        mass += mmt[aa]

    print(round(mass,3))

if __name__ == "__main__":
    main()
