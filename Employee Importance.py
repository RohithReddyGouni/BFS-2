"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        Map={}
        total=0
        Que=deque()
        for emp in employees:
            Map[emp.id]=[emp.importance,emp.subordinates]
        if id in Map:
            Que.append(id)
        while Que:
            node=Que.popleft()
            total+=Map[node][0]
            length=len(Map[node][1])
            for sub in range(length):
                Que.append(Map[node][1][sub])
                
        return total