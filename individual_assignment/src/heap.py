import math
import pydocstyle


class Heap():
    """
    Min/Max Heap implementation.

    Attributes
    - - -
    array : list(int)
        array to store heap in
    heap_type: str
        specifies if the heap is a min/max heap (defaults to min)
    """

    def __init__(self):
        """
        Initialize a min/max heap object.
        """
        self.array = []
        self.__last_index = -1

    def min_max_between(self, a, b):
        """
        Find min or max between a and b based on if heap is min or max.

        Arguments
        - - -
        a : int
            first integer to be compared
        b : int
            second integer to be compared
        """
        if self.heap_type == "min":
            return min(a, b)    # return min if min heap
        return max(a, b)        # return max if max heap

    def parent_child(self, parent, child):
        """
        Find parent to child relationship in the heap.

        Arguments
        - - -
        parent : int
            the parent
        child : int
            the child
        """
        if self.heap_type == 'min':
            return parent < child
        return parent > child

    def insert(self, data):
        """
        Insert data into the heap (either one int or list of ints).

        Arguments
        - - -
        data : int or list(int)
            data to be added
        """

        if isinstance(data, list):
            for i in data:
                self.array.append(i)
                self.__last_index += 1
                self.sift_up(self.__last_index)

        else:
            self.array.append(data)
            self.__last_index += 1
            self.sift_up(self.__last_index)

    def pop(self):
        """Delete first element in heap."""
        if self.__last_index == -1:
            raise IndexError('Heap empty')
        root = self.array[0]
        if self.__last_index > 0:
            self.array[0] = self.array[self.__last_index]
            self.sift_down(0)
        self.__last_index
        return root

    def push(self, val):
        """
        Append to back of heap and sift up.
        """
        self.array.append(val)
        self.__last_index += 1
        self.sift_up(self.__last_index)

    def heapify(self, input):
        n = len(input)
        self.array = input
        self.__last_index = n - 1
        for index in reversed(range(n//2)):
            self.sift_down(index)

    @classmethod
    def create_heap(cls, input_list):
        """
        Create heap based on input list.

        # Arguments:
        input_list (list): Input to make a heap from.
        """
        heap = cls()
        heap.heapify(input_list)
        return heap

    def sift_up(self, i):
        """
        Move smaller items up in heap recursively.

        Arguments
        - - -
        position : int
            position to start sift_up procedure from
        """
        current_val = self.array[i]
        parent = (i - 1) >> 1
        if i > 0:
            parent_val = self.array[parent]
            if self.compare(current_val, parent_val):
                self.array[parent], self.array[i] = current_val, parent_val
                self.sift_up(parent)

    def sift_down(self, i):
        """
        Move smaller items down the heap recursively.

        Arguments
        - - -
        position : int
            position to start sift_down procedure from
        """
        current_val = self.array[i]
        left, left_val = self.__get_left(i)
        right, right_val = self.__get_right(i)
        best, best_val = (left, left_val)
        if right is not None and self.compare(right_val, left_val):
            best, best_val = (right, right_val)

        if best is not None and self.compare(best_val, current_val):
            self.array[i], self.array[best] = best_val, current_val
            self.sift_down(best)

    def compare(self, a_val, b_val):
        raise NotImplementedError('use MinHeap or MaxHeap classes')

    def __get_parent(self, i):
        if i == 0:
            return None, None
        parent_index = (i - 1) // 2
        return parent_index, self.array[parent_index]

    def __get_left(self, i):
        left_child_index = 2 * i + 1
        if left_child_index > self.__last_index:
            return None, None
        return left_child_index, self.array[left_child_index]

    def __get_right(self, i):
        right_child_index = 2 * i + 2
        if right_child_index > self.__last_index:
            return None, None
        return right_child_index, self.array[right_child_index]

    def __repr__(self):
        return str(self.array[:self.__last_index + 1])

    def __eq__(self, other):
        if isinstance(other, Heap):
            return self.array == other.array
        if isinstance(other, list):
            return self.array == other
        return NotImplemented

class MinHeap(Heap):
    def compare(self, a_val, b_val):
        return a_val < b_val

class MaxHeap(Heap):
    def compare(self, a_val, b_val):
        return a_val > b_val
