from sympy import symbols, solve, sympify
import sympy as sp
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

def simplify(eqns, unknowns, values):
    """
    Take equations as strings, unknowns as strings, and values as a dict.
    Automates symbol creation, solves, substitutes, and simplifies.
    """
    # 1. Gather all unique variable names from equations and unknowns/values
    varnames = set()
    # from equations
    for eq in eqns:
        varnames.update([str(sym) for sym in sp.sympify(eq).free_symbols])
    # from unknowns & values
    varnames.update([str(u) for u in unknowns])
    varnames.update([str(k) for k in values.keys()])
    # 2. Create sympy symbols for all
    symbols = {name: sp.symbols(name) for name in varnames}
    # 3. Parse equations as sympy expressions, turning "=" into Eq
    parsed_eqns = []
    for eq in eqns:
        if "=" in eq:
            left, right = eq.split("=")
            parsed_eqns.append(sp.Eq(sp.sympify(left, locals=symbols), sp.sympify(right, locals=symbols)))
        else:
            parsed_eqns.append(sp.sympify(eq, locals=symbols))
    # 4. Build unknown symbols
    unknown_syms = [symbols[str(u)] for u in unknowns]
    # 5. Substitute values as sympy symbols
    sub_dict = {symbols[str(k)]: v for k, v in values.items()}
    # 6. Solve
    sol = sp.solve(parsed_eqns, unknown_syms, dict=True)
    if not sol:
        raise ValueError("No solution found!")
    sol = sol[0]
    # 7. Substitute and simplify
    results = []
    for var in unknowns:
        expr = sol[symbols[var]]
        expr_sub = expr.subs(sub_dict)
        expr_simp = sp.simplify(expr_sub)
        results.append(expr_simp)
    return tuple(results)
