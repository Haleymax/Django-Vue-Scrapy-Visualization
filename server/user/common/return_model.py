from dataclasses import dataclass, asdict


@dataclass
class ReturnBase:
    status:int = None
    message:str = None

    def get_dict(self):
        return asdict(self)