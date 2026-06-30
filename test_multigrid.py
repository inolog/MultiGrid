# test_multigrid.py
"""
Tests for MultiGrid module.
"""

import unittest
from multigrid import MultiGrid

class TestMultiGrid(unittest.TestCase):
    """Test cases for MultiGrid class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = MultiGrid()
        self.assertIsInstance(instance, MultiGrid)
        
    def test_run_method(self):
        """Test the run method."""
        instance = MultiGrid()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
