import unittest
from FileProcessing import FileProcess
from os import path
from config import in_directory, out_directory

file = FileProcess()

class TestFileProcessing(unittest.TestCase):
    def test_fileCreation(self):
        createdFile = file.createInFile(['DLA.ZIP'])
        path_to_file = path.join(path.abspath(in_directory), path.basename(createdFile))
        self.assertTrue(path.isfile(path_to_file))

    def test_fileDeletion(self):
        createdFile = file.createInFile(['DLA.ZIP'])
        path_to_file = path.join(path.abspath(in_directory), path.basename(createdFile))
        self.assertTrue(path.isfile(path_to_file))
        file.deleteFile(in_directory, createdFile)
        self.assertFalse(path.isfile(path_to_file))

    def test_moveFile(self):
        createdFile = file.createInFile(['DLA.ENCODE'])
        path_to_file = path.join(path.abspath(in_directory), path.basename(createdFile))
        self.assertTrue(path.isfile(path_to_file))
        file.moveFile(createdFile, in_directory, out_directory)
        self.assertFalse(path.isfile(path_to_file))
        self.assertTrue(path.isfile(path_to_file))

if __name__ == "__main__":
    unittest.main()
