def lcs_dp(seq1, seq2):
    n1, n2 = len(seq1) ,  len(seq2)
    tbl = [[0 for x in range(n2+1) ] for x in range(n1 +1) ]
    for i in range(n1):
        for j in range(n2):
            if seq1[i] == seq2[j]:
                tbl[i+1][j+1] = 1 + tbl [i] [j]
            else:
                tbl[i+1][j+1]= max(tbl[i+1][j], tbl[i][j+1])


    return tbl[-1][-1]


seq1 ="abcdef"
seq2= "abfeabcdef"
print(lcs_dp(seq1, seq2))