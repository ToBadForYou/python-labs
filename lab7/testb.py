import lab7b


def tests():
    test_traverse()
    test_contains_key()
    test_tree_size()
    test_tree_depth()
    print("Passed all tests")


def test_traverse():
    assert lab7b.traverse([[1, 3, []], 5, [6, 7, 8]], lab7b.inner_node_fn,
                          lab7b.leaf_fn, lab7b.empty_tree_fn) == 9
    assert lab7b.traverse([[5, 6, []], 2, [7, 4, 1]], lab7b.inner_node_fn,
                          lab7b.leaf_fn, lab7b.empty_tree_fn) == 33


def test_contains_key():
    assert not lab7b.contains_key(40, [6, 7, [8, 9, 4]])
    assert lab7b.contains_key(9, [6, 7, [8, 9, 4]])


def test_tree_size():
    assert lab7b.tree_size([2, 4, [[], 5, 6]]) == 4
    assert lab7b.tree_size([2, 7, 3]) == 3
    assert lab7b.tree_size([]) == 0


def test_tree_depth():
    assert lab7b.tree_depth(3) == 1
    assert lab7b.tree_depth([[5, 6, [1, 2, 4]], 2, [7, 4, 1]]) == 4


tests()
