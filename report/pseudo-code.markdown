**Original SiftDown**

```
Procedure SiftDown(N)
    pre     Heap(2, N) and N > 0
    post    Heap(1, N)

I := 1
loop
        /*Inv: Heap(1, N) except perhaps between I
                and its (0, 1, or 2) children */
        C := 2*I
        if C > N then break
        /* C is the left child of I */
        if C + 1 <= N then
            /* C + 1 is the right child of I */
            if X[C+1] < X[C] then
                C := C + 1
        /* C is the least child of I */
        if X[I] <= X[C] then break
        Swap(X[C], X[I])
        I := C
    endloop
```
<div style="page-break-after: always;"></div>
**Modified SiftDown**
```
Procedure SiftDown(L, U)
    pre     Heap(L + 1, U) and N > 0
    post    Heap(L, U)

I := 1
loop
        /*Inv: Heap(1, N) except perhaps between I
                and its (0, 1, or 2) children */
        C := 2*I
        if C > N then break
        /* C is the left child of I */
        if C + 1 <= N then
            /* C + 1 is the right child of I */
            if X[C+1] < X[C] then
                C := C + 1
        /* C is the least child of I */
        if X[I] <= X[C] then break
        Swap(X[C], X[I])
        I := C
    endloop
```
