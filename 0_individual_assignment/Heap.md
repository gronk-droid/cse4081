# Table of Contents

* [Heap](#Heap)
  * [Heap](#Heap.Heap)
    * [\_\_init\_\_](#Heap.Heap.__init__)
    * [min\_max\_between](#Heap.Heap.min_max_between)
    * [parent\_child](#Heap.Heap.parent_child)
    * [insert](#Heap.Heap.insert)
    * [pop](#Heap.Heap.pop)
    * [create\_heap](#Heap.Heap.create_heap)
    * [sift\_up](#Heap.Heap.sift_up)
    * [sift\_down](#Heap.Heap.sift_down)

<a id="Heap"></a>

# Heap

<a id="Heap.Heap"></a>

## Heap Objects

```python
class Heap()
```

Min/Max Heap implementation.

Attributes
- - -
array : list(int)
    array to store heap in
heap_type: str
    specifies if the heap is a min/max heap (defaults to min)

<a id="Heap.Heap.__init__"></a>

#### \_\_init\_\_

```python
def __init__(heap_type="min")
```

Initialize a min/max heap object.

<a id="Heap.Heap.min_max_between"></a>

#### min\_max\_between

```python
def min_max_between(a, b)
```

Find min or max between a and b based on if heap is min or max.

Arguments
- - -
a : int
    first integer to be compared
b : int
    second integer to be compared

<a id="Heap.Heap.parent_child"></a>

#### parent\_child

```python
def parent_child(parent, child)
```

Find parent to child relationship in the heap.

Arguments
- - -
parent : int
    the parent
child : int
    the child

<a id="Heap.Heap.insert"></a>

#### insert

```python
def insert(data)
```

Insert data into the heap (either one int or list of ints).

Arguments
- - -
data : int or list(int)
    data to be added

<a id="Heap.Heap.pop"></a>

#### pop

```python
def pop()
```

Delete first element in heap.

<a id="Heap.Heap.create_heap"></a>

#### create\_heap

```python
@classmethod
def create_heap(cls, input_list)
```

Create heap based on input list.

# Arguments:
input_list (list): Input to make a heap from.

<a id="Heap.Heap.sift_up"></a>

#### sift\_up

```python
def sift_up(i)
```

Move smaller items up in heap recursively.

Arguments
- - -
position : int
    position to start sift_up procedure from

<a id="Heap.Heap.sift_down"></a>

#### sift\_down

```python
def sift_down(i)
```

Move smaller items down the heap recursively.

Arguments
- - -
position : int
    position to start sift_down procedure from

