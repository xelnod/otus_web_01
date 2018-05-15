import os
import collections

from path_tools import extract_function_names_from_path, get_verbs_from_function_name
from utils import flatten_list, remove_magic


def get_top_verbs_in_path(path, top_size=10):
    function_names = extract_function_names_from_path(path)
    print('%s functions extracted' % len(function_names))
    verbs = flatten_list([get_verbs_from_function_name(function_name) for function_name in function_names])
    return collections.Counter(verbs).most_common(top_size)


def get_top_functions_names_in_path(path, top_size=10):
    function_names = extract_function_names_from_path(path)
    function_names_nonmagic = remove_magic(function_names)
    return collections.Counter(function_names_nonmagic).most_common(top_size)


words = []
projects = [
    'django',
    'flask',
    'pyramid',
    'reddit',
    'requests',
    'sqlalchemy',
]

for project in projects:
    path = os.path.join('.', project)
    words += get_top_verbs_in_path(path)

top_size = 200

print('total %s words, %s unique' % (len(words), len(set(words))))

for word, occurence in collections.Counter(words).most_common(top_size):
    print(word, occurence)
