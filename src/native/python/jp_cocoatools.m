#import <Cocoa/Cocoa.h>
#import <objc/objc.h>

#import "jp_runloopstopper.h"
#import "jp_cocoatools.h"

/*
def runConsoleEventLoop(argv=None, installInterrupt=False, mode=NSDefaultRunLoopMode):
    if argv is None:
        argv = sys.argv
    if installInterrupt:
        installMachInterrupt()
    runLoop = NSRunLoop.currentRunLoop()
    stopper = PyObjCAppHelperRunLoopStopper.alloc().init()
    PyObjCAppHelperRunLoopStopper.addRunLoopStopper_toRunLoop_(stopper, runLoop)
    try:

        while stopper.shouldRun():
            nextfire = runLoop.limitDateForMode_(mode)
            if not stopper.shouldRun():
                break
            if not runLoop.runMode_beforeDate_(mode, nextfire):
                stopper.stop()

    finally:
        PyObjCAppHelperRunLoopStopper.removeRunLoopStopperFromRunLoop_(runLoop)
*/

void JPRunConsoleEventLoop()
{
    NSRunLoop *runLoop = [NSRunLoop currentRunLoop];
    NSString *mode = NSDefaultRunLoopMode;
    JPRunLoopStopper *stopper = [[JPRunLoopStopper alloc] init];
    [JPRunLoopStopper addRunLoopStopper: stopper toRunLoop: runLoop];
    
    while ([stopper shouldRun]) {
        NSDate *nextfire = [runLoop limitDateForMode:mode];
        if (![stopper shouldRun]) {
            break;
        }
        
        if (![runLoop runMode:mode beforeDate: nextfire]) {
            [stopper stop];
        }
    }
    
    [JPRunLoopStopper removeRunLoopStopperFromRunLoop:runLoop];
}

