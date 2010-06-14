#import "jp_runloopstopper.h"

@implementation JPRunLoopStopper : NSObject
{
    BOOL shouldStop;
}

+ currentRunLoopStopper
{
    //TODO: is this necessary for JPype?
}

- init
{
    self = [super init];
    shouldStop = NO;
    return self;
}

- (BOOL) shouldRun
{
    return !shouldStop;
}

+ (void) addRunLoopStopper:(JPRunLoopStopper *) runLoopStopper 
         toRunLoop:(NSRunLoop *) runLoop
{
    //TODO: do we need to check for existing stopper?
    //if runLoop in cls.singletons:
    //        raise ValueError, "Stopper already registered for this runLoop"
    //    cls.singletons[runLoop] = runLoopStopper
}

+ (void) removeRunLoopStopperFromRunLoop:(NSRunLoop *) runLoop
{
    //TODO: do we need to do this?
    //if runLoop not in cls.singletons:
    //        raise ValueError, "Stopper not registered for this runLoop"
    //    del cls.singletons[runLoop]
}

- (void) stop
{
    shouldStop = YES;
    if (NSApp != nil) {
        [NSApp terminate:self];
    }
}

- (void) performStop:(id) sender
{
    [self stop];
}

@end
