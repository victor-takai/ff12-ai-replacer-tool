from enum import Enum

# class Action(Enum):
#     ADD_AUGMENT_ACCURACY_BOOST =            0x4094
#     ADD_AUGMENT_EVASION_BOOST =             0x4096 # 16534
#     ADD_AUGMENT_UNUSED =                    0X40B8 # 16568

# class TargetCondition(Enum):
    # AUGMENT_ACCURACY_BOOST_IS_PRESENT =     0x2002
    # AUGMENT_ACCURACY_BOOST_IS_MISSING =     0x2102

    # AUGMENT_EVASION_BOOST_IS_PRESENT =      0x2004
    # AUGMENT_EVASION_BOOST_IS_MISSING =      0x2104 # 8196

    # AUGMENT_UNUSED_IS_PRESENT =             0x2026 # 8230
    # AUGMENT_UNUSED_IS_MISSING =             0x2126 # 8486

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