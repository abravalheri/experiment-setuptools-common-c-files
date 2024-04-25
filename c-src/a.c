#include <Python.h>
#include "common.h"

static PyObject* squared_sum(PyObject* self, PyObject* args) {
    int x, y;
    if (!PyArg_ParseTuple(args, "ii", &x, &y)) {
        return NULL;
    }
    int result = sum(x, y);
    return Py_BuildValue("i", result * result);
}

static PyMethodDef A_methods[] = {
    {"squared_sum", squared_sum, METH_VARARGS, "Return the square of the sum of two numbers."},
    {NULL, NULL, 0, NULL}
};

static struct PyModuleDef A_module = {
    PyModuleDef_HEAD_INIT,
    "A",
    NULL,
    -1,
    A_methods
};

PyMODINIT_FUNC PyInit_A(void) {
    return PyModule_Create(&A_module);
}

