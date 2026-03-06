# Todas las prueba sunitarias importan la biblioteca unittest
import unittest
# Las pruebas importan los modulos que hacen el trabajo, en este caso el modulo logica_ahorro
import logica_ahorro

# Debe existir por lo menos una clase que contenga las pruebas unitarias
# descediente de unittest.TestCase
class TestCalculoCuotaAhorro(unittest.TestCase): 
   
    # Cada prueba unitaria es un metodo la clase, cuyo nombre debe iniciar con "test"
    def test_normal_1(self):
        # ENTRADAS
        meta = 10000000
        interes = 0.01
        plazo = 24 
        abono = 0
        mes_abono = None

        cuota_calculada = logica_ahorro.calcular_cuota(meta, interes, plazo, abono, mes_abono)

        #SALIDA ESPERADA
        cuota_esperada = 370734.72

        # Prueba que dos variables sean iguales
        self.assertAlmostEqual(cuota_calculada, cuota_esperada, 2)

    def test_normal_2(self):
        # ENTRADAS
        meta = 5000000
        interes = 0.0075
        plazo = 12
        abono = 0
        mes_abono = None

        
        cuota_calculada = logica_ahorro.calcular_cuota(meta, interes, plazo, abono, mes_abono)

        #SALIDA ESPERADA
        cuota_esperada = 399757.38

        # Prueba que dos variables sean iguales
        self.assertAlmostEqual(cuota_calculada, cuota_esperada, 2)

    def test_normal_3(self):
        # ENTRADAS
        meta = 20000000
        interes = 0.0083
        plazo = 36
        abono = 0
        mes_abono = None

        cuota_calculada = logica_ahorro.calcular_cuota(meta, interes, plazo, abono, mes_abono)

        #SALIDA ESPERADA
        cuota_esperada = 478968.21

        # Prueba que dos variables sean iguales
        self.assertAlmostEqual(cuota_calculada, cuota_esperada, 2)

    def testTasaCero(self):
        # ENTRADAS
        meta = 10000000
        interes = 0
        plazo = 24
        abono = 0
        mes_abono = None

        cuota_calculada = logica_ahorro.calcular_cuota(meta, interes, plazo, abono, mes_abono)

        # SALIDA ESPERADA
        cuota_esperada = 416666.67

        # Prueba que dos variables sean iguales redondeando a 2 decimales
        self.assertEqual(round(cuota_calculada, 2), cuota_esperada)

    def testPlazo1Mes(self):
        # ENTRADAS
        meta = 500000
        interes = 0.01
        plazo = 1
        abono = 0
        mes_abono = None

        cuota_calculada = logica_ahorro.calcular_cuota(meta, interes, plazo, abono, mes_abono)

        # SALIDA ESPERADA
        cuota_esperada = 500000

        # Prueba que dos variables sean iguales redondeando a 0 decimales
        self.assertEqual(round(cuota_calculada), cuota_esperada)

    def testAbonoExtra(self):
        # ENTRADAS
        meta = 10000000
        interes = 0.01
        plazo = 24
        abono = 2000000
        mes_abono = 24

        cuota_calculada = logica_ahorro.calcular_cuota(meta, interes, plazo, abono, mes_abono)

        # SALIDA ESPERADA
        cuota_esperada = 296587.78

        # Prueba que dos variables sean iguales redondeando a 2 decimales
        self.assertAlmostEqual(cuota_calculada, cuota_esperada, 2)

    def testAbonoExtra2(self):
        # ENTRADAS
        meta = 20000000
        interes = 0.0083
        plazo = 36
        abono = 5000000 
        mes_abono = 36

        cuota_calculada = logica_ahorro.calcular_cuota(meta, interes, plazo, abono, mes_abono)

        # SALIDA ESPERADA
        cuota_esperada = 359226.16

        # Prueba que dos variables sean iguales redondeando a 2 decimales
        self.assertAlmostEqual(cuota_calculada, cuota_esperada, 2)

    def testErrorMetaCero(self):
        # ENTRADAS
        meta = 0
        interes = 0.01
        plazo = 24
        abono = 0
        mes_abono = None

        # Verifica que se genere una excepcion cuando la meta es cero
        with self.assertRaises(logica_ahorro.MetaInvalida):
            logica_ahorro.calcular_cuota(meta, interes, plazo, abono, mes_abono)

    def testErrorPlazoCero(self):
        # ENTRADAS
        meta = 10000000
        interes = 0.01
        plazo = 0
        abono = 0
        mes_abono = None

        # Verifica que se genere una excepcion cuando el plazo es cero
        with self.assertRaises(logica_ahorro.PlazoInvalido):
            logica_ahorro.calcular_cuota(meta, interes, plazo, abono, mes_abono)


    def testTasaNegativa(self):
        # ENTRADAS
        meta = 10000000
        interes = -0.02
        plazo = 24
        abono = 1000000
        mes_abono = 9

        # Verifica que se genere una excepcion cuando la tasa es negativa
        with self.assertRaises(logica_ahorro.InteresInvalido):
            logica_ahorro.calcular_cuota(meta, interes, plazo, abono, mes_abono)

    def testPlazoNegativo(self):
        # ENTRADAS
        meta = 20000000
        interes = 0.01
        plazo = -12
        abono = 500000
        mes_abono = 2

        # Verifica que se genere una excepcion cuando el plazo es negativo
        with self.assertRaises(logica_ahorro.PlazoInvalido):
            logica_ahorro.calcular_cuota(meta, interes, plazo, abono, mes_abono)

# Este fragmento de codigo permite ejecutar la prueb individualmente
# Va fijo en todas las pruebas unitarias
if __name__ == '__main__':
    # print( Payment.calcularCuota.__doc__)
    unittest.main()