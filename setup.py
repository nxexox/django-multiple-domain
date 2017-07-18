# coding: utf8
import multidomain
import os
from setuptools import setup

README = open(os.path.join(os.path.dirname(__file__), 'README.md')).read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

# ./python3/bin/python setup.py sdist

setup(
    name='django-multidomain',
    version=multidomain.__version__,
    packages=['multidomain'],
    include_package_data=True,  # Включаем все файлы
    license='MIT',  # Ставим дицензию
    description='App for multi domain in django. Python2.x, Python3.x, Django>=1.4',
    long_description=README,
    url='http://www.example.com/',
    author='Deys Timofey',
    author_email='nxexox@gmail.com',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
    test_suite="multidomain.tests",
    install_requires=[
        "Django>=1.4"
    ]
)
