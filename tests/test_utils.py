import sys

sys.path.append('../')
from utils import get_temp

def test_get_temp_function():
    temp = get_temp()
    assert type(temp) == "float"
