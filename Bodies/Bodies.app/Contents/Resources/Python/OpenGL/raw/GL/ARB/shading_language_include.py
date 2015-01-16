'''Autogenerated by get_gl_extensions script, do not edit!'''
from OpenGL import platform as _p, constants as _cs, arrays
from OpenGL.GL import glget
import ctypes
EXTENSION_NAME = 'GL_ARB_shading_language_include'
def _f( function ):
    return _p.createFunction( function,_p.GL,'GL_ARB_shading_language_include',False)
_p.unpack_constants( """GL_SHADER_INCLUDE_ARB 0x8DAE
GL_NAMED_STRING_LENGTH_ARB 0x8DE9
GL_NAMED_STRING_TYPE_ARB 0x8DEA""", globals())
@_f
@_p.types(None,_cs.GLenum,_cs.GLint,arrays.GLcharArray,_cs.GLint,arrays.GLcharArray)
def glNamedStringARB( type,namelen,name,stringlen,string ):pass
@_f
@_p.types(None,_cs.GLint,arrays.GLcharArray)
def glDeleteNamedStringARB( namelen,name ):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLsizei,ctypes.POINTER( ctypes.POINTER( _cs.GLchar )),arrays.GLintArray)
def glCompileShaderIncludeARB( shader,count,path,length ):pass
@_f
@_p.types(_cs.GLboolean,_cs.GLint,arrays.GLcharArray)
def glIsNamedStringARB( namelen,name ):pass
@_f
@_p.types(None,_cs.GLint,arrays.GLcharArray,_cs.GLsizei,arrays.GLintArray,arrays.GLcharArray)
def glGetNamedStringARB( namelen,name,bufSize,stringlen,string ):pass
@_f
@_p.types(None,_cs.GLint,arrays.GLcharArray,_cs.GLenum,arrays.GLintArray)
def glGetNamedStringivARB( namelen,name,pname,params ):pass


def glInitShadingLanguageIncludeARB():
    '''Return boolean indicating whether this extension is available'''
    from OpenGL import extensions
    return extensions.hasGLExtension( EXTENSION_NAME )
