import os, array

def output(fout, l, isFirst=0) :
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

def outputClass(srcfname, tgtfname, cname):
    print cname
    f = open(srcfname, "rb");
    fout = open(tgtfname, "w+")
    
    chunk = 20
    
    print >> fout, '#include <jpype.h>'
    
    print >> fout, "jbyte %s[] = {" % cname

    sz = 0
    l = f.read(chunk)
    output(fout, l, True);
    sz += len(l);
    while len(l) == chunk :
        l = f.read(chunk)
        output(fout, l);    
        sz += len(l);
    
    print >> fout, "};"
    
    print >> fout, "jsize get%sLength() { return %d; }" % (cname, sz)

    f.close()
    fout.close()
    
outputClass("../build/java/jpype/JPypeInvocationHandler.class", "native/common/jp_invocationhandler.cpp", "JPypeInvocationHandler")
outputClass("../build/java/jpype/ref/JPypeReference.class", "native/common/jp_reference.cpp", "JPypeReference")
outputClass("../build/java/jpype/ref/JPypeReferenceQueue.class", "native/common/jp_referencequeue.cpp", "JPypeReferenceQueue")

    