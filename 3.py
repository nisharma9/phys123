import sympy as sp

# Define symbols and vector basis
t, R, tau, v0 = sp.symbols('t R tau v0', real=True, positive=True)

# Unit vectors
x_hat = sp.Matrix([1, 0, 0])
y_hat = sp.Matrix([0, 1, 0])
z_hat = sp.Matrix([0, 0, 1])

# Define acceleration vector
a_vec = (R / tau**2) * (-sp.exp(t / tau) * x_hat + sp.sin(t / tau) * y_hat + 2 * z_hat)

# Integrate acceleration to get velocity
# Velocity at t=0 is v0 in x direction
v_vec = sp.integrate(a_vec, t) + v0 * x_hat

# Integrate velocity to get position
# Position at t=0 is R in z direction
r_vec = sp.integrate(v_vec, t) + R * z_hat

# Simplify results
v_vec_simplified = v_vec.applyfunc(sp.simplify)
r_vec_simplified = r_vec.applyfunc(sp.simplify)

# Output velocity components in LaTeX
print("Velocity vector \\( \\mathbf{v}(t) \\):")
for comp, axis in zip(v_vec_simplified, ['x', 'y', 'z']):
    latex_expr = sp.latex(comp)
    print(f"v_{{{axis}}}(t) = {latex_expr}")

print("\nPosition vector \\( \\mathbf{r}(t) \\):")
for comp, axis in zip(r_vec_simplified, ['x', 'y', 'z']):
    latex_expr = sp.latex(comp)
    print(f"r_{{{axis}}}(t) = {latex_expr}")
