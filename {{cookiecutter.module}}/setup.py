from setuptools import setup

import sys

needs_pytest = {'pytest', 'test', 'ptr'}.intersection(sys.argv)
pytest_runner = ['pytest-runner'] if needs_pytest else []

setup(name="{{cookiecutter.module}}",
      version="0.0.1",
      setup_requires=['pytest-runner'],
      tests_require=['pytest'],
      packages=['{{cookiecutter.module}}'])
