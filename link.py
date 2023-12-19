from typing import List

class Link:
    """
    Represents a directed edge connecting two Nodes in a directed graph.

    Attributes:
        from   (str, str):     Class and Id of the Source Node.
        into   (str, str):     Class and Id of the Goal Node.

                vector (List[float]):  embedding vector of the Link.
    """

    def __init__(self, source: (str, str), goal: (str, str)):
        """
        Initialize a Link object.

        Args:
            source (str,str):  Class and Id of the Source Node.
            goal   (str,str):  Class and Id of the Goal Node.
        """
        self.source : (str, str) = source
        self.goal : (str, str) = goal
        self.vector = []
