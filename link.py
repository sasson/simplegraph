from typing import List

class Link:
    """
    Represents a link in a directed graph.

    Attributes:
        source_class (str): Class of the source node.
        source_id (str): ID of the source node.
        goal_class (str): Class of the goal node.
        goal_id (str): ID of the goal node.
        vector (List[float]): Optional attribute for storing vector representation of the link.
    """

    def __init__(self, source_class: str, source_id: str, goal_class: str, goal_id: str):
        """
        Initialize a Link object.

        Args:
            source_class (str): Class of the source node.
            source_id (str): ID of the source node.
            goal_class (str): Class of the goal node.
            goal_id (str): ID of the goal node.
        """
        self.source_class = source_class
        self.source_id = source_id
        self.goal_class = goal_class
        self.goal_id = goal_id
        self.vector = []
