# Original SiftDown

```{=tex}
\begin{algorithm}[H]
\DontPrintSemicolon
\SetAlgoLined
\KwResult{Sorted Heap}
\SetKwInOut{Input}{Input}\SetKwInOut{Output}{Output}
\Input{An index N}
\Output{Heap(1,N)}
\BlankLine
$I := 1
\While{Heap(1, N) except between I and its children}{
    C := 2*I\;
    \If{C > N}{
        break
    }
    \If{C + 1 <= N}{
        \If{X[C + 1] < X[C]}{
            C := C + 1
        }
    }
    \If{X[I] <= X[C]}{
        break
    }
    Swap(X[C], X[I])
    I := C
}
\caption{pre: Heap(2, N) and N >= 0\\post: Heap(1, N)}
\end{algorithm}
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

**Modified SiftDown**
