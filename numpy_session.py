"""ELEC/COMP 576 - Assignment 0, Task 2
Run the 'Linear Algebra Equivalents' commands from 'NumPy for MATLAB Users'.
Prints each command and its result in an IPython-like transcript.
"""
import numpy as np
import scipy.linalg

_n = [0]
def show(cmd, val="__RUN__", env=None):
    _n[0] += 1
    print(f"In [{_n[0]}]: {cmd}")
    if val == "__RUN__":
        val = eval(cmd, env if env is not None else globals())
    if val is not None:
        out = repr(val)
        # indent multi-line output under an Out[] prompt like IPython
        lines = out.splitlines()
        print(f"Out[{_n[0]}]: {lines[0]}")
        for ln in lines[1:]:
            print(" " * (len(f'Out[{_n[0]}]: ')) + ln)
    print()

print("Python", __import__("sys").version.split()[0], "| NumPy", np.__version__, "| SciPy", __import__("scipy").__version__)
print("=" * 70)

# --- set up example matrices/vectors ---
show("a = np.array([[1., 2., 3.], [4., 5., 6.], [7., 8., 10.]])", None)
a = np.array([[1., 2., 3.], [4., 5., 6.], [7., 8., 10.]])
show("b = np.array([[3.], [3.], [4.]])", None)
b = np.array([[3.], [3.], [4.]])
show("a")

# --- Linear Algebra Equivalents (NumPy for MATLAB users) ---
show("np.ndim(a)")                 # ndims(a): number of dimensions
show("a.size")                     # numel(a): number of elements
show("a.shape")                    # size(a): (rows, cols)
show("a[-1]")                      # a(end): last row
show("a[1, :]")                    # a(2,:): 2nd row
show("a[0:2, :]")                  # a(1:2,:): first two rows
show("a[:, 1]")                    # a(:,2): 2nd column
show("a.T")                        # a.': transpose
show("a @ a")                      # a * a in MATLAB: matrix multiply
show("a * a")                      # a .* a: element-wise multiply
show("a ** 2")                     # a.^2: element-wise power
show("a @ b")                      # matrix-vector product
show("np.linalg.inv(a)")           # inv(a): inverse
show("np.linalg.solve(a, b)")      # a\\b: solve a x = b
show("np.linalg.det(a)")           # det(a): determinant
show("np.linalg.matrix_rank(a)")   # rank(a)
show("np.transpose(a) @ a")        # a' * a
show("np.linalg.eig(a).eigenvalues")   # eig(a): eigenvalues
show("np.linalg.svd(a, compute_uv=False)")  # svd(a): singular values
show("np.concatenate((a, a), axis=0)")  # [a; a]: vertical stack
show("np.concatenate((a, a), axis=1)")  # [a, a]: horizontal stack
show("np.eye(3)")                  # eye(3)
show("np.zeros((2, 3))")           # zeros(2,3)
show("np.ones((2, 3))")            # ones(2,3)
show("np.diag(a)")                 # diag(a): main diagonal
show("np.linalg.norm(b)")          # norm(b)
