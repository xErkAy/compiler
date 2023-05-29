import json
from src.constants import BASE_DIR


class Wrapper:
    def __init__(self, arg):
        self.JSONParsedTree = arg


class Node:
    def __init__(self, arg_name, arg_children=None):
        self.text = arg_name
        self.children = [] if arg_children is None else arg_children


class ParsedTree:
    def __init__(self, root: Node):
        self.nodeStructure = root


def serialize(obj):
    try:
        if type(obj) == ParsedTree:
            return {'parsedTree': obj.nodeStructure}
        return {str(obj.text): obj.children}
    except AttributeError:
        return None


def write(root: Node, filename: str):
    data = json.dumps(ParsedTree(root), default=serialize)
    with open(f'{BASE_DIR.parent}/vtree-master/%s.json' % filename, 'w') as f:
        f.write(data)
