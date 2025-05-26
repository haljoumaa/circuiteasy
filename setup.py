from setuptools import setup, find_packages

setup(
    name="circuiteasy",
    version="1.0.2",
    description="ELE142 and general circuit analysis tools for fast, clear Python calculations.",
    author="Hareth Al-jomaa",
    author_email="harethaljomaa@outlook.com",
    packages=find_packages(),
    install_requires=[
        "numpy",
        "matplotlib",
        "sympy"
    ],
    python_requires=">=3.7",
    include_package_data=True,
    license="MIT",
    url="https://github.com/haljoumaa/circuiteasy.git", 
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
)
