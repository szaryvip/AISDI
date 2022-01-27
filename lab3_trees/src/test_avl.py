from avl import AVLTree


def test_balance_01():
    tree = AVLTree([1,2])
    b = tree.balance()
    assert b == -1


def test_balance_02():
    tree = AVLTree([1,2,3,4])
    b = tree.balance()
    assert b == -1


def test_balance_03():
    tree = AVLTree([1,2,3,4,5])
    b = tree.balance()
    assert b == -1


def test_balance_04():
    tree = AVLTree([1,2][::-1])
    b = tree.balance()
    assert b == 1


def test_balance_05():
    tree = AVLTree([1,2,3,4][::-1])
    b = tree.balance()
    assert b == 1

def test_balance_06():
    tree = AVLTree([1,2,3,4,5][::-1])
    b = tree.balance()
    assert b == 1


def test_balance_07():
    tree = AVLTree()
    b = tree.balance()
    assert b == 0


def test_height_01():
    tree = AVLTree([1,2])
    h = tree.height()
    assert h == 1


def test_height_02():
    tree = AVLTree([1,2,3])
    h = tree.height()
    assert h == 1


def test_height_03():
    tree = AVLTree([1,2,3,4,5])
    h = tree.height()
    assert h == 2


def test_height_04():
    tree = AVLTree([1])
    h = tree.height()
    assert h == 0


def test_height_05():
    tree = AVLTree([])
    h = tree.height()
    assert h == 0


def test_height_06():
    tree = AVLTree(list(range(50)))
    h = tree.height()
    assert h == 5


def test_delete_01():
    tree = AVLTree(list(range(10)))
    tree.delete(3)
    assert tree.top().value() == 2
    assert tree.top().left_son().balance() == 1


def test_delete_02():
    tree = AVLTree(list(range(10)))
    tree.delete(7)
    assert tree.top().right_son().value() == 6
    assert tree.top().right_son().right_son().value() == 8
    assert tree.top().right_son().left_son().value() == 5
    assert tree.top().balance() == -1


def test_delete_03():
    tree = AVLTree([6,4,1,7,9,0,5])
    tree.delete(7)
    assert tree.top().right_son().value() == 6
    assert tree.top().right_son().right_son().value() == 9
    assert tree.top().right_son().left_son().value() == 5
    assert tree.top().balance() == 0


def test_delete_04():
    tree = AVLTree([6,4,1,7,9,0,5])
    tree.delete(4)
    assert tree.top().value() == 6
    assert tree.top().right_son().value() == 7
    assert tree.top().left_son().value() == 1
    assert tree.top().right_son().right_son().value() == 9
    assert tree.top().left_son().left_son().value() == 0
    assert tree.top().balance() == 0


def test_delete_05():
    tree = AVLTree([6,4,1,7,9,0,5])
    tree.delete(4)
    tree.delete(6)
    assert tree.top().value() == 5
    assert tree.top().right_son().value() == 7
    assert tree.top().left_son().value() == 1
    assert tree.top().right_son().right_son().value() == 9
    assert tree.top().left_son().left_son().value() == 0
    assert tree.top().balance() == 0


def test_delete_06():
    tree = AVLTree(range(10))
    for i in range(10):
        tree.delete(i)
    assert tree.top() == None


def test_insert_01():
    tree = AVLTree([6,4,1,7,9,0,5])
    tree.insert(5)
    tree.insert(5)
    tree.insert(6)
    assert tree.top().value() == 4
    assert tree.top().right_son().value() == 6
    assert tree.top().left_son().value() == 1
    assert tree.top().right_son().right_son().value() == 7
    assert tree.top().right_son().left_son().value() == 5
    assert tree.top().balance() == -1


def test_insert_02():
    tree = AVLTree([7,4,7,3,4,3,6])
    tree.insert(9)
    tree.insert(5)
    tree.insert(6)
    assert tree.top().value() == 5
    assert tree.top().right_son().value() == 7
    assert tree.top().left_son().value() == 4
    assert tree.top().left_son().right_son().value() == 4
    assert tree.top().right_son().left_son().value() == 6
    assert tree.top().balance() == 0


def test_insert_03():
    tree = AVLTree()
    tree.insert(3)
    tree.insert(2)
    tree.insert(1)
    assert tree.top().value() == 2
    assert tree.top().left_son().value() == 1
    assert tree.top().right_son().value() == 3


def test_find_01():
    tree = AVLTree()
    assert None == tree.find(1)


def test_find_02():
    tree = AVLTree([1,2,4,5])
    result = tree.find(2)
    assert result.value() == 2
    assert result.left_son().value() == 1
    assert result.parent() == None


def test_find_03():
    tree = AVLTree([1,2,4,5])
    tree.delete(2)
    result = tree.find(2)
    assert result == None


def test_find_04():
    tree = AVLTree([4,7,4,6,3,2,0])
    result = tree.find(0)
    assert result.left_son() == None
    assert result.right_son() == None
    assert result.parent().value() == 2
