# this module is onyl a skeleton to allow auto-generation of the documentation

class JArray :
    '''Wrapper class to manage Java arrays of a given type and number fo dimensions. 
    
       It implements most of the sequence functionality, It is like a list in that it's content can be modified, but also like tuple since it cannot be resized.
       It cannot be currently created from python. They are only used to wrap return values from java method or fields.'''
    pass
    
class JBoolean :
    '''Wrapper class to manage Java primitive boolean. Used mainly to resolve ambiguity in method calls.'''
    
    def __init__(self, v) :
        '''Only legal values of v are int'''
        pass
    
class JByte :
    '''Wrapper class to manage Java primitive byte. Used mainly to resolve ambiguity in method calls.'''
    
    def __init__(self, v) :
        '''Only legal values of v are int and long. An exception will be raised if the value does not in in the java byte (signed 8 bit integer)'''
        pass
    
class JChar :
    '''Wrapper class to manage Java primitive char. Used mainly to resolve ambiguity in method calls.'''

    def __init__(self, v) :
        '''v must be a single character string or unicode object.'''
        pass
    
class JDouble :
    '''Wrapper class to manage Java primitive double. Used mainly to resolve ambiguity in method calls.'''
    
    def __init__(self, v) :
        '''Only legal values of v are float. An exception will be raised if the value does not in in the java byte (signed 64 bit float)'''
        pass
    
class JFloat :
    '''Wrapper class to manage Java primitive float. Used mainly to resolve ambiguity in method calls.'''
    
    def __init__(self, v) :
        '''Only legal values of v are float. An exception will be raised if the value does not in in the java byte (signed 32 bit float)'''
        pass
    
class JInt :
    '''Wrapper class to manage Java primitive int. Used mainly to resolve ambiguity in method calls.'''
    
    def __init__(self, v) :
        '''Only legal values of v are int and long. An exception will be raised if the value does not in in the java byte (signed 32 bit integer)'''
        pass
    
class JLong :
    '''Wrapper class to manage Java primitive long. Used mainly to resolve ambiguity in method calls.'''
    
    def __init__(self, v) :
        '''Only legal values of v are int and long. An exception will be raised if the value does not in in the java byte (signed 64 bit integer)'''
        pass
    
class JShort :
    '''Wrapper class to manage Java primitive short. Used mainly to resolve ambiguity in method calls.'''
    
    def __init__(self, v) :
        '''Only legal values of v are int and long. An exception will be raised if the value does not in in the java byte (signed 16 bit integer)'''
        pass
    
class JString :
    '''Wrapper class to manage Java strings. Used mainly to resolve ambiguity in method calls.'''
    
    def __init__(self, v) :
        '''v must be a string or unicode object.'''
        pass
    
class JObject :
    '''Class used to resolve ambiguities in method calls. This is not the same class as JavaObject, '''
    
    def __init__(self, v, t) :
        '''Create a new object wrapper with a specific target type.
        
           v can be a just about any Python primitive or JPype class, as long as it is compatible with the second parameter.
           t must be a Java type, either as a JavaClass object, or as a String. '''
        pass
    
class JPackage :
    ''' This represents a full or partial java package. All java classes must be accessed through one of these.
        JPackage are made to appear as though they "contain" sub-package and classes, as they are accessed like normal instance attributes .'''
        
    def __init__(self, name) :
        ''' Create a new JPackage. The name can be either a first part of the package, or a full dot-separated package name.'''
        self.__name = name
        
    def __repr__(self) :
        '''defined only for better documentation.'''
        return "predefined JPackage for java package named <%s>" % self.__name
    
class JProxy :
    '''A JProxy is used to receive callbacks from java code.'''
    
    def __init__(self, itf, inst=None, dict=None) :
        '''Create a new JProxy.
        
           itf can be one of string, Unicode, JavaClass, list/tuple of (string, Unicode or JavaClass). This determines which interface(s) the new proxy will implement.
           inst or dict MUST be passed by name, and only one can be specified. 
           inst will receive a Python object instance that implements the right method, as required by the specified interface(s)
           dict will receive a dictionary (or dictionaty-like) object, containing callable object keyed to the method names defined in the interface(s).
           '''
        pass
    

def attachThreadToJVM() :
    '''In a multithreaded python applications, any threads not started from within the JVM must call this once before using any of JPype functionality. Failing to do this will result in a exception raised.'''
    pass
    
def cleanupProxyCache() :
    '''Because of the way JProxy are implemented, it may be necessary to do some cleanup once in a while. This will scan the created proxies and free those that are not used anymore.'''
    pass
    
def detachThreadFromJVM() :
    '''To provide cleanup, any python thread that called attachThreadToJVM() should call this method before finishing.'''
    pass
    
def dumpJVMStats() :
    '''Simple tracing method that will print out various statistics about what JVM usage.'''
    pass
    
def getDefaultJVMPath() :
    '''Try to find the location of the JVM.dll (or jvm.so, depending on platform) so that program do not need to hardcode it. 
    Currently only works on win32.
    Since many platforms do not define a consistent way to install the Jave Runtime Environment, it is possible this method will fail. In which case it will return None.
    '''
    pass
    
def isJVMStarted() :
    '''Check if starJVM has successfully be called before, without shutdownJVM().'''
    pass
    
def isThreadAttachedToJVM() :
    '''Check if the current thread is attached to the JVM.'''
    pass
    
def shutdownJVM() :
    pass
    
def startJVM(vmPath, *arg) :
    pass
    
def synchronized(obj) :
    pass
        

java = JPackage("java")
javax = JPackage("java")
