import time


def stopwatch(seconds):
    start = time.time()
    time.clock()
    elapsed = 0
    while elapsed < seconds:
        elapsed = time.time() - start
        print("loop cycle time: %.1f, seconds count: %02d" % (time.clock(), elapsed))
        time.sleep(1)


stopwatch(20)
