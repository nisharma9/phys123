from sympy import symbols, Matrix, simplify

a1, a2, a3 = symbols('a1 a2 a3')
b1, b2, b3 = symbols('b1 b2 b3')
c1, c2, c3 = symbols('c1 c2 c3')

A = Matrix([a1, a2, a3])
B = Matrix([b1, b2, b3])
C = Matrix([c1, c2, c3])

def triple(X, Y, Z):
    return X.dot(Y.cross(Z))

expr1 = triple(A, B, C)
expr2 = triple(B, C, A)
expr3 = triple(C, A, B)

print("A · (B × C) =", expr1)
print("B · (C × A) =", expr2)
print("C · (A × B) =", expr3)

print(simplify(expr1 - expr2))
print(simplify(expr2 - expr3))

