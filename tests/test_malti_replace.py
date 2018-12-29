from unittest import TestCase
from multi_replace import multi_replace as mr

class test_multi_replace(TestCase):
    def test_upper(self):
        s = 'WORD_STRING_WORDSTRING'
        adict = {
            'WORD':'w',
            'STRING':'str',
            'OR':'AND'
        }
        ans = 'w_str_wstr'
        self.assertEqual(mr(adict)(s), ans)
