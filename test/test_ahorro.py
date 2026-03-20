import unittest
# Las pruebas importan los modulos que hacen el trabajo
import sys
sys.path.append("src")
# Todas las pruebas unitarias importan la biblioteca unittest
from model import logica_ahorro

# Debe existir por lo menos una clase que contenga las pruebas unitarias
# descendiente de unittest.TestCase
class TestCalculoCuotaAhorro(unittest.TestCase):

    # Cada prueba unitaria es un metodo de la clase, cuyo nombre debe iniciar con "test"
    def test_normal_1(self):
        # Cada metodo de prueba debe llamar un metodo assert
        # para comprobar si la prueba pasa
        meta_ahorro = 10000000
        tasa_interes = 0.01
        plazo = 24
        abono_extra = 0
        mes_del_abono = None

        cuota_calculada = logica_ahorro.calcular_cuota(meta_ahorro, tasa_interes, plazo, abono_extra, mes_del_abono)

        cuota_esperada = 370734.72

        self.assertAlmostEqual(cuota_calculada, cuota_esperada, 2)

    def test_normal_2(self):
       
        meta_ahorro = 5000000
        tasa_interes = 0.0075
        plazo = 12
        abono_extra = 0
        mes_del_abono = None

        cuota_calculada = logica_ahorro.calcular_cuota(meta_ahorro, tasa_interes, plazo, abono_extra, mes_del_abono)

      
        cuota_esperada = 399757.38

        self.assertAlmostEqual(cuota_calculada, cuota_esperada, 2)

    def test_normal_3(self):
        
        meta_ahorro = 20000000
        tasa_interes = 0.0083
        plazo = 36
        abono_extra = 0
        mes_del_abono = None

        cuota_calculada = logica_ahorro.calcular_cuota(meta_ahorro, tasa_interes, plazo, abono_extra, mes_del_abono)

       
        cuota_esperada = 478968.21

        
        self.assertAlmostEqual(cuota_calculada, cuota_esperada, 2)

    def test_tasa_cero(self):
        
        meta_ahorro = 10000000
        tasa_interes = 0
        plazo = 24
        abono_extra = 0
        mes_del_abono = None

        cuota_calculada = logica_ahorro.calcular_cuota(meta_ahorro, tasa_interes, plazo, abono_extra, mes_del_abono)

       
        cuota_esperada = 416666.67

       
        self.assertEqual(round(cuota_calculada, 2), cuota_esperada)

    def test_plazo_1_Mes(self):
        
        meta_ahorro = 500000
        tasa_interes = 0.01
        plazo = 1
        abono_extra = 0
        mes_del_abono = None

        cuota_calculada = logica_ahorro.calcular_cuota(meta_ahorro, tasa_interes, plazo, abono_extra, mes_del_abono)

        cuota_esperada = 500000

        
        self.assertEqual(round(cuota_calculada), cuota_esperada)

    def test_abono_extra(self):
       
        meta_ahorro = 10000000
        tasa_interes = 0.01
        plazo = 24
        abono_extra = 2000000
        mes_del_abono = 24

        cuota_calculada = logica_ahorro.calcular_cuota(meta_ahorro, tasa_interes, plazo, abono_extra, mes_del_abono)

        cuota_esperada = 296587.78

        self.assertAlmostEqual(cuota_calculada, cuota_esperada, 2)

    def test_abono_extra_doble(self):
     
        meta_ahorro = 20000000
        tasa_interes = 0.0083
        plazo = 36
        abono_extra = 5000000
        mes_del_abono = 36

        cuota_calculada = logica_ahorro.calcular_cuota(meta_ahorro, tasa_interes, plazo, abono_extra, mes_del_abono)

        cuota_esperada = 359226.16

 
        self.assertAlmostEqual(cuota_calculada, cuota_esperada, 2)

    def test_error_meta_cero(self):
       
        meta_ahorro = 0
        tasa_interes = 0.01
        plazo = 24
        abono_extra = 0
        mes_del_abono = None

        with self.assertRaises(logica_ahorro.MetaInvalida):
            logica_ahorro.calcular_cuota(meta_ahorro, tasa_interes, plazo, abono_extra, mes_del_abono)

    def test_error_plazo_cero(self):
       
        meta_ahorro = 10000000
        tasa_interes = 0.01
        plazo = 0
        abono_extra = 0
        mes_del_abono = None

        with self.assertRaises(logica_ahorro.PlazoInvalido):
            logica_ahorro.calcular_cuota(meta_ahorro, tasa_interes, plazo, abono_extra, mes_del_abono)

    def test_tasa_negativa(self):

        meta_ahorro = 10000000
        tasa_interes = -0.02
        plazo = 24
        abono_extra = 1000000
        mes_del_abono = 9

        # Para controlar que una funcion si genere una excepcion
        # en el caso de prueba, se usa el metodo assertRaises
        # el primer parametro es la Excepcion esperada
        # el segundo es el metodo que se va a invocar
        # y los demas parametros son los parametros del metodo bajo prueba

  
        with self.assertRaises(logica_ahorro.InteresInvalido):
            logica_ahorro.calcular_cuota(meta_ahorro, tasa_interes, plazo, abono_extra, mes_del_abono)

    def test_plazo_negativo(self):
    
        meta_ahorro = 20000000
        tasa_interes = 0.01
        plazo = -12
        abono_extra = 500000
        mes_del_abono = 2

   
        with self.assertRaises(logica_ahorro.PlazoInvalido):
            logica_ahorro.calcular_cuota(meta_ahorro, tasa_interes, plazo, abono_extra, mes_del_abono)


# Este fragmento de codigo permite ejecutar la pruebas individualmente
# Va fijo en todas las pruebas unitarias
if __name__ == '__main__':
    unittest.main()
   
