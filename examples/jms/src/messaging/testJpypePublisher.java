package messaging;

public class testJpypePublisher {

  public static void main(String[] args) {
    JpypePublisher pub = new JpypePublisher(
      "weblogic.jndi.WLInitialContextFactory",  // The java.naming.factory.initial
      "t3://158.188.40.21:7001",                // The java.naming.provider.url
      "weblogic.jms.ConnectionFactory",         // The connectionFactory
      "defaultTopic"                            // The topic
      );
    
    pub.publish("Start");
    long startTime=System.currentTimeMillis();
    for (int i=0; i<10; i++) {
      pub.publish("Hello World! " + i);
    }
    System.out.println("Message Rate = "+10000./(System.currentTimeMillis()-startTime));
    pub.publish("Stop");

    pub.close();
  }
}
