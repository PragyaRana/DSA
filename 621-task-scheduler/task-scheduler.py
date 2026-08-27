class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = [0] * 26
        for task in tasks:
         freq[ord(task) - ord('A')] += 1
        maxFreq = max(freq)     

        maxCount = freq.count(maxFreq)

        result = (maxFreq - 1)* (n+1) + maxCount

        return max(result,len(tasks))
