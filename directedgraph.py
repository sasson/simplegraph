from node import Node
from link import Link

class DirectedGraph:
    """
    Represents a directed graph consisting of nodes and links.

    Attributes:
        nodes (dict): Dictionary storing nodes categorized by their class.
        links (dict): Dictionary storing links.
    """

    def __init__(self):
        """
        Initialize a DirectedGraph object.
        """
        self.nodes = {}
        self.links = {}

    def add_node(self, node : Node):
        """
        Add a node to the graph.

        Args:
            node (Node): The node object to be added.
        """
        if node.cl not in self.nodes:
            self.nodes[node.cl] = {}
        self.nodes[node.cl][node.cl] = node

    def add_link(self, source : (str, str), goal : (str, str) ):
        """
        Add a link between two nodes in the graph.

        Args:
            source (str, str): Class and Id of the source node.
            goal   (str, str): Class and Id of the goal node.
        """
        link = Link(source = source, goal = goal)
        s_cl, s_id = source
        g_cl, g_id = goal

        if s_cl in self.nodes and s_id in self.nodes[s_cl]:
            self.nodes[s_cl][s_id].add_outgoing_link(g_cl, link)

        if g_cl in self.nodes and g_id in self.nodes[g_cl]:
            self.nodes[g_cl][g_id].add_incoming_link(s_cl, link)

        self.links[ (source, goal) ] = link

    def connect_nodes(self, source : Node, goal : Node):
        """
        Create a Link from the "source" Node to the "goal" Node.

        Args:
            source (class Node): The source Node.
            goal   (class Node): The goal Node.
        """

        self.add_link(source.Class, source.Id, goal.Class, goal.Id)
