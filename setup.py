from setuptools import setup

with open('README.md') as f:
    long_description = f.read()

setup(
    name='jsonism',
    version='1.1.2',
    packages=['tests', 'jsonism'],
    url='https://github.com/bmcollier/jsonism',
    license='3-Clause BSD',
    author='Ben Collier',
    author_email='bencollier@fastmail.com',
    description='A simple JSON schema checker',
    long_description=long_description,
    long_description_content_type="text/markdown"
)
