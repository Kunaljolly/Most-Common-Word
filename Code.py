class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        paragraph = paragraph.lower()
        for x in banned:
            paragraph = paragraph.replace(x," ")
        paragraph = paragraph.replace("!", " ")
        paragraph = paragraph.replace("?", " ")
        paragraph = paragraph.replace("'", " ")
        paragraph = paragraph.replace(",", " ")
        paragraph = paragraph.replace(";", " ")
        paragraph = paragraph.replace(".", " ")
        
        print(paragraph)
        paragraph = paragraph.split()
        
        d = [[x,paragraph.count(x)] for x in set(paragraph)]

        ma = 0

        for x,y in d:
            ma = max(ma,y)
        
        for x,y in d:
            if y == ma:
                return x



        
