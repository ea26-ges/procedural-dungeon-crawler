class FiniteStateMachine:
    def __init__(self):
        self.current_state = None
        self.states = {}

    def add_state(self, state_name, state):
        self.states[state_name] = state

    def set_state(self, state_name):
        if state_name in self.states:
            self.current_state = self.states[state_name]
            self.current_state.enter()
        else:
            raise ValueError(f"State '{state_name}' not found.")

    def update(self, *args):
        if self.current_state:
            self.current_state.update(*args)

    def handle_event(self, event):
        if self.current_state:
            next_state_name = self.current_state.handle_event(event)
            if next_state_name:
                self.set_state(next_state_name)

class State:
    def enter(self):
        pass

    def update(self):
        pass

    def handle_event(self, event):
        return None  # return next state name if applicable