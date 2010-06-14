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
import os, array

CHUNK = 20

def _outputChunk(fout, l, isFirst=0) :
    line = []
    if not isFirst :
        line.append("    ")
    else:
        print >> fout, "   ",

    buffer = array.array("B")
    buffer.fromstring(l)
    
    for i in buffer :
        line.append( "(jbyte)0x%02X" % i )
    
    print >> fout, ",".join(line)

def dumpClass(output, name, data) :
    print output, name
    
    # Header
    f = open(output+os.sep+name+".cpp", "w+")
    try :
        print >> f, "#include <jpype.h>"
        print >> f, "jbyte %s[] = {" % name
        
        i = 0
        sz = len(data)
        while (i < sz) :
            sub = data[i:i+CHUNK]
            _outputChunk(f, sub, i == 0)
            i = i + CHUNK
        
        print >> f, "};"
        print >> f
        print >> f, "jsize get_%s_size() { return %d; }" % (name, len(data))
        
    finally :
        f.close()