/*
 * File: 103-python.c
 */

#include <python.h>

void print_python_list(PyObject *p);
void print_python_bytes(PyObject *p);
void print_python_float(PyObject *p);

/**
 * print_python_list - This Prints basic info about Python lists.
 * @p: A PyObject list object.
 */
void print_python_list(PyObject *p)
{
	Py_ssize_t list_size, list_alloc, index;
	const char *element_type;
	PyListObject *python_list = (PyListObject *)p;
	PyVarObject *var_object = (PyVarObject *)p;

	list_size = var_object->ob_size;
	list_alloc = python_list->allocated;

	fflush(stdout);

	printf("[*] Python list info\n");
	if (strcmp(p->ob_type->tp_name, "list") != 0)
	{
		printf("  [ERROR] Invalid List Object\n");
		/*Returns nothing*/
		return;
	}

	printf("[*] Size of the Python List = %ld\n", list_size);
	printf("[*] Allocated = %ld\n", list_alloc);

	for (index = 0; index < list_size; index++)
	{
	element_type = python_list->ob_item[index]->ob_type->tp_name;
	printf("Element %ld: %s\n", index, element_type);
	if (strcmp(element_type, "bytes") == 0)
		print_python_bytes(python_list->ob_item[index]);
	else if (strcmp(element_type, "float") == 0)
		print_python_float(python_list->ob_item[index]);
	}
}

/**
 * print_python_bytes - This Prints basic info about Python byte objects.
 * @p: A PyObject byte object.
 */
void print_python_bytes(PyObject *p)
{
	Py_ssize_t bytes_size, i;
	PyBytesObject *python_bytes = (PyBytesObject *)p;

	fflush(stdout);

	printf("[.] bytes object info\n");
	if (strcmp(p->ob_type->tp_name, "bytes") != 0)
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	printf("  size: %ld\n", ((PyVarObject *)p)->ob_size);
	printf("  trying string: %s\n", python_bytes->ob_sval);

	if (((PyVarObject *)p)->ob_size >= 10)
		bytes_size = 10;
	else
		bytes_size = ((PyVarObject *)p)->ob_size + 1;

	printf("  first %ld bytes: ", bytes_size);
	for (i = 0; i < bytes_size; i++)
	{
	printf("%02hhx", python_bytes->ob_sval[i]);
	if (i == (bytes_size - 1))
		printf("\n");
	else
		printf(" ");
	}
}

/**
 * print_python_float - Prints basic info about Python float objects.
 * @p: A PyObject float object.
 */
void print_python_float(PyObject *p)
{
	char *float_buffer = NULL;

	PyFloatObject *python_float = (PyFloatObject *)p;

	fflush(stdout);

	printf("[.] float object info\n");
	if (strcmp(p->ob_type->tp_name, "float") != 0)
	{
		printf("  [ERROR] Invalid Float Object\n");
		return;
	}

	float_buffer = PyOS_double_to_string(python_float->ob_fval, 'r', 0,
                                          Py_DTSF_ADD_DOT_0, NULL);
	printf("  value: %s\n", float_buffer);
	PyMem_Free(float_buffer);
}
