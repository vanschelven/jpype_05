# Microsoft Developer Studio Project File - Name="jpypepython" - Package Owner=<4>
# Microsoft Developer Studio Generated Build File, Format Version 6.00
# ** DO NOT EDIT **

# TARGTYPE "Win32 (x86) Dynamic-Link Library" 0x0102

CFG=jpypepython - Win32 Debug
!MESSAGE This is not a valid makefile. To build this project using NMAKE,
!MESSAGE use the Export Makefile command and run
!MESSAGE 
!MESSAGE NMAKE /f "jpypepython.mak".
!MESSAGE 
!MESSAGE You can specify a configuration when running NMAKE
!MESSAGE by defining the macro CFG on the command line. For example:
!MESSAGE 
!MESSAGE NMAKE /f "jpypepython.mak" CFG="jpypepython - Win32 Debug"
!MESSAGE 
!MESSAGE Possible choices for configuration are:
!MESSAGE 
!MESSAGE "jpypepython - Win32 Release" (based on "Win32 (x86) Dynamic-Link Library")
!MESSAGE "jpypepython - Win32 Debug" (based on "Win32 (x86) Dynamic-Link Library")
!MESSAGE 

# Begin Project
# PROP AllowPerConfigDependencies 0
# PROP Scc_ProjName ""
# PROP Scc_LocalPath ""
CPP=cl.exe
MTL=midl.exe
RSC=rc.exe

!IF  "$(CFG)" == "jpypepython - Win32 Release"

# PROP BASE Use_MFC 0
# PROP BASE Use_Debug_Libraries 0
# PROP BASE Output_Dir "Release"
# PROP BASE Intermediate_Dir "Release"
# PROP BASE Target_Dir ""
# PROP Use_MFC 0
# PROP Use_Debug_Libraries 0
# PROP Output_Dir "Release"
# PROP Intermediate_Dir "Release"
# PROP Ignore_Export_Lib 0
# PROP Target_Dir ""
# ADD BASE CPP /nologo /MT /W3 /GX /O2 /D "WIN32" /D "NDEBUG" /D "_WINDOWS" /D "_MBCS" /D "_USRDLL" /D "JPYPEPYTHON_EXPORTS" /YX /FD /c
# ADD CPP /nologo /MDd /W3 /GX /O2 /I "c:\tools\jdk5\include\win32" /I "c:\tools\jdk5\include" /I "c:\darkwolf\jpype05\src\native\common\include" /I "c:\darkwolf\jpype05\src\native\python\include" /I "c:\tools\python23\include" /D "WIN32" /D "NDEBUG" /D "_WINDOWS" /D "_MBCS" /D "_USRDLL" /D "JPYPEPYTHON_EXPORTS" /YX"jpype_python.h" /FD /c
# ADD BASE MTL /nologo /D "NDEBUG" /mktyplib203 /win32
# ADD MTL /nologo /D "NDEBUG" /mktyplib203 /win32
# ADD BASE RSC /l 0xc0c /d "NDEBUG"
# ADD RSC /l 0xc0c /d "NDEBUG"
BSC32=bscmake.exe
# ADD BASE BSC32 /nologo
# ADD BSC32 /nologo
LINK32=link.exe
# ADD BASE LINK32 kernel32.lib user32.lib gdi32.lib winspool.lib comdlg32.lib advapi32.lib shell32.lib ole32.lib oleaut32.lib uuid.lib odbc32.lib odbccp32.lib /nologo /dll /machine:I386
# ADD LINK32 kernel32.lib user32.lib gdi32.lib winspool.lib comdlg32.lib advapi32.lib shell32.lib ole32.lib oleaut32.lib uuid.lib odbc32.lib odbccp32.lib /nologo /dll /incremental:yes /machine:I386 /nodefaultlib:"library" /libpath:"c:\tools\python23\libs"
# SUBTRACT LINK32 /pdb:none
# Begin Custom Build
TargetPath=.\Release\jpypepython.dll
InputPath=.\Release\jpypepython.dll
SOURCE="$(InputPath)"

"c:\tools\python\Lib\site-packages\_jpype.pyd" : $(SOURCE) "$(INTDIR)" "$(OUTDIR)"
	copy $(TargetPath) c:\tools\python\Lib\site-packages\_jpype.pyd

# End Custom Build

!ELSEIF  "$(CFG)" == "jpypepython - Win32 Debug"

# PROP BASE Use_MFC 0
# PROP BASE Use_Debug_Libraries 1
# PROP BASE Output_Dir "Debug"
# PROP BASE Intermediate_Dir "Debug"
# PROP BASE Target_Dir ""
# PROP Use_MFC 0
# PROP Use_Debug_Libraries 1
# PROP Output_Dir "Debug"
# PROP Intermediate_Dir "Debug"
# PROP Ignore_Export_Lib 0
# PROP Target_Dir ""
# ADD BASE CPP /nologo /MTd /W3 /Gm /GX /ZI /Od /D "WIN32" /D "_DEBUG" /D "_WINDOWS" /D "_MBCS" /D "_USRDLL" /D "JPYPEPYTHON_EXPORTS" /YX /FD /GZ /c
# ADD CPP /nologo /MDd /W3 /Gm /GX /ZI /Od /I "c:\tools\jdk5\include\win32" /I "c:\tools\jdk5\include" /I "c:\darkwolf\jpype05\src\native\common\include" /I "c:\darkwolf\jpype05\src\native\python\include" /I "c:\tools\python23\include" /D "WIN32" /D "_DEBUG" /D "_WINDOWS" /D "_MBCS" /D "_USRDLL" /D "JPYPEPYTHON_EXPORTS" /FR /YX"jpype_python.h" /FD /GZ /c
# ADD BASE MTL /nologo /D "_DEBUG" /mktyplib203 /win32
# ADD MTL /nologo /D "_DEBUG" /mktyplib203 /win32
# ADD BASE RSC /l 0xc0c /d "_DEBUG"
# ADD RSC /l 0xc0c /d "_DEBUG"
BSC32=bscmake.exe
# ADD BASE BSC32 /nologo
# ADD BSC32 /nologo
LINK32=link.exe
# ADD BASE LINK32 kernel32.lib user32.lib gdi32.lib winspool.lib comdlg32.lib advapi32.lib shell32.lib ole32.lib oleaut32.lib uuid.lib odbc32.lib odbccp32.lib /nologo /dll /debug /machine:I386 /pdbtype:sept
# ADD LINK32 kernel32.lib user32.lib gdi32.lib winspool.lib comdlg32.lib advapi32.lib shell32.lib ole32.lib oleaut32.lib uuid.lib odbc32.lib odbccp32.lib /nologo /dll /debug /machine:I386 /pdbtype:sept /libpath:"c:\tools\python\Lib" /libpath:"c:\tools\python\libs"
# Begin Custom Build
TargetPath=.\Debug\jpypepython.dll
InputPath=.\Debug\jpypepython.dll
SOURCE="$(InputPath)"

"c:\tools\python\Lib\site-packages\_jpype_d.pyd" : $(SOURCE) "$(INTDIR)" "$(OUTDIR)"
	copy $(TargetPath) c:\tools\python\Lib\site-packages\_jpype_d.pyd

# End Custom Build

!ENDIF 

# Begin Target

# Name "jpypepython - Win32 Release"
# Name "jpypepython - Win32 Debug"
# Begin Group "Source Files"

# PROP Default_Filter "cpp;c;cxx;rc;def;r;odl;idl;hpj;bat"
# Begin Source File

SOURCE=..\..\src\native\python\jpype_javaarray.cpp
# End Source File
# Begin Source File

SOURCE=..\..\src\native\python\jpype_javaclass.cpp
# End Source File
# Begin Source File

SOURCE=..\..\src\native\python\jpype_module.cpp
# End Source File
# Begin Source File

SOURCE=..\..\src\native\python\jpype_python.cpp
# ADD CPP /YX
# End Source File
# Begin Source File

SOURCE=..\..\src\native\python\py_class.cpp
# End Source File
# Begin Source File

SOURCE=..\..\src\native\python\py_field.cpp
# End Source File
# Begin Source File

SOURCE=..\..\src\native\python\py_hostenv.cpp
# ADD CPP /YX
# End Source File
# Begin Source File

SOURCE=..\..\src\native\python\py_method.cpp
# End Source File
# Begin Source File

SOURCE=..\..\src\native\python\py_monitor.cpp
# End Source File
# Begin Source File

SOURCE=..\..\src\native\python\pythonenv.cpp
# ADD CPP /YX
# End Source File
# End Group
# Begin Group "Header Files"

# PROP Default_Filter "h;hpp;hxx;hm;inl"
# Begin Source File

SOURCE=..\..\src\native\python\include\jpype_python.h
# End Source File
# Begin Source File

SOURCE=..\..\src\native\python\include\py_exception.h
# End Source File
# Begin Source File

SOURCE=..\..\src\native\python\include\py_hostenv.h
# End Source File
# Begin Source File

SOURCE=..\..\src\native\python\include\py_monitor.h
# End Source File
# Begin Source File

SOURCE=..\..\src\native\python\include\pythonenv.h
# End Source File
# End Group
# Begin Group "Resource Files"

# PROP Default_Filter "ico;cur;bmp;dlg;rc2;rct;bin;rgs;gif;jpg;jpeg;jpe"
# End Group
# End Target
# End Project
