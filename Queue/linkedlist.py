class LinkedList:
    """
    You should implement the methods of this class which are currently
    raising a NotImplementedError!
    Don't change the name of the class or any of the methods.
    """
    def __init__(self):
        self.__root = None

    def get_root(self):
        return self.__root

    def add_start_to_list(self, node):
        """
        You can reuse the method written for the previous assignment here.

        :param node: the node to add at the start
        :return: None
        """
        if self.__root:
            node.set_next(self.__root)
        self.__root = node

    def remove_end_from_list(self):
        """
        Implement this method! It should:
        - Iterate over each node
        - Find both the second-to-last node and the last node
        - Set the second-to-last node's next to be None
        - Return the last node
        :return: the removed Node.
        """
        marker = self.__root

        # Especially delete the root if it by itself. <<COPIED from teachers example>>
        # If there is only one node in the list then this if clause is needed in order to remove it
        # Because a None would be returned by the lower while clause. This is the default python return
        if not marker.get_next():
            self.__root = None
            return marker

        # Iterate over each node in the list.
        while marker:
            # Get the next node
            following_node = marker.get_next()
            if following_node:
                # if the next Node's next Node is None, it means the current marker is the second
                # to last Node. (because there is only one more after it).
                if not following_node.get_next():
                    # make the markers next = None so the very last Node is removed.
                    marker.set_next(None)
                    return following_node
            marker = marker.get_next()

    def print_list(self):
        marker = self.__root
        while marker:
            marker.print_details()
            marker = marker.get_next()

    def find(self, name):
        marker = self.__root
        while marker:
            if marker.name == name:
                return marker
            marker = marker.get_next()
        raise LookupError("Name {} was not found in the list.".format(name))

    def size(self):
        # It should return the amount of Nodes in the list.
        node_count = 0
        marker = self.__root
        while marker:
            node_count += 1
            marker = marker.get_next()
        return node_count
