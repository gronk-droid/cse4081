import pytest
from heap import MinHeap, MaxHeap
from hypothesis import given, assume
import hypothesis.strategies as st


def main():
    @given(st.lists(st.instegers()))
    def test_minheap(l):
        h = MinHeap.createHeap(l)
        s = sorted(l)
        for i in range(len(s)):
            assert h.pop() == s[i]

    @given(st.lists(st.integers()))
    def test_maxheap(l):
        h = MaxHeap.createHeap(l)
        s = sorted(l, reverse=True)
        for i in range(len(s)):
            assert h.pop() == s[i]


main()
