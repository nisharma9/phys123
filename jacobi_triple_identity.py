import sympy as sp

#Jacobi identity for the vector triplw product
# ax(bxc) + bx(cxa) + cx(axb) = 0

U_x, U_y, U_z = sp.symbols('U_x U_y U_z')
W_x, W_y, W_z = sp.symbols('W_x W_y W_z')
V_x, V_y, V_z = sp.symbols('V_x V_y V_z')

U = sp.Matrix([U_x, U_y, U_z])
V = sp.Matrix([V_x, V_y, V_z])
W = sp.Matrix([W_x, W_y, W_z])

p1 = U.cross(V.cross(U))
p2 = V.cross(U.cross(W))
p3 = W.cross(U.cross(V))

d12 = p1-p2
d13 = p1-p3
d23 = p2-p3

p1_tex = sp.latex(p1)
p2_tex = sp.latex(p2)
p3_tex = sp.latex(p3)

print(p1_tex)
print(p2_tex)
print(p3_tex)
