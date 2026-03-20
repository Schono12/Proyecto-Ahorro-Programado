import unittest
import sys
sys.path.append("src")
from model import logica_ahorro

# Debe existir por lo menos una clase que contenga las pruebas unitarias
# descendiente de unittest.TestCase
class TestCalculoCuotaAhorro(unittest.TestCase):

    # Cada prueba unitaria es un metodo de la clase, cuyo nombre debe iniciar con "test"
    def test_normal_1(self):
        # ENTRADAS
        meta_ahorro = 10000000
        tasa_interes = 0.01
        plazo = 24
        abono_extra = 0
        mes_del_abono = None

        cuota_calculada = logica_ahorro.calcular_cuota(meta_ahorro, tasa_interes, plazo, abono_extra, mes_del_abono)

        # SALIDA ESPERADA
        cuota_esperada = 370734.72

        # Prueba que dos variables sean iguales
        self.assertAlmostEqual(cuota_calculada, cuota_esperada, 2)

    def test_normal_2(self):
        # ENTRADAS
        meta_ahorro = 5000000
        tasa_interes = 0.0075
        plazo = 12
        abono_extra = 0
        mes_del_abono = None

        cuota_calculada = logica_ahorro.calcular_cuota(meta_ahorro, tasa_interes, plazo, abono_extra, mes_del_abono)

        # SALIDA ESPERADA
        cuota_esperada = 399757.38

        # Prueba que dos variables sean iguales
        self.assertAlmostEqual(cuota_calculada, cuota_esperada, 2)

    def test_normal_3(self):
        # ENTRADAS
        meta_ahorro = 20000000
        tasa_interes = 0.0083
        plazo = 36
        abono_extra = 0
        mes_del_abono = None

        cuota_calculada = logica_ahorro.calcular_cuota(meta_ahorro, tasa_interes, plazo, abono_extra, mes_del_abono)

        # SALIDA ESPERADA
        cuota_esperada = 478968.21

        # Prueba que dos variables sean iguales
        self.assertAlmostEqual(cuota_calculada, cuota_esperada, 2)

    def test_tasa_cero(self):
        # ENTRADAS
        meta_ahorro = 10000000
        tasa_interes = 0
        plazo = 24
        abono_extra = 0
        mes_del_abono = None

        cuota_calculada = logica_ahorro.calcular_cuota(meta_ahorro, tasa_interes, plazo, abono_extra, mes_del_abono)

        # SALIDA ESPERADA
        cuota_esperada = 416666.67

        # Prueba que dos variables sean iguales redondeando a 2 decimales
        self.assertEqual(round(cuota_calculada, 2), cuota_esperada)

    def test_plazo_1_Mes(self):
        # ENTRADAS
        meta_ahorro = 500000
        tasa_interes = 0.01
        plazo = 1
        abono_extra = 0
        mes_del_abono = None

        cuota_calculada = logica_ahorro.calcular_cuota(meta_ahorro, tasa_interes, plazo, abono_extra, mes_del_abono)

        # SALIDA ESPERADA
        cuota_esperada = 500000

        # Prueba que dos variables sean iguales redondeando a 0 decimales
        self.assertEqual(round(cuota_calculada), cuota_esperada)

    def test_abono_extra(self):
        # ENTRADAS
        meta_ahorro = 10000000
        tasa_interes = 0.01
        plazo = 24
        abono_extra = 2000000
        mes_del_abono = 24

        cuota_calculada = logica_ahorro.calcular_cuota(meta_ahorro, tasa_interes, plazo, abono_extra, mes_del_abono)

        # SALIDA ESPERADA
        cuota_esperada = 296587.78

        # Prueba que dos variables sean iguales redondeando a 2 decimales
        self.assertAlmostEqual(cuota_calculada, cuota_esperada, 2)

    def test_abono_extra_doble(self):
        # ENTRADAS
        meta_ahorro = 20000000
        tasa_interes = 0.0083
        plazo = 36
        abono_extra = 5000000
        mes_del_abono = 36

        cuota_calculada = logica_ahorro.calcular_cuota(meta_ahorro, tasa_interes, plazo, abono_extra, mes_del_abono)

        # SALIDA ESPERADA
        cuota_esperada = 359226.16

        # Prueba que dos variables sean iguales redondeando a 2 decimales
        self.assertAlmostEqual(cuota_calculada, cuota_esperada, 2)

    def test_error_meta_cero(self):
        # ENTRADAS
        meta_ahorro = 0
        tasa_interes = 0.01
        plazo = 24
        abono_extra = 0
        mes_del_abono = None

        # Verifica que se genere una excepcion cuando la meta es cero
        with self.assertRaises(logica_ahorro.MetaInvalida):
            logica_ahorro.calcular_cuota(meta_ahorro, tasa_interes, plazo, abono_extra, mes_del_abono)

    def test_error_plazo_cero(self):
        # ENTRADAS
        meta_ahorro = 10000000
        tasa_interes = 0.01
        plazo = 0
        abono_extra = 0
        mes_del_abono = None

        # Verifica que se genere una excepcion cuando el plazo es cero
        with self.assertRaises(logica_ahorro.PlazoInvalido):
            logica_ahorro.calcular_cuota(meta_ahorro, tasa_interes, plazo, abono_extra, mes_del_abono)

    def test_tasa_negativa(self):
        # ENTRADAS
        meta_ahorro = 10000000
        tasa_interes = -0.02
        plazo = 24
        abono_extra = 1000000
        mes_del_abono = 9

        # Verifica que se genere una excepcion cuando la tasa es negativa
        with self.assertRaises(logica_ahorro.InteresInvalido):
            logica_ahorro.calcular_cuota(meta_ahorro, tasa_interes, plazo, abono_extra, mes_del_abono)

    def test_plazo_negativo(self):
        # ENTRADAS
        meta_ahorro = 20000000
        tasa_interes = 0.01
        plazo = -12
        abono_extra = 500000
        mes_del_abono = 2

        # Verifica que se genere una excepcion cuando el plazo es negativo
        with self.assertRaises(logica_ahorro.PlazoInvalido):
            logica_ahorro.calcular_cuota(meta_ahorro, tasa_interes, plazo, abono_extra, mes_del_abono)


# Este fragmento de codigo permite ejecutar la pruebas individualmente
# Va fijo en todas las pruebas unitarias
if __name__ == '__main__':
    unittest.main()
   
