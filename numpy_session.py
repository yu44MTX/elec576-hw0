"""ELEC/COMP 576 - Assignment 0, Task 2
Run ALL Python commands from the "Linear Algebra Equivalents" table of
'NumPy for MATLAB Users', on a chosen matrix. Printed as an IPython-style
transcript (In[]/Out[] for each command).
"""
import numpy as np
import scipy.linalg

G = globals()
_n = [0]
def S(cmd):          # statement: show input only
    _n[0] += 1
    print(f"In [{_n[0]}]: {cmd}")
    exec(cmd, G)
    print()
def E(cmd):          # expression: show input and Out
    _n[0] += 1
    print(f"In [{_n[0]}]: {cmd}")
    try:
        val = eval(cmd, G)
        lines = repr(val).splitlines()
        pad = " " * len(f"Out[{_n[0]}]: ")
        print(f"Out[{_n[0]}]: {lines[0]}")
        for ln in lines[1:]:
            print(pad + ln)
    except Exception as ex:
        print(f"    {type(ex).__name__}: {ex}")
    print()

print("Python", __import__("sys").version.split()[0],
      "| NumPy", np.__version__, "| SciPy", __import__("scipy").__version__)
print("=" * 72)

# ----- example data -----
S("a = np.array([[1., 2., 3.], [4., 5., 6.], [7., 8., 10.]])")
S("b = np.array([[3.], [3.], [4.]])")
S("v = np.array([1., 2., 3.])")
E("a")

# ----- sizes / shape -----
E("a.ndim")                 # ndims(a)
E("np.ndim(a)")
E("a.size")                 # numel(a)
E("np.size(a)")
E("a.shape")                # size(a)
E("np.shape(a)")
E("a.shape[1]")             # size(a,2)

# ----- construction / stacking -----
E("np.array([[1., 2., 3.], [4., 5., 6.]])")   # [1 2 3; 4 5 6]
E("np.block([[a], [a]])")                      # [a ; a]

# ----- indexing / slicing -----
E("a[-1]")                  # a(end)
E("a[1, 2]")                # a(2,3)
E("a[1]")                   # a(2,:)
E("a[1, :]")
E("a[0:2, :]")              # a(1:2,:)
E("a[-2:]")                 # a(end-1:end,:)
E("a[0:2, 1:3]")            # a(1:2,2:3)
E("a[np.ix_([0, 2], [0, 1])]")   # a([1,3],[1,2])
E("a[::2, :]")              # a(1:2:end,:)
E("a[::-1, :]")             # flipud(a)
E("a[np.r_[:len(a), 0]]")   # a([1:end 1],:)

# ----- transpose -----
E("a.T")                    # a.'
E("a.transpose()")
E("a.conj().T")             # a'  (conjugate transpose)

# ----- element-wise vs matrix ops -----
E("a @ a")                  # a * a  (matrix product)
E("a * a")                  # a .* a
E("a / a")                  # a ./ a
E("a ** 3")                 # a.^3
E("a > 5")                  # (a > 0.5)
E("np.nonzero(a > 5)")      # find(a > 0.5)
E("a * (a > 5)")            # a .* (a > 0.5)

# ----- copies / flatten -----
S("y = a.copy()")           # y = x
E("a.flatten()")            # a(:)

# ----- ranges / creation -----
E("np.arange(1., 11.)")     # 1:10
E("np.arange(10.)")         # 0:9
E("np.arange(1., 11.)[:, np.newaxis]")   # [1:10]'
E("np.zeros((3, 4))")       # zeros(3,4)
E("np.zeros((2, 3, 2))")    # zeros(2,3,2)
E("np.ones((3, 4))")        # ones(3,4)
E("np.eye(3)")              # eye(3)
E("np.diag(a)")             # diag(a)
E("np.diag(v)")             # diag(v)  -> matrix
E("np.linspace(1, 3, 4)")   # linspace(1,3,4)
E("np.tile(a, (2, 1))")     # repmat(a,2,1)
E("np.concatenate((a, a), axis=1)")   # [a a]
E("np.concatenate((a, a), axis=0)")   # [a ; a]
E("np.hstack((a, a))")
E("np.vstack((a, a))")

# ----- reductions -----
E("a.max()")                # max(max(a))
E("a.max(0)")               # max(a)
E("a.max(1)")               # max(a,[],2)
E("np.maximum(a, a.T)")     # max(a,b)
E("a.sum()")                # sum(a(:))
E("a.sum(0)")               # sum(a)
E("a.sum(1)")               # sum(a,2)
E("np.linalg.norm(v)")      # norm(v)

# ----- logical -----
E("np.logical_and(a > 2, a < 8)")   # a & b
E("np.logical_or(a < 2, a > 8)")    # a | b

# ----- linear algebra -----
E("np.linalg.inv(a)")               # inv(a)
E("np.linalg.pinv(a)")              # pinv(a)
E("np.linalg.matrix_rank(a)")       # rank(a)
E("np.linalg.solve(a, b)")          # a\b
E("np.linalg.lstsq(a, b, rcond=None)[0]")   # least squares
E("np.linalg.det(a)")               # det(a)
S("U, s, Vh = np.linalg.svd(a)")    # [U,S,V] = svd(a)
E("s")
S("w, V = np.linalg.eig(a)")        # [V,D] = eig(a)
E("w")
S("Q, R = np.linalg.qr(a)")         # [Q,R] = qr(a)
E("R")
S("P, L, Uu = scipy.linalg.lu(a)")  # [L,U,P] = lu(a)
E("L")
S("spd = a @ a.T")                  # build an SPD matrix
E("scipy.linalg.cholesky(spd)")     # chol(spd)

# ----- misc table entries -----
E("np.sort(a, axis=0)")             # sort(a)
E("np.argsort(v)")                  # [b,I] = sort(a)
E("np.unique(np.array([3, 1, 2, 1, 3]))")   # unique(a)
E("np.fft.fft(v)")                  # fft(a)
E("a.squeeze().shape")              # squeeze(a)
