#!/usr/bin/env python
# -*- coding: utf-8 -*-
#-----------------------------------------------------------------------------
# Copyright (C) 2009-2010  Nicolas P. Rougier
#
# Distributed under the terms of the BSD License. The full license is in
# the file COPYING, distributed as part of this software.
#-----------------------------------------------------------------------------
import ctypes, ctypes.util
from ctypes import c_int, c_char_p, c_void_p, py_object, c_char
from constants import *

name = ctypes.util.find_library('AntTweakBar')
if not name:
    raise RuntimeError, 'AntTweakBar library not found'
__dll__ = ctypes.CDLL(name)
try:
    TwInit         = getattr(__dll__,"_TwInit@8")
    TwTerminate    = getattr(__dll__,"_TwTerminate@0")
    TwGetLastError = getattr(__dll__,"_TwGetLastError@0")
    TwNewBar       = getattr(__dll__,"_TwNewBar@4")
    TwDeleteBar    = getattr(__dll__,"_TwDeleteBar@4")
    TwDeleteAllBars= getattr(__dll__,"_TwDeleteAllBars@0")
    TwAddSeparator = getattr(__dll__,"_TwAddSeparator@12")
    TwAddVarRW     = getattr(__dll__,"_TwAddVarRW@20")
    TwAddVarRO     = getattr(__dll__,"_TwAddVarRO@20")
    TwAddVarCB     = getattr(__dll__,"_TwAddVarCB@28")
    TwAddButton    = getattr(__dll__,"_TwAddButton@20")
    TwGetBarName   = getattr(__dll__,"_TwGetBarName@4")
    TwGetParam     = getattr(__dll__,"_TwGetParam@24")
    TwSetParam     = getattr(__dll__,"_TwSetParam@24")
    TwDefineEnum   = getattr(__dll__,"_TwDefineEnum@12")
    TwDefine       = getattr(__dll__,"_TwDefine@4")
    TwDraw         = getattr(__dll__,"_TwDraw@0")
    TwWindowSize   = getattr(__dll__,"_TwWindowSize@8")
    TwRemoveAllVars= getattr(__dll__,"_TwRemoveAllVars@4")
    TwRemoveVar    = getattr(__dll__,"_TwRemoveVar@8")
    TwRefreshBar   = getattr(__dll__,"_TwRefreshBar@4")
    TwSetTopBar    = getattr(__dll__,"_TwSetTopBar@4")
    TwKeyPressed   = getattr(__dll__,"_TwKeyPressed@8")
    TwMouseButton  = getattr(__dll__,"_TwMouseButton@8")
    TwMouseMotion  = getattr(__dll__,"_TwMouseMotion@8")

    TwEventMouseButtonGLUT = getattr(__dll__,"TwEventMouseButtonGLUT")
    TwEventMouseMotionGLUT = getattr(__dll__,"TwEventMouseMotionGLUT")
    TwEventKeyboardGLUT    = getattr(__dll__,"TwEventKeyboardGLUT")
    TwEventSpecialGLUT     = getattr(__dll__,"TwEventSpecialGLUT")
    TwEventMouseWheelGLUT  = getattr(__dll__,"_TwMouseWheel@4")
except:
    TwInit         = __dll__.TwInit
    TwTerminate    = __dll__.TwTerminate
    TwGetLastError = __dll__.TwGetLastError
    TwNewBar       = __dll__.TwNewBar
    TwDeleteBar    = __dll__.TwDeleteBar
    TwDeleteAllBars= __dll__.TwDeleteAllBars
    TwAddSeparator = __dll__.TwAddSeparator
    TwAddVarRW     = __dll__.TwAddVarRW
    TwAddVarRO     = __dll__.TwAddVarRO
    TwAddVarCB     = __dll__.TwAddVarCB
    TwAddButton    = __dll__.TwAddButton
    TwGetBarName   = __dll__.TwGetBarName
    TwGetParam     = __dll__.TwGetParam
    TwSetParam     = __dll__.TwSetParam
    TwDefineEnum   = __dll__.TwDefineEnum
    TwDefine       = __dll__.TwDefine
    TwDraw         = __dll__.TwDraw
    TwWindowSize   = __dll__.TwWindowSize
    TwRemoveAllVars= __dll__.TwRemoveAllVars
    TwRemoveVar    = __dll__.TwRemoveVar
    TwRefreshBar   = __dll__.TwRefreshBar
    TwSetTopBar    = __dll__.TwSetTopBar
    TwKeyPressed   = __dll__.TwKeyPressed
    TwMouseButton  = __dll__.TwMouseButton
    TwMouseMotion  = __dll__.TwMouseMotion
    TwWindowSize   = __dll__.TwWindowSize

    TwEventMouseButtonGLUT = __dll__.TwEventMouseButtonGLUT
    TwEventMouseMotionGLUT = __dll__.TwEventMouseMotionGLUT
    TwEventKeyboardGLUT    = __dll__.TwEventKeyboardGLUT
    TwEventSpecialGLUT     = __dll__.TwEventSpecialGLUT
    TwEventMouseWheelGLUT  = __dll__.TwMouseWheel

# On Mac OS Snow Leopard, the following definitions seems to be necessary to
# ensure 64bits pointers anywhere needed
c_pointer = ctypes.c_ulonglong 

# In case of problem, this definition must be used
#c_pointer = ctypes.c_void_p

TwGetLastError.restype = c_char_p
TwGetBarName.restype = c_char_p
TwNewBar.restype = c_pointer
TwAddSeparator.restype = c_pointer
TwAddSeparator.argtypes = [c_pointer, c_char_p, c_char_p]
TwAddVarRW.restype   = c_pointer
TwAddVarRW.argtypes  = [c_pointer, c_char_p, c_int, c_void_p, c_void_p]
TwAddVarRO.restype   = c_pointer
TwAddVarRO.argtypes  = [c_pointer, c_char_p, c_int, c_void_p, c_void_p]
TwAddVarCB.restype   = c_pointer
TwAddVarCB.argtypes  = [c_pointer, c_char_p, c_int, c_void_p, c_void_p, py_object, c_char_p]
TwAddButton.argtypes = [c_pointer, c_char_p, c_void_p, py_object, c_char_p]
TwRefreshBar.argtypes = [c_pointer]
TwGetParam.restype = c_int
TwGetParam.argtypes =  [c_pointer, c_char_p, c_char_p, c_int, c_int, c_void_p]
TwSetParam.restype = c_int
TwSetParam.argtypes =  [c_pointer, c_char_p, c_char_p, c_int, c_int, c_void_p]
TwEventKeyboardGLUT.argtypes = [c_char, c_int, c_int]
TwEventSpecialGLUT.argtypes  = [c_int, c_int, c_int]


# Callback prototypes
BUTTON_FUNC = ctypes.CFUNCTYPE(c_void_p, c_void_p)
SET_FUNC    = ctypes.CFUNCTYPE(c_void_p, c_void_p, c_void_p)
GET_FUNC    = ctypes.CFUNCTYPE(c_void_p, c_void_p, c_void_p)
ERROR_FUNC  = ctypes.CFUNCTYPE(c_void_p, c_char_p)


# struct TwEnumVal
class TwEnumVal(ctypes.Structure):
    _fields_ = [("Value", c_int), ("Label", c_char_p)]

