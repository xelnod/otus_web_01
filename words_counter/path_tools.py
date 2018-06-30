import os
import ast
import logging

from utils import flatten_list, remove_magic, is_verb


logger = logging.getLogger(str(__name__))


def get_py_filenames_from_path(_path):
    filenames = []
    for dirname, dirs, files in os.walk(_path, topdown=True):
        filenames += [os.path.join(dirname, file) for file in files if file.endswith('.py')]
    return filenames


def get_trees(_path):
    logger.info(_path)
    filenames = get_py_filenames_from_path(_path)
    trees = []
    logger.info(f'total {len(filenames)} files')
    for filename in filenames:
        with open(filename, 'r', encoding='utf-8') as attempt_handler:
            main_file_content = attempt_handler.read()
        try:
            tree = ast.parse(main_file_content)
        except SyntaxError as e:
            print(e)
            tree = None
        trees.append(tree)
    logger.info(f'{len(trees)} trees generated')
    return [t for t in trees if t]


def get_all_words_in_path(path):
    trees = get_trees(path)
    word_list = flatten_list([get_all_names(t) for t in trees])
    word_names = remove_magic(word_list)

    def split_snake_case_name_to_words(name):
        return [n for n in name.split('_') if n]
    return flatten_list([split_snake_case_name_to_words(word_name) for word_name in word_names])


def get_all_names(tree):
    return [node.id for node in ast.walk(tree) if isinstance(node, ast.Name)]


def get_verbs_from_function_name(function_name):
    return [word for word in function_name.split('_') if is_verb(word)]


def extract_function_names_from_path(path):
    trees = get_trees(path)
    funcs = []
    for tree in trees:
        funcs += [node.name.lower() for node in ast.walk(tree) if isinstance(node, ast.FunctionDef)]
    return remove_magic(funcs)
