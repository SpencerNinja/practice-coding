"""
Do Not Edit this file. You may and are encouraged to look at it for reference.
"""

import unittest
import isbn_index

class test_findBook( unittest.TestCase ):
    
    def setUp(self):
        return

    def tearDown(self):
        return
    
    def test001_findBookExists(self):
        self.assertTrue('findBook' in dir( isbn_index ),
                        'Function "findBook" is not defined, check your spelling')
        return
    
    def test002_findBookFindsExistingBook(self):
        isbn = "0000-00000000"
        title = "Book Title"
        expected = title
        
        index = isbn_index.createIndex( )
        isbn_index.recordBook( index, isbn, title )
        
        self.assertEqual( isbn_index.findBook( index, isbn ), expected )
        return

    def test003_findBookDoesNotFindMissingBook(self):
        isbn1 = "0000-00000000"
        isbn2 = "0000-12345678"
        title = "Book Title"
        expected = ""
        
        index = isbn_index.createIndex( )
        isbn_index.recordBook( index, isbn1, title )
        
        self.assertEqual( isbn_index.findBook( index, isbn2 ), expected )
        return



if __name__ == '__main__':
    unittest.main()
