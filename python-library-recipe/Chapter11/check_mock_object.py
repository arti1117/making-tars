from unittest.mock import MagicMock

api = OutsideAPI()
api.do_something = MagicMock()
api.do_something.return_value = 'mock 객체로 대체된 결과'
api.do_something.assert_called_with()

api.do_something()
