class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        output = 0
        for x in operations:
            if "++" in x:
                output+=1
            else :
                output=output-1
        return output