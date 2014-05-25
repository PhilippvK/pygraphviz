# This file was automatically generated by SWIG (http://www.swig.org).
# Version 2.0.10
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
            fp, pathname, description = imp.find_module('_graphviz', [dirname(__file__)])
        except ImportError:
            import _graphviz
            return _graphviz
        if fp is not None:
            try:
                _mod = imp.load_module('_graphviz', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _graphviz = swig_import_helper()
    del swig_import_helper
else:
    import _graphviz
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



def agopen(*args):
  return _graphviz.agopen(*args)
agopen = _graphviz.agopen
def agraphnew(name,strict=False,directed=False):
    if strict:
       if directed:
            return _graphviz.agopen(name,_graphviz.cvar.Agstrictdirected,None)
       else:
            return _graphviz.agopen(name,_graphviz.cvar.Agstrictundirected,None)
    else:
        if directed:
            return _graphviz.agopen(name,_graphviz.cvar.Agdirected,None)
        else:		 
            return _graphviz.agopen(name,_graphviz.cvar.Agundirected,None)


def agclose(*args):
  return _graphviz.agclose(*args)
agclose = _graphviz.agclose

def agread(*args):
  return _graphviz.agread(*args)
agread = _graphviz.agread

def agwrite(*args):
  return _graphviz.agwrite(*args)
agwrite = _graphviz.agwrite

def agisundirected(*args):
  return _graphviz.agisundirected(*args)
agisundirected = _graphviz.agisundirected

def agisdirected(*args):
  return _graphviz.agisdirected(*args)
agisdirected = _graphviz.agisdirected

def agisstrict(*args):
  return _graphviz.agisstrict(*args)
agisstrict = _graphviz.agisstrict

def agnode(*args):
  return _graphviz.agnode(*args)
agnode = _graphviz.agnode

def agidnode(*args):
  return _graphviz.agidnode(*args)
agidnode = _graphviz.agidnode

def agsubnode(*args):
  return _graphviz.agsubnode(*args)
agsubnode = _graphviz.agsubnode

def agfstnode(*args):
  return _graphviz.agfstnode(*args)
agfstnode = _graphviz.agfstnode

def agnxtnode(*args):
  return _graphviz.agnxtnode(*args)
agnxtnode = _graphviz.agnxtnode

def aglstnode(*args):
  return _graphviz.aglstnode(*args)
aglstnode = _graphviz.aglstnode

def agprvnode(*args):
  return _graphviz.agprvnode(*args)
agprvnode = _graphviz.agprvnode

def agedge(*args):
  return _graphviz.agedge(*args)
agedge = _graphviz.agedge

def agidedge(*args):
  return _graphviz.agidedge(*args)
agidedge = _graphviz.agidedge

def agsubedge(*args):
  return _graphviz.agsubedge(*args)
agsubedge = _graphviz.agsubedge

def agfstin(*args):
  return _graphviz.agfstin(*args)
agfstin = _graphviz.agfstin

def agnxtin(*args):
  return _graphviz.agnxtin(*args)
agnxtin = _graphviz.agnxtin

def agfstout(*args):
  return _graphviz.agfstout(*args)
agfstout = _graphviz.agfstout

def agnxtout(*args):
  return _graphviz.agnxtout(*args)
agnxtout = _graphviz.agnxtout

def agfstedge(*args):
  return _graphviz.agfstedge(*args)
agfstedge = _graphviz.agfstedge

def agnxtedge(*args):
  return _graphviz.agnxtedge(*args)
agnxtedge = _graphviz.agnxtedge

def aghead(*args):
  return _graphviz.aghead(*args)
aghead = _graphviz.aghead

def agtail(*args):
  return _graphviz.agtail(*args)
agtail = _graphviz.agtail

def agattr(*args):
  return _graphviz.agattr(*args)
agattr = _graphviz.agattr

def agattrsym(*args):
  return _graphviz.agattrsym(*args)
agattrsym = _graphviz.agattrsym

def agnxtattr(*args):
  return _graphviz.agnxtattr(*args)
agnxtattr = _graphviz.agnxtattr

def agget(*args):
  return _graphviz.agget(*args)
agget = _graphviz.agget

def agxget(*args):
  return _graphviz.agxget(*args)
agxget = _graphviz.agxget

def agset(*args):
  return _graphviz.agset(*args)
agset = _graphviz.agset

def agxset(*args):
  return _graphviz.agxset(*args)
agxset = _graphviz.agxset

def agsafeset(*args):
  return _graphviz.agsafeset(*args)
agsafeset = _graphviz.agsafeset

def agattrname(*args):
  return _graphviz.agattrname(*args)
agattrname = _graphviz.agattrname

def agattrdefval(*args):
  return _graphviz.agattrdefval(*args)
agattrdefval = _graphviz.agattrdefval

def agsafeset_label(*args):
  return _graphviz.agsafeset_label(*args)
agsafeset_label = _graphviz.agsafeset_label

def agattr_label(*args):
  return _graphviz.agattr_label(*args)
agattr_label = _graphviz.agattr_label

def agsubg(*args):
  return _graphviz.agsubg(*args)
agsubg = _graphviz.agsubg

def agfstsubg(*args):
  return _graphviz.agfstsubg(*args)
agfstsubg = _graphviz.agfstsubg

def agnxtsubg(*args):
  return _graphviz.agnxtsubg(*args)
agnxtsubg = _graphviz.agnxtsubg

def agparent(*args):
  return _graphviz.agparent(*args)
agparent = _graphviz.agparent

def agroot(*args):
  return _graphviz.agroot(*args)
agroot = _graphviz.agroot

def agdelsubg(*args):
  return _graphviz.agdelsubg(*args)
agdelsubg = _graphviz.agdelsubg

def agnnodes(*args):
  return _graphviz.agnnodes(*args)
agnnodes = _graphviz.agnnodes

def agnedges(*args):
  return _graphviz.agnedges(*args)
agnedges = _graphviz.agnedges

def agdegree(*args):
  return _graphviz.agdegree(*args)
agdegree = _graphviz.agdegree

def agraphof(*args):
  return _graphviz.agraphof(*args)
agraphof = _graphviz.agraphof

def agnameof(*args):
  return _graphviz.agnameof(*args)
agnameof = _graphviz.agnameof

def agdelnode(*args):
  return _graphviz.agdelnode(*args)
agdelnode = _graphviz.agdelnode

def agdeledge(*args):
  return _graphviz.agdeledge(*args)
agdeledge = _graphviz.agdeledge
def agnameof(handle):
  name=_graphviz.agnameof(handle)
  if name is None:
     return None
  if name==b'' or name.startswith(b'%'):
    return None
  else:
    return name 

AGRAPH = _graphviz.AGRAPH
AGNODE = _graphviz.AGNODE
AGOUTEDGE = _graphviz.AGOUTEDGE
AGINEDGE = _graphviz.AGINEDGE
AGEDGE = _graphviz.AGEDGE
# This file is compatible with both classic and new-style classes.
