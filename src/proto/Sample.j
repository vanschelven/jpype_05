;
; Output created by D-Java (mailto:umsilve1@cc.umanitoba.ca)
;

;Classfile version:
;    Major: 48
;    Minor: 0

.source Sample.java
.class  public synchronized jpype/Sample
.super  java/lang/Object
.implements java/io/Serializable
.implements java/lang/Comparable

.field private m_Target J
.field public m_Overloaded Ljava/util/BitSet;
.field public m_Checked Ljava/util/BitSet;
.field private static final RETURN_TYPES [Ljava/lang/Class;
.field private static final ARG_TYPES [[Ljava/lang/Class;
.field static class$0 Ljava/lang/Class;

; >> METHOD 1 <<
.method static <clinit>()V
    .limit stack 8
    .limit locals 1
.line 15
Label1:
    iconst_3
    anewarray java/lang/Class
    dup
    iconst_0
.line 16
    getstatic java/lang/Void/TYPE Ljava/lang/Class;
    aastore
    dup
    iconst_1
.line 17
    getstatic java/lang/Void/TYPE Ljava/lang/Class;
    aastore
    dup
    iconst_2
.line 18
    getstatic java/lang/Void/TYPE Ljava/lang/Class;
    aastore
.line 15
    putstatic jpype/Sample/RETURN_TYPES [Ljava/lang/Class;
.line 21
    iconst_1
    anewarray [Ljava/lang/Class;
    dup
    iconst_0
.line 22
    iconst_2
    anewarray java/lang/Class
    dup
    iconst_0
    getstatic jpype/Sample/class$0 Ljava/lang/Class;
    dup
    ifnonnull Label0
    pop
.catch java/lang/ClassNotFoundException from Label0 to Label2 using Label3
    ldc "java.lang.String"
    invokestatic java/lang/Class/forName(Ljava/lang/String;)Ljava/lang/Class;
Label2:
    dup
    putstatic jpype/Sample/class$0 Ljava/lang/Class;
    goto Label0
Label3:
    new java/lang/NoClassDefFoundError
    dup_x1
    swap
    invokevirtual java/lang/Throwable/getMessage()Ljava/lang/String;
    invokenonvirtual java/lang/NoClassDefFoundError/<init>(Ljava/lang/String;)V
    athrow
    aastore
    dup
Label4:
    iconst_1
    getstatic java/lang/Integer/TYPE Ljava/lang/Class;
    aastore
    aastore
.line 21
    putstatic jpype/Sample/ARG_TYPES [[Ljava/lang/Class;
.line 28
.catch java/lang/Exception from Label5 to Label6 using Label6
Label5:
    ldc "java.lang.Object"
    invokestatic java/lang/Class/forName(Ljava/lang/String;)Ljava/lang/Class;
    pop
    goto Label0
.line 30
Label6:
    astore_0
.line 32
.var 0 is ex Ljava/lang/Exception; from Label7 to Label8
Label7:
    aload_0
    invokevirtual java/lang/Exception/printStackTrace()V
.line 8
    return
Label8:
.end method

; >> METHOD 2 <<
.method public <init>()V
    .limit stack 4
    .limit locals 1
.line 8
.var 0 is this Ljpype/Sample; from Label1 to Label2
Label1:
    aload_0
    invokenonvirtual java/lang/Object/<init>()V
.line 12
    aload_0
    new java/util/BitSet
    dup
    iconst_2
    invokenonvirtual java/util/BitSet/<init>(I)V
    putfield jpype/Sample/m_Overloaded Ljava/util/BitSet;
.line 13
    aload_0
    new java/util/BitSet
    dup
    iconst_2
    invokenonvirtual java/util/BitSet/<init>(I)V
    putfield jpype/Sample/m_Checked Ljava/util/BitSet;
.line 8
    return
Label2:
.end method

; >> METHOD 3 <<
.method public add(Ljava/lang/String;I)V
    .throws java/io/IOException

    .limit stack 7
    .limit locals 5
.line 39
.var 0 is this Ljpype/Sample; from Label1 to Label7
.var 1 is a1 Ljava/lang/String; from Label1 to Label7
.var 2 is a2 I from Label1 to Label7
Label1:
    iconst_0
    istore_3
.line 41
.var 3 is methodIndex I from Label2 to Label7
Label2:
    aload_0
    getfield jpype/Sample/m_Checked Ljava/util/BitSet;
    iconst_0
    invokevirtual java/util/BitSet/get(I)Z
    ifne Label3
.line 43
    aload_0
    getfield jpype/Sample/m_Checked Ljava/util/BitSet;
    iconst_0
    iconst_1
    invokevirtual java/util/BitSet/set(IZ)V
.line 44
    aload_0
    getfield jpype/Sample/m_Overloaded Ljava/util/BitSet;
    iconst_0
    aload_0
    getfield jpype/Sample/m_Target J
    ldc "add"
    invokestatic jpype/PythonMethodCaller/hasMethod(JLjava/lang/String;)Z
    invokevirtual java/util/BitSet/set(IZ)V
.line 47
Label3:
    aload_0
    getfield jpype/Sample/m_Overloaded Ljava/util/BitSet;
    iconst_0
    invokevirtual java/util/BitSet/get(I)Z
    ifeq Label5
.line 49
    iconst_2
    anewarray java/lang/Object
    astore 4
.line 50
.var 4 is args [Ljava/lang/Object; from Label4 to Label5
Label4:
    aload 4
    iconst_0
    aload_1
    aastore
.line 51
    aload 4
    iconst_1
    new java/lang/Integer
    dup
    iload_2
    invokenonvirtual java/lang/Integer/<init>(I)V
    aastore
.line 53
    aload_0
    getfield jpype/Sample/m_Target J
    ldc "add"
    aload 4
    getstatic jpype/Sample/ARG_TYPES [[Ljava/lang/Class;
    iconst_0
    aaload
    getstatic jpype/Sample/RETURN_TYPES [Ljava/lang/Class;
    iconst_0
    aaload
    invokestatic jpype/PythonMethodCaller/invoke(JLjava/lang/String;[Ljava/lang/Object;[Ljava/lang/Class;Ljava/lang/Class;)Ljava/lang/Object;
    pop
    goto Label6
.line 58
Label5:
    new java/lang/NoSuchMethodError
    dup
    ldc "add"
    invokenonvirtual java/lang/NoSuchMethodError/<init>(Ljava/lang/String;)V
    athrow
.line 60
Label6:
    return
Label7:
.end method

; >> METHOD 4 <<
.method public equals(Ljava/lang/Object;)Z
    .limit stack 2
    .limit locals 2
.line 67
.var 0 is this Ljpype/Sample; from Label1 to Label2
.var 1 is arg0 Ljava/lang/Object; from Label1 to Label2
Label1:
    aload_0
    aload_1
    invokenonvirtual java/lang/Object/equals(Ljava/lang/Object;)Z
    ireturn
Label2:
.end method

; >> METHOD 5 <<
.method public compareTo(Ljava/lang/Object;)I
    .limit stack 1
    .limit locals 2
.line 75
.var 0 is this Ljpype/Sample; from Label1 to Label2
.var 1 is arg0 Ljava/lang/Object; from Label1 to Label2
Label1:
    iconst_0
    ireturn
Label2:
.end method

