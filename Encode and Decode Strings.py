class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""
        for word in strs:
            lengthWord = len(word)
            result += str(lengthWord)
            result +="#"
            for letter in word:
                result += letter
        
        print(result)
        
        return result
    def decode(self, s: str) -> List[str]:
        
        result = [""]
        counter = 0
        i = 0
        while i < len(s):
            if s[i].isdigit() and s[i + 1] == "#":
                length = int(s[i])
                start = i + 2
                end = start + length

                if end <= len(s):
                    group = s[start:end]
                    result[counter] = (group)
                    i = end
                else:
                    break
            else:
                i +=1
        
            # i+= int(length) + 2
        return result
            