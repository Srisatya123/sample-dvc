
import pytest

class NotinRangeError(Exception):
    def __init__(self,input_='' ,message="value not in in rage"):
        self.message=message
        super().__init__(self.message)

def test_generic():
    a=5
    with pytest.raises(NotinRangeError):
        if a not in range(10,20):
            raise NotinRangeError
     