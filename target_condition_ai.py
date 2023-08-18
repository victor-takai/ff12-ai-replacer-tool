from enum import Enum

class TargetCondition(Enum):
    HIGHEST_ATTACK_POWER =          0x0200 # 512
    LOWEST_ATTACK_POWER =           0x0300 # 768

    HIGHEST_DEFENSE =               0x0201 # 513
    LOWEST_DEFENSE =                0x0301 # 769

    # UNUSED_0X0202 =                 0x0202 # 514

    HIGHEST_MAGICK_RESIST =         0x0203 # 515
    LOWEST_MAGICK_RESIST =          0x0303 # 771

    HIGHEST_CURRENT_HP =            0x0204 # 516
    LOWEST_CURRENT_HP =             0x0304 # 772

    HIGHEST_CURRENT_MP =            0x0205 # 517
    LOWEST_CURRENT_MP =             0x0305 # 773

    HIGHEST_LEVEL =                 0x0206 # 518
    LOWEST_LEVEL =                  0x0306 # 774

    FURTHEST =                      0x0207 # 519
    NEAREST =                       0x0307 # 775

    HIGHEST_ATTACKER_COUNT =        0x0208 # 520
    LOWEST_ATTACKER_COUNT =         0x0308 # 776

    HIGHEST_MAX_HP =                0x0209 # 521
    LOWEST_MAX_HP =                 0x0309 # 777

    HIGHEST_MAX_MP =                0x020A # 522
    LOWEST_MAX_MP =                 0x030A # 778

    # UNUSED_0X020B =                 0x020B # 523

    HIGHEST_STRENGTH =              0x020C # 524
    LOWEST_STRENGTH =               0x030C # 780

    HIGHEST_MAGICK_POWER =          0x020D # 525
    LOWEST_MAGICK_POWER =           0x030D # 781

    HIGHEST_VITALITY =              0x020E # 526
    LOWEST_VITALITY =               0x030E # 782

    HIGHEST_SPEED =                 0x020F # 527
    LOWEST_SPEED =                  0x030F # 783

    # UNUSED_0X0210 =                 0x0210 # 528

    HIGHEST_ENMITY =                0x0211 # 529
    LOWEST_ENMITY =                 0x0311 # 785

    # UNUSED_0X0400 =                 0x0400 # 1024

    #========================= Status Effects =========================#

    STATUS_EFFECT_KO_IS_PRESENT =                   0x0600 # 1536
    STATUS_EFFECT_KO_IS_MISSING =                   0x0700 # 1792

    STATUS_EFFECT_STONE_IS_PRESENT =                0x0601 # 1537
    STATUS_EFFECT_STONE_IS_MISSING =                0x0701 # 1793

    STATUS_EFFECT_PETRIFY_IS_PRESENT =              0x0602 # 1538
    STATUS_EFFECT_PETRIFY_IS_MISSING =              0x0702 # 1794

    STATUS_EFFECT_STOP_IS_PRESENT =                 0x0603 # 1539
    STATUS_EFFECT_STOP_IS_MISSING =                 0x0703 # 1795

    STATUS_EFFECT_SLEEP_IS_PRESENT =                0x0604 # 1540
    STATUS_EFFECT_SLEEP_IS_MISSING =                0x0704 # 1796

    STATUS_EFFECT_CONFUSE_IS_PRESENT =              0x0605 # 1541
    STATUS_EFFECT_CONFUSE_IS_MISSING =              0x0705 # 1797

    STATUS_EFFECT_DOOM_IS_PRESENT =                 0x0606 # 1542
    STATUS_EFFECT_DOOM_IS_MISSING =                 0x0706 # 1798

    STATUS_EFFECT_BLIND_IS_PRESENT =                0x0607 # 1543
    STATUS_EFFECT_BLIND_IS_MISSING =                0x0707 # 1799

    STATUS_EFFECT_POISON_IS_PRESENT =               0x0608 # 1544
    STATUS_EFFECT_POISON_IS_MISSING =               0x0708 # 1800

    STATUS_EFFECT_SILENCE_IS_PRESENT =              0x0609 # 1545
    STATUS_EFFECT_SILENCE_IS_MISSING =              0x0709 # 1801

    STATUS_EFFECT_SAP_IS_PRESENT =                  0x060A # 1546
    STATUS_EFFECT_SAP_IS_MISSING =                  0x070A # 1802

    STATUS_EFFECT_OIL_IS_PRESENT =                  0x060B # 1547
    STATUS_EFFECT_OIL_IS_MISSING =                  0x070B # 1803

    STATUS_EFFECT_REVERSE_IS_PRESENT =              0x060C # 1548
    STATUS_EFFECT_REVERSE_IS_MISSING =              0x070C # 1804

    STATUS_EFFECT_DISABLE_IS_PRESENT =              0x060D # 1549
    STATUS_EFFECT_DISABLE_IS_MISSING =              0x070D # 1805

    STATUS_EFFECT_IMMOBOLIZE_IS_PRESENT =           0x060E # 1550
    STATUS_EFFECT_IMMOBOLIZE_IS_MISSING =           0x070E # 1806

    STATUS_EFFECT_SLOW_IS_PRESENT =                 0x060F # 1551
    STATUS_EFFECT_SLOW_IS_MISSING =                 0x070F # 1807

    STATUS_EFFECT_DISEASE_IS_PRESENT =              0x0610 # 1552
    STATUS_EFFECT_DISEASE_IS_MISSING =              0x0710 # 1808

    STATUS_EFFECT_LURE_IS_PRESENT =                 0x0611 # 1553
    STATUS_EFFECT_LURE_IS_MISSING =                 0x0711 # 1809

    STATUS_EFFECT_PROTECT_IS_PRESENT =              0x0612 # 1554
    STATUS_EFFECT_PROTECT_IS_MISSING =              0x0712 # 1810

    STATUS_EFFECT_SHELL_IS_PRESENT =                0x0613 # 1555
    STATUS_EFFECT_SHELL_IS_MISSING =                0x0713 # 1811

    STATUS_EFFECT_HASTE_IS_PRESENT =                0x0614 # 1556
    STATUS_EFFECT_HASTE_IS_MISSING =                0x0714 # 1812

    STATUS_EFFECT_BRAVERY_IS_PRESENT =              0x0615 # 1557
    STATUS_EFFECT_BRAVERY_IS_MISSING =              0x0715 # 1813

    STATUS_EFFECT_FAITH_IS_PRESENT =                0x0616 # 1558
    STATUS_EFFECT_FAITH_IS_MISSING =                0x0716 # 1814

    STATUS_EFFECT_REFLECT_IS_PRESENT =              0x0617 # 1559
    STATUS_EFFECT_REFLECT_IS_MISSING =              0x0717 # 1815

    STATUS_EFFECT_INVISIBLE_IS_PRESENT =            0x0618 # 1560
    STATUS_EFFECT_INVISIBLE_IS_MISSING =            0x0718 # 1816

    STATUS_EFFECT_REGEN_IS_PRESENT =                0x0619 # 1561
    STATUS_EFFECT_REGEN_IS_MISSING =                0x0719 # 1817

    STATUS_EFFECT_FLOAT_IS_PRESENT =                0x061A # 1562
    STATUS_EFFECT_FLOAT_IS_MISSING =                0x071A # 1818

    STATUS_EFFECT_BERSERK_IS_PRESENT =              0x061B # 1563
    STATUS_EFFECT_BERSERK_IS_MISSING =              0x071B # 1819

    STATUS_EFFECT_BUBBLE_IS_PRESENT =               0x061C # 1564
    STATUS_EFFECT_BUBBLE_IS_MISSING =               0x071C # 1820

    STATUS_EFFECT_HP_CRITICAL_IS_PRESENT =          0x061D # 1565
    STATUS_EFFECT_HP_CRITICAL_IS_MISSING =          0x071D # 1821

    STATUS_EFFECT_LIBRA_IS_PRESENT =                0x061E # 1566
    STATUS_EFFECT_LIBRA_IS_MISSING =                0x071E # 1822

    STATUS_EFFECT_X_ZONE_IS_PRESENT =               0x061F # 1567
    STATUS_EFFECT_X_ZONE_IS_MISSING =               0x071F # 1823

    #========================= AUGMENTS =========================#

    AUGMENT_STABILITY_IS_PRESENT =                      0x2000 # 8192
    AUGMENT_STABILITY_IS_MISSING =                      0x2100 # 8448

    AUGMENT_SAFETY_IS_PRESENT =                         0x2001 # 8193
    AUGMENT_SAFETY_IS_MISSING =                         0x2101 # 8449

    AUGMENT_ACCURACY_BOOST_IS_PRESENT =                 0x2002 # 8194
    AUGMENT_ACCURACY_BOOST_IS_MISSING =                 0x2102 # 8450

    AUGMENT_SHIELD_BOOST_IS_PRESENT =                   0x2003 # 8195
    AUGMENT_SHIELD_BOOST_IS_MISSING =                   0x2103 # 8451

    AUGMENT_EVASION_BOOST_IS_PRESENT =                  0x2004 # 8196
    AUGMENT_EVASION_BOOST_IS_MISSING =                  0x2104 # 8452

    AUGMENT_LAST_STAND_IS_PRESENT =                     0x2005 # 8197
    AUGMENT_LAST_STAND_IS_MISSING =                     0x2105 # 8453

    AUGMENT_COUNTER_IS_PRESENT =                        0x2006 # 8198
    AUGMENT_COUNTER_IS_MISSING =                        0x2106 # 8454

    AUGMENT_COUNTER_BOOST_IS_PRESENT =                  0x2007 # 8199
    AUGMENT_COUNTER_BOOST_IS_MISSING =                  0x2107 # 8455

    AUGMENT_SPELLBREAKER_IS_PRESENT =                   0x2008 # 8200
    AUGMENT_SPELLBREAKER_IS_MISSING =                   0x2108 # 8456

    AUGMENT_BRAWLER_IS_PRESENT =                        0x2009 # 8201
    AUGMENT_BRAWLER_IS_MISSING =                        0x2109 # 8457

    AUGMENT_ADRENALINE_IS_PRESENT =                     0x200A # 8202
    AUGMENT_ADRENALINE_IS_MISSING =                     0x210A # 8458

    AUGMENT_FOCUS_IS_PRESENT =                          0x200B # 8203
    AUGMENT_FOCUS_IS_MISSING =                          0x210B # 8459

    AUGMENT_LOBBYING_IS_PRESENT =                       0x200C # 8204
    AUGMENT_LOBBYING_IS_MISSING =                       0x210C # 8460

    AUGMENT_COMBO_BOOST_IS_PRESENT =                    0x200D # 8205
    AUGMENT_COMBO_BOOST_IS_MISSING =                    0x210D # 8461

    AUGMENT_ITEM_BOOST_IS_PRESENT =                     0x200E # 8206
    AUGMENT_ITEM_BOOST_IS_MISSING =                     0x210E # 8462

    AUGMENT_MEDICINE_REVERSE_IS_PRESENT =               0x200F # 8207
    AUGMENT_MEDICINE_REVERSE_IS_MISSING =               0x210F # 8463

    AUGMENT_WEATHERPROOF_IS_PRESENT =                   0x2010 # 8208
    AUGMENT_WEATHERPROOF_IS_MISSING =                   0x2110 # 8464

    AUGMENT_THIEVERY_IS_PRESENT =                       0x2011 # 8209
    AUGMENT_THIEVERY_IS_MISSING =                       0x2111 # 8465

    AUGMENT_SABOTEUR_IS_PRESENT =                       0x2012 # 8210
    AUGMENT_SABOTEUR_IS_MISSING =                       0x2112 # 8466

    AUGMENT_MAGICK_LORE_1_IS_PRESENT =                  0x2013 # 8211
    AUGMENT_MAGICK_LORE_1_IS_MISSING =                  0x2113 # 8467

    AUGMENT_WARMAGE_IS_PRESENT =                        0x2014 # 8212
    AUGMENT_WARMAGE_IS_MISSING =                        0x2114 # 8468

    AUGMENT_MARTYR_IS_PRESENT =                         0x2015 # 8213
    AUGMENT_MARTYR_IS_MISSING =                         0x2115 # 8469

    AUGMENT_MAGICK_LORE_2_IS_PRESENT =                  0x2016 # 8214
    AUGMENT_MAGICK_LORE_2_IS_MISSING =                  0x2116 # 8470

    AUGMENT_HEADSMAN_IS_PRESENT =                       0x2017 # 8215
    AUGMENT_HEADSMAN_IS_MISSING =                       0x2117 # 8471

    AUGMENT_MAGICK_LORE_3_IS_PRESENT =                  0x2018 # 8216
    AUGMENT_MAGICK_LORE_3_IS_MISSING =                  0x2118 # 8472

    AUGMENT_TREASURE_HUNTER_IS_PRESENT =                0x2019 # 8217
    AUGMENT_TREASURE_HUNTER_IS_MISSING =                0x2119 # 8473

    AUGMENT_MAGICK_LORE_4_IS_PRESENT =                  0x201A # 8218
    AUGMENT_MAGICK_LORE_4_IS_MISSING =                  0x211A # 8474

    AUGMENT_DOUBLE_EXP_IS_PRESENT =                     0x201B # 8219
    AUGMENT_DOUBLE_EXP_IS_MISSING =                     0x211B # 8475

    AUGMENT_DOUBLE_LP_IS_PRESENT =                      0x201C # 8220
    AUGMENT_DOUBLE_LP_IS_MISSING =                      0x211C # 8476

    AUGMENT_NO_EXP_IS_PRESENT =                         0x201D # 8221
    AUGMENT_NO_EXP_IS_MISSING =                         0x211D # 8477

    AUGMENT_SPELLBOUND_IS_PRESENT =                     0x201E # 8222
    AUGMENT_SPELLBOUND_IS_MISSING =                     0x211E # 8478

    AUGMENT_PIERCING_MAGICK_IS_PRESENT =                0x201F # 8223
    AUGMENT_PIERCING_MAGICK_IS_MISSING =                0x211F # 8479

    AUGMENT_OFFERING_IS_PRESENT =                       0x2020 # 8224
    AUGMENT_OFFERING_IS_MISSING =                       0x2120 # 8480

    AUGMENT_MUFFLE_IS_PRESENT =                         0x2021 # 8225
    AUGMENT_MUFFLE_IS_MISSING =                         0x2121 # 8481

    AUGMENT_LIFE_CLOAK_IS_PRESENT =                     0x2022 # 8226
    AUGMENT_LIFE_CLOAK_IS_MISSING =                     0x2122 # 8482

    AUGMENT_BATTLE_LORE_1_IS_PRESENT =                  0x2023 # 8227
    AUGMENT_BATTLE_LORE_1_IS_MISSING =                  0x2123 # 8483

    AUGMENT_PARSIMONY_IS_PRESENT =                      0x2024 # 8228
    AUGMENT_PARSIMONY_IS_MISSING =                      0x2124 # 8484

    AUGMENT_TREAD_LIGHTLY_IS_PRESENT =                  0x2025 # 8229
    AUGMENT_TREAD_LIGHTLY_IS_MISSING =                  0x2125 # 8485

    AUGMENT_UNUSED_IS_PRESENT =                         0x2026 # 8230
    AUGMENT_UNUSED_IS_MISSING =                         0x2126 # 8486

    AUGMENT_EMPTINESS_IS_PRESENT =                      0x2027 # 8231
    AUGMENT_EMPTINESS_IS_MISSING =                      0x2127 # 8487

    AUGMENT_RESIST_PIERCING_DAMAGE_IS_PRESENT =         0x2028 # 8232
    AUGMENT_RESIST_PIERCING_DAMAGE_IS_MISSING =         0x2128 # 8488

    AUGMENT_ANTI_LIBRA_IS_PRESENT =                     0x2029 # 8233
    AUGMENT_ANTI_LIBRA_IS_MISSING =                     0x2129 # 8489

    AUGMENT_BATTLE_LORE_2_IS_PRESENT =                  0x202A # 8234
    AUGMENT_BATTLE_LORE_2_IS_MISSING =                  0x212A # 8490

    AUGMENT_BATTLE_LORE_3_IS_PRESENT =                  0x202B # 8235
    AUGMENT_BATTLE_LORE_3_IS_MISSING =                  0x212B # 8491

    AUGMENT_BATTLE_LORE_4_IS_PRESENT =                  0x202C # 8236
    AUGMENT_BATTLE_LORE_4_IS_MISSING =                  0x212C # 8492

    AUGMENT_BATTLE_LORE_5_IS_PRESENT =                  0x202D # 8237
    AUGMENT_BATTLE_LORE_5_IS_MISSING =                  0x212D # 8493

    AUGMENT_BATTLE_LORE_6_IS_PRESENT =                  0x202E # 8238
    AUGMENT_BATTLE_LORE_6_IS_MISSING =                  0x212E # 8494

    AUGMENT_BATTLE_LORE_7_IS_PRESENT =                  0x202F # 8239
    AUGMENT_BATTLE_LORE_7_IS_MISSING =                  0x212F # 8495

    AUGMENT_STONESKIN_IS_PRESENT =                      0x2030 # 8240
    AUGMENT_STONESKIN_IS_MISSING =                      0x2130 # 8496

    AUGMENT_ATTACK_BOOST_IS_PRESENT =                   0x2031 # 8241
    AUGMENT_ATTACK_BOOST_IS_MISSING =                   0x2131 # 8497

    AUGMENT_DOUBLE_EDGED_IS_PRESENT =                   0x2032 # 8242
    AUGMENT_DOUBLE_EDGED_IS_MISSING =                   0x2132 # 8498

    AUGMENT_SPELLSPRING_IS_PRESENT =                    0x2033 # 8243
    AUGMENT_SPELLSPRING_IS_MISSING =                    0x2133 # 8499

    AUGMENT_ELEMENTAL_SHIFT_IS_PRESENT =                0x2034 # 8244
    AUGMENT_ELEMENTAL_SHIFT_IS_MISSING =                0x2134 # 8500

    AUGMENT_CELERITY_IS_PRESENT =                       0x2035 # 8245
    AUGMENT_CELERITY_IS_MISSING =                       0x2135 # 8501

    AUGMENT_SWIFTCAST_IS_PRESENT =                      0x2036 # 8246
    AUGMENT_SWIFTCAST_IS_MISSING =                      0x2136 # 8502

    AUGMENT_ATTACK_IMMUNITY_IS_PRESENT =                0x2037 # 8247
    AUGMENT_ATTACK_IMMUNITY_IS_MISSING =                0x2137 # 8503

    AUGMENT_MAGICK_IMMUNITY_IS_PRESENT =                0x2038 # 8248
    AUGMENT_MAGICK_IMMUNITY_IS_MISSING =                0x2138 # 8504

    AUGMENT_STATUS_IMMUNITY_IS_PRESENT =                0x2039 # 8249
    AUGMENT_STATUS_IMMUNITY_IS_MISSING =                0x2139 # 8505

    AUGMENT_DAMAGE_SPIKES_IS_PRESENT =                  0x203A # 8250
    AUGMENT_DAMAGE_SPIKES_IS_MISSING =                  0x213A # 8506

    AUGMENT_SUICIDAL_IS_PRESENT =                       0x203B # 8251
    AUGMENT_SUICIDAL_IS_MISSING =                       0x213B # 8507

    AUGMENT_BATTLE_LORE_8_IS_PRESENT =                  0x203C # 8252
    AUGMENT_BATTLE_LORE_8_IS_MISSING =                  0x213C # 8508

    AUGMENT_BATTLE_LORE_9_IS_PRESENT =                  0x203D # 8253
    AUGMENT_BATTLE_LORE_9_IS_MISSING =                  0x213D # 8509

    AUGMENT_BATTLE_LORE_10_IS_PRESENT =                 0x203E # 8254
    AUGMENT_BATTLE_LORE_10_IS_MISSING =                 0x213E # 8510

    AUGMENT_BATTLE_LORE_11_IS_PRESENT =                 0x203F # 8255
    AUGMENT_BATTLE_LORE_11_IS_MISSING =                 0x213F # 8511

    AUGMENT_BATTLE_LORE_12_IS_PRESENT =                 0x2040 # 8256
    AUGMENT_BATTLE_LORE_12_IS_MISSING =                 0x2140 # 8512

    AUGMENT_BATTLE_LORE_13_IS_PRESENT =                 0x2041 # 8257
    AUGMENT_BATTLE_LORE_13_IS_MISSING =                 0x2141 # 8513

    AUGMENT_BATTLE_LORE_14_IS_PRESENT =                 0x2042 # 8258
    AUGMENT_BATTLE_LORE_14_IS_MISSING =                 0x2142 # 8514

    AUGMENT_BATTLE_LORE_15_IS_PRESENT =                 0x2043 # 8259
    AUGMENT_BATTLE_LORE_15_IS_MISSING =                 0x2143 # 8515

    AUGMENT_BATTLE_LORE_16_IS_PRESENT =                 0x2044 # 8260
    AUGMENT_BATTLE_LORE_16_IS_MISSING =                 0x2144 # 8516

    AUGMENT_MAGICK_LORE_5_IS_PRESENT =                  0x2045 # 8261
    AUGMENT_MAGICK_LORE_5_IS_MISSING =                  0x2145 # 8517

    AUGMENT_MAGICK_LORE_6_IS_PRESENT =                  0x2046 # 8262
    AUGMENT_MAGICK_LORE_6_IS_MISSING =                  0x2146 # 8518

    AUGMENT_MAGICK_LORE_7_IS_PRESENT =                  0x2047 # 8263
    AUGMENT_MAGICK_LORE_7_IS_MISSING =                  0x2147 # 8519

    AUGMENT_MAGICK_LORE_8_IS_PRESENT =                  0x2048 # 8264
    AUGMENT_MAGICK_LORE_8_IS_MISSING =                  0x2148 # 8520

    AUGMENT_MAGICK_LORE_9_IS_PRESENT =                  0x2049 # 8265
    AUGMENT_MAGICK_LORE_9_IS_MISSING =                  0x2149 # 8521

    AUGMENT_HP_PLUS_30_IS_PRESENT =                     0x204A # 8266
    AUGMENT_HP_PLUS_30_IS_MISSING =                     0x214A # 8522

    AUGMENT_HP_PLUS_70_IS_PRESENT  =                    0x204B # 8267
    AUGMENT_HP_PLUS_70_IS_MISSING  =                    0x214B # 8523

    AUGMENT_HP_PLUS_110_IS_PRESENT  =                   0x204C # 8268
    AUGMENT_HP_PLUS_110_IS_MISSING  =                   0x214C # 8524

    AUGMENT_HP_PLUS_150_IS_PRESENT  =                   0x204D # 8269
    AUGMENT_HP_PLUS_150_IS_MISSING  =                   0x214D # 8525

    AUGMENT_HP_PLUS_190_IS_PRESENT  =                   0x204E # 8270
    AUGMENT_HP_PLUS_190_IS_MISSING  =                   0x214E # 8526

    AUGMENT_HP_PLUS_230_IS_PRESENT  =                   0x204F # 8271
    AUGMENT_HP_PLUS_230_IS_MISSING  =                   0x214F # 8527

    AUGMENT_HP_PLUS_270_IS_PRESENT  =                   0x2050 # 8272
    AUGMENT_HP_PLUS_270_IS_MISSING  =                   0x2150 # 8528

    AUGMENT_HP_PLUS_310_IS_PRESENT  =                   0x2051 # 8273
    AUGMENT_HP_PLUS_310_IS_MISSING  =                   0x2151 # 8529

    AUGMENT_HP_PLUS_350_IS_PRESENT  =                   0x2052 # 8274
    AUGMENT_HP_PLUS_350_IS_MISSING  =                   0x2152 # 8530

    AUGMENT_HP_PLUS_390_IS_PRESENT  =                   0x2053 # 8275
    AUGMENT_HP_PLUS_390_IS_MISSING  =                   0x2153 # 8531

    AUGMENT_HP_PLUS_435_IS_PRESENT  =                   0x2054 # 8276
    AUGMENT_HP_PLUS_435_IS_MISSING  =                   0x2154 # 8532

    AUGMENT_HP_PLUS_500_IS_PRESENT  =                   0x2055 # 8277
    AUGMENT_HP_PLUS_500_IS_MISSING  =                   0x2155 # 8533

    AUGMENT_INQUISITOR_IS_PRESENT =                     0x2056 # 8278
    AUGMENT_INQUISITOR_IS_MISSING =                     0x2156 # 8534

    AUGMENT_MAGICK_LORE_10_IS_PRESENT =                 0x2057 # 8279
    AUGMENT_MAGICK_LORE_10_IS_MISSING =                 0x2157 # 8535

    AUGMENT_SHIELD_BLOCK_3_IS_PRESENT =                 0x2058 # 8280
    AUGMENT_SHIELD_BLOCK_3_IS_MISSING =                 0x2158 # 8536

    AUGMENT_SHIELD_BLOCK_2_IS_PRESENT =                 0x2059 # 8281
    AUGMENT_SHIELD_BLOCK_2_IS_MISSING =                 0x2159 # 8537

    AUGMENT_SHIELD_BLOCK_1_IS_PRESENT =                 0x205A # 8282
    AUGMENT_SHIELD_BLOCK_1_IS_MISSING =                 0x215A # 8538

    AUGMENT_CHANNELING_3_IS_PRESENT =                   0x205B # 8283
    AUGMENT_CHANNELING_3_IS_MISSING =                   0x215B # 8539

    AUGMENT_CHANNELING_2_IS_PRESENT =                   0x205C # 8284
    AUGMENT_CHANNELING_2_IS_MISSING =                   0x215C # 8540

    AUGMENT_CHANNELING_1_IS_PRESENT =                   0x205D # 8285
    AUGMENT_CHANNELING_1_IS_MISSING =                   0x215D # 8541

    AUGMENT_SWIFTNESS_3_IS_PRESENT =                    0x205E # 8286
    AUGMENT_SWIFTNESS_3_IS_MISSING =                    0x215E # 8542

    AUGMENT_SWIFTNESS_2_IS_PRESENT =                    0x205F # 8287
    AUGMENT_SWIFTNESS_2_IS_MISSING =                    0x215F # 8543

    AUGMENT_SWIFTNESS_1_IS_PRESENT =                    0x2060 # 8288
    AUGMENT_SWIFTNESS_1_IS_MISSING =                    0x2160 # 8544

    AUGMENT_MAGICK_LORE_11_IS_PRESENT =                 0x2061 # 8289
    AUGMENT_MAGICK_LORE_11_IS_MISSING =                 0x2161 # 8545

    AUGMENT_MAGICK_LORE_12_IS_PRESENT =                 0x2062 # 8290
    AUGMENT_MAGICK_LORE_12_IS_MISSING =                 0x2162 # 8546

    AUGMENT_MAGICK_LORE_13_IS_PRESENT =                 0x2063 # 8291
    AUGMENT_MAGICK_LORE_13_IS_MISSING =                 0x2163 # 8547

    AUGMENT_MAGICK_LORE_14_IS_PRESENT =                 0x2064 # 8292
    AUGMENT_MAGICK_LORE_14_IS_MISSING =                 0x2164 # 8548

    AUGMENT_MAGICK_LORE_15_IS_PRESENT =                 0x2065 # 8293
    AUGMENT_MAGICK_LORE_15_IS_MISSING =                 0x2165 # 8549

    AUGMENT_MAGICK_LORE_16_IS_PRESENT =                 0x2066 # 8294
    AUGMENT_MAGICK_LORE_16_IS_MISSING =                 0x2166 # 8550

    AUGMENT_SERENITY_IS_PRESENT =                       0x2067 # 8295
    AUGMENT_SERENITY_IS_MISSING =                       0x2167 # 8551

    AUGMENT_GAMBIT_SLOT_1_IS_PRESENT =                  0x2068 # 8296
    AUGMENT_GAMBIT_SLOT_1_IS_MISSING =                  0x2168 # 8552

    AUGMENT_GAMBIT_SLOT_2_IS_PRESENT =                  0x2069 # 8297
    AUGMENT_GAMBIT_SLOT_2_IS_MISSING =                  0x2169 # 8553

    AUGMENT_GAMBIT_SLOT_3_IS_PRESENT =                  0x206A # 8298
    AUGMENT_GAMBIT_SLOT_3_IS_MISSING =                  0x216A # 8554

    AUGMENT_GAMBIT_SLOT_4_IS_PRESENT =                  0x206B # 8299
    AUGMENT_GAMBIT_SLOT_4_IS_MISSING =                  0x216B # 8555

    AUGMENT_GAMBIT_SLOT_5_IS_PRESENT =                  0x206C # 8300
    AUGMENT_GAMBIT_SLOT_5_IS_MISSING =                  0x216C # 8556

    AUGMENT_GAMBIT_SLOT_6_IS_PRESENT =                  0x206D # 8301
    AUGMENT_GAMBIT_SLOT_6_IS_MISSING =                  0x216D # 8557

    AUGMENT_GAMBIT_SLOT_7_IS_PRESENT =                  0x206E # 8302
    AUGMENT_GAMBIT_SLOT_7_IS_MISSING =                  0x216E # 8558

    AUGMENT_GAMBIT_SLOT_8_IS_PRESENT =                  0x206F # 8303
    AUGMENT_GAMBIT_SLOT_8_IS_MISSING =                  0x216F # 8559

    AUGMENT_GAMBIT_SLOT_9_IS_PRESENT =                  0x2070 # 8304
    AUGMENT_GAMBIT_SLOT_9_IS_MISSING =                  0x2170 # 8560

    AUGMENT_GAMBIT_SLOT_10_IS_PRESENT =                 0x2071 # 8305
    AUGMENT_GAMBIT_SLOT_10_IS_MISSING =                 0x2171 # 8561

    AUGMENT_ESSENTIALS_IS_PRESENT =                     0x2072 # 8306
    AUGMENT_ESSENTIALS_IS_MISSING =                     0x2172 # 8562

    AUGMENT_UNUSED_0X73_IS_PRESENT =                    0x2073 # 8307
    AUGMENT_UNUSED_0X73_IS_MISSING =                    0x2173 # 8563

    AUGMENT_REMEDY_LORE_3_IS_PRESENT =                  0x2074 # 8308
    AUGMENT_REMEDY_LORE_3_IS_MISSING =                  0x2174 # 8564

    AUGMENT_REMEDY_LORE_2_IS_PRESENT =                  0x2075 # 8309
    AUGMENT_REMEDY_LORE_2_IS_MISSING =                  0x2175 # 8565

    AUGMENT_REMEDY_LORE_1_IS_PRESENT =                  0x2076 # 8310
    AUGMENT_REMEDY_LORE_1_IS_MISSING =                  0x2176 # 8566

    AUGMENT_POTION_LORE_3_IS_PRESENT =                  0x2077 # 8311
    AUGMENT_POTION_LORE_3_IS_MISSING =                  0x2177 # 8567

    AUGMENT_POTION_LORE_2_IS_PRESENT =                  0x2078 # 8312
    AUGMENT_POTION_LORE_2_IS_MISSING =                  0x2178 # 8568

    AUGMENT_POTION_LORE_1_IS_PRESENT =                  0x2079 # 8313
    AUGMENT_POTION_LORE_1_IS_MISSING =                  0x2179 # 8569

    AUGMENT_ETHER_LOR_3_IS_PRESENT =                    0x207A # 8314
    AUGMENT_ETHER_LOR_3_IS_MISSING =                    0x217A # 8570

    AUGMENT_ETHER_LOR_2_IS_PRESENT =                    0x207B # 8315
    AUGMENT_ETHER_LOR_2_IS_MISSING =                    0x217B # 8571

    AUGMENT_ETHER_LOR_1_IS_PRESENT =                    0x207C # 8316
    AUGMENT_ETHER_LOR_1_IS_MISSING =                    0x217C # 8572

    AUGMENT_PHOENIX_LORE_3_IS_PRESENT =                 0x207D # 8317
    AUGMENT_PHOENIX_LORE_3_IS_MISSING =                 0x217D # 8573

    AUGMENT_PHOENIX_LORE_2_IS_PRESENT =                 0x207E # 8318
    AUGMENT_PHOENIX_LORE_2_IS_MISSING =                 0x217E # 8574

    AUGMENT_PHOENIX_LORE_1_IS_PRESENT =                 0x207F # 8319
    AUGMENT_PHOENIX_LORE_1_IS_MISSING =                 0x217F # 8575

    #========================= HP =========================#

    HP_GREATER_OR_EQUAL_90_PERCENT =            0x0E00 # 3584
    HP_LESSER_OR_EQUAL_90_PERCENT =             0x0F00 # 3840

    HP_GREATER_OR_EQUAL_80_PERCENT =            0x0E01 # 3585
    HP_LESSER_OR_EQUAL_80_PERCENT =             0x0F01 # 3841

    HP_GREATER_OR_EQUAL_70_PERCENT =            0x0E02 # 3586
    HP_LESSER_OR_EQUAL_70_PERCENT =             0x0F02 # 3842

    HP_GREATER_OR_EQUAL_60_PERCENT =            0x0E03 # 3587
    HP_LESSER_OR_EQUAL_60_PERCENT =             0x0F03 # 3843

    HP_GREATER_OR_EQUAL_50_PERCENT =            0x0E04 # 3588
    HP_LESSER_OR_EQUAL_50_PERCENT =             0x0F04 # 3844

    HP_GREATER_OR_EQUAL_40_PERCENT =            0x0E05 # 3589
    HP_LESSER_OR_EQUAL_40_PERCENT =             0x0F05 # 3845

    HP_GREATER_OR_EQUAL_30_PERCENT =            0x0E06 # 3590
    HP_LESSER_OR_EQUAL_30_PERCENT =             0x0F06 # 3846

    HP_GREATER_OR_EQUAL_20_PERCENT =            0x0E07 # 3591
    HP_LESSER_OR_EQUAL_20_PERCENT =             0x0F07 # 3847

    HP_GREATER_OR_EQUAL_10_PERCENT =            0x0E08 # 3592
    HP_LESSER_OR_EQUAL_10_PERCENT =             0x0F08 # 3848

    HP_GREATER_OR_EQUAL_0_PERCENT=              0x0E09 # 3593
    HP_LESSER_OR_EQUAL_0_PERCENT=               0x0F09 # 3849
    
    MAX_HP_GREATER_OR_EQUAL_500 =                       0x1000 # 4096
    MAX_HP_LESSER_OR_EQUAL_500 =                        0x1100 # 4352

    MAX_HP_GREATER_OR_EQUAL_1000 =                      0x1001 # 4097
    MAX_HP_LESSER_OR_EQUAL_1000 =                       0x1101 # 4353

    MAX_HP_GREATER_OR_EQUAL_2000 =                      0x1002 # 4098
    MAX_HP_LESSER_OR_EQUAL_2000 =                       0x1102 # 4354

    MAX_HP_GREATER_OR_EQUAL_5000 =                      0x1003 # 4099
    MAX_HP_LESSER_OR_EQUAL_5000 =                       0x1103 # 4355

    MAX_HP_GREATER_OR_EQUAL_10000 =                     0x1004 # 4100
    MAX_HP_LESSER_OR_EQUAL_10000 =                      0x1104 # 4356

    MAX_HP_GREATER_OR_EQUAL_20000 =                     0x1005 # 4101
    MAX_HP_LESSER_OR_EQUAL_20000 =                      0x1105 # 4357

    MAX_HP_GREATER_OR_EQUAL_30000 =                     0x1006 # 4102
    MAX_HP_LESSER_OR_EQUAL_30000 =                      0x1106 # 4358

    MAX_HP_GREATER_OR_EQUAL_50000 =                     0x1007 # 4103
    MAX_HP_LESSER_OR_EQUAL_50000 =                      0x1107 # 4359

    #========================= ELEMENTS =========================#

    IS_WEAK_TO_FIRE =                                   0x1400 # 5120
    IS_WEAK_TO_LIGHTNING =                              0x1401 # 5121
    IS_WEAK_TO_ICE =                                    0x1402 # 5122
    IS_WEAK_TO_EARTH =                                  0x1403 # 5123
    IS_WEAK_TO_WATER =                                  0x1404 # 5124
    IS_WEAK_TO_WIND =                                   0x1405 # 5125
    IS_WEAK_TO_HOLY =                                   0x1406 # 5126
    IS_WEAK_TO_DARK =                                   0x1407 # 5127
    
    IS_HALF_WEAK_TO_WATER =                             0x1500 # 5376
    IS_HALF_WEAK_TO_WIND =                              0x1501 # 5377
    IS_HALF_WEAK_TO_HOLY =                              0x1502 # 5378
    IS_HALF_WEAK_TO_DARK =                              0x1503 # 5379
    IS_HALF_WEAK_TO_FIRE =                              0x1504 # 5380
    IS_HALF_WEAK_TO_LIGHTNING =                         0x1505 # 5381
    IS_HALF_WEAK_TO_ICE =                               0x1506 # 5382
    IS_HALF_WEAK_TO_EARTH =                             0x1507 # 5383
    
    ABSORBS_FIRE =                                      0x1600 # 5632
    ABSORBS_LIGHTNING =                                 0x1601 # 5633
    ABSORBS_ICE =                                       0x1602 # 5634
    ABSORBS_EARTH =                                     0x1603 # 5635
    ABSORBS_WATER =                                     0x1604 # 5636
    ABSORBS_WIND =                                      0x1605 # 5637
    ABSORBS_HOLY =                                      0x1606 # 5638
    ABSORBS_DARK =                                      0x1607 # 5639
    
    VULNERABLE_TO_FIRE =                                0x1700 # 5888
    VULNERABLE_TO_LIGHTNING =                           0x1701 # 5889
    VULNERABLE_TO_ICE =                                 0x1702 # 5890
    VULNERABLE_TO_EARTH =                               0x1703 # 5891
    VULNERABLE_TO_WATER =                               0x1704 # 5892
    VULNERABLE_TO_WIND =                                0x1705 # 5893
    VULNERABLE_TO_HOLY =                                0x1706 # 5894
    VULNERABLE_TO_DARK =                                0x1707 # 5895