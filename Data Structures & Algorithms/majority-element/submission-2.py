class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        m_dict = {}
        for n in nums:
            if n in m_dict:
                m_dict[n] += 1
            else:
                m_dict[n] = 1
        for [k,v] in m_dict.items():
            if v > len(nums) / 2:
                return k
        return 0