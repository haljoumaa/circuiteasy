import sympy as sp

def laplace_transform_of(expr):
    """
    Compute the Laplace transform of an expression of t (symbolic or as string).
    Args:
        expr: Expression in time domain (as SymPy or string, using 't').
    Returns:
        Laplace transform as string (in 's' domain).
    Raises:
        ValueError or RuntimeError on bad input or failure.
    """
    t, s = sp.symbols('t s')

    if isinstance(expr, str):
        try:
            expr = sp.sympify(expr)
        except sp.SympifyError:
            raise ValueError("Input expression could not be parsed.")

    allowed_vars = {t}
    expr_vars = expr.free_symbols
    if not expr_vars.issubset(allowed_vars):
        raise ValueError(f"Unsupported variables present: {expr_vars - allowed_vars}")

    try:
        L = sp.laplace_transform(expr, t, s, noconds=True)
    except Exception as e:
        raise RuntimeError(f"Laplace transform calculation failed: {e}")

    return str(L)

def inverse_laplace_transform_of(expr):
    """
    Compute the inverse Laplace transform of an expression of s (symbolic or as string).
    Args:
        expr: Expression in s-domain (as SymPy or string, using 's').
    Returns:
        Inverse Laplace transform as string (in 't' domain).
    Raises:
        ValueError or RuntimeError on bad input or failure.
    """
    t, s = sp.symbols('t s')

    if isinstance(expr, str):
        try:
            expr = sp.sympify(expr)
        except sp.SympifyError:
            raise ValueError("Input expression could not be parsed.")

    allowed_vars = {s}
    expr_vars = expr.free_symbols
    if not expr_vars.issubset(allowed_vars):
        raise ValueError(f"Unsupported variables present: {expr_vars - allowed_vars}")

    try:
        inv_L = sp.inverse_laplace_transform(expr, s, t)
    except Exception as e:
        raise RuntimeError(f"Inverse Laplace transform calculation failed: {e}")

    return str(inv_L)
