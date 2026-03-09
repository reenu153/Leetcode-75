class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """

        anagrams={}
        
        for word in strs:
            sorted_word=str(sorted(word))
            if sorted_word in anagrams.keys():
                anagrams[sorted_word].append(word)
            else:
                anagrams[sorted_word]=[word]
        
        return anagrams.values()
                

        