import os

from setuptools import Extension, setup

setup(
    name="myproj",
    version="0.1",
    libraries=[
        # Compile shared files once and re-use in extensions
        ("common", {"sources": ["c-src/common.c"]}),
    ],
    ext_modules=[
        Extension(
            "myproj.A",
            sources=["c-src/a.c"],
            libraries=["common"],
            include_dirs=[os.path.join(os.path.dirname(__file__), "c-src")],
        ),
        Extension(
            "myproj.B",
            sources=["c-src/b.c"],
            libraries=["common"],
            include_dirs=[os.path.join(os.path.dirname(__file__), "c-src")],
        ),
    ],
)
