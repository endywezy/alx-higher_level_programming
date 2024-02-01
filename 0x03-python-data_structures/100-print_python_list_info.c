#include <Python.h>
#include <object.h>
#include <listobject.h>
#include <stdio.h>

void print_python_list_info(PyObject *p) {
    Py_ssize_t size, i;
    PyObject *item;

    printf("[*] Size of the Python List = %ld\n", PyList_Size(p));
    printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);

    size = PyList_Size(p);
    for (i = 0; i < size; i++) {
        item = PyList_GetItem(p, i);
        printf("Element %ld: %s\n", i, Py_TYPE(item)->tp_name);
    }
}
