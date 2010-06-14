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
import dumpclass



if __name__== '__main__' :
    root = os.path.dirname(__file__)
    dumpclass.generateJar(
        "%s%sasm-1.5.1.jar" % (root, os.sep), 
        "jasm", 
        "%s%s..%ssrc%snative%scommon%sjasm" % ( root, os.sep, os.sep, os.sep, os.sep, os.sep)
        )