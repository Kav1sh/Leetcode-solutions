class Solution:
    def reverseWords(self, s: str) -> str:
      list_1= s.split()
      list_2 = []
      for x in list_1:
        list_2.insert(0,x)
      return " ".join(map(str,list_2))