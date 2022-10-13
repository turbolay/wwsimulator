from enum import Enum 

class Phase(Enum):
    InputRegistration = 0,
    ConnectionConfirmation = 1,
    OutputRegistration = 2,
    TransactionSigning = 3,
    Ended = 4