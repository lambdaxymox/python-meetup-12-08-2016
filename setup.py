try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'Python Meetup December 8, 2016',
    'author': 'Stallmanifold',
    'url': 'https://github.com/stallmanifold/python-meetup-12-08-2016',
    'download_url': 'https://github.com/stallmanifold/python-meetup-12-08-2016.git',
    'author_email': 'stallmanifold@gmail.com',
    'version': '0.1',
    'install_requires': ['pytest'],
    'packages': ['exercises'],
    'scripts': [],
    'name': 'python-meetup-12-08-2016'
}

setup(**config)
