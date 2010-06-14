# this file generates the "boilerplate" code for JPype.
#
# I am using this low-tech method to get rid of pre-processor differences ...
import types

COPYRIGHT = """
/*****************************************************************************
   Copyright 2004-2008 Steve Menard
   
   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
   
*****************************************************************************/   
"""

# {{0}} = ct {{1}} = jt {{2}} = t
TYPE_METHODS_DECL = """
    /** GetStatic{{2}}Field */
    {{1}} GetStatic{{2}}Field(jclass clazz, jfieldID fid); 
    
    /** Get{{2}}Field */
    {{1}} Get{{2}}Field(jobject clazz, jfieldID fid); 
    
    /** SetStatic{{2}}Field */
    void SetStatic{{2}}Field(jclass clazz, jfieldID fid, {{3}} val); 
    
    /** Set{{2}}Field */
    void Set{{2}}Field(jobject clazz, jfieldID fid, {{3}} val); 
    
    /** CallStatic{{2}}MethodA */
    {{1}} CallStatic{{2}}MethodA(jclass clazz, jmethodID mid, jvalue* val); 
    
    /** CallStatic{{2}}Method */
    {{1}} CallStatic{{2}}Method(jclass clazz, jmethodID mid); 
    
    /** Call{{2}}MethodA */
    {{1}} Call{{2}}MethodA(jobject obj, jmethodID mid, jvalue* val); 
    
    /** Call{{2}}Method */
    {{1}} Call{{2}}Method(jobject obj, jmethodID mid);

    /** Call{{2}}MethodA */
    {{1}} CallNonvirtual{{2}}MethodA(jobject obj, jclass claz, jmethodID mid, jvalue* val); 
    
    /** Call{{2}}Method */
    {{1}} CallNonvirtual{{2}}Method(jobject obj, jclass claz, jmethodID mid);
"""

# {{0}} = ct {{1}} = jt {{2}} = t
PRIMITIVE_ARRAY_METHODS_DECL = """
    /** New{{2}}Array */
    {{1}}Array New{{2}}Array(jint len); 
    
    /** Set{{2}}ArrayRegion */
    void Set{{2}}ArrayRegion({{1}}Array array, int start, int len, {{1}}* vals); 

    /** Get{{2}}ArrayRegion */
    void Get{{2}}ArrayRegion({{1}}Array array, int start, int len, {{1}}* vals); 

    /** Get{{2}}ArrayElements */
    {{1}}* Get{{2}}ArrayElements({{1}}Array array, jboolean* isCopy);

    /** Release{{2}}ArrayElements */
    void Release{{2}}ArrayElements({{1}}Array, {{1}}* v, jint mode);
"""

# {{0}} = ct {{1}} = jt {{2}} = t
TYPE_METHODS = """
{{1}} JPJavaEnv::GetStatic{{2}}Field(jclass clazz, jfieldID fid) 
{
    JNIEnv* env = getJNIEnv(); 
    {{1}} res = env->functions->GetStatic{{2}}Field(env, clazz, fid);
    JAVA_CHECK("GetStatic{{2}}Field");
    return res;
}

{{1}} JPJavaEnv::Get{{2}}Field(jobject clazz, jfieldID fid)
{
    JNIEnv* env = getJNIEnv(); 
    {{1}} res = env->functions->Get{{2}}Field(env, clazz, fid);
    JAVA_CHECK("Get{{2}}Field");
    return res;
}
void JPJavaEnv::SetStatic{{2}}Field(jclass clazz, jfieldID fid, {{3}} val)
{
    JNIEnv* env = getJNIEnv(); 
    env->functions->SetStatic{{2}}Field(env, clazz, fid, val{{4}});
    JAVA_CHECK("SetStatic{{2}}Field");
}

void JPJavaEnv::Set{{2}}Field(jobject clazz, jfieldID fid, {{3}} val)
{
    JNIEnv* env = getJNIEnv(); 
    env->functions->Set{{2}}Field(env, clazz, fid, val{{4}});
    JAVA_CHECK("Set{{2}}Field"); 
}

{{1}} JPJavaEnv::CallStatic{{2}}MethodA(jclass clazz, jmethodID mid, jvalue* val)
{
    PREPARE_EXTERNAL 
    res = env->functions->CallStatic{{2}}MethodA(env, clazz, mid, val); 
    RETURN_EXTERNAL 
}

{{1}} JPJavaEnv::CallStatic{{2}}Method(jclass clazz, jmethodID mid)
{
    PREPARE_EXTERNAL 
    res = env->functions->CallStatic{{2}}Method(env, clazz, mid); 
    RETURN_EXTERNAL 
}

{{1}} JPJavaEnv::Call{{2}}MethodA(jobject obj, jmethodID mid, jvalue* val)
{
    PREPARE_EXTERNAL 
    res = env->functions->Call{{2}}MethodA(env, obj, mid, val); 
    RETURN_EXTERNAL 
}

{{1}} JPJavaEnv::Call{{2}}Method(jobject obj, jmethodID mid)
{
    PREPARE_EXTERNAL 
    res = env->functions->Call{{2}}Method(env, obj, mid); 
    RETURN_EXTERNAL 
}

{{1}} JPJavaEnv::CallNonvirtual{{2}}MethodA(jobject obj, jclass claz, jmethodID mid, jvalue* val)
{
    PREPARE_EXTERNAL 
    res = env->functions->CallNonvirtual{{2}}MethodA(env, obj, claz, mid, val); 
    RETURN_EXTERNAL 
}

{{1}} JPJavaEnv::CallNonvirtual{{2}}Method(jobject obj, jclass claz, jmethodID mid)
{
    PREPARE_EXTERNAL 
    res = env->functions->CallNonvirtual{{2}}Method(env, obj, claz, mid); 
    RETURN_EXTERNAL 
}
"""   

# {{0}} = ct {{1}} = jt {{2}} = t
PRIMITIVE_ARRAY_METHODS = """
{{1}}Array JPJavaEnv::New{{2}}Array(jint len)
{
    JNIEnv* env = getJNIEnv(); 
    {{1}}Array res = env->functions->New{{2}}Array(env, len);
    JAVA_CHECK("New{{2}}Array");
    return res;
}

void JPJavaEnv::Set{{2}}ArrayRegion({{1}}Array array, int start, int len, {{1}}* vals)
{
    JNIEnv* env = getJNIEnv(); 
    env->functions->Set{{2}}ArrayRegion(env, array, start, len, vals);
    JAVA_CHECK("Set{{2}}ArrayRegion");
}

void JPJavaEnv::Get{{2}}ArrayRegion({{1}}Array array, int start, int len, {{1}}* vals)
{
    JNIEnv* env = getJNIEnv(); 
    env->functions->Get{{2}}ArrayRegion(env, array, start, len, vals);
    JAVA_CHECK("Get{{2}}ArrayRegion");
}

{{1}}* JPJavaEnv::Get{{2}}ArrayElements({{1}}Array array, jboolean* isCopy)
{
    JNIEnv* env = getJNIEnv(); 
    {{1}}* res = env->functions->Get{{2}}ArrayElements(env, array, isCopy);
    JAVA_CHECK("Get{{2}}ArrayElements");
    return res;
}

void JPJavaEnv::Release{{2}}ArrayElements({{1}}Array array, {{1}}* v, jint mode)
{
    JNIEnv* env = getJNIEnv(); 
    env->functions->Release{{2}}ArrayElements(env, array, v, mode);
    JAVA_CHECK("Release{{2}}ArrayElements");
}
"""    

TYPE_BLOCK = """
jarray JP{{0}}Type::newArrayInstance(int sz)
{
    return JPEnv::getJava()->New{{0}}Array(sz);
}

HostRef* JP{{0}}Type::getStaticValue(jclass c, jfieldID fid, JPTypeName& tgtType) 
{
    jvalue v;
    v.{{1}} = JPEnv::getJava()->GetStatic{{0}}Field(c, fid);
    
    return asHostObject(v);
}

HostRef* JP{{0}}Type::getInstanceValue(jobject c, jfieldID fid, JPTypeName& tgtType) 
{
    jvalue v;
    v.{{1}} = JPEnv::getJava()->Get{{0}}Field(c, fid);
    
    return asHostObject(v);
}

HostRef* JP{{0}}Type::invokeStatic(jclass claz, jmethodID mth, jvalue* val)
{
    jvalue v;
    v.{{1}} = JPEnv::getJava()->CallStatic{{0}}MethodA(claz, mth, val);
    return asHostObject(v);
}

HostRef* JP{{0}}Type::invoke(jobject obj, jclass clazz, jmethodID mth, jvalue* val)
{
    jvalue v;
    v.{{1}} = JPEnv::getJava()->CallNonvirtual{{0}}MethodA(obj, clazz, mth, val);
    return asHostObject(v);
}

void JP{{0}}Type::setStaticValue(jclass c, jfieldID fid, HostRef* obj) 
{
    {{2}} val = convertToJava(obj).{{1}};
    JPEnv::getJava()->SetStatic{{0}}Field(c, fid, val);
}

void JP{{0}}Type::setInstanceValue(jobject c, jfieldID fid, HostRef* obj) 
{
    {{2}} val = convertToJava(obj).{{1}};
    JPEnv::getJava()->Set{{0}}Field(c, fid, val);
}

vector<HostRef*> JP{{0}}Type::getArrayRange(jarray a, int start, int length)
{
    {{2}}Array array = ({{2}}Array)a;    
    {{2}}* val = NULL;
    jboolean isCopy;
    JPCleaner cleaner;
    
    try {
        val = JPEnv::getJava()->Get{{0}}ArrayElements(array, &isCopy);
        vector<HostRef*> res;
        
        jvalue v;
        for (int i = 0; i < length; i++)
        {
            v.{{1}} = val[i+start];
            HostRef* pv = asHostObject(v);
            res.push_back(pv);
        }
        JPEnv::getJava()->Release{{0}}ArrayElements(array, val, JNI_ABORT);
        
        return res;
    }
    RETHROW_CATCH( if (val != NULL) { JPEnv::getJava()->Release{{0}}ArrayElements(array, val, JNI_ABORT); } );
}

void JP{{0}}Type::setArrayRange(jarray a, int start, int length, vector<HostRef*>& vals)
{
    {{2}}Array array = ({{2}}Array)a;    
    {{2}}* val = NULL;
    jboolean isCopy;
    JPCleaner cleaner;

    try {
        val = JPEnv::getJava()->Get{{0}}ArrayElements(array, &isCopy);
        
        for (int i = 0; i < length; i++)
        {
            HostRef* pv = vals[i];
            
            val[start+i] = convertToJava(pv).{{1}};            
        }
        JPEnv::getJava()->Release{{0}}ArrayElements(array, val, 0);        
    }
    RETHROW_CATCH( if (val != NULL) { JPEnv::getJava()->Release{{0}}ArrayElements(array, val, JNI_ABORT); } );
}

HostRef* JP{{0}}Type::getArrayItem(jarray a, int ndx)
{
    {{2}}Array array = ({{2}}Array)a;    
    {{2}}* val = NULL;
    jboolean isCopy;
    JPCleaner cleaner;
    
    try {
        val = JPEnv::getJava()->Get{{0}}ArrayElements(array, &isCopy);
        
        jvalue v;
        v.{{1}} = val[ndx];
        JPEnv::getJava()->Release{{0}}ArrayElements(array, val, JNI_ABORT);

        return asHostObject(v);
    }
    RETHROW_CATCH( if (val != NULL) { JPEnv::getJava()->Release{{0}}ArrayElements(array, val, JNI_ABORT); } );
}

void JP{{0}}Type::setArrayItem(jarray a, int ndx , HostRef* obj)
{
    {{2}}Array array = ({{2}}Array)a;    
    {{2}}* val = NULL;
    jboolean isCopy;
    
    try {
        val = JPEnv::getJava()->Get{{0}}ArrayElements(array, &isCopy);
        
        val[ndx] = convertToJava(obj).{{1}};
        JPEnv::getJava()->Release{{0}}ArrayElements(array, val, 0);
    }
    RETHROW_CATCH( if (val != NULL) { JPEnv::getJava()->Release{{0}}ArrayElements(array, val, JNI_ABORT); } );
}
"""

PREPARE_VOID_EXTERNAL = """
    JNIEnv* env = getJNIEnv();
    void* _save = JPEnv::getHost()->gotoExternal();
"""

PREPARE_EXTERNAL = "    {{0}} res;\n" + PREPARE_VOID_EXTERNAL

RETURN_VOID_EXTERNAL = """
    JPEnv::getHost()->returnExternal(_save);
    JAVA_CHECK("{{0}}");
"""

PREPARE_EXTERNAL = "    {{0}} res;\n" + PREPARE_VOID_EXTERNAL
RETURN_EXTERNAL = RETURN_VOID_EXTERNAL + "    return res;\n"

def applyTemplate(tmpl, o, col) :
    for ct, jt, t, jt2, ex in col :
        result = tmpl.replace("{{0}}", ct)
        result = result.replace("{{1}}", jt)
        result = result.replace("{{2}}", t)
        result = result.replace("{{3}}", jt2)
        result = result.replace("{{4}}", ex)
        result = result.replace("PREPARE_EXTERNAL", outputPrepareExternal(jt))
        result = result.replace("RETURN_EXTERNAL", RETURN_EXTERNAL.replace("{{0}}", t))        
        o.write(result)

def makeArgPairs(arg) :
    rt = []
    rnames = []
    ndx = 0
    
    for p in arg :
        if type(p) == types.TupleType :
            rnames.append("a"+str(ndx)+"")
            rt.append( p[0]+" a"+str(ndx) )
        else:
            rnames.append("a"+str(ndx))
            rt.append( p+" a"+str(ndx) )
        ndx += 1

    return rt, rnames

def outputPrepareExternal(rt) :
    return PREPARE_EXTERNAL.replace("{{0}}", rt)

def outputJavaCheck(o, name) :
    print >> o, 'JAVA_CHECK("'+name+'");'

class VoidExternal:
    def __init__(self, name, args=[]) :  
        self.name = name
        self.args = args
        
    def generateHeader(self, o) :
        argPairs, argNames = makeArgPairs(self.args)
        print >> o, "".join(["/** ", self.name, " */"]);
        print >> o, "".join(["void ", self.name, "(", ", ".join(argPairs), ");"])
        
    def generateBody(self, o) :
        argPairs, argNames = makeArgPairs(self.args)
        
        if len(self.args) > 0 : 
            argSep = ", "
        else:
            argSep = ""
        
        print >> o
        print >> o, "".join(["void JPJavaEnv::", self.name, "(", ", ".join(argPairs), ")"])
        print >> o, "{", PREPARE_VOID_EXTERNAL
        print >> o, "".join(["\tenv->functions->", self.name, "(env", argSep, ", ".join(argNames), ");"])
        print >> o, "", RETURN_VOID_EXTERNAL.replace("{{0}}", self.name)
        print >> o, "}"

class External:
    def __init__(self, rt, name, args=[]) :
        self.name = name
        self.rt = rt
        self.args = args
        
    def generateHeader(self, o) :
        argPairs, argNames = makeArgPairs(self.args)
        print >> o, "".join(["/** ", self.name, " */"]);
        print >> o, "".join([self.rt, " ", self.name, "(", ", ".join(argPairs), ");"])
        
    def generateBody(self, o) :
        argPairs, argNames = makeArgPairs(self.args)
        
        if len(self.args) > 0 :
            argSep = ", "
        else:
            argSep = ""
        
        print >> o
        print >> o, "".join([self.rt, " JPJavaEnv::", self.name, "(", ", ".join(argPairs), ")"])
        print >> o, "{", outputPrepareExternal(self.rt)
        print >> o, "".join(["\tres = env->functions->", self.name, "(env", argSep, ", ".join(argNames), ");"])
        print >> o, "", RETURN_EXTERNAL.replace("{{0}}", self.name)
        print >> o, "}"
    
class VoidInternal:
    def __init__(self, name, args=[]) :
        self.name = name
        self.args = args
        
    def generateHeader(self, o) :
        argPairs, argNames = makeArgPairs(self.args)
        print >> o, "".join(["/** ", self.name, " */"]);
        print >> o, "".join(["void ", self.name, "(", ", ".join(argPairs), ");"])
        
    def generateBody(self, o) :
        argPairs, argNames = makeArgPairs(self.args)
        
        if len(self.args) > 0 :
            argSep = ", "
        else:
            argSep = ""

        print >> o
        print >> o, "".join(["void JPJavaEnv::", self.name, "(", ", ".join(argPairs), ")"])
        print >> o, "{"
        print >> o, "\tJNIEnv* env = getJNIEnv();"
        print >> o, "".join(["\tenv->functions->", self.name, "(env", argSep, ", ".join(argNames), ");"])
        outputJavaCheck(o, self.name);
        print >> o, "}"

class Internal:
    def __init__(self, rt, name, args=[]) :
        self.name = name
        self.rt = rt
        self.args = args
        
    def generateHeader(self, o) :
        argPairs, argNames = makeArgPairs(self.args)
        print >> o, "".join(["/** ", self.name, " */"]);
        print >> o, "".join([self.rt, " ", self.name, "(", ", ".join(argPairs), ");"])
        
    def generateBody(self, o) :
        argPairs, argNames = makeArgPairs(self.args)
        
        if len(self.args) > 0 :
            argSep = ", "
        else:
            argSep = ""
        
        print >> o
        print >> o, "".join([self.rt, " JPJavaEnv::", self.name, "(", ", ".join(argPairs), ")"])
        print >> o, "{"
        print >> o, "\t", self.rt, "res;"
        print >> o, "\tJNIEnv* env = getJNIEnv();"
        print >> o, "".join(["\tres = env->functions->", self.name, "(env", argSep, ", ".join(argNames), ");"])
        outputJavaCheck(o, self.name);        
        print >> o, "\treturn res;"
        print >> o, "}"

basic = [
    ["_byte", "jbyte", "Byte", "jbyte", ""],
    ["_short", "jshort", "Short", "jshort", ""],
    ["_int", "jint", "Int", "jint", ""],
    ["_long", "jlong", "Long", "jlong", ""],
    ["_float", "jfloat", "Float", "jfloat", ""],
    ["_double", "jdouble", "Double", "jdouble", ""],
    ["_char", "jchar", "Char", "jchar", ""],
    ["_boolean", "jboolean", "Boolean", "jboolean", ""],
]

advanced = basic + [["_object", "jobject", "Object", "jobject", ""]]


METHODS = [
    External("int", "MonitorEnter", [("jobject", True)]),
    External("int", "MonitorExit", [("jobject", True)]),
    External("jmethodID", "FromReflectedMethod", [("jobject", True)]),
    External("jfieldID", "FromReflectedField", [("jobject", True)]),
    External("jclass", "FindClass", ["const char*"]),
    External("jboolean", "IsInstanceOf", [("jobject", True), ("jclass", True)]),
    External("jobjectArray", "NewObjectArray", ["int", ("jclass", True), ("jobject", True)]),
    VoidExternal("SetObjectArrayElement", ["jobjectArray", "int", ("jobject", True)]),
    VoidExternal("CallStaticVoidMethodA", [("jclass", True), "jmethodID", "jvalue*"]),
    VoidExternal("CallVoidMethodA", [("jobject", True), "jmethodID", "jvalue*"]),
    VoidExternal("CallVoidMethod", [("jobject", True), "jmethodID"]),
#    External("jobject", "NewObjectA", [("jclass", True), "jmethodID", "jvalue*"]),
#    External("jobject", "NewObject", [("jclass", True), "jmethodID"]),
    External("jboolean", "IsAssignableFrom", [("jclass", True), ("jclass", True)]),
    External("jstring", "NewString", ["const jchar*", "int"]),
    External("jclass", "GetSuperclass", [("jclass", True)]),
    External("const char*", "GetStringUTFChars", [("jstring", True), "jboolean*"]),
    VoidExternal("ReleaseStringUTFChars", [("jstring", True), "const char*"]),
    External("jsize", "GetArrayLength", [("jarray", True)]),
    External("jobject", "GetObjectArrayElement", [("jobjectArray", True), "int"]), 
    External("jclass", "GetObjectClass", [("jobject", True)]),
    External("jmethodID", "GetMethodID", [("jclass", True), "char*", "char*"]),
    External("jmethodID", "GetStaticMethodID", [("jclass", True), "char*", "char*"]),
    External("jfieldID", "GetFieldID", [("jclass", True), "char*", "char*"]),
    External("jfieldID", "GetStaticFieldID", [("jclass", True), "char*", "char*"]),
    Internal("const jchar*", "GetStringChars", [("jstring", True), "jboolean*"]),
    VoidInternal("ReleaseStringChars", [("jstring", True), "const jchar*"]),
    Internal("jsize", "GetStringLength", [("jstring", True)]),
    External("jclass", "DefineClass", ["const char*", ("jobject", True), "const jbyte*", "jsize"]),
    External("jint", "RegisterNatives", [("jclass", True), "const JNINativeMethod*", "jint"]),    
]

f = open("src/native/common/include/jp_javaenv_autogen.h", "w+")
try:
    f.write(COPYRIGHT)
    print >> f
    print >> f, "// This code has been automatically generated ... No not edit"
    print >> f

    print >> f
    
    applyTemplate(TYPE_METHODS_DECL, f, advanced)
    applyTemplate(PRIMITIVE_ARRAY_METHODS_DECL, f, basic)
 
    print >> f
    for i in METHODS :
        i.generateHeader(f)
    
finally:
    f.close()

f = open("src/native/common/jp_javaenv_autogen.cpp", "w+")
try:
    f.write(COPYRIGHT)
    print >> f
    print >> f, "// This code has been automatically generated ... No not edit"
    print >> f
    print >> f, '#include <jpype.h>'
    print >> f, '#define JAVA_CHECK(msg) \\'
    print >> f, 'if (JPEnv::getJava()->ExceptionCheck()) \\'
    print >> f, '{ \\'
    print >> f, '    RAISE(JavaException, msg); \\'
    print >> f, '} \\'
    print >> f
    print >> f
    
    applyTemplate(TYPE_METHODS, f, advanced)
    applyTemplate(PRIMITIVE_ARRAY_METHODS, f, basic)

    for i in METHODS :
        i.generateBody(f)
    
finally:
    f.close()
    
prim_types = (
    ("Byte", "b", "jbyte"),
    ("Short", "s", "jshort"),
    ("Int", "i", "jint"),
    ("Long", "j", "jlong"),
    ("Float", "f", "jfloat"),
    ("Double", "d", "jdouble"),
    ("Char", "c", "jchar"),
    ("Boolean", "z", "jboolean")
)
    
f = open("src/native/common/jp_primitivetypes_autogen.cpp", "w+")
try:
    f.write(COPYRIGHT)
    print >> f
    print >> f, "// This code has been automatically generated ... No not edit"
    print >> f
    print >> f, '#include <jpype.h>'
    print >> f
    
    for i in prim_types :
        s = TYPE_BLOCK.replace("{{0}}", i[0])
        s = s.replace("{{1}}", i[1])
        s = s.replace("{{2}}", i[2])
        print >> f, s
        print >> f
        print >> f, "//----------------------------------------------------------"
        print >> f
        
    
finally:
    f.close()
    