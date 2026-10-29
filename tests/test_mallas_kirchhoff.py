import pathlib
import sys
import unittest

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
import mallas_kirchhoff as m


class Mallas(unittest.TestCase):
    def test_caso_conocido(self):
        # 12 V con r1=100 en serie y r2=220 en paralelo con r3=330: la
        # resistencia total es 100 + 220·330/550 = 232 Ω, así que i1 = 12/232
        # y por el divisor de corriente i2 = i1·r2/(r2+r3)
        total = 100.0 + 220.0 * 330.0 / (220.0 + 330.0)
        i1, i2 = m.resolver_mallas(12.0, 100.0, 220.0, 330.0)
        self.assertAlmostEqual(i1, 12.0 / total, places=12)
        self.assertAlmostEqual(i2, (12.0 / total) * 220.0 / 550.0, places=12)
        self.assertAlmostEqual(i1, 0.0517241379310345, places=12)
        self.assertAlmostEqual(i2, 0.0206896551724138, places=12)

    def test_kirchhoff_en_ambos_lazos(self):
        for v1, r1, r2, r3 in ((12, 100, 220, 330), (5, 10, 10, 10), (24, 470, 47, 100)):
            with self.subTest(v1=v1):
                i1, i2 = m.resolver_mallas(v1, r1, r2, r3)
                self.assertTrue(m.comprobar(v1, r1, r2, r3, i1, i2))

    def test_caidas_suman_la_fuente(self):
        i1, i2 = m.resolver_mallas(9.0, 100.0, 100.0, 100.0)
        v = m.caidas(i1, i2, 100.0, 100.0, 100.0)
        self.assertAlmostEqual(v["r1"] + v["r2"], 9.0, places=9)

    def test_entradas_invalidas(self):
        with self.assertRaises(ValueError):
            m.resolver_mallas(12.0, 0.0, 220.0, 330.0)


if __name__ == "__main__":
    unittest.main()
