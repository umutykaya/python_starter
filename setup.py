from setuptools import setup

setup(name='sample_python_project',
      version='0.0.1',
      description='An example package for Python.',
      author='Umut Yalcinkaya',
      author_email='yalcinkayaumut@outlook.com',
      packages=['my_package', 'Tokenizer'],
      install_requires=['nltk'])