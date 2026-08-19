class Solution(object):
    def maxNumberOfFamilies(self, n, reservedSeats):
        """
        :type n: int
        :type reservedSeats: List[List[int]]
        :rtype: int
        """
        reserved = {}
        for row, seat in reservedSeats:
            if row not in reserved:
                reserved[row] = set()
            reserved[row].add(seat)

        left_block = {2, 3, 4, 5}
        mid_block = {4, 5, 6, 7}
        right_block = {6, 7, 8, 9}

        count = 0
        for row in reserved:
            taken = reserved[row]
            

            if not (taken & left_block):
                count +=1
                if not (taken & right_block):
                    count +=1
            elif not (taken & right_block):
                count +=1
            elif not (taken & mid_block):
                count +=1
            
            
        
        count += (n-len(reserved)) *2

        return count