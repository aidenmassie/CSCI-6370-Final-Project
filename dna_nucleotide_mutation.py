#DNA Encryption

#convert bits into DNA
def dna_encode(binary):
    
    #convert to DNA
    dna = ''

    for i in range(0, len(binary), 2):
        if binary[i] == '0' and binary[i+1] == '0':
            dna += 'A'
        elif binary[i] == '0' and binary[i+1] == '1':
            dna += 'G'
        elif binary[i] == '1' and binary[i+1] == '0':
            dna += 'T'
        elif binary[i] == '1' and binary[i+1] == '1':
            dna += 'C'
    
    #if the length of dna is less than 60, replicate from the start
    print (f"Length of DNA: {len(dna)}")

    if len(dna) < 60:
        for i in range(0,len(dna)):
            dna += dna[i]
    
    #last element of dna
    last = dna[-1]

    #if the length of dna is not a multiple of 3, replicate the last element until it is
    while len(dna)%3 != 0:
        dna += last

        
    return dna
    

#combines two DNA strands
def Anneal(key):

    new_key = key
    for char in key:
        if char == 'A':
            new_key += 'T'
        elif char == 'T':
            new_key += 'A'
        elif char == 'C':
            new_key += 'G'
        elif char == 'G':
            new_key += 'C'
    
    return new_key

##transcription of DNA to mRNA
def transcription(dna):

    mRNA = ''
    for char in dna:
        if char == 'A':
            mRNA += 'A'
        elif char == 'T':
            mRNA += 'U'
        elif char == 'C':
            mRNA += 'C'
        elif char == 'G':
            mRNA += 'G'
    
    return mRNA

def nonsense_mutation(dna):

    # cag -> uag
    # cga -> uga
    # ugg -> uga



def main():
    #get the key
    key = input("Enter the key: ")
    
    #encode to DNA
    dna = dna_encode(key)
    
    #combine the DNA strands
    new_key = Anneal(dna)
    
    print(f"Encoded DNA: {dna}")
    print(f"Combined DNA: {new_key}")
    print(f"Transcription: {transcription(new_key)}")

main()