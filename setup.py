from setuptools import setup, find_packages
from codecs import open
from os import path

__version__ = '0.0.3'

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()
    

install_requires = []
dependency_links = []

setup(
    name='simpleplotdigitizer',
    version=__version__,
    description='A simple plot digitizer',
    long_description=long_description,
    url='https://github.com/spidezad/simpleplotdigitizer',
    download_url='https://github.com/spidezad/simpleplotdigitizer/tarball/' + __version__,
    license='MIT',
    classifiers=[
      'Development Status :: 3 - Alpha',
      'Intended Audience :: Developers',
      'Programming Language :: Python :: 3',
    ],
    keywords='',
    packages=find_packages(exclude=['docs', 'tests*']),
    include_package_data=True,
    author='Tan Kok Hua',
    install_requires=install_requires,
    dependency_links=dependency_links,
    author_email='kokhua81@gmail.com'
)
