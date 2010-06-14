#*****************************************************************************
#   Copyright 2004-2008 Steve Menard
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.
#   
#*****************************************************************************
import sys, os, os.path
from zipfile import *
import dumpjavaclass

def generateJar(jar, prefix, output) :
    if not os.path.exists(output) :
        os.makedirs(output)
    if not os.path.exists(output+os.sep+"include") :
        os.makedirs(output+os.sep+"include")
        
    names = []
    zf = ZipFile(jar, 'r')
    try :
        for i in zf.namelist() :
            if i[-6:] == '.class' :
                data = zf.read(i)
                name = i[:-6].replace('/', '_')
                dumpjavaclass.dumpClass(output, name, data)
                names.append(name)
    finally :
        zf.close()
        
    f = open(output+os.sep+"include"+os.sep+prefix+".h", "w+")
    try :
        for i in names :
            print >> f, "extern jbyte %s[];" % i
        print >> f
        for i in names :
            print >> f, "jsize get_%s_size();" % i
            
        print >> f
        print >> f, "void define_%s_classes();" % prefix
    finally :
        f.close()

    f = open(output+os.sep+prefix+".cpp", "w+")
    try :
        print >> f, "#include <jpype.h>"
        print >> f, '#include "include%s%s.h"' % (os.sep, prefix)
        print >> f
        print >> f, "void define_%s_classes()" % prefix
        print >> f, "{"
        print >> f, "    jobject cl = JPJNIClass::getSystemClassLoader();"
        print >> f, "    jclass newClass;"
        for i in names :
            print >> f, '    newClass = JPEnv::getJava()->DefineClass("%s", cl, %s, get_%s_size());' % ( i.replace('_', '/'), i, i)
            
        print >> f, "}"
    finally :
        f.close()
    