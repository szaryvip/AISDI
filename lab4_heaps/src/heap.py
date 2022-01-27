from abstract_heap import AbstractHeap
from abstract_heap import List, C
from math import floor


class Heap(AbstractHeap):
    def __init__(self, num_children: int, elements=None) -> None:
        self._elements = []
        self._num_child = num_children
        if elements is not None:
            for element in elements:
                self.push(element)

    def __len__(self) -> int:
        return len(self._elements)

    def _replace_elements(self, index1: int, index2: int) -> None:
        """
        Replace the elements with the given indexes.

        In:
            - Indexes of two elements
        """
        self._elements[index1], self._elements[index2] = (
            self._elements[index2],
            self._elements[index1],
        )

    def _get_sons(self, actual_index: int) -> List[C]:
        """
        Returns the list with sons of the actual index element.

        Parameters:
            - index of actual element
        Returns:
            - list with sons of the element
        """
        sons = []
        for son_nr in range(1, self._num_child+1):
            try:
                sons.append(self._elements[self._num_child * actual_index + son_nr])
            except IndexError:
                pass
        return sons

    def peek(self) -> C:
        """Get the topmost element without changing the heap."""
        if self._elements == []:
            raise IndexError("Nothing in heap!")
        return self._elements[0]

    def push(self, value: C) -> None:
        """Add an element to the heap."""
        index = len(self._elements)
        self._elements.append(value)
        parent_index = floor((index - 1) / self._num_child)
        while index > 0 and self._elements[parent_index] < value:
            self._replace_elements(index, parent_index)
            index = parent_index
            parent_index = floor((index - 1) / self._num_child)

    def pop(self) -> C:
        """Remove the topmost element from the heap and return it."""
        print(len(self.get_raw_data()))
        if self._elements == []:
            raise IndexError("Nothing to pop!")
        self._replace_elements(0, -1)
        top = self._elements.pop()
        actual_index = 0
        sons = self._get_sons(actual_index)
        while (sons != []) and (max(sons) > self._elements[actual_index]):
            if sons[0] == max(sons):
                self._replace_elements(actual_index, actual_index * self._num_child + 1)
                actual_index = actual_index * self._num_child + 1
            elif sons[1] == max(sons):
                self._replace_elements(actual_index, actual_index * self._num_child + 2)
                actual_index = actual_index * self._num_child + 2
            elif len(sons) >= 3 and sons[2] == max(sons):
                self._replace_elements(actual_index, actual_index * self._num_child + 3)
                actual_index = actual_index * self._num_child + 3
            elif len(sons) == 4 and sons[3] == max(sons):
                self._replace_elements(actual_index, actual_index * self._num_child + 4)
                actual_index = actual_index * self._num_child + 4
            sons = self._get_sons(actual_index)
        return top

    def get_raw_data(self) -> List[C]:
        """Get the underlying data storage."""
        return self._elements

    def num_children(self) -> int:
        return self._num_child
