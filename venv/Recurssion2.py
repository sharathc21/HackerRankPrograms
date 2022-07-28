
def lcs_memo(seq1, seq2):
    memo={}

    def lcs_recursive(i=0, j=0):
        key=(i, j)
        if key in memo:
            return memo[key]
        elif i== len(seq1) or j== len(seq2):
            memo[key]= 0
        elif seq1[i] == seq2[j]:
            memo[key] = 1 + (lcs_recursive( i+1, j+1))
        else:
            memo[key] = max(lcs_recursive( i+1, j), lcs_recursive(i, j+1))

        return memo[key]
    return lcs_recursive(0, 0)


seq1 ="abcdef"
seq2= "badcfe"
print(lcs_memo(seq1, seq2))