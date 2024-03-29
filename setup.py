#!/usr/bin/env python

"""The setup script."""

from setuptools import find_packages, setup

with open("README.md") as readme_file:
    readme = readme_file.read()

requirements = [
    "Click>=7.0,<9",
    "arrow>1,<2",
    "xdg>5,<6",
    "bullet>2,<3",
]

setup_requirements = [
    "pytest-runner",
]

test_requirements = [
    "pytest>=3",
]

setup(
    author="Oscar Arbeláez",
    author_email="oscar@arbelaez.dev",
    python_requires=">=3.6",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "Intended Audience :: Education",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
    description="Turns bancolombia reports into YNAB readable input files.",
    entry_points={"console_scripts": ["bmynab=bmynab.cli:main"]},
    install_requires=requirements,
    license="MIT license",
    long_description=readme,
    long_description_content_type="text/markdown",
    include_package_data=True,
    keywords="finance,ynab",
    name="bmynab",
    packages=find_packages(where="src"),
    package_dir={"": "src/", "bmynab": "src/bmynab"},
    setup_requires=setup_requirements,
    test_suite="tests",
    tests_require=test_requirements,
    url="https://github.com/odarbelaeze/bmynab",
    version="1.0.0",
    zip_safe=False,
)
