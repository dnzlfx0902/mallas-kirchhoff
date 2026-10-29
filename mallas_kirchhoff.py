"""Resolución de mallas por ley de Kirchhoff (2 incógnitas).

Plantea el sistema de dos mallas de un circuito de fuentes y resistencias, lo resuelve por determinantes e imprime ecuaciones, corrientes y comprobación de la ley en cada lazo.
"""
from __future__ import annotations


def resolver_mallas(v1, r1, r2, r3):
    """Resuelve las dos mallas de un circuito con fuente v1 y tres resistencias.

    Malla 1: (r1 + r2)·i1 - r2·i2 = v1
    Malla 2: -r2·i1 + (r2 + r3)·i2 = 0
    """
    if min(v1, r1, r2, r3) <= 0:
        raise ValueError("todas las magnitudes deben ser positivas")
    a11, a12 = r1 + r2, -r2
    a21, a22 = -r2, r2 + r3
    det = a11 * a22 - a12 * a21
    if abs(det) < 1e-12:
        raise ValueError("sistema indeterminado: determinante nulo")
    i1 = (v1 * a22 - a12 * 0) / det
    i2 = (a11 * 0 - v1 * a21) / det
    return i1, i2


def comprobar(v1, r1, r2, r3, i1, i2, tol=1e-9):
    """Comprueba la ley de Kirchhoff en cada lazo con las corrientes dadas."""
    malla1 = (r1 + r2) * i1 - r2 * i2
    malla2 = -r2 * i1 + (r2 + r3) * i2
    return abs(malla1 - v1) < tol and abs(malla2) < tol


def caidas(i1, i2, r1, r2, r3):
    """Tensión en cada resistencia a partir de las corrientes de malla."""
    return {"r1": i1 * r1, "r2": (i1 - i2) * r2, "r3": i2 * r3}


def main(argv=None):
    import argparse
    p = argparse.ArgumentParser(description="Resolución de mallas por ley de Kirchhoff (2 incógnitas)")
    p.add_argument("--v1", type=float, default=12.0)
    p.add_argument("--r1", type=float, default=100.0)
    p.add_argument("--r2", type=float, default=220.0)
    p.add_argument("--r3", type=float, default=330.0)
    p.add_argument("--demo", action="store_true")
    a = p.parse_args(argv)
    if not a.demo and argv is None:
        p.print_help()
        return 0
    i1, i2 = resolver_mallas(a.v1, a.r1, a.r2, a.r3)
    print(f"malla 1: (r1+r2)·i1 - r2·i2 = {a.v1:g}")
    print(f"malla 2: -r2·i1 + (r2+r3)·i2 = 0")
    print(f"i1={i1 * 1000:.3f} mA  i2={i2 * 1000:.3f} mA")
    print(f"kirchhoff={'ok' if comprobar(a.v1, a.r1, a.r2, a.r3, i1, i2) else 'falla'}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
