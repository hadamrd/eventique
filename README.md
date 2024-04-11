# Eventique a simple and standalone event manager for Python

Eventique is a simple and standalone event manager for Python. It is designed to be used in a standalone manner, without any dependencies on other libraries. It is designed to be simple to use and easy to understand.

## Example Usage

```python
# Create an instance of the EventsHandler
evtHandler = EventsHandler()

# Define a callback function
evtHandler.on("my_event", lambda event: print("Event triggered!"))
evtHandler.send("my_event")  # Output: Event triggered!
```

## More complex example

```python
import threading
import time
from eventique.EventsHandler import EventsHandler
from eventique.ThreadSharedSingleton import ThreadSharedSingleton

class MyEventsHandler(EventsHandler, metaclass=ThreadSharedSingleton):
    def __init__(self):
        super().__init__()

class MyThread(threading.Thread):
    def __init__(self):
        super().__init__()
        self.daemon = True
        self.stop = threading.Event()
        MyEventsHandler().on("stop_event", self.onStopEvent, originator=self)
        MyEventsHandler().on("print_something", self.onPrintSomething, originator=self)

    def onStopEvent(self, event):
        print("Stop Event triggered!")
        self.stop.set()

    def onPrintSomething(self, event, something):
        print(something)
    
    def run(self):
        self.stop.wait()

mt = MyThread()
mt.start()
time.sleep(2)
MyEventsHandler().send("print_something", "Something to print 1")
time.sleep(2)
MyEventsHandler().send("print_something", "Something to print 2")
time.sleep(1)
MyEventsHandler().send("stop_event")
```
