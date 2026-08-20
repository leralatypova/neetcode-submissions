class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = ''
        for s in strs:
            encoded_string += str(len(s))+":"+s
        return encoded_string

    def decode(self, s: str) -> List[str]:
        decoded_strs = []
        i=0
        while i < len(s):
            k = i
            while s[k] != ':':
                k += 1
            length = int(s[i:k])  
            decoded_strs.append(s[k+1 : k+1+length])  
            i = k + 1 + length  

        return decoded_strs

