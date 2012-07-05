from distutils.core import setup as distSetup, Extension
    
import os, os.path, sys

class JPypeSetup(object):
    def __init__(self) :
        self.extra_compile_args = []
        self.macros = []

    def setupFiles(self) :
        cpp_files = [
                 map(lambda x : "src/native/common/"+x, os.listdir("src/native/common")),
                 map(lambda x : "src/native/python/"+x, os.listdir("src/native/python")),
                 ]

        all_src = []
        for i in cpp_files :
            all_src += i

        self.cpp = filter(lambda x : x[-4:] == '.cpp', all_src)
        self.objc = filter(lambda x : x[-2:] == '.m', all_src)



    def setupWindows(self):
        print 'Choosing the Windows profile'
        self.javaHome = os.getenv("JAVA_HOME")
        if self.javaHome is None :
            print "environment variable JAVA_HOME must be set"
            sys.exit(-1)
        self.jdkInclude = "win32"
        self.libraries = ["Advapi32"]
        self.libraryDir = [self.javaHome+"/lib"]
        self.macros = [ ("WIN32",1) ]
        self.extra_compile_args = ['/EHsc']
    
    def setupMacOSX(self):
        self.javaHome = '/Developer/SDKs/MacOSX10.7.sdk/System/Library/Frameworks/JavaVM.framework/Versions/Current/'
        self.javaMac = '/System/Library/Frameworks/JavaVM.framework/Versions/CurrentJDK'
        self.jdkInclude = ""
        self.libraries = ["dl"]
        self.libraryDir = [self.javaMac+"/Libraries"]
        self.macros = [('MACOSX',1)]
    
    def setupLinux(self):
        self.javaHome = os.getenv("JAVA_HOME")
        if self.javaHome is None :
            for path in [
                '/usr/java/jdk1.5.0_05',             # original implementation as found by Klaas
                '/usr/lib/jvm/java-6-sun',           # Ubuntu 10.04 Lucid Lynx w/ Sun Java
                '/usr/lib/jvm/java-6-openjdk-amd64', # Ubuntu 12.04 Precise Pangolin
                    ]:
                if os.path.exists(path):
                    self.javaHome = path
                    break
            else:
                raise Exception("No version of Java found")

        self.jdkInclude = "linux"    
        self.libraries = ["dl"]
        self.libraryDir = [self.javaHome+"/lib"]
    
    def setupPlatform(self):
        if sys.platform == 'win32' :
            self.setupWindows()
        elif sys.platform == 'darwin' :
            self.setupMacOSX()
        else:
            self.setupLinux()

    def setupInclusion(self):
        self.includeDirs = [
            self.javaHome+"/include", 
            self.javaHome+"/include/"+self.jdkInclude,
            self.javaHome+"/Headers", 
            self.javaHome+"/Headers/"+self.jdkInclude,
            "src/native/common/include",  
            "src/native/python/include", 
        ]


    def setup(self):
        self.setupFiles()
        self.setupPlatform()
        self.setupInclusion()
        
        jpypeLib = Extension("_jpype", 
                             self.cpp, 
                             libraries=self.libraries, 
                             define_macros=self.macros, 
                             include_dirs=self.includeDirs, 
                             library_dirs=self.libraryDir,
                             extra_compile_args=self.extra_compile_args
                             )
         
        distSetup( 
            name="JPype", 
            version="0.5.4.2",
            description="Python-Java bridge",
            author="Steve Menard",
            author_email="devilwolf@users.sourceforge.net",
            url="http://jpype.sourceforge.net/",
            packages=[
                "jpype", 'jpype.awt', 'jpype.awt.event', 
                'jpypex', 'jpypex.swing'],
            package_dir={
                "jpype" : "src/python/jpype",
                'jpypex' : 'src/python/jpypex',
            },
            
            ext_modules=[jpypeLib]
        )

JPypeSetup().setup()
