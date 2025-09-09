import sympy as sp

a1, a2, a3 = sp.symbols('a1 a2 a3')
b1, b2, b3 = sp.symbols('b1 b2 b3')
c1, c2, c3 = sp.symbols('c1 c2 c3')

a = sp.Matrix([a1, a2, a3])
b = sp.Matrix([b1, b2, b3])
c = sp.Matrix([c1, c2, c3])

lhs = a.cross(b.cross(c))

rhs = b * (a.dot(c)) - c * (a.dot(b))

proof = sp.simplify(lhs - rhs)

lhs_latex = sp.latex(lhs)
rhs_latex = sp.latex(rhs)

print("LHS =", lhs_latex)
print("RHS =", rhs_latex)
print("LHS - RHS =", proof)
