# Using SymPy to symbolically prove the vector identity.
from sympy import symbols, Matrix, simplify, Eq, zeros
import sympy as sp

u1,u2,u3 = symbols('u1 u2 u3')
v1,v2,v3 = symbols('v1 v2 v3')
w1,w2,w3 = symbols('w1 w2 w3')
x1,x2,x3 = symbols('x1 x2 x3')

U = Matrix([u1, u2, u3])
V = Matrix([v1, v2, v3])
W = Matrix([w1, w2, w3])
X = Matrix([x1, x2, x3])

def scalar_triple(a, b, c):
    return a.dot(b.cross(c))

expr = (scalar_triple(V, W, X))*U - (scalar_triple(U, V, W))*X + (scalar_triple(X, U, V))*W - (scalar_triple(W, X, U))*V
expr_simpl = simplify(expr)


exprtex=sp.latex(expr)

print(exprtex)
print(expr_simpl)

