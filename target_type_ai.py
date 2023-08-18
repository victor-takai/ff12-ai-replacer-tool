from enum import Enum

class TargetType(Enum):
    NONE =                                  0x0
    FOE =                                   0x1
    ALLY =                                  0x2
    LEADER =                                0x3
    SELF =                                  0x4
    SAME_GROUP =                            0x5
    ALLY_EXCL_SELF =                        0x6
    SAME_GROUP_EXCL_SELF =                  0x7
    DIFFERENT_GROUP =                       0x8
    ATTACKER =                              0x9
    FUTURE_ATTACKER =                       0xA