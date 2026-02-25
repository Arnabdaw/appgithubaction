from src.math_operations import add,sub
 
def test_add():
    assert add(2,3)==5
    assert add(4,5)==9
    assert add(-10,4)==-6
    assert add(1,2)==3

def test_sub():
    assert sub(5,3)==2
    assert sub(7,2)==5
    assert sub(6,9)==-3
    assert sub(3,4)==-1