class Incident:
    def __init__(self, name, stages, root_cause, valid_actions, metrics):
        self.name = name
        self.stages = stages              # list of (delay, level, message)
        self.root_cause = root_cause      # correct final action
        self.valid_actions = valid_actions  # partial fixes
        self.metrics = metrics
        self.logs = []
        self.resolved = False