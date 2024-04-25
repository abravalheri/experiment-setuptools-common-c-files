#include <Python.h>
#include "common.h"

static PyObject* sum_squared(PyObject* self, PyObject* args) {
    int x, y;
    if (!PyArg_ParseTuple(args, "ii", &x, &y)) {
        return NULL;
    }
    int result = sum(x*x, y*y);
    return Py_BuildValue("i", result);
}

static PyMethodDef B_methods[] = {
    {"sum_squared", sum_squared, METH_VARARGS, "Return the sum of the squares of two numbers."},
    {NULL, NULL, 0, NULL}
};

static struct PyModuleDef B_module = {
    PyModuleDef_HEAD_INIT,
    "B",
    NULL,
    -1,
    B_methods
};

PyMODINIT_FUNC PyInit_B(void) {
    return PyModule_Create(&B_module);
}

