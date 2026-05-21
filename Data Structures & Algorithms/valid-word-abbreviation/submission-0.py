class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        i = 0  # pointer for word
        j = 0  # pointer for abbr
        
        while i < len(word) and j < len(abbr):
            
            # If current character in abbr is a letter
            if abbr[j].isalpha():
                if word[i] != abbr[j]:
                    return False
                i += 1
                j += 1
            
            else:
                # Leading zero is invalid
                if abbr[j] == '0':
                    return False
                
                num = 0
                
                # Build the full number
                while j < len(abbr) and abbr[j].isdigit():
                    num = num * 10 + int(abbr[j])
                    j += 1
                
                # Skip num characters in word
                i += num
        
        # Both pointers should reach the end
        return i == len(word) and j == len(abbr)