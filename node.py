from typing import List

class Vertix:
    """
    Represents a node in a directed graph.

    Attributes:
        Class (str): Class of the node.
        Id (str): Unique identifier of the node.
        text (str): Optional textual description of the node.
        vector (List[float]): Optional vector representation of the node.
        incoming_links (dict): Dictionary of incoming links categorized by their source class.
        outgoing_links (dict): Dictionary of outgoing links categorized by their goal class.
    """

    def __init__(self, cl : str, id : str, text : str = "", vector : List[float] = []):
        """
        Initialize a Node object.

        Args:
            Class (str): Class of the node.
            Id (str): Unique identifier of the node.
            text (str): Textual description of the node.
            vector (List[float]): Vector representation of the node.
        """
        self.cl = cl
        self.id = id
        self.text = text
        self.vector = vector
        self.incoming_edges = {}
        self.outgoing_edges = {}


