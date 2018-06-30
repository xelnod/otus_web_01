from nltk import pos_tag

VERB_TAGS = ('VB', 'VBD', 'VBG', 'VBN', 'VBP', 'VBZ')


def flatten_list(_list):
    """ [(1,2), (3,4)] -> [1, 2, 3, 4]"""
    return sum([list(item) for item in _list], [])


def is_verb(_word):
    if not _word:
        return False
    pos_info = pos_tag([_word])
    return pos_info[0][1] in VERB_TAGS


def remove_magic(names_list):
    return [name for name in names_list if not(name.startswith('__') and name.endswith('__'))]
