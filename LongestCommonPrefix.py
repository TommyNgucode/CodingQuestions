class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        #find lenght of smallest string
        minWord = strs[0]
        #o(n) 
        for word in strs:
            length = len(word)
            if length < len(minWord):
                minWord = word

        longestPrefix = ""
        for i in range(len(minWord)):
            currentLetter = minWord[i]
            for word in strs:
                #wrong mismatch then break 
                if currentLetter != word[i]:
                    return longestPrefix
            #only runs if for loop wasn't broken
            #"If the loop didn't break early, then run the else"
            else:
                longestPrefix += currentLetter          
            

 
        return longestPrefix