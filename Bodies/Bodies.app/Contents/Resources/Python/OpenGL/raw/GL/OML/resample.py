'''Autogenerated by get_gl_extensions script, do not edit!'''
from OpenGL import platform as _p
from OpenGL.GL import glget
EXTENSION_NAME = 'GL_OML_resample'
_p.unpack_constants( """GL_PACK_RESAMPLE_OML 0x8984
GL_UNPACK_RESAMPLE_OML 0x8985
GL_RESAMPLE_REPLICATE_OML 0x8986
GL_RESAMPLE_ZERO_FILL_OML 0x8987
GL_RESAMPLE_AVERAGE_OML 0x8988
GL_RESAMPLE_DECIMATE_OML 0x8989""", globals())
glget.addGLGetConstant( GL_PACK_RESAMPLE_OML, (1,) )
glget.addGLGetConstant( GL_UNPACK_RESAMPLE_OML, (1,) )


def glInitResampleOML():
    '''Return boolean indicating whether this extension is available'''
    from OpenGL import extensions
    return extensions.hasGLExtension( EXTENSION_NAME )
