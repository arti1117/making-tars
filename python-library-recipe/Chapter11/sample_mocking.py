from sample_processing import OutsideAPI
from unittest.mock import MagicMock

print('--')
api = OutsideAPI()
api.do_something = MagicMock()
print(api.do_something)
print('--')

api.do_something.return_value='mock 객체로 대체된 결과'
print(api.do_something())
print('--')

api.do_something.side_effect = Exception('예외를 설정합니다.')
print(api.do_something())
print('--')
