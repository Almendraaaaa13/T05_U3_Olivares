"""Referencia analítica y error entre nodos."""
import numpy as np


def desplazamiento_referencia(x, L, E, A, P, q):
    """Devuelve el desplazamiento analítico en mm."""
    x = np.asarray(x, dtype=float)
    return ((P + q * L) * x - q * x**2 / 2) / (E * A)


def error_puntos_medios(resultado, L, E, A, P, q):
    """Devuelve el máximo error absoluto en puntos medios, en mm."""

    # Coordenada del punto medio de cada elemento.
    x_medios = (resultado.x[:-1] + resultado.x[1:]) / 2

    # Desplazamiento MEF interpolado en cada punto medio.
    u_mef = (resultado.u[:-1] + resultado.u[1:]) / 2

    # Desplazamiento analítico en los mismos puntos.
    u_ref = desplazamiento_referencia(
        x_medios, L, E, A, P, q
    )

    return float(np.max(np.abs(u_mef - u_ref)))
