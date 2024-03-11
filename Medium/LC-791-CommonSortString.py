class Solution:
    def customSortString(self, order: str, s: str) -> str:
        freq = Counter(s)
        new_string = ""

        for ptr in order:
            if ptr in freq:
                new_string += ptr * freq[ptr]
                freq[ptr] -= freq[ptr]

        for char in freq:
            new_string += char * freq[char]
        
        return new_string