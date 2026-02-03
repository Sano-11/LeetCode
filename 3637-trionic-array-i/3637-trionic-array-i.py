class Solution:
    def isTrionic(self, nums):
        n = len(nums)
        
        # Need at least 4 elements minimum
        if n < 4:
            return False
        
        # Try each possible pair (p, q) where 0 < p < q < n-1
        for p in range(1, n - 1):
            for q in range(p + 1, n):
                if q >= n - 1:  # q must be < n-1
                    continue
                    
                # Check if this (p, q) forms a valid trionic array
                valid = True
                
                # Section 1: [0...p] strictly increasing
                for i in range(p):
                    if nums[i] >= nums[i + 1]:
                        valid = False
                        break
                
                if not valid:
                    continue
                
                # Section 2: [p...q] strictly decreasing
                for i in range(p, q):
                    if nums[i] <= nums[i + 1]:
                        valid = False
                        break
                
                if not valid:
                    continue
                
                # Section 3: [q...n-1] strictly increasing
                for i in range(q, n - 1):
                    if nums[i] >= nums[i + 1]:
                        valid = False
                        break
                
                if valid:
                    return True
        
        return False


# Test
sol = Solution()
print(sol.isTrionic([5, 9, 1, 7]))  # Should return True