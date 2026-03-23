class Incident:
    def __init__(self, name, stages, root_cause, valid_actions, metrics=None):
        self.name = name
        self.stages = stages
        self.root_cause = root_cause
        self.valid_actions = valid_actions
        self.metrics = metrics or {}
        self.logs = []
        self.resolved = False