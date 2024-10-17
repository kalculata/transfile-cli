from setuptools import setup, find_packages

setup(
  name='transfile',
  version='1.0.1',
  packages=find_packages(),
  author='kalculata',
  install_requires=[
      'openai',
  ],
  entry_points={
    'console_scripts': [
      'transfile = transfile.translate:main'
    ],
  },
)
