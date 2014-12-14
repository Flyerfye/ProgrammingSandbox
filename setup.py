try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'Tabl_homework',
    'author': 'Issa Beekun',
    'author_email': 'Issa.Beekun@gmail.com',
    'version': '1.0',
    'test_suite':'nose.collector',
    'test_requires': ['nose'],
    'install_requires': ['nose', 're'],
    'packages': ['BinarySearch', 'WordReversal'],
    'scripts': [],
    'name': 'Tabl-homework'
}

setup(**config)