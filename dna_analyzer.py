
# My first Bioinformatics project
# DNA Sequence Analyzer

# A sample DNA sequence
dna = "ATGCGATCGATCGATCG"

# Calculate sequence length
length = len(dna)

# Count each nucleotide
A = dna.count("A")
T = dna.count("T")
G = dna.count("G")
C = dna.count("C")

# Calculate GC content
gc_content = ((G + C) / length) * 100
at_content = ((A + T) / length) * 100

# Display results
print("DNA SEQUENCE ANALYSIS")
print("---------------------")

print("DNA sequence:", dna)
print("Length:", length)
print("Adenine:", A)
print("Thymine:", T)
print("Guanine:", G)
print("Cytosine:", C)

print("GC Content:", round(gc_content, 2), "%")
print("AT Content:", round(at_content, 2), "%")