from setuptools import setup

setup(
    name='pre-commit-qmllint',
    version='1.0.0',
    author='Mercotui',
    description='Installs the specified conan package, and exposes a pre-commit hook for qmllint',
    url='https://github.com/Mercotui/pre-commit-qmllint',
    scripts=['bin/qmllint.py',],
    license='LICENSE',
    long_description=open('README.md').read(),
    install_requires=["conan",],
)
