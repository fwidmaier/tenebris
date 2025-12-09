from setuptools import setup, find_packages

setup(name='tenebris',
      version='1.0',
      description='Python library for autodifferentiation and other cool mathematics',
      author='Felix Widmaier',
      author_email='',
      url='https://github.com/fwidmaier/tenebris',
      packages=find_packages(include=['tenebris', 'tenebris.*']),
      install_requires=[],
      options={'bdist_wheel': {'universal': '1'}},
      )
