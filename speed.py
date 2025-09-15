import sympy as sp

# define symbols
A, alpha, t = sp.symbols('A alpha t', real=True)

x, y = sp.symbols('x y')


rx = (A * alpha * t * sp.cos(alpha * t)) 
ry = (A * alpha * t * sp.sin(alpha * t))


vx = sp.simplify(sp.diff(rx, t))
vy = sp.simplify(sp.diff(ry, t))
v = vx + vy
vx_tex = sp.latex(vx)
vy_tex = sp.latex(vy)

v_mag = sp.simplify(sp.sqrt(vx**2 + vy**2))

ax = sp.simplify(sp.diff(vx, t))
ay = sp.simplify(sp.diff(vy, t))
aT = sp.simplify((vx * ax + vy * ay) / v_mag)
a_mag = sp.sqrt(ax**2 + ay**2)
aN = sp.simplify(sp.sqrt(a_mag**2 - aT**2))

ax_tex = sp.latex(ax)
ay_tex = sp.latex(ay)
aT_tex = sp.latex(aT)
aN_tex = sp.latex(aN)

dvdt = sp.simplify(sp.diff(v_mag, t))
dvdt_tex = sp.latex(dvdt)


print("v = ", vx, ", ", vy)
print("a = ", ax, ", ",ay)

print("v · v =", v_mag)

print(vx_tex, ", ", vy_tex)
print(ax_tex, ", ", ay_tex)
print("aT = ",aT_tex)
print("aN = ",aN_tex)
print("dvdt =", dvdt_tex
      )
