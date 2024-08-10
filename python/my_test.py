import importlib
import pytest

module_name = '06_NumberSpiral'
module = importlib.import_module(module_name)


def test_main():
    tests = [[2,3,8],[4,2,15],[1,1,1]]
    for (a,b,c) in tests:
        assert module.main(a,b) == c


if __name__ == "__main__":
    pytest.main()