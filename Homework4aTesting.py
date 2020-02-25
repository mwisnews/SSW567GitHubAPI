import unittest
from nose.tools import assert_true
import requests
from Homework4a import getRepositories

class TestHomeworka(unittest.TestCase):

    #def testWorkingUsernameA(self):
        #self.assertEqual(Homework4a.getRepositories("mwisnews"), [['BusinessCardReader', 30], ['MWSSW567', 2], ['SSW567GitHubAPI', 16], ['TexasHoldem', 15], ['TriangleTestingAssignment2', 10], ['TriangleTestingClassification', 1], ['VentureHacks-Fintech', 30]])

   # def testWorkingUsernameB(self):
    #    response = requests.get('')
    def testWorkingUsernameB(self):
        self.assertEqual(getRepositories("richkempinski"), [['hellogitworld', 30], ['helloworld', 6], ['Mocks', 10], ['Project1', 2], ['threads-of-life', 1]])

    def testInvalidInputA(self):
        self.assertEqual(getRepositories(True), "Username must be entered as a string")
    
    def testInvalidInputB(self):
        self.assertEqual(getRepositories(77), "Username must be entered as a string")

if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()
