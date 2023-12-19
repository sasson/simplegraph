from typing import List

class Link:
    def __init__(self, source_class : str, source_id : str, goal_class : str, goal_id : str):
        self.source_class, self.source_id = source_class, source_id
        self.  goal_class, self.goal_id   =   goal_class,   goal_id

        self.vector : List[float] = []
        
