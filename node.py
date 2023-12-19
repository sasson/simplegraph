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

    def __init__(self, Class : str, Id : str, text : str = "", vector : List[float] = []):
        """
        Initialize a Node object.

        Args:
            Class (str): Class of the node.
            Id (str): Unique identifier of the node.
            text (str): Textual description of the node.
            vector (List[float]): Vector representation of the node.
        """
        self.Class, self.Id = (Class, Id)
        self.text = text
        self.vector = vector
        self.incoming_links = {}
        self.outgoing_links = {}

    def add_incoming_link(self, link : Link):
        """
        Add an incoming link to this node.

        Args:
            link (Link): The link to be added.
        """
        source_class = link.source_class
        if source_class not in self.incoming_links:
            self.incoming_links[source_class] = LinksById(source_class)
        self.incoming_links[link.source_class][link.source_id] = link

    def add_outgoing_link(self, link : Link):
        """
        Add an outgoing link from this node.

        Args:
            link (Link): The link to be added.
        """
        goal_class = link.goal_class
        if goal_class not in self.outgoing_links:
            self.outgoing_links[goal_class] = LinksById(goal_class)
        self.outgoing_links[goal_class][link.goal_id] = link

class NodesById(dict):
    def __init__(self, node_class : str):
        self.node_class = node_class

class LinksById(dict):
    def __init__(self, goal_class : str):
        self.goal_class = goal_class
