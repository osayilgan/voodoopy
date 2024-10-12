class State:
    def __init__(self):
        self.components = {}

    def update_state(self, state_data):
        """Frontend'den gelen state'i günceller."""
        for key, value in state_data.items():
            self.components[key] = value

    def __getattr__(self, name):
        """Dinamik olarak state.input1 gibi çağrılara izin verir."""
        if name in self.components:
            return self.components[name]
        else:
            raise AttributeError(f"'State' object has no attribute '{name}'")

    def __setattr__(self, name, value):
        """Dinamik olarak state.input1 = 'değer' şeklinde atama yapmayı sağlar."""
        if name == 'components':
            super().__setattr__(name, value)
        else:
            self.components[name] = value
