from eventique.EventsHandler import EventsHandler

# Create an instance of the EventsHandler
evtHandler = EventsHandler()

# Define a callback function
evtHandler.on("my_event", lambda event: print("Event triggered!"))
evtHandler.send("my_event")  # Output: Event triggered!

