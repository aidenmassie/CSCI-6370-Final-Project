import random

def rahti_encryption_improved(plaintext, key):
    print(plaintext)
    if len(plaintext) > 64:
        raise ValueError('Plaintext message exceeds 64 length.')
    elif len(plaintext) < 64:
        plaintext += '.'*(64 - len(plaintext))

    m = [[ord(plaintext[i+8*j]) for i in range(8)] for j in range(8)]

    m_t = [[m[j][i] for j in range(8)] for i in range(8)]

    key_sub = [key[i:i+8] for i in range(0,len(key),8)]
    k_t = [[None for _ in range(8)] for _ in range(8)]

    for i, x in enumerate(key_sub):
        for j, y in enumerate(x):
            match y:
                case 'A':
                    k_t[i][j] = 0
                case 'C':
                    k_t[i][j] = 1
                case 'G':
                    k_t[i][j] = 2
                case 'T':
                    k_t[i][j] = 3
    
    m_k = [[m_t[i][j]+k_t[i][j] for j in range(8)] for i in range(8)]

    m_r = m_k

    for i in range(8):
        for j in range(8-i):
            m_r[i].insert(0,m_r[i].pop())
    
    temp = zip(*m_r[::-1])
    m_c = [list(x) for x in temp]

    for i in range(8):
        for j in range(8-i):
            m_c[i].append(m_c[i].pop(0))

    for i in range(3):
        temp = zip(*m_c[::-1])
        m_c = [list(x) for x in temp]

    c = [[chr(m_c[i][j]) for j in range(8)] for i in range(8)]

    ciphertext = ''
    for row in c:
        for col in row:
            ciphertext = ''.join((ciphertext,col))

    return ciphertext

def rahti_key_generation_improved():
    k_t = [[random.randrange(0, 128) % 4 for _ in range(8)] for _ in range(8)]

    key = ''

    for row in k_t:
        for col in row:
            match str(col):
                case '0':
                    key = ''.join((key,'A'))
                case '1':
                    key = ''.join((key,'C'))
                case '2':
                    key = ''.join((key,'G'))
                case '3':
                    key = ''.join((key,'T'))
    return key

def rahti_decryption_improved(ciphertext, key):
    m_c = [[ord(ciphertext[i+8*j]) for i in range(8)] for j in range(8)]
    
    temp = zip(*m_c[::-1])
    m_r = [list(x) for x in temp]

    for i in range(8):
        for j in range(8-i):
            m_r[i].insert(0,m_r[i].pop())

    for i in range(3):
        temp = zip(*m_r[::-1])
        m_r = [list(x) for x in temp]
    
    m_k = m_r

    for i in range(8):
        for j in range(8-i):
            m_k[i].append(m_k[i].pop(0))

    key_sub = [key[i:i+8] for i in range(0,len(key),8)]
    k_t = [[None for _ in range(8)] for _ in range(8)]

    for i, x in enumerate(key_sub):
        for j, y in enumerate(x):
            match y:
                case 'A':
                    k_t[i][j] = 0
                case 'C':
                    k_t[i][j] = 1
                case 'G':
                    k_t[i][j] = 2
                case 'T':
                    k_t[i][j] = 3

    m_t = [[m_k[i][j]-k_t[i][j] for j in range(8)] for i in range(8)]

    m = [[chr(m_t[j][i]) for j in range(8)] for i in range(8)]

    plaintext = ''
    for row in m:
        for col in row:
            plaintext = ''.join((plaintext,col))

    return plaintext