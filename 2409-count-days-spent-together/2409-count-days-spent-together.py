class Solution(object):
    def countDaysTogether(self, arriveAlice, leaveAlice, arriveBob, leaveBob):
        """
        :type arriveAlice: str
        :type leaveAlice: str
        :type arriveBob: str
        :type leaveBob: str
        :rtype: int
        """
        def getDate(date):
            days = [31,28,31,30,31,30,31,31,30,31,30,31]
            month = int(date[:2])
            day = int(date[3:])
            return sum(days[:month-1])+day
        
        return max(0,min(getDate(leaveAlice),getDate(leaveBob))+1 - max(getDate(arriveAlice),getDate(arriveBob)))