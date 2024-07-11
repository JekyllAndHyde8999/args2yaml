from setuptools import find_packages, setup

setup(
    name="args2yaml",
    packages=find_packages(),
    version="0.1",
    description="A library that saves your script's arguments in a yaml file in your preferred location",
    author="Sravan Vinakota",
    install_requires=["yaml"],
)
