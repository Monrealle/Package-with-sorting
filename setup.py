from setuptools import setup, find_packages

setup(
    name="sorts",
    version="0.1",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    py_modules=['bubble', 'heap', 'merge', 'quick'],
)
