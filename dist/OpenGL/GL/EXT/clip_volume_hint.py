'''OpenGL extension EXT.clip_volume_hint

This module customises the behaviour of the 
OpenGL.raw.GL.EXT.clip_volume_hint to provide a more 
Python-friendly API

Overview (from the spec)
	
	EXT_clip_volume_hint provides a mechanism for applications to
	indicate that they do not require clip volume clipping for
	primitives. It allows applications to maximize performance in
	situations where they know that clipping is unnecessary.
	EXT_clip_volume_hint is only an indication, though, and
	implementations are free to ignore it.

The official definition of this extension is available here:
http://www.opengl.org/registry/specs/EXT/clip_volume_hint.txt
'''
from OpenGL import platform, constants, constant, arrays
from OpenGL import extensions, wrapper
from OpenGL.GL import glget
import ctypes
from OpenGL.raw.GL.EXT.clip_volume_hint import *
### END AUTOGENERATED SECTION