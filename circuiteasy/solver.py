from sympy import symbols, solve, sympify
import cmath
import math

def solve_equations(variables, equations, component_values):
    """
    Solve a system of equations symbolically (with SymPy) for circuit analysis.
    Args:
        variables        : List of variable names to solve for (strings).
        equations        : List of equations as strings (e.g., 'I1 + I2 - 2').
        component_values : Dictionary of {component_name: value} for substitution.
    Returns:
        dict with:
            'formatted': List of formatted solution strings (mag∠deg, real+j imag).
            'values'   : Dict {var: solution as complex}
    Example:
        solve_equations(['I1','I2'], ['I1+I2-2', '2*I1-I2-1'], {})
    """
    syms = symbols(variables)
    var_map = dict(zip(variables, syms))
    eqs = []
    for eq in equations:
        sym_eq = sympify(eq, locals=var_map)
        for comp, val in component_values.items():
            sym_eq = sym_eq.subs(var_map.get(comp, comp), val)
        eqs.append(sym_eq)
    sol = solve(eqs, syms, dict=True)
    if not sol:
        return None

    formatted = []
    values = {}
    for var in variables:
        val = sol[0][var_map[var]]
        try:
            val_c = complex(val.evalf())
        except Exception:
            val_c = val
        values[var] = val_c
        mag, angle_rad = cmath.polar(val_c)
        angle_deg = math.degrees(angle_rad)
        formatted.append(f"{var}: ({mag:.4f}) ∠ ({angle_deg:.4f}°)")
        formatted.append(f"{var}: ({val_c.real:.4f}) + ({val_c.imag:.4f})j\n")
    return {"formatted": formatted, "values": values}
