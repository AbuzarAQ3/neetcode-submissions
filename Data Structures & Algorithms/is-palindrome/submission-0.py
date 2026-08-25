class Solution:
    def isPalindrome(self, s: str) -> bool:
        processed_str = ("".join(char for char in s if char.isalnum())).lower()
        n = len(processed_str)
        l, r = 0, len(processed_str)-1
        print(processed_str)

        while l<(n//2):
            if not processed_str[l] == processed_str[r]:
                return False
            else:
                l+=1
                r-=1
        print(processed_str)
        return True
