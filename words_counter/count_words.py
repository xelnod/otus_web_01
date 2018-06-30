import os
import collections
import logging
import sys
import argparse

from path_tools import extract_function_names_from_path, get_verbs_from_function_name
from utils import flatten_list, remove_magic_names

DEFAULT_TOP_SIZE = 200

logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)
logger = logging.getLogger(str(__name__))

parser = argparse.ArgumentParser()
parser.add_argument('top_size', default=200, type=int, nargs='?',
                    help=f'number of top words to display. Defaults to {DEFAULT_TOP_SIZE}')

args = parser.parse_args()


def get_top_verbs_in_path(path, top_size=10):
    function_names = extract_function_names_from_path(path)
    logger.info(f'{len(function_names)} functions extracted')
    verbs = flatten_list([get_verbs_from_function_name(function_name) for function_name in function_names])
    return collections.Counter(verbs).most_common(top_size)


def get_top_functions_names_in_path(path, top_size=10):
    function_names = extract_function_names_from_path(path)
    function_names_nonmagic = remove_magic_names(function_names)
    return collections.Counter(function_names_nonmagic).most_common(top_size)


if __name__ == '__main__':

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

    logger.info(f'total {len(words)} words, {len(set(words))} unique')

    for word, occurence in collections.Counter(words).most_common(args.top_size):
        logger.info(word, occurence)
