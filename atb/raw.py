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
    TwAddButton                 = getattr(__dll__,"_TwAddButton@20")
    TwAddSeparator              = getattr(__dll__,"_TwAddSeparator@12")
    TwAddVarCB                  = getattr(__dll__,"_TwAddVarCB@28")
    TwAddVarRO                  = getattr(__dll__,"_TwAddVarRO@20")
    TwAddVarRW                  = getattr(__dll__,"_TwAddVarRW@20")
    TwCopyCDStringToClientFunc  = getattr(__dll__,"_TwCopyCDStringToClientFunc@4")
    TwCopyCDStringToLibrary     = getattr(__dll__,"_TwCopyCDStringToLibrary@8")
    TwCopyStdStringToClientFunc = getattr(__dll__,"_TwCopyStdStringToClientFunc@4")
    TwCopyStdStringToLibrary    = getattr(__dll__,"_TwCopyStdStringToLibrary@8")
    TwDefine                    = getattr(__dll__,"_TwDefine@4")
    TwDefineEnum                = getattr(__dll__,"_TwDefineEnum@12")
    TwDefineEnumFromString      = getattr(__dll__,"_TwDefineEnumFromString@8")
    TwDefineStruct              = getattr(__dll__,"_TwDefineStruct@24")
    TwDeleteAllBars             = getattr(__dll__,"_TwDeleteAllBars@0")
    TwDeleteBar                 = getattr(__dll__,"_TwDeleteBar@4")
    TwDraw                      = getattr(__dll__,"_TwDraw@0")
    wEventCharGLFW              = getattr(__dll__,"_TwEventCharGLFW@8")
    TwEventKeyGLFW              = getattr(__dll__,"_TwEventKeyGLFW@8")
    TwEventMouseButtonGLFW      = getattr(__dll__,"_TwEventMouseButtonGLFW@8")
    TwEventSDL                  = getattr(__dll__,"_TwEventSDL@12")
    TwEventSFML                 = getattr(__dll__,"_TwEventSFML@12")
    TwEventWin32                = getattr(__dll__,"_TwEventWin32@16")
    TwEventWin                  = getattr(__dll__,"_TwEventWin@16")
    TwGLUTModifiersFunc         = getattr(__dll__,"_TwGLUTModifiersFunc@4")
    TwGetBarByIndex             = getattr(__dll__,"_TwGetBarByIndex@4")
    TwGetBarByName              = getattr(__dll__,"_TwGetBarByName@4")
    TwGetBarCount               = getattr(__dll__,"_TwGetBarCount@0")
    TwGetBarName                = getattr(__dll__,"_TwGetBarName@4")
    TwGetBottomBar              = getattr(__dll__,"_TwGetBottomBar@0")
    TwGetCurrentWindow          = getattr(__dll__,"_TwGetCurrentWindow@0")
    TwGetLastError              = getattr(__dll__,"_TwGetLastError@0")
    TwGetParam                  = getattr(__dll__,"_TwGetParam@24")
    TwGetTopBar                 = getattr(__dll__,"_TwGetTopBar@0")
    TwHandleErrors              = getattr(__dll__,"_TwHandleErrors@4")
    TwInit                      = getattr(__dll__,"_TwInit@8")
    TwKeyPressed                = getattr(__dll__,"_TwKeyPressed@8")
    TwKeyTest                   = getattr(__dll__,"_TwKeyTest@8")
    TwMouseButton               = getattr(__dll__,"_TwMouseButton@8")
    TwMouseMotion               = getattr(__dll__,"_TwMouseMotion@8")
    TwMouseWheel                = getattr(__dll__,"_TwMouseWheel@4")
    TwNewBar                    = getattr(__dll__,"_TwNewBar@4")
    TwRefreshBar                = getattr(__dll__,"_TwRefreshBar@4")
    TwRemoveAllVars             = getattr(__dll__,"_TwRemoveAllVars@4")
    TwRemoveVar                 = getattr(__dll__,"_TwRemoveVar@8")
    TwSetBottomBar              = getattr(__dll__,"_TwSetBottomBar@4")
    TwSetCurrentWindow          = getattr(__dll__,"_TwSetCurrentWindow@4")
    TwSetParam                  = getattr(__dll__,"_TwSetParam@24")
    TwSetTopBar                 = getattr(__dll__,"_TwSetTopBar@4")
    TwTerminate                 = getattr(__dll__,"_TwTerminate@0")
    TwWindowExists              = getattr(__dll__,"_TwWindowExists@4")
    TwWindowSize                = getattr(__dll__,"_TwWindowSize@8")

    TwEventCharGLFWcdecl        = getattr(__dll__,"TwEventCharGLFWcdecl")
    TwEventKeyGLFWcdecl         = getattr(__dll__,"TwEventKeyGLFWcdecl")
    TwEventKeyboardGLUT         = getattr(__dll__,"TwEventKeyboardGLUT")
    TwEventMouseButtonGLFWcdecl = getattr(__dll__,"TwEventMouseButtonGLFWcdecl")
    TwEventMouseButtonGLUT      = getattr(__dll__,"TwEventMouseButtonGLUT")
    TwEventMouseMotionGLUT      = getattr(__dll__,"TwEventMouseMotionGLUT")
    TwEventMousePosGLFWcdecl    = getattr(__dll__,"TwEventMousePosGLFWcdecl")
    TwEventMouseWheelGLFWcdecl  = getattr(__dll__,"TwEventMouseWheelGLFWcdecl")
    TwEventSpecialGLUT          = getattr(__dll__,"TwEventSpecialGLUT")
except:
    TwAddButton                 = getattr(__dll__,"TwAddButton")
    TwAddSeparator              = getattr(__dll__,"TwAddSeparator")
    TwAddVarCB                  = getattr(__dll__,"TwAddVarCB")
    TwAddVarRO                  = getattr(__dll__,"TwAddVarRO")
    TwAddVarRW                  = getattr(__dll__,"TwAddVarRW")
    TwCopyCDStringToClientFunc  = getattr(__dll__,"TwCopyCDStringToClientFunc")
    TwCopyCDStringToLibrary     = getattr(__dll__,"TwCopyCDStringToLibrary")
    TwCopyStdStringToClientFunc = getattr(__dll__,"TwCopyStdStringToClientFunc")
    TwCopyStdStringToLibrary    = getattr(__dll__,"TwCopyStdStringToLibrary")
    TwDefine                    = getattr(__dll__,"TwDefine")
    TwDefineEnum                = getattr(__dll__,"TwDefineEnum")
    TwDefineEnumFromString      = getattr(__dll__,"TwDefineEnumFromString")
    TwDefineStruct              = getattr(__dll__,"TwDefineStruct")
    TwDeleteAllBars             = getattr(__dll__,"TwDeleteAllBars")
    TwDeleteBar                 = getattr(__dll__,"TwDeleteBar")
    TwDraw                      = getattr(__dll__,"TwDraw")
    wEventCharGLFW              = getattr(__dll__,"TwEventCharGLFW")
    TwEventKeyGLFW              = getattr(__dll__,"TwEventKeyGLFW")
    TwEventMouseButtonGLFW      = getattr(__dll__,"TwEventMouseButtonGLFW")
    TwEventSDL                  = getattr(__dll__,"TwEventSDL")
    TwEventSFML                 = getattr(__dll__,"TwEventSFML")
    try:
        TwEventWin32                = getattr(__dll__,"TwEventWin32")
        TwEventWin                  = getattr(__dll__,"TwEventWin")
    except:
        pass
    TwGLUTModifiersFunc         = getattr(__dll__,"TwGLUTModifiersFunc")
    TwGetBarByIndex             = getattr(__dll__,"TwGetBarByIndex")
    TwGetBarByName              = getattr(__dll__,"TwGetBarByName")
    TwGetBarCount               = getattr(__dll__,"TwGetBarCount")
    TwGetBarName                = getattr(__dll__,"TwGetBarName")
    TwGetBottomBar              = getattr(__dll__,"TwGetBottomBar")
    TwGetCurrentWindow          = getattr(__dll__,"TwGetCurrentWindow")
    TwGetLastError              = getattr(__dll__,"TwGetLastError")
    TwGetParam                  = getattr(__dll__,"TwGetParam")
    TwGetTopBar                 = getattr(__dll__,"TwGetTopBar")
    TwHandleErrors              = getattr(__dll__,"TwHandleErrors")
    TwInit                      = getattr(__dll__,"TwInit")
    TwKeyPressed                = getattr(__dll__,"TwKeyPressed")
    TwKeyTest                   = getattr(__dll__,"TwKeyTest")
    TwMouseButton               = getattr(__dll__,"TwMouseButton")
    TwMouseMotion               = getattr(__dll__,"TwMouseMotion")
    TwMouseWheel                = getattr(__dll__,"TwMouseWheel")
    TwNewBar                    = getattr(__dll__,"TwNewBar")
    TwRefreshBar                = getattr(__dll__,"TwRefreshBar")
    TwRemoveAllVars             = getattr(__dll__,"TwRemoveAllVars")
    TwRemoveVar                 = getattr(__dll__,"TwRemoveVar")
    TwSetBottomBar              = getattr(__dll__,"TwSetBottomBar")
    TwSetCurrentWindow          = getattr(__dll__,"TwSetCurrentWindow")
    TwSetParam                  = getattr(__dll__,"TwSetParam")
    TwSetTopBar                 = getattr(__dll__,"TwSetTopBar")
    TwTerminate                 = getattr(__dll__,"TwTerminate")
    TwWindowExists              = getattr(__dll__,"TwWindowExists")
    TwWindowSize                = getattr(__dll__,"TwWindowSize")

    try:
        TwEventCharGLFWcdecl        = getattr(__dll__,"TwEventCharGLFWcdecl")
        TwEventKeyGLFWcdecl         = getattr(__dll__,"TwEventKeyGLFWcdecl")
    except:pass
    TwEventKeyboardGLUT         = getattr(__dll__,"TwEventKeyboardGLUT")
    try:
        TwEventMouseButtonGLFWcdecl = getattr(__dll__,"TwEventMouseButtonGLFWcdecl")
    except:pass
    TwEventMouseButtonGLUT      = getattr(__dll__,"TwEventMouseButtonGLUT")
    TwEventMouseMotionGLUT      = getattr(__dll__,"TwEventMouseMotionGLUT")
    try:
        TwEventMousePosGLFWcdecl    = getattr(__dll__,"TwEventMousePosGLFWcdecl")
        TwEventMouseWheelGLFWcdecl  = getattr(__dll__,"TwEventMouseWheelGLFWcdecl")
    except:pass
    TwEventSpecialGLUT          = getattr(__dll__,"TwEventSpecialGLUT")

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

