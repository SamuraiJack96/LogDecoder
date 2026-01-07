# test_logdecoder.py
"""
Tests for LogDecoder module.
"""

import unittest
from logdecoder import LogDecoder

class TestLogDecoder(unittest.TestCase):
    """Test cases for LogDecoder class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = LogDecoder()
        self.assertIsInstance(instance, LogDecoder)
        
    def test_run_method(self):
        """Test the run method."""
        instance = LogDecoder()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
