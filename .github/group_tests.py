import group

def test_groups_of_3():
    assert group.groups_of_3([1, 2, 3, 4, 5, 6, 7, 8, 9]) == [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    assert group.groups_of_3([1, 2, 3, 4, 5, 6, 7, 8]) == [[1, 2, 3], [4, 5, 6], [7, 8]]
    assert group.groups_of_3([]) == []
    assert group.groups_of_3([1, 2]) == [[1, 2]]
    print("All tests passed!")

test_groups_of_3()
