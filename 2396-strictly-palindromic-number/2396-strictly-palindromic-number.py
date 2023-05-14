class Solution:
    def isStrictlyPalindromic(self, n: int) -> bool:
        bin_n = format(n, 'b')
        # making 2 bin number strings to compare.
        # even, odd lengths can be handled regardless of both.
        bin_n_left = str(bin_n[:len(bin_n)%2])
        bin_n_right = str(bin_n[len(bin_n)%2::-1])
                              
        if bin_n_left == bin_n_right:
            return True
        else:
            return False
                