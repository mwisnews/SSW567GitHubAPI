import unittest
import Homework4a

class TestHomeworka(unittest.TestCase):

    def testWorkingUsernameA(self):
        self.assertEqual(Homework4a.getRepositories("mwisnews"), [['BusinessCardReader', 30], ['MWSSW567', 2], ['SSW567GitHubAPI', 12], ['TexasHoldem', 15], ['TriangleTestingAssignment2', 10], ['TriangleTestingClassification', 1], ['VentureHacks-Fintech', 30]])

    def testWorkingUsernameB(self):
        self.assertEqual(Homework4a.getRepositories("richkempinski"), [['hellogitworld', 30], ['helloworld', 6], ['Mocks', 10], ['Project1', 2], ['threads-of-life', 1]])

    def testInvalidInputA(self):
        self.assertEqual(Homework4a.getRepositories(True), "Username must be entered as a string")
    
    def testInvalidInputB(self):
        self.assertEqual(Homework4a.getRepositories(77), "Username must be entered as a string")

if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()
