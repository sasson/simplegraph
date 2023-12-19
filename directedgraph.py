from node import Node, NodesById
from link import Link

class DirectedGraph:
    def __init__(self):
        self.nodes = {}
        self.links = {}

    def add_node(self, class_string : str, node : Node):
        if class_string not in self.nodes:
            self.nodes[class_string] = NodesById()
        self.nodes[class_string][node.Id] = node

    def add_link(self, source_class : str, source_id : str, goal_class : str, goal_id : str):
        link = Link(source_class, source_id, goal_class, goal_id)
        if source_class in self.nodes and source_id in self.nodes[source_class]:
            self.nodes[source_class][source_id].add_outgoing_link(goal_class, link)
        if goal_class in self.nodes and goal_id in self.nodes[goal_class]:
            self.nodes[goal_class][goal_id].add_incoming_link(source_class, link)
        link_key = (source_class, source_id, goal_class, goal_id)
        self.links[link_key] = link

    def connect_nodes(self, source : Node, goal : Node):
        self.add_link(source.Class, source.Id, goal.Class, goal.Id)
