package org.darkwolf.jpype.classgen;

import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileOutputStream;
import java.io.IOException;
import java.lang.reflect.Field;
import java.lang.reflect.Method;
import java.lang.reflect.Modifier;
import java.util.ArrayList;
import java.util.BitSet;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

import org.objectweb.asm.ClassVisitor;
import org.objectweb.asm.ClassWriter;
import org.objectweb.asm.Label;
import org.objectweb.asm.MethodVisitor;
import org.objectweb.asm.Opcodes;
import org.objectweb.asm.Type;

public class ClassGen implements Opcodes
{
	private static final Map WRAPPERS = new HashMap();
	static
	{
		WRAPPERS.put(Void.TYPE.getName(), Void.class.getName().replace('.', '/'));
		WRAPPERS.put(Byte.TYPE.getName(), Byte.class.getName().replace('.', '/'));
		WRAPPERS.put(Short.TYPE.getName(), Short.class.getName().replace('.', '/'));
		WRAPPERS.put(Integer.TYPE.getName(), Integer.class.getName().replace('.', '/'));
		WRAPPERS.put(Long.TYPE.getName(), Long.class.getName().replace('.', '/'));
		WRAPPERS.put(Float.TYPE.getName(), Float.class.getName().replace('.', '/'));
		WRAPPERS.put(Double.TYPE.getName(), Double.class.getName().replace('.', '/'));
		WRAPPERS.put(Character.TYPE.getName(), Character.class.getName().replace('.', '/'));
		WRAPPERS.put(Boolean.TYPE.getName(), Boolean.class.getName().replace('.', '/'));
	}

	public static void main(String[] argv)
	{
		// Class base = JFrame.class;
		Class base = Object.class;

		Class[] interfaces = new Class[] { Comparable.class /*
																				 * ,
																				 * CellEditor.class
																				 */};

		try
		{
			Class result = generateClass("com.darkwolf.jpype.classgen.TestClass", base, interfaces, "_classgen");

			dumpClassInformation(result);
		}
		catch (IOException ex)
		{
			ex.printStackTrace();
		}
	}

	public static Class generateClass(String name, Class base, Class[] interfaces, String outRootDir) throws IOException
	{

		List sortedMethods = getAllMethods(base, interfaces);

		ClassWriter cw = startClass(name, base, interfaces);
		createFields(cw);
		createStaticInit(name, cw, sortedMethods);
		createConstructor(name, base.getName(), sortedMethods, cw);
		for (int i = 0; i < sortedMethods.size(); i++)
		{
			Method m = (Method)sortedMethods.get(i);
			createMethod(cw, i, name, m);
		}
		cw.visitEnd();

		byte[] bytes = cw.toByteArray();

		saveClass(name, outRootDir, bytes);

		return defineClass(name, bytes);
	}

	private static void createMethod(ClassVisitor cw, int ndx, String name, Method m)
	{
		int argumentCount = m.getParameterTypes().length;
		int access = ACC_PUBLIC;
		if (Modifier.isSynchronized(m.getModifiers()))
		{
			access += ACC_SYNCHRONIZED;
		}
		
		Class[] exceptionsTypes = m.getExceptionTypes();
		String[] exceptions = new String[exceptionsTypes.length];
		for (int i = 0; i < exceptions.length; i++)
		{
			exceptions[i] = Type.getInternalName(exceptionsTypes[i]);
		}
		
		MethodVisitor mv = cw.visitMethod(access,
				m.getName(),
				Type.getMethodDescriptor(m),
				null,
				exceptions
				);
		mv.visitCode();
		
		// Check if we've cheked this method before
	   mv.visitVarInsn(ALOAD, 0);
	   mv.visitFieldInsn(GETFIELD, name.replace('.', '/'), "_jpype_checked", "Ljava/util/BitSet;");
	   mv.visitIntInsn(SIPUSH, ndx);
	   mv.visitMethodInsn(INVOKEVIRTUAL, "java/util/BitSet", "get", "(I)Z");
	   Label label3 = new Label();
	   mv.visitJumpInsn(IFNE, label3);

	   // If we get here, we havent checked before
	   // Say we've checked
	   mv.visitVarInsn(ALOAD, 0);
	   mv.visitFieldInsn(GETFIELD, name.replace('.', '/'), "_jpype_checked", "Ljava/util/BitSet;");
	   mv.visitIntInsn(SIPUSH, ndx);
	   mv.visitInsn(ICONST_1);
	   mv.visitMethodInsn(INVOKEVIRTUAL, "java/util/BitSet", "set", "(IZ)V");

	   // Check with the callback
	   mv.visitVarInsn(ALOAD, 0);
	   mv.visitFieldInsn(GETFIELD, name.replace('.', '/'), "_jpype_overloaded", "Ljava/util/BitSet;");
	   mv.visitIntInsn(SIPUSH, ndx);
	   mv.visitVarInsn(ALOAD, 0);
	   mv.visitFieldInsn(GETFIELD, name.replace('.', '/'), "_jpype_target", "J");
	   mv.visitLdcInsn(m.getName());
	   mv.visitMethodInsn(INVOKESTATIC, "jpype/PythonMethodCaller", "hasMethod", "(JLjava/lang/String;)Z");
	   mv.visitMethodInsn(INVOKEVIRTUAL, "java/util/BitSet", "set", "(IZ)V");

	   // Check if we DO have a method ...
	   mv.visitLabel(label3);
	   mv.visitVarInsn(ALOAD, 0);
	   mv.visitFieldInsn(GETFIELD, name.replace('.', '/'), "_jpype_overloaded", "Ljava/util/BitSet;");
	   mv.visitIntInsn(SIPUSH, ndx);
	   mv.visitMethodInsn(INVOKEVIRTUAL, "java/util/BitSet", "get", "(I)Z");
	   Label returnLabel = new Label();
	   Label label4 = new Label();
	   mv.visitJumpInsn(IFNE, label4);
	   
	   // Here, we do NOT have the overload ...
	   Class[] parameters = m.getParameterTypes();
	   if (Modifier.isAbstract(m.getModifiers()))
	   {
	   	// Generate an error
	   	mv.visitTypeInsn(NEW, "java/lang/NoSuchMethodError");
	   	mv.visitInsn(DUP);
	   	mv.visitLdcInsn(m.getName());
	   	mv.visitMethodInsn(INVOKESPECIAL, "java/lang/NoSuchMethodError", "<init>", "(Ljava/lang/String;)V");
	   	mv.visitInsn(ATHROW);
	   }
	   else
	   {	
	   	// Call the super
		   mv.visitVarInsn(ALOAD, 0);
		   for (int i = 0; i < parameters.length; i++)
		   {
		   	if (parameters[i].isPrimitive())
		   	{
		   		if (parameters[i].getName().equals("byte"))
		   		{
		   			mv.visitVarInsn(ILOAD, i+1);
		   		}
		   		else if (parameters[i].getName().equals("short"))
		   		{
		   			mv.visitVarInsn(ILOAD, i+1);
		   		}
		   		else if (parameters[i].getName().equals("int"))
		   		{
		   			mv.visitVarInsn(ILOAD, i+1);
		   		}
		   		else if (parameters[i].getName().equals("long"))
		   		{
		   			mv.visitVarInsn(LLOAD, i+1);
		   		}
		   		else if (parameters[i].getName().equals("boolean")) 
		   		{
		   			mv.visitVarInsn(ILOAD, i+1);
		   		}
		   		else if (parameters[i].getName().equals("char"))
		   		{
		   			mv.visitVarInsn(ILOAD, i+1);
		   		}
		   		else if (parameters[i].getName().equals("float"))
		   		{
		   			mv.visitVarInsn(FLOAD, i+1);
		   		}
		   		else if (parameters[i].getName().equals("double"))
		   		{
		   			mv.visitVarInsn(DLOAD, i+1);
		   		}
		   		else
		   		{
		   			throw new RuntimeException("WTF is this type?? "+parameters[i].getName());
		   		}
		   	}
		   	else
		   	{
	   			mv.visitVarInsn(ALOAD, i+1);
		   	}
		   }
		   mv.visitMethodInsn(INVOKESPECIAL, m.getDeclaringClass().getName().replace('.', '/'), 
		   		m.getName(), Type.getMethodDescriptor(m));
		   
	   	mv.visitJumpInsn(GOTO, returnLabel);
	   }

	   mv.visitLabel(label4);
	   // Prepare the call to the Ptyon caller
	   // Put the target on stack
	   mv.visitVarInsn(ALOAD, 0);
	   mv.visitFieldInsn(GETFIELD, name.replace('.', '/'), "_jpype_target", "J");
	   // Put the method name on the stack
	   mv.visitLdcInsn(m.getName());
	   // Put the args on the stack 
	   mv.visitIntInsn(BIPUSH, parameters.length);
	   mv.visitTypeInsn(ANEWARRAY, "java/lang/Object");
	   for (int i = 0; i < parameters.length; i++)
	   {
	   	mv.visitInsn(DUP);
			mv.visitIntInsn(BIPUSH, i);
	   	if (parameters[i].isPrimitive())
	   	{
	   		if (parameters[i].getName().equals("byte"))
	   		{
	   			mv.visitTypeInsn(NEW, "java/lang/Byte");
	   	   	mv.visitInsn(DUP);
	   			mv.visitVarInsn(ILOAD, i+1);
	   			mv.visitMethodInsn(INVOKESPECIAL, "java/lang/Byte", "<init>", "(B)V");
	   		}
	   		else if (parameters[i].getName().equals("short"))
	   		{
	   			mv.visitTypeInsn(NEW, "java/lang/Short");
	   	   	mv.visitInsn(DUP);
	   			mv.visitVarInsn(ILOAD, i+1);
	   			mv.visitMethodInsn(INVOKESPECIAL, "java/lang/Short", "<init>", "(S)V");
	   		}
	   		else if (parameters[i].getName().equals("int"))
	   		{
	   			mv.visitTypeInsn(NEW, "java/lang/Integer");
	   	   	mv.visitInsn(DUP);
	   			mv.visitVarInsn(ILOAD, i+1);
	   			mv.visitMethodInsn(INVOKESPECIAL, "java/lang/Integer", "<init>", "(I)V");
	   		}
	   		else if (parameters[i].getName().equals("long"))
	   		{
	   			mv.visitTypeInsn(NEW, "java/lang/Long");
	   	   	mv.visitInsn(DUP);
	   			mv.visitVarInsn(LLOAD, i+1);
	   			mv.visitMethodInsn(INVOKESPECIAL, "java/lang/Long", "<init>", "(J)V");
	   		}
	   		else if (parameters[i].getName().equals("boolean")) 
	   		{
	   			mv.visitTypeInsn(NEW, "java/lang/Boolean");
	   	   	mv.visitInsn(DUP);
	   			mv.visitVarInsn(ILOAD, i+1);
	   			mv.visitMethodInsn(INVOKESPECIAL, "java/lang/Boolean", "<init>", "(Z)V");
	   		}
	   		else if (parameters[i].getName().equals("char"))
	   		{
	   			mv.visitTypeInsn(NEW, "java/lang/Character");
	   	   	mv.visitInsn(DUP);
	   			mv.visitVarInsn(ILOAD, i+1);
	   			mv.visitMethodInsn(INVOKESPECIAL, "java/lang/Character", "<init>", "(C)V");
	   		}
	   		else if (parameters[i].getName().equals("float"))
	   		{
	   			mv.visitTypeInsn(NEW, "java/lang/Float");
	   	   	mv.visitInsn(DUP);
	   			mv.visitVarInsn(FLOAD, i+1);
	   			mv.visitMethodInsn(INVOKESPECIAL, "java/lang/Float", "<init>", "(F)V");
	   		}
	   		else if (parameters[i].getName().equals("double"))
	   		{
	   			mv.visitTypeInsn(NEW, "java/lang/Double");
	   	   	mv.visitInsn(DUP);
	   			mv.visitVarInsn(DLOAD, i+1);
	   			mv.visitMethodInsn(INVOKESPECIAL, "java/lang/Double", "<init>", "(D)V");
	   		}
	   		else
	   		{
	   			throw new RuntimeException("WTF is this type?? "+parameters[i].getName());
	   		}
	   	}
	   	else
	   	{
   			mv.visitVarInsn(ALOAD, i+1);
	   	}
	   	mv.visitInsn(AASTORE);
	   }

	   // Load the arg types
	   mv.visitFieldInsn(GETSTATIC, name.replace('.', '/'), "_jpype_arg_types", "[[Ljava/lang/Class;");
	   mv.visitIntInsn(SIPUSH, ndx);
	   mv.visitInsn(AALOAD);
	   
	   // Load the return type
	   mv.visitFieldInsn(GETSTATIC, name.replace('.', '/'), "_jpype_return_types", "[Ljava/lang/Class;");
	   mv.visitIntInsn(SIPUSH, ndx);
	   mv.visitInsn(AALOAD);
	   
	   // Call the "caller"
	   mv.visitMethodInsn(INVOKESTATIC, "jpype/PythonMethodCaller", "invoke", "(JLjava/lang/String;[Ljava/lang/Object;[Ljava/lang/Class;Ljava/lang/Class;)Ljava/lang/Object;");
	   
	   // Do the return code thing ...
	   if (m.getReturnType().equals(Void.TYPE))
	   {
	   	mv.visitInsn(POP);
	   }
	   
	   mv.visitLabel(returnLabel);
	   Class returnType = m.getReturnType(); 
	   if (returnType.equals(Void.TYPE))
	   {
	   	mv.visitInsn(RETURN);
	   }
	   else if (returnType.isPrimitive())
   	{
   		if (returnType.getName().equals("byte"))
   		{
   	   	mv.visitInsn(IRETURN);
   		}
   		else if (returnType.getName().equals("short"))
   		{
   	   	mv.visitInsn(IRETURN);
   		}
   		else if (returnType.getName().equals("int"))
   		{
   	   	mv.visitInsn(IRETURN);
   		}
   		else if (returnType.getName().equals("long"))
   		{
   	   	mv.visitInsn(LRETURN);
   		}
   		else if (returnType.getName().equals("boolean")) 
   		{
   	   	mv.visitInsn(IRETURN);
   		}
   		else if (returnType.getName().equals("char"))
   		{
   	   	mv.visitInsn(IRETURN);
   		}
   		else if (returnType.getName().equals("float"))
   		{
   	   	mv.visitInsn(FRETURN);
   		}
   		else if (returnType.getName().equals("double"))
   		{
   	   	mv.visitInsn(DRETURN);
   		}
   		else
   		{
   			throw new RuntimeException("WTF is this type?? "+returnType.getName());
   		}
   	}
   	else
   	{
			mv.visitInsn(ARETURN);
   	}
		mv.visitMaxs(argumentCount+10, argumentCount+3); // TODO tweak
		mv.visitEnd();
	}
	
	private static Class defineClass(String name, byte[] bytes)
	{
		try
		{
			return new JPypeClassLoader(name, bytes).loadClass(name);
		}
		catch (ClassNotFoundException ex)
		{
			ex.printStackTrace();
			return null;
		}
	}

	private static void saveClass(String name, String outRootDir, byte[] bytes) throws FileNotFoundException,
			IOException
	{
		if (outRootDir != null)
		{
			File classFile = new File(outRootDir + File.separatorChar + name.replace('.', File.separatorChar) + ".class");
			File packDir = classFile.getParentFile();
			if (!packDir.exists())
			{
				packDir.mkdirs();
			}

			FileOutputStream fout = new FileOutputStream(classFile);
			fout.write(bytes);
			fout.close();
		}
	}

	private static void createStaticInit(String className, ClassVisitor cw, List methods)
	{
		MethodVisitor mv = cw.visitMethod(ACC_STATIC, "<clinit>", "()V", null, null);
		mv.visitCode();
		createReturnTypesArray(className, methods, mv);
		createArgTypesArray(className, methods, mv);
		
		mv.visitIntInsn(SIPUSH, methods.size());
		mv.visitTypeInsn(ANEWARRAY, "java/lang/Class");
		
		mv.visitInsn(RETURN);
		mv.visitMaxs(7, 0);
		mv.visitEnd();

	}

	private static void createConstructor(String className, String superClass, List methods, ClassVisitor cw)
	{
		MethodVisitor mv = cw.visitMethod(ACC_PUBLIC, "<init>", "(J)V", null, null);
		mv.visitCode();

		// Call super
		mv.visitVarInsn(ALOAD, 0);
		mv.visitMethodInsn(INVOKESPECIAL, superClass.replace('.', '/'), "<init>", "()V");
		
		// Store the target
		mv.visitVarInsn(ALOAD, 0);
		mv.visitVarInsn(LLOAD, 1);
		mv.visitFieldInsn(PUTFIELD, className.replace('.', '/'), "_jpype_target", "J");
		
		// Create the checked bitset
		mv.visitVarInsn(ALOAD, 0);
	   mv.visitTypeInsn(NEW, "java/util/BitSet");
	   mv.visitInsn(DUP);
	   mv.visitIntInsn(SIPUSH, methods.size());
	   mv.visitMethodInsn(INVOKESPECIAL, "java/util/BitSet", "<init>", "(I)V");
	   mv.visitFieldInsn(PUTFIELD, className.replace('.', '/'), "_jpype_checked", "Ljava/util/BitSet;");
	   
		// Create the overloaded bitset
		mv.visitVarInsn(ALOAD, 0);
	   mv.visitTypeInsn(NEW, "java/util/BitSet");
	   mv.visitInsn(DUP);
	   mv.visitIntInsn(SIPUSH, methods.size());
	   mv.visitMethodInsn(INVOKESPECIAL, "java/util/BitSet", "<init>", "(I)V");
	   mv.visitFieldInsn(PUTFIELD, className.replace('.', '/'), "_jpype_overloaded", "Ljava/util/BitSet;");
		
		mv.visitInsn(RETURN);
		mv.visitMaxs(4, 3);
		mv.visitEnd();
	}
	
	/**
	 * @param className
	 * @param methods
	 * @param mv
	 */
	private static void createArgTypesArray(String className, List methods, MethodVisitor mv)
	{
		mv.visitIntInsn(SIPUSH, methods.size());
		mv.visitTypeInsn(ANEWARRAY, "[Ljava/lang/Class;");
		for (int i = 0; i < methods.size(); i++)
		{
			mv.visitInsn(DUP);
			
			Method m = (Method)methods.get(i);
			Class[] argTypes = m.getParameterTypes();
			
			mv.visitIntInsn(SIPUSH, i);
			if (argTypes.length == 0)
			{
				mv.visitInsn(ICONST_0);
				mv.visitTypeInsn(ANEWARRAY, "java/lang/Class");
			}
			else
			{
				mv.visitIntInsn(BIPUSH, argTypes.length);
				mv.visitTypeInsn(ANEWARRAY, "java/lang/Class");
				
				for (int j = 0; j < argTypes.length; j++)
				{
					mv.visitInsn(DUP);
					switch (j)
					{
						case 0:
							mv.visitInsn(ICONST_0);
							break;
						case 1:
							mv.visitInsn(ICONST_1);
							break;
						case 2:
							mv.visitInsn(ICONST_2);
							break;
						case 3:
							mv.visitInsn(ICONST_3);
							break;
						case 4:
							mv.visitInsn(ICONST_4);
							break;
						case 5:
							mv.visitInsn(ICONST_5);
							break;
						default:
							mv.visitIntInsn(BIPUSH, j);
					}
					if (argTypes[j].isPrimitive())
					{
						mv.visitFieldInsn(GETSTATIC, (String) WRAPPERS.get(argTypes[j].getName()), "TYPE", "Ljava/lang/Class;");
					}
					else
					{
						mv.visitLdcInsn(argTypes[j].getName());
						mv.visitMethodInsn(INVOKESTATIC, "java/lang/Class", "forName", "(Ljava/lang/String;)Ljava/lang/Class;");
					}
					mv.visitInsn(AASTORE);			
				}
			}
			
			mv.visitInsn(AASTORE);			
		}
		mv.visitFieldInsn(PUTSTATIC, className.replace('.', '/'), "_jpype_arg_types", "[[Ljava/lang/Class;");
	}
	
	/**
	 * @param className
	 * @param methods
	 * @param mv
	 */
	private static void createReturnTypesArray(String className, List methods, MethodVisitor mv)
	{
		mv.visitIntInsn(SIPUSH, methods.size());
		mv.visitTypeInsn(ANEWARRAY, "java/lang/Class");
		for (int i = 0; i < methods.size(); i++)
		{
			Method m = (Method) methods.get(i);

			mv.visitInsn(DUP);
			switch (i)
			{
				case 0:
					mv.visitInsn(ICONST_0);
					break;
				case 1:
					mv.visitInsn(ICONST_1);
					break;
				case 2:
					mv.visitInsn(ICONST_2);
					break;
				case 3:
					mv.visitInsn(ICONST_3);
					break;
				case 4:
					mv.visitInsn(ICONST_4);
					break;
				case 5:
					mv.visitInsn(ICONST_5);
					break;
				default:
					mv.visitIntInsn(SIPUSH, i);
			}
			Class returnType = m.getReturnType();
			if (returnType.isPrimitive())
			{
				mv.visitFieldInsn(GETSTATIC, (String) WRAPPERS.get(returnType.getName()), "TYPE", "Ljava/lang/Class;");
			}
			else
			{
				mv.visitLdcInsn(returnType.getName());
				mv.visitMethodInsn(INVOKESTATIC, "java/lang/Class", "forName", "(Ljava/lang/String;)Ljava/lang/Class;");
			}
			mv.visitInsn(AASTORE);
		}
		mv.visitFieldInsn(PUTSTATIC, className.replace('.', '/'), "_jpype_return_types", "[Ljava/lang/Class;");
	}

	private static List getAllMethods(Class base, Class[] interfaces)
	{
		Map methods = new HashMap();

		extractMethods(base, methods);
		for (int i = 0; i < interfaces.length; i++)
		{
			extractMethods(interfaces[i], methods);
		}

		return new ArrayList(methods.values());
	}

	private static void createFields(ClassVisitor cw)
	{
		int access = ACC_PUBLIC; // ACC_PRIVATE
		cw.visitField(access, "_jpype_checked", Type.getType(BitSet.class).getDescriptor(), null, null).visitEnd();
		cw.visitField(access, "_jpype_overloaded", Type.getType(BitSet.class).getDescriptor(), null, null).visitEnd();
		cw.visitField(access, "_jpype_target", Type.getType(Long.TYPE).getDescriptor(), null, null).visitEnd();
		cw.visitField(access + ACC_FINAL + ACC_STATIC, "_jpype_return_types",
				Type.getType(Class[].class).getDescriptor(), null, null).visitEnd();
		cw.visitField(access + ACC_FINAL + ACC_STATIC, "_jpype_arg_types", Type.getType(Class[][].class).getDescriptor(),
				null, null).visitEnd();
	}

	private static ClassWriter startClass(String name, Class base, Class[] interfaces)
	{
		String[] intNames;
		if (interfaces.length == 0)
		{
			intNames = null;
		}
		else
		{
			intNames = new String[interfaces.length];
			for (int i = 0; i < interfaces.length; i++)
			{
				intNames[i] = interfaces[i].getName().replace('.', '/');
			}
		}

		ClassWriter cw = new ClassWriter(false);
		cw.visit(V1_4, ACC_PUBLIC, name.replace('.', '/'), null, base.getName().replace('.', '/'), intNames);
		return cw;
	}

	private static void extractMethods(Class type, Map methods)
	{
		Method[] myMethods = type.getDeclaredMethods();

		for (int i = 0; i < myMethods.length; i++)
		{
			Method m = myMethods[i];
			int modifiers = m.getModifiers();
			if (Modifier.isFinal(modifiers) || Modifier.isStatic(modifiers))
			{
				continue;
			}

			if (!(Modifier.isPublic(modifiers) || Modifier.isProtected(modifiers)))
			{
				continue;
			}

			String sig = getSignature(m);
			if (methods.containsKey(sig))
			{
				// already there
				continue;
			}

			methods.put(sig, m);
		}

		Class[] superIntf = type.getInterfaces();
		for (int i = 0; i < superIntf.length; i++)
		{
			extractMethods(superIntf[i], methods);
		}

		if (type.getSuperclass() != null)
		{
			extractMethods(type.getSuperclass(), methods);
		}
	}

	private static String getSignature(Method m)
	{
		StringBuffer sb = new StringBuffer();
		sb.append(m.getReturnType().getName());
		sb.append(" ");
		sb.append(m.getName());
		sb.append("(");
		Class[] args = m.getParameterTypes();
		for (int i = 0; i < args.length; i++)
		{
			if (i != 0)
			{
				sb.append(", ");
			}
			sb.append(args[i].getName());
		}
		sb.append(")");

		return sb.toString();
	}

	private static void dumpClassInformation(Class c)
	{
		try
		{
			System.out.println("Information regarding class " + c.getName());
			System.out.println("  Base class = "+c.getSuperclass().getName());
			Class[] intf = c.getInterfaces();
			for (int i = 0; i < intf.length; i++)
			{
				System.out.println("   Intf = "+intf[i].getName());
			}
			
			Field[] f = c.getDeclaredFields();
			System.out.println("Fields (" + f.length + ") :");
			for (int i = 0; i < f.length; i++)
			{
				System.out.println("\t" + f[i].getName() + " : " + f[i].getType().getName());
			}

			Class[] returnTypes = (Class[]) c.getDeclaredField("_jpype_return_types").get(null);
			System.out.println("Value of _jpype_return_types ("+returnTypes.length+") :");
			for (int i = 0; i < returnTypes.length; i++)
			{
				System.out.println("\t"+returnTypes[i]);
			}

			Class[][] argTypes = (Class[][]) c.getDeclaredField("_jpype_arg_types").get(null);
			System.out.println("Value of _jpype_arg_types ("+argTypes.length+") :");
			for (int i = 0; i < argTypes.length; i++)
			{
				Class[] args = argTypes[i];
				System.out.print("\t{");
				for (int j = 0; j < args.length; j++)
				{
					System.out.print(args[j]+" ");
				}
				System.out.println("}");
			}
}
		catch (Exception ex)
		{
			ex.printStackTrace();
		}
	}
}
