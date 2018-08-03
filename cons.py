import pandas as pd
import numpy as np
from Bio import SeqIO

def main():
    
    strings = []

    with open("rosalind_cons.txt") as f:
        for record in SeqIO.parse(f, "fasta"):
            strings.append(str(record.seq))
   
    n = len(strings[0])

    counts = pd.DataFrame(0, index=["A","C","G","T"], columns = range(n))
    
    for dna in strings:
        for i, bp in enumerate(dna):
            counts.loc[bp,i] += 1
    
    consensus = []
    for i in range(n):
        consensus.append(counts[i].idxmax(axis=1))
    
    with open("rosalind_cons_sol.txt", "w") as f:
        f.write("".join(consensus)+"\n")
        f.write("A: " + " ".join(str(x) for x in counts.loc['A'])+"\n")
        f.write("C: " + " ".join(str(x) for x in counts.loc['C'])+"\n")
        f.write("G: " + " ".join(str(x) for x in counts.loc['G'])+"\n")
        f.write("T: " + " ".join(str(x) for x in counts.loc['T'])+"\n")
     

if __name__ == "__main__":
    main()
