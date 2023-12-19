from typing import List
from link import Link

class Node:
    def __init__(self, Class : str, Id : str, text : str = "", vector : List[float] = []):
        self.Class, self.Id = (Class, Id)
        self.text = text
        self.vector = vector
        self.incoming_links = {}
        self.outgoing_links = {}

    def add_incoming_link(self, link : Link):
        source_class = link.source_class
        if source_class not in self.incoming_links:
            self.incoming_links[source_class] = LinksById(source_class)
        self.incoming_links[link.source_class][link.source_id] = link

    def add_outgoing_link(self, link : Link):
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
