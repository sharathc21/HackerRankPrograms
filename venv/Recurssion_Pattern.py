def lcs_recursive(seq1, seq2, i=0, j=0):
    if i== len(seq1) or j== len(seq2):
        return 0
    elif seq1[i] == seq2[j]:
        return 1 + (lcs_recursive(seq1, seq2, i+1, j+1))
    else:
        option1 = lcs_recursive(seq1, seq2, i+1, j)
        option2 = lcs_recursive(seq1, seq2, i, j+1)
        return max(option1 , option2)


# seq1 ="abcdef"
# seq2= "badcfe"
#
# print(lcs_recursive(seq1, seq2))


t0 = {
    'input' :{ 'seq1' : "abcdef", 'seq2' :"badcfe"},
    'output' : 3
}


print(lcs_recursive(t0['input'] ['seq1'], t0['input'] ['seq2']) == t0['output'])



