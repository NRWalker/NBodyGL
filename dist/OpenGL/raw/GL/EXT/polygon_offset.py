'''Autogenerated by get_gl_extensions script, do not edit!'''
from OpenGL import platform as _p, constants as _cs, arrays
from OpenGL.GL import glget
import ctypes
EXTENSION_NAME = 'GL_EXT_polygon_offset'
def _f( function ):
    return _p.createFunction( function,_p.GL,'GL_EXT_polygon_offset',False)
_p.unpack_constants( """GL_POLYGON_OFFSET_EXT 0x8037
GL_POLYGON_OFFSET_FACTOR_EXT 0x8038
GL_POLYGON_OFFSET_BIAS_EXT 0x8039""", globals())
glget.addGLGetConstant( GL_POLYGON_OFFSET_EXT, (1,) )
glget.addGLGetConstant( GL_POLYGON_OFFSET_FACTOR_EXT, (1,) )
glget.addGLGetConstant( GL_POLYGON_OFFSET_BIAS_EXT, (1,) )
@_f
@_p.types(None,_cs.GLfloat,_cs.GLfloat)
def glPolygonOffsetEXT( factor,bias ):pass


def glInitPolygonOffsetEXT():
    '''Return boolean indicating whether this extension is available'''
    from OpenGL import extensions
    return extensions.hasGLExtension( EXTENSION_NAME )
