def DNA_strand(dna):
    output = ''
    for d in dna:
        if d == 'A':
            output += 'T'
        elif d == 'T':
            output += 'A'
        elif d == 'G':
            output += 'C'
        elif d == 'C':
            output += 'G'
    return output
