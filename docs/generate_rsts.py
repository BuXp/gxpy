import os
import inspect
from pkg_resources import parse_version
import geosoft.gxpy as gxpy
import geosoft.gxapi as gxa
import re

min_version = parse_version("8.5")
ver_add_re = re.compile(".*versionadded\:\:\s+([0-9\.]+)", re.MULTILINE)

def _is_some_method(obj):
    return (inspect.isfunction(obj) or
            inspect.ismethod(obj) or
            inspect.isbuiltin(obj) or
            inspect.ismethoddescriptor(obj))

def add_object_to_history(mod, version_history, object, name, collection, parent_name=None):
    if not name.startswith('_') and hasattr(object, '__doc__'):
        doc = str(object.__doc__)
        match = ver_add_re.search(doc)
        if match:
            ver_string = match.group(1)
            version = parse_version(ver_string)
            if version >= min_version:
                version_history[version] = version_history.get(version, {'classes': [], 'functions': []})
                if parent_name:
                    version_history[version][collection].append(":func:`{}.{}.{}`".format(mod.__name__, parent_name, name))
                else:
                    if _is_some_method(object):
                        version_history[version][collection].append(":func:`{}.{}`".format(mod.__name__, name))
                    elif inspect.isclass(object) and issubclass(object, BaseException):
                        version_history[version][collection].append(":exc:`{}.{}`".format(mod.__name__, name))
                    else:
                        version_history[version][collection].append(":class:`{}.{}`".format(mod.__name__, name))

def sort_version_history(version_history):
    for key, val in version_history.items():
        val['classes'].sort()
        val['functions'].sort()

def parse_module_history(mod, version_history):
    functions = inspect.getmembers(mod, _is_some_method)
    for fn_key, fn_value in functions:
        add_object_to_history(mod, version_history, fn_value, fn_key, 'functions')
    classes = inspect.getmembers(mod, inspect.isclass)
    for cl_key, cl_value in classes:
        add_object_to_history(mod, version_history, cl_value, cl_key, 'classes')
        cl_functions = inspect.getmembers(cl_value, _is_some_method)
        for fn_key, fn_value in cl_functions:
            add_object_to_history(mod, version_history, fn_value, fn_key, 'functions', parent_name=cl_key)
    sort_version_history(version_history)

def collect_gxa_version_history():
    gxa._version_history = {}
    parse_module_history(gxa, gxa._version_history)
    gxa._versions = reversed(sorted(gxa._version_history.keys()))

def collect_gxpy_version_history():
    gxpy._version_history = {}
    parse_module_history(gxpy.gx, gxpy._version_history)
    parse_module_history(gxpy.gdb, gxpy._version_history)
    parse_module_history(gxpy.grd, gxpy._version_history)
    parse_module_history(gxpy.ipj, gxpy._version_history)
    parse_module_history(gxpy.om, gxpy._version_history)
    parse_module_history(gxpy.system, gxpy._version_history)
    parse_module_history(gxpy.utility, gxpy._version_history)
    parse_module_history(gxpy.vv, gxpy._version_history)
    parse_module_history(gxpy.geometry, gxpy._version_history)
    parse_module_history(gxpy.view, gxpy._version_history)
    parse_module_history(gxpy.map, gxpy._version_history)
    gxpy._versions = reversed(sorted(gxpy._version_history.keys()))

def gen_version_history(j2env, output_dir):
    collect_gxpy_version_history()
    collect_gxa_version_history()
    modules = [gxpy, gxa]
    template = j2env.get_template('version_history.rst')
    output_file = os.path.join(output_dir, 'version_history.rst')
    with open(output_file, 'w+') as f:
        f.write(template.render(modules=modules))


def generate():
    from jinja2 import Environment, FileSystemLoader
    global __global_collection

    dir = os.path.split(__file__)[0]
    templates_dir = os.path.join(dir,'templates')
    j2env = Environment(loader=FileSystemLoader(templates_dir), 
						trim_blocks = True,
						lstrip_blocks = True)

    gen_version_history(j2env, dir)

if __name__ == "__main__":
    generate()