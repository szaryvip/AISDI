from node import Node
import tree_painter

class BSTTree:
    def __init__(self, elements: list = None):
        self._top = None
        if elements == None or elements == []:
            self._elements = []
        else:
            for element in elements:
                self.insert(element)


    def __str__(self):
        return tree_painter.draw(self)


    def top(self):
        """
        Return the node on the top of the tree.
        """
        return self._top


    def height(self):
        """
        Return the height of the tree.
        """
        if self._top == None:
            return 0
        return self._top.height()


    def insert(self, element):
        """
        Inserting new node to tree
        """
        if self._top == None:
            self._top = Node(None, element)
        else:
            actual_node = self._top
            while not actual_node.is_leaf():
                if element >= actual_node.value():
                    if actual_node.right_son() != None:
                        actual_node = actual_node.right_son()
                    else:
                        break
                else:
                    if actual_node.left_son() != None:
                        actual_node = actual_node.left_son()
                    else:
                        break
            new_node = Node(actual_node, element)
            if element >= actual_node.value():
                actual_node.set_right_son(new_node)
            else:
                actual_node.set_left_son(new_node)


    def find(self, element):
        """
        Returns node with that element or
        None if there is no such element in nodes
        """
        actual_node = self._top
        if self._top == None:
            return None
        while actual_node.value() != element:
            if actual_node.is_leaf():
                return None
            if element > actual_node.value():
                actual_node = actual_node.right_son()
                if actual_node == None:
                    return None
            else:
                actual_node = actual_node.left_son()
                if actual_node == None:
                    return None
        return actual_node


    def delete(self, element):
        """
        Deleting node from tree. Returns none if element not found
        """
        if self.find(element) == None:
            return None
        actual_node = self._top
        while actual_node.value() != element:
            if element >= actual_node.value():
                actual_node = actual_node.right_son()
            else:
                actual_node = actual_node.left_son()
        parent = actual_node.parent()
        if actual_node.is_leaf():
            if actual_node == self._top:
                self._top == None
            else:
                #zwyczajnie usuwamy podpięcie rodzica do tego elementu
                if parent.left_son() == actual_node:
                    parent.set_left_son(None)
                elif parent.right_son() == actual_node:
                    parent.set_right_son(None)
        elif actual_node.one_son():
            #przepinamy syna do ojca tego usuwanego
            if actual_node.right_son() != None:
                son = actual_node.right_son()
            else:
                son = actual_node.left_son()
            if actual_node == self._top:
                self._top == son
            else:
                if parent.right_son() == actual_node:
                    parent.set_right_son(son)
                else:
                    parent.set_left_son(son)
        else:
            #znajdujemy następnik i usuwamy go przepisując jego wartość do węzła zktórego usuwamy element
            next_node = find_next_node(actual_node)
            if next_node.parent().right_son() == next_node:
                next_node.parent().set_right_son(None)
            else:
                next_node.parent().set_left_son(None)
            if actual_node == self._top:
                self._top = next_node
            else:
                if parent.right_son() == actual_node:
                    parent.set_right_son(next_node)
                else:
                    parent.set_left_son(next_node)
            if next_node.right_son() != None:
                next_node.parent().set_left_son(next_node.right_son())
            next_node.set_left_son(actual_node.left_son())
            next_node.set_right_son(actual_node.right_son())


def find_next_node(actual_node):
    """
    Returns node which is higher that actual node
    """
    node = actual_node.right_son()
    while node.left_son() != None:
        node = node.left_son()
    return node

