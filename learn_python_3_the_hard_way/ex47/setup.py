try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'skeleton',
    'author': 'JY',
    'url': 'https://github.com/arti1117/learn_python_3_the_hard_way',
    'download_url': 'https://github.com/arti1117/learn_python_3_the_hard_way/Exercise/skeleton',
    'author_email': 'darkmoonz1004@gmail.com',
    'version': '0.0.1',
    'install_requires': ['pytest'],
    'packages': ['NAME'],
    'scripts': [],
    'name': 'skeleton'
}

setup(**config)
