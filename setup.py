from setuptools import setup, find_packages

setup(
    name="functogui",
    version="0.0.1",
    packages=find_packages(),
    package_data={
        'functogui': ['*.kv'],
    },
    install_requires=[
        'kivy',
        'pyler',
    ],
)