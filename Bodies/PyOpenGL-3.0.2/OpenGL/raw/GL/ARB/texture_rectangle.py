'''Autogenerated by get_gl_extensions script, do not edit!'''
from OpenGL import platform as _p
from OpenGL.GL import glget
EXTENSION_NAME = 'GL_ARB_texture_rectangle'
_p.unpack_constants( """GL_TEXTURE_RECTANGLE_ARB 0x84F5
GL_TEXTURE_BINDING_RECTANGLE_ARB 0x84F6
GL_PROXY_TEXTURE_RECTANGLE_ARB 0x84F7
GL_MAX_RECTANGLE_TEXTURE_SIZE_ARB 0x84F8""", globals())
glget.addGLGetConstant( GL_TEXTURE_RECTANGLE_ARB, (1,) )
glget.addGLGetConstant( GL_TEXTURE_BINDING_RECTANGLE_ARB, (1,) )
glget.addGLGetConstant( GL_MAX_RECTANGLE_TEXTURE_SIZE_ARB, (1,) )


def glInitTextureRectangleARB():
    '''Return boolean indicating whether this extension is available'''
    from OpenGL import extensions
    return extensions.hasGLExtension( EXTENSION_NAME )