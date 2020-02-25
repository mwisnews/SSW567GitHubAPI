import unittest
from unittest import mock
import requests
from Homework4a import getRepositories

class TestHomeworka(unittest.TestCase):

    @mock.patch('Homework4a.getRepositories')
    
    def testWorkingUsername(self, mock_getRepositories):
        mock_getRepositories.return_value.status_code = [['hellogitworld', 30], ['helloworld', 6], ['Mocks', 10], ['Project1', 2], ['threads-of-life', 1]]
        self.assertEqual(getRepositories("richkempinski"), [['hellogitworld', 30], ['helloworld', 6], ['Mocks', 10], ['Project1', 2], ['threads-of-life', 1]])

    def testInvalidInputA(self):
        self.assertEqual(getRepositories(True), "Username must be entered as a string")
    
    def testInvalidInputB(self):
        self.assertEqual(getRepositories(77), "Username must be entered as a string")

if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()
