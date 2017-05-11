// Copyright (c) 2017 Oleg Bulkin
// MIT License (https://opensource.org/licenses/MIT)

// Include necessary headers
#include <Python.h>
#include "levenshtein.h"
#include "rdlevenshtein.h"

// Create array of PyMethodDef structs, which provide the Python API with the
// info used to create a Python method from a C function
static PyMethodDef methods[] = {
    {
        "levenshtein",
        levenshtein,
        METH_VARARGS,
        "Calculates the Levenshtein distance between two string arguments"
    },
    {
        "levenshtein_norm",
        levenshtein_norm,
        METH_VARARGS,
        "Calculates the normalized Levenshtein distance between two string"
        " arguments. The result will be a float in the range [0.0, 1.0], with"
        " 1.0 signifying the biggest possible distance between two strings"
        " with these lengths"
    },
    {
        "rdlevenshtein",
        rdlevenshtein,
        METH_VARARGS,
        "Calculates the restricted Damerau-Levenshtein distance (a.k.a. the"
        " optimal string alignment distance) between two string arguments"
    },
    {
        "rdlevenshtein_norm",
        rdlevenshtein_norm,
        METH_VARARGS,
        "Calculates the normalized restricted Damerau-Levenshtein distance"
        " (a.k.a. the normalized optimal string alignment distance) between"
        " two string arguments. The result will be a float in the range"
        " [0.0, 1.0], with 1.0 signifying the biggest possible distance"
        " between two strings with these lengths"
    },
    // This is a sentinel value that indicates the end of the array
    {NULL, NULL, 0, NULL}
};
 
// Create PyModuleDef struct, which outlines the desired C extension module
static struct PyModuleDef cstringdist = {
    PyModuleDef_HEAD_INIT,
    "cstringdist",
    "Calculates several different string distance metrics",
    -1,
    methods,
    NULL,
    NULL,
    NULL,
    NULL
};

// Module initialization function for the cstringdist module, which is called
// when the module is imported for the first time
PyMODINIT_FUNC PyInit_cstringdist(void)
{
    // Use Python API to create module, passing in address of module struct
    return PyModule_Create(&cstringdist);
}
