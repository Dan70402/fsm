

class Input(object):

    def __init__(self, event, state=None, extras=None):
        self.event = event
        self.state = state

        #extras msg channel for communicating between condition and transition
        if not extras:
            self.extras = {}
        else:
            self.extras = extras