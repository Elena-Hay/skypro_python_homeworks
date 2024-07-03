import pytest
from string_utils import StringUtils

# capitilize
@pytest.mark.parametrize('input, result', 
[("test","Test"), ("test123","Test123"), ("lena test","Lena test"), ("lena_test","Lena_test"), ("123456", "123456"), ("test, lena", "Test, lena"), ("test. lena", "Test. lena")])
def test_positive_capitilize(input, result):
    string_utils = StringUtils()
    res = string_utils.capitilize(input)
    assert res == result

@pytest.mark.xfail
@pytest.mark.parametrize('input, result', 
[("  test", False), ("", False), (" ", False), ("!lena", False), (12345, False), (None, False)])
def test_negative_capitilize(input, result):
    string_utils = StringUtils()
    res = string_utils.capitilize(input)
    assert res == result

# trim
@pytest.mark.parametrize('input, result', 
[("    test", "test"), ("    1234", "1234"), ("    lena test", "lena test"), ("    lena_test", "Lena_test"), ("   test, lena", "test, lena"), ("   test. lena", "test. lena")])
def test_positive_trim(input, result):
    string_utils = StringUtils()
    res = string_utils.trim(input)
    assert res == result

@pytest.mark.xfail
@pytest.mark.parametrize('input, result', 
[("test    ", False), (None, False), ("", False), (" ", False), (12345, False)])
def test_negative_trim(input, result):
    string_utils = StringUtils()
    res = string_utils.trim(input)
    assert res == result

# to_list
@pytest.mark.parametrize('input, delimeter, result', 
[("a,b,c,d", None, ["a", "b", "c", "d"]), ("a.b.c", ".", ["a", "b", "c"]), ("a:b:c", ":", ["a", "b", "c"]), ("a;b;c", ";", ["a", "b", "c"]), ("a/b/c", "/", ["a", "b", "c"]), ("a-b-c", "-", ["a", "b", "c"]), ("a+b+c", "+", ["a", "b", "c"]), ("1,2,3", None, ["1", "2", "3"])])
def test_positive_to_list(input, delimeter, result):
    string_utils = StringUtils()
    if delimeter is None:
        res = string_utils.to_list(input)
    else:
        res = string_utils.to_list(input, delimeter)
    assert res == result

@pytest.mark.xfail
@pytest.mark.parametrize('input, delimeter, result', 
[("a.b.c", "/", False), ("abc", None, False), (12345, None, False), ("", None, False), (" ", None, False)])
def test_negative_to_list(input, delimeter, result):
    string_utils = StringUtils()
    if delimeter is None:
        res = string_utils.to_list(input)
    else:
        res = string_utils.to_list(input, delimeter)
    assert res == result

# contains
@pytest.mark.parametrize('string, symbol, result', 
[("lena", "a", True), ("12345", "4", True), ("Lena test", "e", True), ("lena_test", "t", True), ("test, lena", "a", True), ("test. lena", "l", True)])
def test_positive_contains(string, symbol, result):
    string_utils = StringUtils()
    res = string_utils.contains(string, symbol)
    assert res == result

@pytest.mark.xfail
@pytest.mark.parametrize('string, symbol, result', 
[("", "h", False), (None, "k", False), (" ", "o", False), (12345, "g", False), ("lena", "na", False), ("lena", "", False)])
def test_negative_contains(string, symbol, result):
    string_utils = StringUtils()
    res = string_utils.contains(string, symbol)
    assert res == result

# delete_symbol
@pytest.mark.parametrize('string, symbol, result', 
[("lena", "a", "len"), ("12345", "34", "125"), ("Lena test", "e", "Lna tst"), ("lena_test", "t", "lena_es"), ("test, lena", "a", "test, len"), ("test.lena", "l", "test.ena")])
def test_positive_delete_symbol(string, symbol, result):
    string_utils = StringUtils()
    res = string_utils.delete_symbol(string, symbol)
    assert res == result

@pytest.mark.xfail
@pytest.mark.parametrize('string, symbol',
[("", "a"), (None, "k"), (" ", "l"), (12345, "g"), ("lena", "89"), ("lena", "")])
def test_negative_delete_symbol(string, symbol, result):
    string_utils = StringUtils()
    res = string_utils.delete_symbol(string, symbol)
    assert res == result
 
 # starts_with
@pytest.mark.parametrize('string, symbol, result', 
[("lena", "l", True), ("12345", "1", True), ("Lena test", "L", True), ("lena_test", "l", True), ("test, lena", "t", True), ("test. lena", "t", True)])
def test_positive_starts_with(string, symbol, result):
    string_utils = StringUtils()
    res = string_utils.starts_with(string, symbol)
    assert res == result

@pytest.mark.xfail
@pytest.mark.parametrize('string, symbol, result', 
[("", "h", False), (None, "k", False), (" ", "o", False), (12345, "g", False), ("lena", "h", False), ("lena", "", False)])
def test_negative_starts_with(string, symbol, result):
    string_utils = StringUtils()
    res = string_utils.starts_with(string, symbol)
    assert res == result

# end_with
@pytest.mark.parametrize('string, symbol, result', 
[("lena", "a", True), ("12345", "5", True), ("Lena test", "t", True), ("lena_test", "t", True), ("test, lena", "a", True), ("test. lena", "a", True)])
def test_positive_end_with(string, symbol, result):
    string_utils = StringUtils()
    res = string_utils.end_with(string, symbol)
    assert res == result

@pytest.mark.xfail
@pytest.mark.parametrize('string, symbol, result', 
[("", "h", False), (None, "k", False), (" ", "o", False), (12345, "g", False), ("lena", "h", False), ("lena", "", False)])
def test_negative_end_with(string, symbol, result):
    string_utils = StringUtils()
    res = string_utils.end_with(string, symbol)
    assert res == result

# is_empty
@pytest.mark.parametrize('string, result', 
[("", True), (" ", True), ("      ", True), ("test", False), ("test lena", False)])
def test_positive_is_empty(string, result):
    string_utils = StringUtils()
    res = string_utils.is_empty(string)
    assert res == result

@pytest.mark.xfail
@pytest.mark.parametrize('string, result', 
[(None, False), (12345, False)])
def test_negative_is_empty(string, result):
    string_utils = StringUtils()
    res = string_utils.is_empty(string)
    assert res == result

# list_to_string
@pytest.mark.parametrize('list, joiner, result', 
[(["le","na"], None, "le, na"), (["a","b","c"], ".", "a.b.c"), (["a","b","c"], ":", "a:b:c"), (["a","b","c"], ";", "a;b;c"), (["a","b","c"], "/", "a/b/c"), (["a","b","c"], "-", "a-b-c"), (["1","2","3"], None, "1, 2, 3"), (["1, 2, 3"], None, "1, 2, 3")])
def test_positive_list_to_string(list, joiner, result):
    string_utils = StringUtils()
    if joiner is None:
        res = string_utils.list_to_string(list)
    else:
        res = string_utils.list_to_string(list, joiner)
    assert res == result

@pytest.mark.xfail
@pytest.mark.parametrize('list, joiner, result', 
[([], None, False), ([  ], None, False), (None, None, False)])
def test_negative_list_to_string(list, joiner, result):
    string_utils = StringUtils()
    if joiner is None:
        res = string_utils.list_to_string(list)
    else:
        res = string_utils.list_to_string(list, joiner)
    assert res == result
