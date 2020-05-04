
def is_empty_tree(tree):
    return isinstance(tree, list) and not tree


def is_leaf(tree):
    return isinstance(tree, int)


def left_subtree(tree):
    return tree[0]


def right_subtree(tree):
    return tree[2]


def empty_tree_fn():
    return 0


def leaf_fn(key):
    return key**2


def inner_node_fn(key, left_value, right_value):
    return key + left_value


def key_value(tree):
    """Returns the key value of given tree"""
    return tree[1]


# Del uppgift 1
def traverse(tree, inner_node, leaf, empty_tree):
    """Runs given inner node, leaf and empty tree functions on given tree"""
    if is_empty_tree(tree):
        return empty_tree()
    elif is_leaf(tree):
        return leaf(tree)
    else:
        left = traverse(left_subtree(tree), inner_node, leaf, empty_tree)
        rgt = traverse(right_subtree(tree), inner_node, leaf, empty_tree)
        return inner_node(key_value(tree), left, rgt)


# Del uppgift 2
def set_key(key):
    """
    Creates a inner function, checks if given key is equal to any of the
    inner functions arguments, returns the key value or False
    """
    def inner_node_2(node_key, left, right):
        if node_key == key or left == key or right == key:
            return key
        return False
    return inner_node_2


def leaf_2(key):
    """Returns the key value of the leaf"""
    return key


def empty_tree_2():
    """Returns false"""
    return False


def contains_key(key, tree):
    """Checks if given tree contains the given key, return True or False"""
    inner_node = set_key(key)
    return key == traverse(tree, inner_node, leaf_2, empty_tree_2)


# Del uppgift 3
def inner_node_3(key, left, right):
    """Returns left + right + 1"""
    return left + right + 1


def leaf_3(key):
    """Returns 1"""
    return 1


def empty_3():
    """Returns 0"""
    return 0


def tree_size(tree):
    """Returns the number of nodes in the tree"""
    return traverse(tree, inner_node_3, leaf_3, empty_3)


# Del uppgift 4
def inner_node_4(key, left, right):
    """Returns the depth of the deepest subtree"""
    if left > right:
        return left + 1
    else:
        return right + 1


def leaf_4(key):
    """Returns 1"""
    return 1


def empty_4():
    """Returns 0"""
    return 0


def tree_depth(tree):
    """Returns the depth of given tree"""
    return traverse(tree, inner_node_4, leaf_4, empty_4)
