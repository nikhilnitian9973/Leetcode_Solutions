class Solution(object):
    def secondsBetweenTimes(self, startTime, endTime):
        """
        :type startTime: str
        :type endTime: str
        :rtype: int
        """
        hour1 = int(startTime[:2])
        minute1 = int(startTime[3:5])
        second1 = int(startTime[6:])

        hour2 = int(endTime[:2])
        minute2 = int(endTime[3:5])
        second2 = int(endTime[6:])

        sum_second = 0

        if second1 <= second2:
            sum_second += second2-second1
        else:
            second2 += 60
            sum_second += second2-second1

            minute2 -= 1
        if minute1 <= minute2:
            sum_second += 60*(minute2-minute1)
        else:
            minute2 += 60
            sum_second += 60*(minute2-minute1)
            hour2-=1
        sum_second += 60*60*(hour2-hour1)
        return sum_second