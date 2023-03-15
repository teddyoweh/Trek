from setuptools import setup, find_packages
import pathlib
 
HERE = pathlib.Path(__file__).parent

 
README = (HERE / "README.md").read_text()
 
VERSION = '0.0.5'
DESCRIPTION = 'Using graph theory algorithms and simulations, to optimaize paths and travel times between nodes on a geospatial map'
LONG_DESCRIPTION = 'Using graph theory algorithms and simulations, to optimaize paths and travel times between nodes on a geospatial map'

setup(
    name="trekpy",
    version=VERSION,
    description=DESCRIPTION,
    long_description=README,
    long_description_content_type="text/markdown",
    author="Teddy Oweh",
    author_email="teddyoweh@gmail.com",
    license='MIT',
    url="https://github.com/teddyoweh/Trek",
    
    
    packages=find_packages(),
    install_requires=[
    'matplotlib',
    'networkx'
    ],
    keywords='Trek',
    classifiers= [
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        'License :: OSI Approved :: MIT License',
        "Programming Language :: Python :: 3",
    ]
)
