class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        text = []

        for i in range(max(len(word1), len(word2))):
            text.append(word1[i])
            text.append(word2[i])

            if len(word1) - 1 == i:
                text.append(word2[i+1:len(word2)])
                break
            elif len(word2) - 1 == i:
                text.append(word1[i+1:len(word1)])
                break

        return "".join(text)
