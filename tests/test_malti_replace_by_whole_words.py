from unittest import TestCase
from multi_replace import multi_replace_by_whole_words as mrw

class test_multi_replace_by_whole_words(TestCase):
    def test_upper(self):
        s = 'WORD_STRING_WORDSTRING'
        adict = {
            'WORD':'w',
            'STRING':'str'
        }
        ans = 'w_str_WORDSTRING'
        self.assertEqual(mrw(adict)(s), ans)

