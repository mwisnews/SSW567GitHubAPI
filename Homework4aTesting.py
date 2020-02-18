import unittest
import Homework4a

class TestHomeworka(unittest.TestCase):

    def testWorkingUsername(self):
        self.assertEqual(Homework4a.getRepositories("mwisnews"), [['BusinessCardReader', 30], ['MWSSW567', 2], ['SSW567GitHubAPI', 3], ['TexasHoldem', 15], ['TriangleTestingAssignment2', 10], ['TriangleTestingClassification', 1], ['VentureHacks-Fintech', 30]])

if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()