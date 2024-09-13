# tests/test_services.py - Unit tests for the file copying service

import unittest
from file_copy_app.services import FileCopyService
from file_copy_app.config import AppConfig
import os

class TestFileCopyService(unittest.TestCase):
    def setUp(self):
        """Set up test environment."""
        self.config = AppConfig("/path/to/source", "/path/to/destination", 60)
        self.service = FileCopyService(self.config)

    def test_copy_file(self):
        """Test if the file copying works."""
        # Create test directories and files (in real case, use mock or temp directories)
        src_file = "/path/to/source/test.txt"
        with open(src_file, 'w') as f:
            f.write("Test file content")

        self.service.copy_file(src_file, "/path/to/source", "test.txt")
        dest_file = "/path/to/destination/test.txt"
        self.assertTrue(os.path.exists(dest_file))
        
        # Clean up
        os.remove(src_file)
        os.remove(dest_file)

if __name__ == "__main__":
    unittest.main()
