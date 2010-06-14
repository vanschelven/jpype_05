package org.darkwolf.jpype.classgen;

public class JPypeClassLoader extends ClassLoader
{
	private String m_Name;

	private byte[] m_Bytes;

	public JPypeClassLoader(String name, byte[] data)
	{
		m_Name = name;
		m_Bytes = data;
	}

	/**
	 * @see java.lang.ClassLoader#findClass(java.lang.String)
	 */
	protected Class findClass(String arg0) throws ClassNotFoundException
	{
		if (arg0.equals(m_Name))
		{
			return defineClass(m_Name, m_Bytes, 0, m_Bytes.length);
		}

		return super.findClass(arg0);
	}
}