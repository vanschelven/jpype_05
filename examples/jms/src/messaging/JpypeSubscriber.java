package messaging;

import java.io.*;
import javax.naming.Context;
import javax.jms.*;
import java.util.*;
import javax.naming.*;

public class JpypeSubscriber implements MessageListener, ExceptionListener {

  private Context context = null;
  private Properties props = null;
  private TopicConnectionFactory factory = null;
  private TopicConnection connection = null;
  private TopicSession session = null;
  private Topic topic = null;
  private TopicSubscriber subscriber = null;
  private JpypeSubscriberCallback _callback = null;

  public JpypeSubscriber(
    JpypeSubscriberCallback callback, // The callback instance          
    String javaNamingFactory,         // The java.naming.factory.initial
    String javaNamingProvider,        // The java.naming.provider.url   
    String connectionFactory,         // The connectionFactory          
    String topicName) {               // The topic                      

    _callback = callback;
    
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

      // create a subscriber and make it listen
      subscriber = session.createSubscriber(topic);
      subscriber.setMessageListener(this);
      connection.setExceptionListener(this);

      // start the connection
      connection.start();

    } catch (Exception exception) {
      exception.printStackTrace();
      exit("Fatal error: "+exception +"\nExiting.....");
    }
  }

  /**
   * Implementation of MessageListener.onMessage
   */
  public void onMessage(Message message) {
    try {
      TextMessage textMessage = (TextMessage)message;
      _callback.onMessage(textMessage.getText());
    } catch (Exception exception) {
      exception.printStackTrace();
      exit("Fatal error: "+exception +"\nExiting.....");
    }
  }

  // Implementation of ExceptionListener.onException
  public void onException(JMSException exception) {
    exit("Received onException notification");
  }

  private void exit(String message) {
    System.err.println(message);

    try {
      connection.close();
    } catch (Exception error) {
      error.printStackTrace();
    }
    System.exit(0);
  }

}
