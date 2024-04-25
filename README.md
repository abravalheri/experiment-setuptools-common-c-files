# experiment-setuptools-common-c-files

This repository is an experiment to check if
`setuptools.setup(libraries=[...])` can be used to avoid race conditions when
compiling in parallel `Extension()` objects that share the same `.c` files.
