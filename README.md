# Resolución de mallas por ley de Kirchhoff (2 incógnitas)

Plantea el sistema de dos mallas de un circuito de fuentes y resistencias, lo resuelve por determinantes e imprime ecuaciones, corrientes y comprobación de la ley en cada lazo.

`electronica` · 2026-10-29

## Instalación

```bash
python3 --version   # 3.10 o superior
# sin dependencias: sólo biblioteca estándar
```

## Uso

```bash
python3 mallas_kirchhoff.py --demo
python3 mallas_kirchhoff.py --v1 9 --r1 100 --r2 100 --r3 100
```

Salida real de una corrida de ejemplo:

```text
malla 1: (r1+r2)·i1 - r2·i2 = 12
malla 2: -r2·i1 + (r2+r3)·i2 = 0
i1=51.724 mA  i2=20.690 mA
kirchhoff=ok
```

## Cómo probar

```bash
python3 -m unittest discover -s tests -v
```

## Estructura

```text
2026-10-29-mallas-kirchhoff/
├── .github/
│   └── workflows/
│       └── ci-python.yml
├── .gitignore
├── LICENSE
├── mallas_kirchhoff.py
└── tests/
    └── test_mallas_kirchhoff.py
```

## Licencia

Distribuido bajo la licencia MIT.
