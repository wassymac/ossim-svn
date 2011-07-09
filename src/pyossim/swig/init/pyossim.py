# This file was automatically generated by SWIG (http://www.swig.org).
# Version 2.0.4
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.



from sys import version_info
if version_info >= (2,6,0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_pyossim', [dirname(__file__)])
        except ImportError:
            import _pyossim
            return _pyossim
        if fp is not None:
            try:
                _mod = imp.load_module('_pyossim', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _pyossim = swig_import_helper()
    del swig_import_helper
else:
    import _pyossim
del version_info
try:
    _swig_property = property
except NameError:
    pass # Python < 2.2 doesn't have 'property'.
def _swig_setattr_nondynamic(self,class_type,name,value,static=1):
    if (name == "thisown"): return self.this.own(value)
    if (name == "this"):
        if type(value).__name__ == 'SwigPyObject':
            self.__dict__[name] = value
            return
    method = class_type.__swig_setmethods__.get(name,None)
    if method: return method(self,value)
    if (not static):
        self.__dict__[name] = value
    else:
        raise AttributeError("You cannot add attributes to %s" % self)

def _swig_setattr(self,class_type,name,value):
    return _swig_setattr_nondynamic(self,class_type,name,value,0)

def _swig_getattr(self,class_type,name):
    if (name == "thisown"): return self.this.own()
    method = class_type.__swig_getmethods__.get(name,None)
    if method: return method(self)
    raise AttributeError(name)

def _swig_repr(self):
    try: strthis = "proxy of " + self.this.__repr__()
    except: strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)

try:
    _object = object
    _newclass = 1
except AttributeError:
    class _object : pass
    _newclass = 0


ossimInit_HEADER = _pyossim.ossimInit_HEADER
class ossimInit(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, ossimInit, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, ossimInit, name)
    def __init__(self, *args, **kwargs): raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __swig_destroy__ = _pyossim.delete_ossimInit
    __del__ = lambda self : None;
    __swig_getmethods__["instance"] = lambda x: _pyossim.ossimInit_instance
    if _newclass:instance = staticmethod(_pyossim.ossimInit_instance)
    def addOptions(self, *args): return _pyossim.ossimInit_addOptions(self, *args)
    def initialize(self, *args): return _pyossim.ossimInit_initialize(self, *args)
    def finalize(self): return _pyossim.ossimInit_finalize(self)
    def usage(self): return _pyossim.ossimInit_usage(self)
    def getElevEnabledFlag(self): return _pyossim.ossimInit_getElevEnabledFlag(self)
    def setElevEnabledFlag(self, *args): return _pyossim.ossimInit_setElevEnabledFlag(self, *args)
    def setPluginLoaderEnabledFlag(self, *args): return _pyossim.ossimInit_setPluginLoaderEnabledFlag(self, *args)
    def loadPlugins(self, *args): return _pyossim.ossimInit_loadPlugins(self, *args)
    def initializePlugins(self): return _pyossim.ossimInit_initializePlugins(self)
    def initializeDefaultFactories(self): return _pyossim.ossimInit_initializeDefaultFactories(self)
    def initializeElevation(self): return _pyossim.ossimInit_initializeElevation(self)
    def initializeLogFile(self): return _pyossim.ossimInit_initializeLogFile(self)
    def version(self): return _pyossim.ossimInit_version(self)
    def appName(self): return _pyossim.ossimInit_appName(self)
ossimInit_swigregister = _pyossim.ossimInit_swigregister
ossimInit_swigregister(ossimInit)

def ossimInit_instance():
  return _pyossim.ossimInit_instance()
ossimInit_instance = _pyossim.ossimInit_instance

# This file is compatible with both classic and new-style classes.

