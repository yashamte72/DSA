from collections import Counter
class Solution:
    def frequencySort(self, s: str) -> str:
        freq = Counter(s)

        result = "".join(ch * count for ch,count in freq.most_common())
        return result

        