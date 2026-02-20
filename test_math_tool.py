from math_tool import ad, multiply , is_even, substract, largest
def test_ad():
    assert ad(2,3) == 5
    assert ad(1,-1) == 0
    assert ad(0,0) == 0
    print("test_ad all passed")
    
def test_mul():
    assert multiply(3,4) == 12
    assert multiply(-2,5) == -10
    assert multiply(0,100) == 0
    print("Multiply all test passed")

def test_is_even():
    assert is_even(4) == True
    assert is_even(7) == False
    assert is_even(0) == True
    print("Even all test passed")
    
    
def test_substract():
    assert substract(2,3) == -1
    assert substract(0,0) == 0
    assert substract(8,8) == 0
    print("Subtract test pass")
    
def test_largest():
    assert largest([2,3,4]) == 4
    assert largest([4,4,5]) == 5
    assert largest([4,4,4]) == 4
    print("largest test pass")
    
    
test_largest()
test_substract()
test_ad()
test_mul()
test_is_even()
print("All test passed")
    