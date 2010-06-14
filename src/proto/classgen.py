import jpype
import os, os.path

WRAPPERS = {
		"void" : ( "java/lang/Void", 'V', 'return', None, None),
		"byte" : ( "java/lang/Byte", 'B', 'ireturn', "iload", "byteValue()B"),
		"short" : ( "java/lang/Short", 'S', 'ireturn', "iload", "shortValue()S"),
		"int" : ( "java/lang/Integer", 'I', 'ireturn', "iload", "intValue()I"),
		"long" : ( "java/lang/Long", 'J', 'lreturn', "lload", "longValue()L"),
		"float" : ( "java/lang/Float", 'F', 'freturn', "fload", "floatValue()F"),
		"double" : ( "java/lang/Double", 'D', 'dreturn', "dload", "doubleValue()D"),
		"char" : ( "java/lang/Character", 'C', 'ireturn', "iload", "charValue()C"),
		"boolean" : ( "java/lang/Boolean", 'Z', 'ireturn', "iload", "booleanValue()Z"),
		}

def classGen( ) :	
	global Modifier
	root = os.path.abspath( os.path.dirname( __file__ ) )
	cp = os.path.abspath(root+"/../../build-support/jasmin.jar;"+root+"/../../_bin;"+root+"/../../_classgen")
	jpype.startJVM( jpype.getDefaultJVMPath( ), "-ea", "-Djava.class.path=%s"%cp)
	
	Modifier = jpype.JClass( "java.lang.reflect.Modifier" )
	
	try :
		# base = jpype.JClass("javax.swing.JFrame")
		base = jpype.JClass( "java.lang.Object" )
		intf = [ jpype.JClass( "java.lang.Comparable" ), 
				 #jpype.JClass("javax.swing.CellEditor"),
		]
		
		try :
			result = generateClass( "com.darkwolf.jpype.classgen.TestClass", base, intf, "../../_classgen" );

			dumpClassInformation( result );
		except :
			import traceback
			traceback.print_exc( )
			
	finally :
		jpype.shutdownJVM( )	

def generateClass(name, base, intf, outRootDir) :
	slashName = name.replace('.', '/')
	slashBaseName = base.__javaclass__.getName().replace('.', '/')
	slashIntfNames = map(lambda x : x.__javaclass__.getName().replace('.', '/'), intf)
	
	methods = getAllMethods(base, intf)
	
	lines = []
	lines += startClass(slashName, slashBaseName, slashIntfNames)
	lines += createFields()
	lines += createStaticInit(slashName, methods)
	lines += createConstructor(slashName, slashBaseName, methods)
	for i in range(len(methods)) :
		m = methods[i]
		lines += createMethod(i, slashName, m);

	lines.append("")
	bytes = saveClass(slashName, outRootDir, lines);
	
	return defineClass(name, bytes)

def createMethod(ndx, name, m) :
	argumentCount = len(m.parameterTypes)
	Modifier = jpype.java.lang.reflect.Modifier
	access = "public"
	if Modifier.isSynchronized(m.modifiers) :
		access += " synchronized"

	exceptions = map(lambda x : x.__javaclass__.getName().replace('.', '/'), m.exceptionTypes)
	
	res = [
		".method %s %s%s" % (access, m.name, getSignature(m))
	]
	
	for i in exceptions :
		res.append("    .throws %s" % i)
	
	res += [
		"    .limit stack %d" % (argumentCount+10),
		"    .limit locals %d" % (argumentCount+3),
		"    ; Have we checked this method before?",
		"    aload_0",
		"    getfield %s/_jpype_checked Ljava/util/BitSet;" % name,
		"    %s" % getIPush(ndx),
		"    invokevirtual java/util/BitSet/get(I)Z",
		"    ifne Label3",
		"",
		"    ; If we're here, we havent checked before",
		"    ; Set the checked bit",
		"    aload_0",
		"    getfield %s/_jpype_checked Ljava/util/BitSet;" % name,
		"    %s" % getIPush(ndx),
		"    iconst_1",
		"    invokevirtual java/util/BitSet/set(IZ)V",
		"",
		"    ; check with the PythonCaller",
		"    aload_0",
		"    getfield %s/_jpype_overloaded Ljava/util/BitSet;" % name,
		"    %s" % getIPush(ndx),
		"    aload_0",
		"    getfield %s/_jpype_target J" % name,
		'    ldc "%s"' % m.name, 
		"    invokestatic jpype/PythonMethodCaller/hasMethod/(JLjava/lang/String;)Z",
		"    invokevirtual java/util/BitSet/set(IZ)V",
		"",
		"    ; if the method is overloaded ...",
		"Label3:",
		"    aload_0",
		"    getfield %s/_jpype_overloaded Ljava/util/BitSet;" % name,
		"    %s" % getIPush(ndx), 
		"    invokevirtual java/util/BitSet/get(I)Z",
		"    ifne Label4",
		"",
		"    ; If here, the is NO overload",
	]

	params = m.parameterTypes
	if Modifier.isAbstract(m.modifiers) :
		res += [
			"    ; The method is Abstract and MUST be overloaded ... thrown an exception",
			"    new java/lang/NoSuchMethodError",
			"    dup",
			'    ldc "%s"' % m.name,
			"    invokenonvirtual java/lang/NoSuchMethodError/<init>(Ljava/lang/String;)V",
			"    athrow",			
		]
	else:
		res += [
			"    ; Call super",
			"    aload_0"
		]
		for i in range(len(params)) :
			param = params[i]
			if WRAPPERS.has_key(param.__javaclass__.getName()) :
				res.append("    %s %d" % (WRAPPERS[param.__javaclass__.getName()][3], i+1))
			else:
				res += [
					"    aload %d" % (i+1),
					"    checkcast %s" % param.__javaclass__.getName().replace('.', '/')
				]
					
		res+= [
			"    invokenonvirtual %s/%s%s" % (m.getDeclaringClass().__javaclass__.getName().replace('.', '/'), m.name, getSignature(m)),
			"    goto Label0",
			"",
			]
			
	res+= [
		"    ; Prepare the call to Python Caller",
		"Label4:",
		"    ; Put the target",
		"      aload_0",
		"      getfield %s/_jpype_target J" % name,
		"    ; load the method name",
		'      ldc "%s"' % m.name,
		"    ; load the args",
		"      %s" % getIPush(len(params)),
		"      anewarray java/lang/Object",
	]
	for i in range(len(params)) :
		param = params[i]
		res += [
			"      dup",
			"      %s" % getIPush(i)
		]
		if WRAPPERS.has_key(param.__javaclass__.getName()) :
			res += [
				"      new %s" % WRAPPERS[param.__javaclass__.getName()][1],
				"      dup",
				"      %s %d" % (WRAPPERS[param.__javaclass__.getName()][3], i+1),
				"      invokenonvirtual %s/<init>(%s)V" % (WRAPPERS[param.__javaclass__.getName()][1], WRAPPER[param.__javaclass__.getName()][0]),
			]
		else:
			res += [
				"      aload %d" % (i+1),
			]
		res += [
			"      aastore",
			"",
			]
	res += [
		"    ; Load the args array",
		"      getstatic %s/_java_param_types [[Ljava/lang/Class;" % name,
		"      %s" % getIPush(ndx),
		"      aaload"
		"",
		"    ; Load the return type array",
		"      getstatic %s/_java_return_types [Ljava/lang/Class;" % name,
		"      %s" % getIPush(ndx),
		"      aaload"
		"",
		"    ; Call the Python Caller",
		"      invokestatic jpype/PythonMethodCaller/invoke(JLjava/lang/String;[Ljava/lang/Object;[Ljava/lang/Class;Ljava/lang/Class;)Ljava/lang/Object;",
	]

	if m.returnType.__javaclass__.isPrimitive() :
		t = WRAPPERS[m.returnType.__javaclass__.getName()]
		if t[4] is not None :
			res.append("      checkcast %s" % t[0])
			res.append("      invokevirtual %s/%s" % (t[0], t[4]))
	else:
		res.append("      checkcast %s" % m.returnType.__javaclass__.getName().replace('.', '/'))
	
	
	if m.returnType.__javaclass__.getName() == "void" :
		res.append("      pop")
	
	res.append("Label0:")
	if WRAPPERS.has_key(m.returnType.__javaclass__.getName()) :
		res.append("    %s" % WRAPPERS[m.returnType.__javaclass__.getName()][2])
	else:
		res.append("    areturn")
			
	res += [
		".end method",
		"",
		]
		
	return res
	
def defineClass(name, bytes) :
	JPypeClassLoader = jpype.JClass("org.darkwolf.jpype.classgen.JPypeClassLoader")
	cl = JPypeClassLoader(name, bytes)
	return cl.loadClass(name)

def saveClass(name, outRootDir, lines) :
	outFileName = outRootDir+"/"+name
	parentDir = os.path.split(outFileName)[0]
	if not os.path.exists(parentDir) :
		os.makedirs(parentDir)
		
	f = open(outFileName+".j", "w+")
	for i in lines :
		print >> f, i
	f.close()

	src = "\n".join(lines)

	ClassFile = jpype.JClass("jasmin.ClassFile")
	ByteArrayInputStream = jpype.java.io.ByteArrayInputStream
	ByteArrayOutputStream = jpype.java.io.ByteArrayOutputStream
	FileOutputStream = jpype.java.io.FileOutputStream
	
	bytes = jpype.java.lang.String(src).getBytes()
	bais = ByteArrayInputStream(bytes)

	try :	
		cf = ClassFile()
		cf.readJasmin(bais, name, True)
	except jpype.java.lang.ArrayIndexOutOfBoundsException.PYEXC, ex :
		print ex.stacktrace()
	
	fout = FileOutputStream(outFileName+".class")
	cf.write(fout)
	fout.close()
	
	fout = ByteArrayOutputStream()
	cf.write(fout)
	bytes = fout.toByteArray()
	fout.close()
	
	return bytes
	 
def createStaticInit(name, methods) :
	return [
		".method static <clinit>()V",
		"    .limit stack 7",
		"    .limit locals 1",
		".catch java/lang/Exception from Label1 to Label2 using Label2",
		"Label1:",
	] + createArgTypesArray(name, methods) + createReturnTypesArray(name, methods) + [
		"    goto Label3",
		"Label2:",
		"    astore_0",
		".var 0 is ex Ljava/lang/Exception; from Label4 to Label3",
		"Label4:",
		"    aload_0",
		"    invokevirtual java/lang/Exception/printStackTrace()V",
		"Label3:",
		"    return",
		".end method",
		"",
	]
	
def createConstructor(name, superName, methods) :
	return [
		".method public <init>(J)V",
		"    .limit stack 4",
		"    .limit locals 3",
		"    ; Store the target",
		"    aload_0",
		"    lload 1",
		"    putfield %s/_jpype_target J" % name,
		"    ; Call super",
		"    aload_0",
		"    invokenonvirtual %s/<init>()V" % superName,
		"    ; Create the checked bitset",
		"    aload_0",
		"    new java/util/BitSet",
		"    dup",
		"    %s" % getIPush(len(methods)),
		"    invokespecial java/util/BitSet/<init>(I)V",
		"    putfield %s/_jpype_checked Ljava/util/BitSet;" % name,
		"    ; Create the overloaded bitset",
		"    aload_0",
		"    new java/util/BitSet",
		"    dup",
		"    %s" % getIPush(len(methods)),
		"    invokespecial java/util/BitSet/<init>(I)V",
		"    putfield %s/_jpype_overloaded Ljava/util/BitSet;" % name,
		"    return",
		".end method",
		""
	]
		
def createArgTypesArray(name, methods) :
	res = [
		"    ;",
		"    ; Create the parameter types array",
		"    ;",
		"    %s" % getIPush(len(methods)),
		"    anewarray [Ljava/lang/Class;",
	]
	for i in range(len(methods)) :
		m = methods[i]
		res += [
			"    ; Method %d : %s%s" % (i, m.name, getSignature(m)),
			"      dup",
			"      %s" % getIPush(i),
			]
		
		argTypes = m.parameterTypes

		res += [
			"      %s" % getIPush(len(argTypes)),
			"      anewarray Ljava/lang/Class;",
			]
		for j in range(len(argTypes)) :
			res += [
				"      ; Argument %d" % j,
				"        dup",
				"        %s" % getIPush(j),
			]				
			if argTypes[j].__javaclass__.isPrimitive() :
				res.append("        getstatic %s/TYPE Ljava/lang/Class;" % WRAPPER[argTypes[j].__javaclass__.getName()])
			else:
				res += [			
				'        ldc "%s"' % argTypes[j].__javaclass__.getName(),
				'        invokestatic java/lang/Class/forName(Ljava/lang/String;)Ljava/lang/Class;'
				]
			res.append("        aastore")
		res.append("      aastore")
	res.append("    putstatic %s/_jpype_param_types [[Ljava/lang/Class;" % name )
	return res
	
def createReturnTypesArray(name, methods) :
	res= [
		"    ;",
		"    ; Create the Return types array",
		"    ;",
		"    %s" % getIPush(len(methods)),
		"    anewarray java/lang/Class",
	]
		
	for i in range(len(methods)) :
		m = methods[i]
		returnType = m.returnType.__javaclass__
		res += [
			"    ; Method %d : %s%s" % (i, m.name, getSignature(m)),
			"      dup",
			"      %s" % getIPush(i),
		]

		if returnType.isPrimitive() :
			res.append( "      getstatic %s/TYPE Ljava/lang/Class;" % WRAPPERS[returnType.getName()][0] )
		else :
			res += [ 
				'      ldc "%s"' % returnType.getName(),
				'      invokestatic java/lang/Class/forName(Ljava/lang/String;)Ljava/lang/Class;'
				]
		res.append("      aastore")
	res.append("    putstatic %s/_jpype_return_types [Ljava/lang/Class;" % name)
	return res

def getAllMethods(base, interfaces) :
	methods = {}
	
	extractMethods(base.__javaclass__, methods);
	for i in interfaces :
		extractMethods(i.__javaclass__, methods);

	return methods.values()

def createFields() :
	# TODO change the public to private ...
	return [ 
		".field public _jpype_target J",
		".field public _jpype_checked Ljava/util/BitSet;",
		".field public _jpype_overloaded Ljava/util/BitSet;",
		".field public static final _jpype_return_types [Ljava/lang/Class;",
		".field public static final _jpype_param_types [[Ljava/lang/Class;",
		""
	]

def startClass(name, base, intf) :
	return [
	".class %s" % name,
	".super %s" % base,
	] + map(lambda x : ".implements %s" % x, intf) + [""]
	
def extractMethods(type, methods) :
	myMethods = type.getDeclaredMethods()
	
	for m in myMethods :
		modifiers = m.modifiers
		if Modifier.isFinal(modifiers) or Modifier.isStatic(modifiers) :
			continue;
		
		if not (Modifier.isPublic(modifiers) or Modifier.isProtected(modifiers)) :
			continue;

		sig = getSignature(m);
		if methods.has_key(sig) :
			continue
		
		methods[sig] = m

	superIntf = type.getBaseInterfaces();
	for i in superIntf :
		extractMethods(superIntf[i], methods);

	if type.getName() != 'java.lang.Object' and not type.isInterface():
		extractMethods(type.getBaseClass(), methods)

def getSignature(m) :
	sb = [ "(" ]
	args = m.parameterTypes
	for i in range(len(args)) :
		if WRAPPERS.has_key(args[i].__javaclass__.getName()) :
			sb.append(WRAPPERS[args[i].__javaclass__.getName()][1])
		elif args[i].__javaclass__.isArray() :
			sb.append(args[i].__javaclass__.getName())
		else:
			sb.append("L"+args[i].__javaclass__.getName().replace(".", "/")+";")
	sb.append(")")
	if WRAPPERS.has_key(m.returnType.__javaclass__.getName()) :
		sb.append(WRAPPERS[m.returnType.__javaclass__.getName()][1])
	elif m.returnType.__javaclass__.isArray() :
		print 'type', m.returnType.__javaclass__.getName(), 'is an array type'
		sb.append(m.returnType.__javaclass__.getName())
	else:
		print 'type', m.returnType.__javaclass__.getName(), 'is an object type'
		sb.append("L"+m.returnType.__javaclass__.getName().replace(".", "/")+";")
	
	return "".join(sb)

def getIPush(v) :
	if v < 6 :
		return "iconst_%d" % v
	elif v < 255 :
		return "bipush %d" % v
	else:
		return "sipush %d" % v

def dumpClassInformation(c) :
	if c is None :
		return
		
	print "Information regarding class " + c.__javaclass__.getName()
	print "    Base class = "+c.__javaclass__.getBaseClass().getName()
	intf = c.__javaclass__.getBaseInterfaces()
	for i in intf :
		print "    Intf = "+i.getName()

	for i in dir(c) :
		print i
		
	print '    Methods :'
	for i in c.__javaclass__.getDeclaredMethods() :
		print i
		
	print '    Return types :'
	for i in c._jpype_return_types :
		print "       ", i
		
	print '    Param types :'
	for i in c._jpype_param_types :
		print "       ", i
	
if __name__ == '__main__' :
	classGen( )
