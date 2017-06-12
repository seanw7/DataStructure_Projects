class BinaryTree:
    """
    This class is a binary tree implementation.

    Don't modify class or method names, just implement methods that currently raise
    a NotImplementedError!
    """

    def __init__(self):
        self.__root = None

    def get_root(self):
        return self.__root

    def add(self, node):
        """
        You should implement this method.
        It should add a node to the binary tree.
        If a node with that value already exists, raise a ValueError
        :param node: The Node to add
        :return: None
        """
        # The root is None, so set the root to be the new Node.
        if not self.__root:
            self.__root = node
        else:
            # Start iterating over the tree.
            marker = self.__root
            while marker:
                if node.value == marker.value:
                    raise ValueError("The value was already inside the Binary Tree.")
                    # Raise a ValueError, because the node's value already exists.
                elif node.value > marker.value:
                    marker.get_right()
                    if marker.value == None:
                        marker.set_right()
                    # elif node.value < marker.value:
                    #     if marker.value == None:
                    #         marker.set_left()

                    # Move to the right in the tree.

                else:
                    marker.get_left()
                    if node.value > marker.value:
                        marker.get_right()
                        if marker.value == None:
                            marker.set_right()


                    # Move to the left in the tree.

    def find(self, value):
        """
        You should implement this method.
        It should locate a node with a given value, and return it.
        If the Node is not found, it should raise a LookupError

        :param value: The value of the Node to locate.
        :return: Node, the found Node
        """
        marker = self.__root

        while marker:
            if value > marker.value:
                marker.get_right()
            elif value < marker.value:
                marker.get_left()
            elif value == marker.value:
                return marker
            else:
                return LookupError("Did not find value: {}, in the Binary Tree".format(value))

    def print_inorder(self):
        self.__print_inorder_r(self.__root)

    def __print_inorder_r(self, current_node):
        if not current_node:
            return
        self.__print_inorder_r(current_node.get_left())
        print(current_node.print_details())
        self.__print_inorder_r(current_node.get_right())
