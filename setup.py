from setuptools import setup

setup(
  name = "major_system",
  version = "1.0.0",
  author = "John Baber-Lucero",
  author_email = "pypi@frundle.com",
  description = ("Tools for making major system words from numbers"),
  license = "GPL",
  packages = ['major_system'],
  install_requires = ['docopt'],
  tests_require=['pytest'],
  entry_points = {
    'console_scripts': ['major_words=major_system.major_system:main'],
  }
)
