package jpype;

import java.io.Serializable;
import java.util.BitSet;

/**
 */
public class Sample implements Serializable, Comparable
{
	private long m_Target;
	
	public BitSet m_Overloaded = new BitSet(2);  
	public BitSet m_Checked = new BitSet(2);  
	
	private static final Class[] RETURN_TYPES = {
		Void.TYPE,
		Void.TYPE,
		Void.TYPE,
	};
	
	private static final Class[][] ARG_TYPES = {
		{ String.class, Integer.TYPE }
	};

	static
	{
		try {
			Class.forName("java.lang.Object");
		}
		catch(Exception ex)
		{
			ex.printStackTrace();
		}
	}
	
	public void add(String a1, int a2)
		throws java.io.IOException
	{
		final int methodIndex = 0;
		
		if (! m_Checked.get(methodIndex))
		{
			m_Checked.set(methodIndex, true);
			m_Overloaded.set(methodIndex, PythonMethodCaller.hasMethod(m_Target, "add"));
		}
		
		if (m_Overloaded.get(methodIndex))
		{
			Object[] args = new Object[2];
			args[0] = a1;
			args[1] = new Integer(a2);
			
			PythonMethodCaller.invoke(m_Target, "add", args, ARG_TYPES[methodIndex], RETURN_TYPES[methodIndex]);
		}
		
		else
		{
			throw new NoSuchMethodError("add"); 
		}
	}

	/* (non-Javadoc)
	 * @see java.lang.Object#equals(java.lang.Object)
	 */
	public boolean equals(Object arg0)
	{
		return super.equals(arg0);
	}

	/* (non-Javadoc)
	 * @see java.lang.Comparable#compareTo(java.lang.Object)
	 */
	public int compareTo(Object arg0)
	{
		return 0;
	}
	
	
}
