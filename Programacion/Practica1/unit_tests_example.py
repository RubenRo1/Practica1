# Definir la función que queremos probar.

def add(x, y):
    return x + y

# Usar el módulo unittest, librería estándar para escribir y ejecutar tests.

import unittest

# Escribir un ejemplo de test para la función add

class TestAddFunction(unittest.TestCase):
    """Suite de tests para la función add"""

    def test_add(self):
        """Test básico"""
        #TODO: Prueba a cambiar la línea self.assertEqual(add(1, 2), 3)
        #a self.assertEqual(add(1, 2), 2) y ver qué ocurre al ejecutarla    

        self.assertEqual(add(1, 2), 3)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(-1, -1), -2)
    
    def test_add_positive_numbers(self):
        """Test suma de números positivos"""
        self.assertEqual(add(2, 3), 5)
    
    def test_add_negative_numbers(self):
        """Test suma de números negativos"""
        self.assertEqual(add(-5, -3), -8)
    
    def test_add_mixed_numbers(self):
        """Test suma de números positivos y negativos"""
        self.assertEqual(add(5, -3), 2)
        self.assertEqual(add(-5, 3), -2)
        self.assertEqual(add(10, -10), 0)
    
    def test_add_with_zero(self):
        """Test suma con cero"""
        self.assertEqual(add(0, 5), 5)
        self.assertEqual(add(5, 0), 5)
        self.assertEqual(add(0, 0), 0)
    
    def test_add_floats(self):
        """Test suma de números decimales"""
        self.assertAlmostEqual(add(2.5, 3.7), 6.2)
        self.assertAlmostEqual(add(0.1, 0.2), 0.3)
    
    def test_add_large_numbers(self):
        """Test suma de números grandes"""
        self.assertEqual(add(1000000, 2000000), 3000000)
        self.assertEqual(add(999999999, 1), 1000000000)


class TestAddEdgeCases(unittest.TestCase):
    """Tests de casos extremos"""
    
    def test_add_strings(self):
        """Test concatenación de strings (comportamiento de Python)"""
        self.assertEqual(add("Hello", "World"), "HelloWorld")
        self.assertEqual(add("3", "5"), "35")
    
    def test_add_lists(self):
        """Test concatenación de listas"""
        self.assertEqual(add([1, 2], [3, 4]), [1, 2, 3, 4])


def suite():
    """Crea una suite de tests."""
    loader = unittest.TestLoader()
    return unittest.TestSuite([
        loader.loadTestsFromTestCase(TestAddFunction),
        loader.loadTestsFromTestCase(TestAddEdgeCases)
    ])

if __name__ == '__main__':
    # Ejecutar tests con verbosidad
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite())