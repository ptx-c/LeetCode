class Solution:
    def isMonotonic(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        inc, dec = False, False
        for i in range(len(A) - 1):
            if A[i] > A[i + 1]:
                if inc:
                    return False
                dec = True
            elif A[i] < A[i + 1]:
                if dec:
                    return False
                inc = True
        return True
