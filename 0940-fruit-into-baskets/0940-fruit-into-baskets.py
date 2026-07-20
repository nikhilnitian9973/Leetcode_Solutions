class Solution(object):
    def totalFruit(self, fruits):
        """
        :type fruits: List[int]
        :rtype: int
        """
        left = 0
        right = 0
        maxi = 0
        my_dic = {}
        while right < len(fruits):
            my_dic[fruits[right]] = my_dic.get(fruits[right],0) +1
            if len(my_dic) > 2:

                my_dic[fruits[left]] -=1
                if my_dic[fruits[left]] == 0:
                    my_dic.pop(fruits[left])
                left +=1
            maxi = max(maxi,right-left+1)
            right +=1
        return maxi



            
