import unittest

from WordPathKeeperFile import WordPathKeeper

class MyTestCase(unittest.TestCase):

    def test_1_num_mismatched(self):
        my_WPK = WordPathKeeper()
        self.assertTrue(my_WPK.num_mismatched_letters("goods", "golds")==1)
        self.assertTrue(my_WPK.num_mismatched_letters("a", " ") == 1)
        #self.assertRaises(AssertionError, my_WPK.num_mismatched_letters, "a", "a ")
        with self.assertRaises(AssertionError,):
            my_WPK.num_mismatched_letters("a", "a ")
            my_WPK.num_mismatched_letters("a ", "a")

        self.assertTrue(my_WPK.num_mismatched_letters("coulda shoulda woulda", "woulda shoulda coulda")==2)
        print("here")
    def test_2_build_edges(self):
        print("here")
        my_WPK = WordPathKeeper()
        my_WPK.load_words_from_file("Four_letters_nodes_subset.txt")
        self.assertEqual(my_WPK.build_edges(), 25)
        self.assertTrue(my_WPK.edges.__contains__([14, 15]))
        self.assertFalse(my_WPK.edges.__contains__([16, 19]))
        print("here")
        my_WPK = WordPathKeeper()
        my_WPK.load_words_from_file("Four_letters_nodes.txt")
        self.assertEqual(my_WPK.build_edges(), 19384)
        self.assertTrue(my_WPK.edges.__contains__([6, 7]))
        self.assertFalse(my_WPK.edges.__contains__([0, 3]))

    def test_3_get_neighbors(self):
        my_WPK = WordPathKeeper()
        my_WPK.load_words_from_file("Four_letters_nodes_subset.txt")
        my_WPK.build_edges()
        self.assertEqual(len(my_WPK.get_neighbors(0)), 4)
        self.assertEqual(len(my_WPK.get_neighbors(9)), 3)
        self.assertEqual(len(my_WPK.get_neighbors(18)), 4)
        my_WPK = WordPathKeeper()
        my_WPK.load_words_from_file("Four_letters_nodes.txt")
        my_WPK.build_edges()
        self.assertEqual(len(my_WPK.get_neighbors(284)), 26)
        self.assertEqual(len(my_WPK.get_neighbors(282)), 14)
        self.assertEqual(len(my_WPK.get_neighbors(353)), 27)
        self.assertEqual(len(my_WPK.get_neighbors(17)), 4)
        self.assertEqual(len(my_WPK.get_neighbors(3681)), 7)
        self.assertTrue(7 in my_WPK.get_neighbors(6))
        self.assertTrue(2464 in my_WPK.get_neighbors(2465))
        self.assertTrue(2465 in my_WPK.get_neighbors(2464))
        # TODO: you should write this test!
        # Here are a few things to try: search for the neighbors of a word near the start of your list of words, from
        #      the end of the list, and in the middle.

        # Note: for the subset, 'bins" should have 4 neighbors, 'bind' should have 3, and 'bots' should have 4
        # Note: for the full set of four-letter words, 'bins" should have 26 neighbors, 'bind' should have 14, and 'bots' should have 27
        # Note: for the full set of four-letter words, 'acid' should have 4 neighbors, and 'zoom' should have 7 neighbors.

        # You might also wish to hand check that the neighbors really are neighbors of the source words!

if __name__ == '__main__':
    unittest.main()
