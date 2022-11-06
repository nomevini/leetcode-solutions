class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        substring = []
        test_substring = []
        # iterando pela string
        for i in range(len(s)):
            # adicionando a letra da repeticao
            test_substring.append(s[i])
            # iterando pelas letras a frente de cada letra
            for j in range(i + 1, len(s)):
                if s[j] not in test_substring:
                    test_substring.append(s[j])
                else:
                    break
            # verificar se a substring criada eh maior que a strign anterior criada
            if len(test_substring) > len(substring):
                substring = []
                substring = test_substring.copy()
            test_substring = []
        return len(substring)


s = Solution()
print(s.lengthOfLongestSubstring('pwwkew'))