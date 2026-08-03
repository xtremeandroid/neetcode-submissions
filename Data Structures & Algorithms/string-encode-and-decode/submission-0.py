class Solution:

    def encode(self, strs: List[str]) -> str:
        # ["ayush", "singh"]
        # encoded string will be 5#ayush5#singh
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        return res

    def decode(self, s: str) -> List[str]:
        res,i = [], 0

        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            lengthOfWord = int(s[i:j])
            extractedWord = s[j+1: j + 1 + lengthOfWord]
            res.append(extractedWord)
            i = j + 1 + lengthOfWord

        return res        
            
