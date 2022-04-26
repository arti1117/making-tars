import pytest

@pytest.mark.parametrize("obj", ['1', '2', 'Foo'])
def test_isdigit(obj):
    assert obj.isdigit()
 
