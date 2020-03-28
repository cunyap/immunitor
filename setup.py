"""A setuptools based setup module."""
from os import path
from setuptools import setup, find_packages
from io import open

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='App',
    version='0.0.1',
    description='App',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/cunyap/codevscovid19_app',
    author='Andreas P. Cuny',
    author_email='andreas.cuny@bsse.ethz.ch',
    classifiers=[
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    keywords='App',
    packages=find_packages(),
    install_requires=['Flask',
                      'Flask-WTF'],
    extras_require={
        'dev': ['check-manifest'],
        'test': ['coverage'],
        'env': ['python-dotenv']
    },
    entry_points={
        'console_scripts': [
            'run=wsgi:__main__',
        ],
    },
    project_urls={
        'Bug Reports': 'https://github.com/cunyap/codevscovid19_app/issues',
        'Source': 'https://github.com/cunyap/codevscovid19_app',
    },
)
