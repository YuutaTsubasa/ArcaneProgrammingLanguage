class VariableDefinition:
    def __init__(self, name, addr, type, is_mutable) -> None:
        self.name = name
        self.addr = addr
        self.type = type
        self.is_mutable = is_mutable