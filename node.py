from typing import List
from link import Link

class Node:
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
        self.incoming_links = {}
        self.outgoing_links = {}

    def add_incoming_link(self, link : Link):
        """
        Add an incoming link.

        Args:
            link  (Link): The incoming link to be added.
        """

        cl, id = link.source
        if cl not in self.incoming_links:
            self.incoming_links[cl] = {}
        self.incoming_links[cl][id] = link

    def add_outgoing_link(self, link : Link):
        """
        Add an outgoing link.

        Args:
            link  (Link): The link to be added.
        """

        cl, id = link.goal
        if cl not in self.outgoing_links:
            self.outgoing_links[cl] = {}
        self.outgoing_links[cl][id] = link

