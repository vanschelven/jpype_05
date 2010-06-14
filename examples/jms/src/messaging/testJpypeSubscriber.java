package messaging;

public class testJpypeSubscriber implements JpypeSubscriberCallback {

  private long startTime=0;

  public static void main(String[] args) {
    testJpypeSubscriber tester = new testJpypeSubscriber();
    JpypeSubscriber sub = new JpypeSubscriber(
      tester,                                   // The callback instance
      "weblogic.jndi.WLInitialContextFactory",  // The java.naming.factory.initial
      "t3://158.188.40.21:7001",                // The java.naming.provider.url
      "weblogic.jms.ConnectionFactory",         // The connectionFactory
      "defaultTopic"                            // The topic
      );
    try {
      System.out.println("Waiting for thread to finish");
      synchronized(sub) {
        sub.wait();
      }
      System.out.println("Thread has finished");
    } catch (InterruptedException ex) {      
    }
  }

  public void onMessage(String message) {
    System.out.println(message);
    if (message.equals("Start")) {
      startTime = System.currentTimeMillis();
    } else if (message.equals("Stop")) {
      System.out.println("Message Rate = "+10000./(System.currentTimeMillis()-startTime));
    }
  }
}
