import os
from setuptools import setup, Extension, find_packages

# Define the shared library

# Define the extension modules
ext_module_a = Extension(
    "A",
    sources=["a.c"],
    libraries=["common"],
    include_dirs=[os.path.dirname(__file__)],
)
ext_module_b = Extension(
    "B",
    sources=["b.c"],
    libraries=["common"],
    include_dirs=[os.path.dirname(__file__)],
)

setup(
    name="MyProject",
    version="0.1",
    ext_modules=[ext_module_a, ext_module_b],
    libraries=[
        ("common", {"sources": ["common.c"]}),
    ],
)
