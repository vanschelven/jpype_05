# Microsoft Developer Studio Project File - Name="jpype" - Package Owner=<4>
# Microsoft Developer Studio Generated Build File, Format Version 6.00
# ** DO NOT EDIT **

# TARGTYPE "Win32 (x86) Static Library" 0x0104

CFG=jpype - Win32 Debug
!MESSAGE This is not a valid makefile. To build this project using NMAKE,
!MESSAGE use the Export Makefile command and run
!MESSAGE 
!MESSAGE NMAKE /f "jpype.mak".
!MESSAGE 
!MESSAGE You can specify a configuration when running NMAKE
!MESSAGE by defining the macro CFG on the command line. For example:
!MESSAGE 
!MESSAGE NMAKE /f "jpype.mak" CFG="jpype - Win32 Debug"
!MESSAGE 
!MESSAGE Possible choices for configuration are:
!MESSAGE 
!MESSAGE "jpype - Win32 Release" (based on "Win32 (x86) Static Library")
!MESSAGE "jpype - Win32 Debug" (based on "Win32 (x86) Static Library")
!MESSAGE 

# Begin Project
# PROP AllowPerConfigDependencies 0
# PROP Scc_ProjName ""
# PROP Scc_LocalPath ""
CPP=cl.exe
RSC=rc.exe

!IF  "$(CFG)" == "jpype - Win32 Release"

# PROP BASE Use_MFC 0
# PROP BASE Use_Debug_Libraries 0
# PROP BASE Output_Dir "Release"
# PROP BASE Intermediate_Dir "Release"
# PROP BASE Target_Dir ""
# PROP Use_MFC 0
# PROP Use_Debug_Libraries 0
# PROP Output_Dir "Release"
# PROP Intermediate_Dir "Release"
# PROP Target_Dir ""
# ADD BASE CPP /nologo /W3 /GX /O2 /D "WIN32" /D "NDEBUG" /D "_MBCS" /D "_LIB" /YX /FD /c
# ADD CPP /nologo /MD /W3 /GX /O2 /I "c:\tools\jdk\include\win32" /I "c:\tools\jdk\include" /I "e:\darkwolf\jpype\src\native\common\include" /I "c:\tools\jdk5\include\win32" /I "c:\tools\jdk5\include" /I "c:\darkwolf\jpype05\src\native\common\include" /D "WIN32" /D "NDEBUG" /D "_MBCS" /D "_LIB" /YX"jpype.h" /FD /c
# ADD BASE RSC /l 0xc0c /d "NDEBUG"
# ADD RSC /l 0xc0c /d "NDEBUG"
BSC32=bscmake.exe
# ADD BASE BSC32 /nologo
# ADD BSC32 /nologo
LIB32=link.exe -lib
# ADD BASE LIB32 /nologo
# ADD LIB32 /nologo

!ELSEIF  "$(CFG)" == "jpype - Win32 Debug"

# PROP BASE Use_MFC 0
# PROP BASE Use_Debug_Libraries 1
# PROP BASE Output_Dir "Debug"
# PROP BASE Intermediate_Dir "Debug"
# PROP BASE Target_Dir ""
# PROP Use_MFC 0
# PROP Use_Debug_Libraries 1
# PROP Output_Dir "Debug"
# PROP Intermediate_Dir "Debug"
# PROP Target_Dir ""
# ADD BASE CPP /nologo /W3 /Gm /GX /ZI /Od /D "WIN32" /D "_DEBUG" /D "_MBCS" /D "_LIB" /YX /FD /GZ /c
# ADD CPP /nologo /MDd /W3 /Gm /GX /ZI /Od /I "c:\tools\jdk5\include\win32" /I "c:\tools\jdk5\include" /I "c:\darkwolf\jpype05\src\native\common\include" /D "WIN32" /D "_DEBUG" /D "_MBCS" /D "_LIB" /YX"jpype.h" /FD /GZ /c
# ADD BASE RSC /l 0xc0c /d "_DEBUG"
# ADD RSC /l 0xc0c /d "_DEBUG"
BSC32=bscmake.exe
# ADD BASE BSC32 /nologo
# ADD BSC32 /nologo
LIB32=link.exe -lib
# ADD BASE LIB32 /nologo
# ADD LIB32 /nologo

!ENDIF 

# Begin Target

# Name "jpype - Win32 Release"
# Name "jpype - Win32 Debug"
# Begin Group "Source Files"

# PROP Default_Filter "cpp;c;cxx;rc;def;r;odl;idl;hpj;bat"
# Begin Source File

SOURCE=..\..\src\native\common\jp_array.cpp
# End Source File
# Begin Source File

SOURCE=..\..\src\native\common\jp_arrayclass.cpp
# End Source File
# Begin Source File

SOURCE=..\..\src\native\common\jp_class.cpp
# End Source File
# Begin Source File

SOURCE=..\..\src\native\common\jp_classbase.cpp
# End Source File
# Begin Source File

SOURCE=..\..\src\native\common\jp_env.cpp
# End Source File
# Begin Source File

SOURCE=..\..\src\native\common\jp_field.cpp
# End Source File
# Begin Source File

SOURCE=..\..\src\native\common\jp_invocationhandler.cpp
# End Source File
# Begin Source File

SOURCE=..\..\src\native\common\jp_javaenv.cpp
# End Source File
# Begin Source File

SOURCE=..\..\src\native\common\jp_javaenv_autogen.cpp
# End Source File
# Begin Source File

SOURCE=..\..\src\native\common\jp_jniutil.cpp
# End Source File
# Begin Source File

SOURCE=..\..\src\native\common\jp_method.cpp
# End Source File
# Begin Source File

SOURCE=..\..\src\native\common\jp_methodoverload.cpp
# End Source File
# Begin Source File

SOURCE=..\..\src\native\common\jp_monitor.cpp
# End Source File
# Begin Source File

SOURCE=..\..\src\native\common\jp_object.cpp
# End Source File
# Begin Source File

SOURCE=..\..\src\native\common\jp_objecttypes.cpp
# End Source File
# Begin Source File

SOURCE=..\..\src\native\common\jp_platform_linux.cpp
# End Source File
# Begin Source File

SOURCE=..\..\src\native\common\jp_platform_win32.cpp
# End Source File
# Begin Source File

SOURCE=..\..\src\native\common\jp_primitivetypes.cpp
# End Source File
# Begin Source File

SOURCE=..\..\src\native\common\jp_primitivetypes_autogen.cpp
# End Source File
# Begin Source File

SOURCE=..\..\src\native\common\jp_proxy.cpp
# End Source File
# Begin Source File

SOURCE=..\..\src\native\common\jp_typemanager.cpp
# End Source File
# Begin Source File

SOURCE=..\..\src\native\common\jp_typename.cpp
# End Source File
# Begin Source File

SOURCE=..\..\src\native\common\jp_voidtype.cpp
# End Source File
# End Group
# Begin Group "Header Files"

# PROP Default_Filter "h;hpp;hxx;hm;inl"
# Begin Source File

SOURCE=..\..\src\native\common\include\jp_array.h
# End Source File
# Begin Source File

SOURCE=..\..\src\native\common\include\jp_arrayclass.h
# End Source File
# Begin Source File

SOURCE=..\..\src\native\common\include\jp_class.h
# End Source File
# Begin Source File

SOURCE=..\..\src\native\common\include\jp_classbase.h
# End Source File
# Begin Source File

SOURCE=..\..\src\native\common\include\jp_env.h
# End Source File
# Begin Source File

SOURCE=..\..\src\native\common\include\jp_field.h
# End Source File
# Begin Source File

SOURCE=..\..\src\native\common\include\jp_hostenv.h
# End Source File
# Begin Source File

SOURCE=..\..\src\native\common\include\jp_invocationhandler.h
# End Source File
# Begin Source File

SOURCE=..\..\src\native\common\include\jp_javaenv.h
# End Source File
# Begin Source File

SOURCE=..\..\src\native\common\include\jp_javaenv_autogen.h
# End Source File
# Begin Source File

SOURCE=..\..\src\native\common\include\jp_jniutil.h
# End Source File
# Begin Source File

SOURCE=..\..\src\native\common\include\jp_method.h
# End Source File
# Begin Source File

SOURCE=..\..\src\native\common\include\jp_methodoverload.h
# End Source File
# Begin Source File

SOURCE=..\..\src\native\common\include\jp_monitor.h
# End Source File
# Begin Source File

SOURCE=..\..\src\native\common\include\jp_object.h
# End Source File
# Begin Source File

SOURCE=..\..\src\native\common\include\jp_objectbase.h
# End Source File
# Begin Source File

SOURCE=..\..\src\native\common\include\jp_objecttypes.h
# End Source File
# Begin Source File

SOURCE=..\..\src\native\common\include\jp_platform_linux.h
# End Source File
# Begin Source File

SOURCE=..\..\src\native\common\include\jp_platform_win32.h
# End Source File
# Begin Source File

SOURCE=..\..\src\native\common\include\jp_primitivetypes.h
# End Source File
# Begin Source File

SOURCE=..\..\src\native\common\include\jp_proxy.h
# End Source File
# Begin Source File

SOURCE=..\..\src\native\common\include\jp_type.h
# End Source File
# Begin Source File

SOURCE=..\..\src\native\common\include\jp_typemanager.h
# End Source File
# Begin Source File

SOURCE=..\..\src\native\common\include\jp_typename.h
# End Source File
# Begin Source File

SOURCE=..\..\src\native\common\include\jp_utility.h
# End Source File
# Begin Source File

SOURCE=..\..\src\native\common\include\jpype.h
# End Source File
# End Group
# End Target
# End Project
