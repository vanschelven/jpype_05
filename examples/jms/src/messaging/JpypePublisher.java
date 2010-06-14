package messaging;

import java.io.*;
import java.net.InetAddress;
import java.util.*;
import javax.jms.*;
import javax.naming.*;

public class JpypePublisher {
  private Context context = null;
  private String factoryName = null;
  private Properties props = null;
  private TopicConnectionFactory factory = null;
  private TopicConnection connection = null;
  private TopicSession session = null;
  private Topic topic = null;
  private TopicSubscriber subscriber = null;
  private TopicPublisher publisher = null;

  public JpypePublisher (          
    String javaNamingFactory,  // The java.naming.factory.initial
    String javaNamingProvider, // The java.naming.provider.url   
    String connectionFactory,  // The connectionFactory          
    String topicName) {        // The topic                      

    // connect to the JNDI server and get a reference to 
    // root context
    props = new Properties(System.getProperties());
    try {
      props.put("java.naming.factory.initial",javaNamingFactory);
      props.put("java.naming.provider.url",javaNamingProvider);
      props.put("connectionFactory",connectionFactory);
      context = new InitialContext(props);

      // create a factory, connection, session and topic
      factory = (TopicConnectionFactory)context.lookup(connectionFactory);
      connection = factory.createTopicConnection();
      session = connection.createTopicSession(false, Session.DUPS_OK_ACKNOWLEDGE);
      topic = (Topic)context.lookup(topicName);

      // create a publisher
      publisher = session.createPublisher(topic);
    } catch (Exception exception) {
      exception.printStackTrace();
    }
  }

  /**
   * Publish a JMS message
   */
  public void publish(String message) {
    try {
      TextMessage textMessage = session.createTextMessage(message);
      publisher.publish(textMessage);
    } catch (JMSException exception) {
      exception.printStackTrace();
    }
  }

  /**
   * Close the JMS connection
   */
  public void close() {
    try {
      connection.close();
    } catch (JMSException exception) {
      exception.printStackTrace();
    }
  }

}

