'''Autogenerated by get_gl_extensions script, do not edit!'''
from OpenGL import platform as _p, constants as _cs, arrays
from OpenGL.GL import glget
import ctypes
EXTENSION_NAME = 'GL_EXT_light_texture'
def _f( function ):
    return _p.createFunction( function,_p.GL,'GL_EXT_light_texture',False)
_p.unpack_constants( """GL_FRAGMENT_MATERIAL_EXT 0x8349
GL_FRAGMENT_NORMAL_EXT 0x834A
GL_FRAGMENT_COLOR_EXT 0x834C
GL_ATTENUATION_EXT 0x834D
GL_SHADOW_ATTENUATION_EXT 0x834E
GL_TEXTURE_APPLICATION_MODE_EXT 0x834F
GL_TEXTURE_LIGHT_EXT 0x8350
GL_TEXTURE_MATERIAL_FACE_EXT 0x8351
GL_TEXTURE_MATERIAL_PARAMETER_EXT 0x8352""", globals())
@_f
@_p.types(None,_cs.GLenum)
def glApplyTextureEXT( mode ):pass
@_f
@_p.types(None,_cs.GLenum)
def glTextureLightEXT( pname ):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLenum)
def glTextureMaterialEXT( face,mode ):pass


def glInitLightTextureEXT():
    '''Return boolean indicating whether this extension is available'''
    from OpenGL import extensions
    return extensions.hasGLExtension( EXTENSION_NAME )
