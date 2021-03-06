# class Solution:
#     def lengthOfLongetSubstring(self, s):
#         char_map = {}
#         max_length =0
#         window_start = 0

#         for i in range(len(s)):
#             end_char =s[i]
#             if end_char in char_map and char_map[end_char] >= window_start:
#                 window_start =  char_map[end_char] + 1
#                 char_map[end_char] = i
#                 max_length = max(max_length, i- window_start + 1)
                
#         return max_length

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        ht = {}
        left = 0
        right = 0
        answer = 0
        length = len(s)
        while (left < length and  right< length):
            el = s[right]
            if el in ht:
                left = max(left, ht[el] + 1)
            ht[el] = right
            answer = max(answer, (right - left) + 1)
            right += 1
        return answer
