import re

class multi_replace:
    """
    To replace multi words
    """
    def __init__(self, *args, **kwds):
        self.adict = dict(*args, **kwds)
        self.rx = self.make_rx()
    def make_rx(self):
        return re.compile(r'|'.join(map(re.escape, self.adict)))
    def one_dict(self, match):
        return self.adict[match.group(0)]
    def __call__(self, text):
        return self.rx.sub(self.one_dict, text)

class multi_replace_by_whole_words(multi_replace):
    """
    To replace multi words by whole words
    'whole words' is defined as below:
     - When the first char is Upper case, the proceded char shall be Lower case, else Upper case.
     - When the last char is Upper case, the next char shall be Lower case, else Upper case.
    """
    def make_rx(self):
        return re.compile('|'.join(map(self.get_pattern, self.adict)))
    def get_pattern(self, key):
        pattern = re.escape(key)
        if key[0].islower():
            pattern = r'(?<![a-z])%s' % (pattern)
        else:
            pattern = r'(?<![A-Z])%s' % (pattern)
        if key[-1].islower():
            pattern = r'%s(?![a-z])' % (pattern)
        else:
            pattern = r'%s(?![A-Z])' % (pattern)
        return pattern

if __name__ == "__main__":
    adict = {
        'This':'That',
        'this':'that',
        'is':'was',
        'am':'was',
        'whole':'entire',
        'word':'string'
    }
    s = 'This is sample code for this "multi_replace_by_whole_words".'
    mrw = multi_replace_by_whole_words(adict)
    print mrw(s) # print replaced string
