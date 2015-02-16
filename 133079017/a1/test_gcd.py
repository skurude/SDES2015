from gcd import gcd
def test_gcd():
    assert gcd(120, 90) == 30
    assert gcd(19, 17) == 1
    assert gcd(0,1) == 1
    print "Test Completed Successfully"

test_gcd()