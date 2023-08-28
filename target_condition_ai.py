from enum import Enum

class TargetCondition(Enum):
    UNCONDITIONAL =                                     0x0000 # 0

    #========================= Character Stats =========================#

    HAS_HIGHEST_ATTACK_POWER =                          0x0200 # 512
    HAS_LOWEST_ATTACK_POWER =                           0x0300 # 768

    HAS_HIGHEST_DEFENSE =                               0x0201 # 513
    HAS_LOWEST_DEFENSE =                                0x0301 # 769

    # UNUSED_0X0202 =                                     0x0202 # 514

    HAS_HIGHEST_MAGICK_RESIST =                         0x0203 # 515
    HAS_LOWEST_MAGICK_RESIST =                          0x0303 # 771

    HAS_HIGHEST_CURRENT_HP =                            0x0204 # 516
    HAS_LOWEST_CURRENT_HP =                             0x0304 # 772

    HAS_HIGHEST_CURRENT_MP =                            0x0205 # 517
    HAS_LOWEST_CURRENT_MP =                             0x0305 # 773

    HAS_HIGHEST_LEVEL =                                 0x0206 # 518
    HAS_LOWEST_LEVEL =                                  0x0306 # 774

    IS_FURTHEST =                                       0x0207 # 519
    IS_NEAREST =                                        0x0307 # 775

    HAS_HIGHEST_ATTACKER_COUNT =                        0x0208 # 520
    HAS_LOWEST_ATTACKER_COUNT =                         0x0308 # 776

    HAS_HIGHEST_MAX_HP =                                0x0209 # 521
    HAS_LOWEST_MAX_HP =                                 0x0309 # 777

    HAS_HIGHEST_MAX_MP =                                0x020A # 522
    HAS_LOWEST_MAX_MP =                                 0x030A # 778

    # UNUSED_0X020B =                                     0x020B # 523

    HAS_HIGHEST_STRENGTH =                              0x020C # 524
    HAS_LOWEST_STRENGTH =                               0x030C # 780

    HAS_HIGHEST_MAGICK_POWER =                          0x020D # 525
    HAS_LOWEST_MAGICK_POWER =                           0x030D # 781

    HAS_HIGHEST_VITALITY =                              0x020E # 526
    HAS_LOWEST_VITALITY =                               0x030E # 782

    HAS_HIGHEST_SPEED =                                 0x020F # 527
    HAS_LOWEST_SPEED =                                  0x030F # 783

    # UNUSED_0X0210 =                                     0x0210 # 528

    HAS_HIGHEST_ENMITY =                                0x0211 # 529
    HAS_LOWEST_ENMITY =                                 0x0311 # 785

    # UNUSED_0X0400 =                                     0x0400 # 1024

    #========================= Status Effects =========================#

    IS_STATUS_EFFECT_KO_PRESENT =                       0x0600 # 1536
    IS_STATUS_EFFECT_KO_MISSING =                       0x0700 # 1792

    IS_STATUS_EFFECT_STONE_PRESENT =                    0x0601 # 1537
    IS_STATUS_EFFECT_STONE_MISSING =                    0x0701 # 1793

    IS_STATUS_EFFECT_PETRIFY_PRESENT =                  0x0602 # 1538
    IS_STATUS_EFFECT_PETRIFY_MISSING =                  0x0702 # 1794

    IS_STATUS_EFFECT_STOP_PRESENT =                     0x0603 # 1539
    IS_STATUS_EFFECT_STOP_MISSING =                     0x0703 # 1795

    IS_STATUS_EFFECT_SLEEP_PRESENT =                    0x0604 # 1540
    IS_STATUS_EFFECT_SLEEP_MISSING =                    0x0704 # 1796

    IS_STATUS_EFFECT_CONFUSE_PRESENT =                  0x0605 # 1541
    IS_STATUS_EFFECT_CONFUSE_MISSING =                  0x0705 # 1797

    IS_STATUS_EFFECT_DOOM_PRESENT =                     0x0606 # 1542
    IS_STATUS_EFFECT_DOOM_MISSING =                     0x0706 # 1798

    IS_STATUS_EFFECT_BLIND_PRESENT =                    0x0607 # 1543
    IS_STATUS_EFFECT_BLIND_MISSING =                    0x0707 # 1799

    IS_STATUS_EFFECT_POISON_PRESENT =                   0x0608 # 1544
    IS_STATUS_EFFECT_POISON_MISSING =                   0x0708 # 1800

    IS_STATUS_EFFECT_SILENCE_PRESENT =                  0x0609 # 1545
    IS_STATUS_EFFECT_SILENCE_MISSING =                  0x0709 # 1801

    IS_STATUS_EFFECT_SAP_PRESENT =                      0x060A # 1546
    IS_STATUS_EFFECT_SAP_MISSING =                      0x070A # 1802

    IS_STATUS_EFFECT_OIL_PRESENT =                      0x060B # 1547
    IS_STATUS_EFFECT_OIL_MISSING =                      0x070B # 1803

    IS_STATUS_EFFECT_REVERSE_PRESENT =                  0x060C # 1548
    IS_STATUS_EFFECT_REVERSE_MISSING =                  0x070C # 1804

    IS_STATUS_EFFECT_DISABLE_PRESENT =                  0x060D # 1549
    IS_STATUS_EFFECT_DISABLE_MISSING =                  0x070D # 1805

    IS_STATUS_EFFECT_IMMOBOLIZE_PRESENT =               0x060E # 1550
    IS_STATUS_EFFECT_IMMOBOLIZE_MISSING =               0x070E # 1806

    IS_STATUS_EFFECT_SLOW_PRESENT =                     0x060F # 1551
    IS_STATUS_EFFECT_SLOW_MISSING =                     0x070F # 1807

    IS_STATUS_EFFECT_DISEASE_PRESENT =                  0x0610 # 1552
    IS_STATUS_EFFECT_DISEASE_MISSING =                  0x0710 # 1808

    IS_STATUS_EFFECT_LURE_PRESENT =                     0x0611 # 1553
    IS_STATUS_EFFECT_LURE_MISSING =                     0x0711 # 1809

    IS_STATUS_EFFECT_PROTECT_PRESENT =                  0x0612 # 1554
    IS_STATUS_EFFECT_PROTECT_MISSING =                  0x0712 # 1810

    IS_STATUS_EFFECT_SHELL_PRESENT =                    0x0613 # 1555
    IS_STATUS_EFFECT_SHELL_MISSING =                    0x0713 # 1811

    IS_STATUS_EFFECT_HASTE_PRESENT =                    0x0614 # 1556
    IS_STATUS_EFFECT_HASTE_MISSING =                    0x0714 # 1812

    IS_STATUS_EFFECT_BRAVERY_PRESENT =                  0x0615 # 1557
    IS_STATUS_EFFECT_BRAVERY_MISSING =                  0x0715 # 1813

    IS_STATUS_EFFECT_FAITH_PRESENT =                    0x0616 # 1558
    IS_STATUS_EFFECT_FAITH_MISSING =                    0x0716 # 1814

    IS_STATUS_EFFECT_REFLECT_PRESENT =                  0x0617 # 1559
    IS_STATUS_EFFECT_REFLECT_MISSING =                  0x0717 # 1815

    IS_STATUS_EFFECT_INVISIBLE_PRESENT =                0x0618 # 1560
    IS_STATUS_EFFECT_INVISIBLE_MISSING =                0x0718 # 1816

    IS_STATUS_EFFECT_REGEN_PRESENT =                    0x0619 # 1561
    IS_STATUS_EFFECT_REGEN_MISSING =                    0x0719 # 1817

    IS_STATUS_EFFECT_FLOAT_PRESENT =                    0x061A # 1562
    IS_STATUS_EFFECT_FLOAT_MISSING =                    0x071A # 1818

    IS_STATUS_EFFECT_BERSERK_PRESENT =                  0x061B # 1563
    IS_STATUS_EFFECT_BERSERK_MISSING =                  0x071B # 1819

    IS_STATUS_EFFECT_BUBBLE_PRESENT =                   0x061C # 1564
    IS_STATUS_EFFECT_BUBBLE_MISSING =                   0x071C # 1820

    IS_STATUS_EFFECT_HP_CRITICAL_PRESENT =              0x061D # 1565
    IS_STATUS_EFFECT_HP_CRITICAL_MISSING =              0x071D # 1821

    IS_STATUS_EFFECT_LIBRA_PRESENT =                    0x061E # 1566
    IS_STATUS_EFFECT_LIBRA_MISSING =                    0x071E # 1822

    IS_STATUS_EFFECT_X_ZONE_PRESENT =                   0x061F # 1567
    IS_STATUS_EFFECT_X_ZONE_MISSING =                   0x071F # 1823

    #========================= Types =========================#

    IS_CLASS_EQUAL_HUMAN =                              0x0800 # 2048
    IS_CLASS_EQUAL_HUMANOID =                           0x0801 # 2049
    IS_CLASS_EQUAL_GIANT =                              0x0802 # 2050
    IS_CLASS_EQUAL_DRAGON =                             0x0803 # 2051
    IS_CLASS_EQUAL_BEAST =                              0x0804 # 2052
    IS_CLASS_EQUAL_INSECT =                             0x0805 # 2053
    IS_CLASS_EQUAL_PLANT =                              0x0806 # 2054
    IS_CLASS_EQUAL_AVION =                              0x0807 # 2055
    IS_CLASS_EQUAL_AMORPH =                             0x0808 # 2056
    IS_CLASS_EQUAL_FIEND =                              0x0809 # 2057
    IS_CLASS_EQUAL_ELEMENTAL =                          0x080A # 2058
    IS_CLASS_EQUAL_WARMECH =                            0x080B # 2059
    IS_CLASS_EQUAL_UNKNOWN =                            0x080C # 2060
    IS_CLASS_EQUAL_UNDEAD =                             0x080D # 2061
    IS_CLASS_EQUAL_CONSTRUCT =                          0x080E # 2062
    IS_CLASS_EQUAL_ICHTHIAN =                           0x080F # 2063
            
    IS_GENUS_EQUAL_TITANTOISE =                         0x0A00 # 2560
    IS_GENUS_EQUAL_GATOR =                              0x0A01 # 2561
    IS_GENUS_EQUAL_SERPENT =                            0x0A02 # 2562
    IS_GENUS_EQUAL_BEHEMOTH =                           0x0A03 # 2563
    IS_GENUS_EQUAL_WOLF =                               0x0A04 # 2564
    IS_GENUS_EQUAL_COEURL =                             0x0A05 # 2565
    IS_GENUS_EQUAL_DREAMHARE =                          0x0A06 # 2566
    IS_GENUS_EQUAL_TOAD =                               0x0A07 # 2567
    IS_GENUS_EQUAL_URSTRIX =                            0x0A08 # 2568
    IS_GENUS_EQUAL_WYVERN =                             0x0A09 # 2569
    IS_GENUS_EQUAL_PLATE_WYRM =                         0x0A0A # 2570
    IS_GENUS_EQUAL_TYRANT =                             0x0A0B # 2571
    IS_GENUS_EQUAL_FELL_WYRM =                          0x0A0C # 2572
    IS_GENUS_EQUAL_SLEIPNIR =                           0x0A0D # 2573
    IS_GENUS_EQUAL_NIGHTMARE =                          0x0A0E # 2574
    IS_GENUS_EQUAL_BOMB =                               0x0A0F # 2575
    IS_GENUS_EQUAL_GARGOYLE =                           0x0A10 # 2576
    IS_GENUS_EQUAL_MANTIS =                             0x0A11 # 2577
    IS_GENUS_EQUAL_MIMIC =                              0x0A12 # 2578
    IS_GENUS_EQUAL_COCKATRICE =                         0x0A13 # 2579
    IS_GENUS_EQUAL_STEELING =                           0x0A14 # 2580
    IS_GENUS_EQUAL_DIVER =                              0x0A15 # 2581
    IS_GENUS_EQUAL_MALBORO =                            0x0A16 # 2582
    IS_GENUS_EQUAL_MANDRAGORA =                         0x0A17 # 2583
    IS_GENUS_EQUAL_FLAN =                               0x0A18 # 2584
    IS_GENUS_EQUAL_PIRAHNA =                            0x0A19 # 2585
    IS_GENUS_EQUAL_ELEMENTAL =                          0x0A1A # 2586
    IS_GENUS_EQUAL_SLAVEN =                             0x0A1B # 2587
    IS_GENUS_EQUAL_HEADLESS =                           0x0A1C # 2588
    IS_GENUS_EQUAL_GOLEM =                              0x0A1D # 2589
    IS_GENUS_EQUAL_FACER =                              0x0A1E # 2590
    IS_GENUS_EQUAL_GHOST =                              0x0A1F # 2591
    IS_GENUS_EQUAL_REAPER =                             0x0A20 # 2592
    IS_GENUS_EQUAL_ZOMBIE =                             0x0A21 # 2593
    IS_GENUS_EQUAL_SKELETON =                           0x0A22 # 2594
    IS_GENUS_EQUAL_CHOCOBO =                            0x0A23 # 2595
    IS_GENUS_EQUAL_MINDFLAYER =                         0x0A24 # 2596
    IS_GENUS_EQUAL_BANGAA =                             0x0A25 # 2597
    IS_GENUS_EQUAL_VIERA =                              0x0A26 # 2598
    IS_GENUS_EQUAL_URUTAN_YENSA =                       0x0A27 # 2599
    IS_GENUS_EQUAL_GARIF =                              0x0A28 # 2600
    IS_GENUS_EQUAL_BAKNAMY =                            0x0A29 # 2601
    IS_GENUS_EQUAL_SEEQ =                               0x0A2A # 2602
    IS_GENUS_EQUAL_ESPER =                              0x0A2B # 2603
    IS_GENUS_EQUAL_GUARDIAN =                           0x0A2C # 2604
    IS_GENUS_EQUAL_JUDGE =                              0x0A2D # 2605
    IS_GENUS_EQUAL_DIVER_WYVERN =                       0x0A2E # 2606

    # IS_GENUS_EQUAL_RESERVE_0X2F =                       0x0A2F # 2607
    # IS_GENUS_EQUAL_RESERVE_0X30 =                       0x0A30 # 2608
    # IS_GENUS_EQUAL_RESERVE_0X31 =                       0x0A31 # 2609
    # IS_GENUS_EQUAL_RESERVE_0X32 =                       0x0A32 # 2610
    # IS_GENUS_EQUAL_RESERVE_0X33 =                       0x0A33 # 2611
    # IS_GENUS_EQUAL_RESERVE_0X34 =                       0x0A34 # 2612

    IS_GENUS_EQUAL_UNKNOWN =                            0x0A35 # 2613
    IS_GENUS_EQUAL_RAT =                                0x0A36 # 2614
    IS_GENUS_EQUAL_CACTUS =                             0x0A37 # 2615
    IS_GENUS_EQUAL_PIRATE =                             0x0A38 # 2616
    IS_GENUS_EQUAL_IMPERIAL_ARMY =                      0x0A39 # 2617
    IS_GENUS_EQUAL_DALMASCAN_ARMY =                     0x0A3A # 2618
    IS_GENUS_EQUAL_ROOK =                               0x0A3B # 2619
    IS_GENUS_EQUAL_COMMONER =                           0x0A3C # 2620
    IS_GENUS_EQUAL_UNCLASSIFIED =                       0x0A3D # 2621
    IS_GENUS_EQUAL_ANCIENT_BOMB =                       0x0A3E # 2622
    IS_GENUS_EQUAL_YENSA =                              0x0A3F # 2623

    #========================= Unknown =========================#

    # 0x0C00	3072	BattleWorkBaseInfo[0x52] == 0
    # 0x0C01	3073	BattleWorkBaseInfo[0x52] == 1
    # 0x0C02	3074	BattleWorkBaseInfo[0x52] == 2
    # ...	    ...     ...
    # 0x0CFF	3327	BattleWorkBaseInfo[0x52] == 255

    #========================= HP =========================#

    IS_HP_GREATER_OR_EQUAL_90_PERCENT =                 0x0E00 # 3584
    IS_HP_LESSER_OR_EQUAL_90_PERCENT =                  0x0F00 # 3840

    IS_HP_GREATER_OR_EQUAL_80_PERCENT =                 0x0E01 # 3585
    IS_HP_LESSER_OR_EQUAL_80_PERCENT =                  0x0F01 # 3841

    IS_HP_GREATER_OR_EQUAL_70_PERCENT =                 0x0E02 # 3586
    IS_HP_LESSER_OR_EQUAL_70_PERCENT =                  0x0F02 # 3842

    IS_HP_GREATER_OR_EQUAL_60_PERCENT =                 0x0E03 # 3587
    IS_HP_LESSER_OR_EQUAL_60_PERCENT =                  0x0F03 # 3843

    IS_HP_GREATER_OR_EQUAL_50_PERCENT =                 0x0E04 # 3588
    IS_HP_LESSER_OR_EQUAL_50_PERCENT =                  0x0F04 # 3844

    IS_HP_GREATER_OR_EQUAL_40_PERCENT =                 0x0E05 # 3589
    IS_HP_LESSER_OR_EQUAL_40_PERCENT =                  0x0F05 # 3845

    IS_HP_GREATER_OR_EQUAL_30_PERCENT =                 0x0E06 # 3590
    IS_HP_LESSER_OR_EQUAL_30_PERCENT =                  0x0F06 # 3846

    IS_HP_GREATER_OR_EQUAL_20_PERCENT =                 0x0E07 # 3591
    IS_HP_LESSER_OR_EQUAL_20_PERCENT =                  0x0F07 # 3847

    IS_HP_GREATER_OR_EQUAL_10_PERCENT =                 0x0E08 # 3592
    IS_HP_LESSER_OR_EQUAL_10_PERCENT =                  0x0F08 # 3848

    IS_HP_GREATER_OR_EQUAL_0_PERCENT=                   0x0E09 # 3593
    IS_HP_LESSER_OR_EQUAL_0_PERCENT=                    0x0F09 # 3849
    
    IS_MAX_HP_GREATER_OR_EQUAL_500 =                    0x1000 # 4096
    IS_MAX_HP_LESSER_OR_EQUAL_500 =                     0x1100 # 4352

    IS_MAX_HP_GREATER_OR_EQUAL_1000 =                   0x1001 # 4097
    IS_MAX_HP_LESSER_OR_EQUAL_1000 =                    0x1101 # 4353

    IS_MAX_HP_GREATER_OR_EQUAL_2000 =                   0x1002 # 4098
    IS_MAX_HP_LESSER_OR_EQUAL_2000 =                    0x1102 # 4354

    IS_MAX_HP_GREATER_OR_EQUAL_5000 =                   0x1003 # 4099
    IS_MAX_HP_LESSER_OR_EQUAL_5000 =                    0x1103 # 4355

    IS_MAX_HP_GREATER_OR_EQUAL_10000 =                  0x1004 # 4100
    IS_MAX_HP_LESSER_OR_EQUAL_10000 =                   0x1104 # 4356

    IS_MAX_HP_GREATER_OR_EQUAL_20000 =                  0x1005 # 4101
    IS_MAX_HP_LESSER_OR_EQUAL_20000 =                   0x1105 # 4357

    IS_MAX_HP_GREATER_OR_EQUAL_30000 =                  0x1006 # 4102
    IS_MAX_HP_LESSER_OR_EQUAL_30000 =                   0x1106 # 4358

    IS_MAX_HP_GREATER_OR_EQUAL_50000 =                  0x1007 # 4103
    IS_MAX_HP_LESSER_OR_EQUAL_50000 =                   0x1107 # 4359

    #========================= Unused =========================#

    # UNUSED_0X1200 =                                     0x1200 # 4608

    #========================= Element Weakness =========================#

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
    
    HAS_FIRE_ABSORPTION =                               0x1600 # 5632
    HAS_LIGHTNING_ABSORPTION =                          0x1601 # 5633
    HAS_ICE_ABSORPTION =                                0x1602 # 5634
    HAS_EARTH_ABSORPTION =                              0x1603 # 5635
    HAS_WATER_ABSORPTION =                              0x1604 # 5636
    HAS_WIND_ABSORPTION =                               0x1605 # 5637
    HAS_HOLY_ABSORPTION =                               0x1606 # 5638
    HAS_DARK_ABSORPTION =                               0x1607 # 5639
    
    IS_VULNERABLE_TO_FIRE =                             0x1700 # 5888
    IS_VULNERABLE_TO_LIGHTNING =                        0x1701 # 5889
    IS_VULNERABLE_TO_ICE =                              0x1702 # 5890
    IS_VULNERABLE_TO_EARTH =                            0x1703 # 5891
    IS_VULNERABLE_TO_WATER =                            0x1704 # 5892
    IS_VULNERABLE_TO_WIND =                             0x1705 # 5893
    IS_VULNERABLE_TO_HOLY =                             0x1706 # 5894
    IS_VULNERABLE_TO_DARK =                             0x1707 # 5895

    #========================= Party Member =========================#

    IS_PARTY_MEMBER_EQUAL_VAAN =                        0x1800 # 6144
    IS_PARTY_MEMBER_EQUAL_ASHE =                        0x1801 # 6145
    IS_PARTY_MEMBER_EQUAL_FRAN =                        0x1802 # 6146
    IS_PARTY_MEMBER_EQUAL_BALTHIER =                    0x1803 # 6147
    IS_PARTY_MEMBER_EQUAL_BASCH =                       0x1804 # 6148
    IS_PARTY_MEMBER_EQUAL_PENELO =                      0x1805 # 6149
    IS_PARTY_MEMBER_EQUAL_REKS =                        0x1806 # 6150
    IS_PARTY_MEMBER_EQUAL_AMALIA =                      0x1807 # 6151
    IS_PARTY_MEMBER_EQUAL_BASCH_PRISONER =              0x1808 # 6152
    IS_PARTY_MEMBER_EQUAL_BASCH_DARK_SUIT =             0x1809 # 6153
    IS_PARTY_MEMBER_EQUAL_LAMONT =                      0x180A # 6154
    IS_PARTY_MEMBER_EQUAL_VOSSLER_IMPERIAL =            0x180B # 6155
    IS_PARTY_MEMBER_EQUAL_VOSSLER_RESISTANCE =          0x180C # 6156
    IS_PARTY_MEMBER_EQUAL_LARSA =                       0x180D # 6157
    IS_PARTY_MEMBER_EQUAL_REDDAS =                      0x180E # 6158
    IS_PARTY_MEMBER_EQUAL_RESERVE_0X0F =                0x180F # 6159
    IS_PARTY_MEMBER_EQUAL_RESERVE_0X10 =                0x1810 # 6160
    IS_PARTY_MEMBER_EQUAL_RESERVE_0X11 =                0x1811 # 6161
    IS_PARTY_MEMBER_EQUAL_RESERVE_0X12 =                0x1812 # 6162
    IS_PARTY_MEMBER_EQUAL_RESERVE_0X13 =                0x1813 # 6163
    IS_PARTY_MEMBER_EQUAL_RESERVE_0X14 =                0x1814 # 6164
    IS_PARTY_MEMBER_EQUAL_RESERVE_0X15 =                0x1815 # 6165
    IS_PARTY_MEMBER_EQUAL_RESERVE_0X16 =                0x1816 # 6166
    IS_PARTY_MEMBER_EQUAL_RESERVE_0X17 =                0x1817 # 6167
    IS_PARTY_MEMBER_EQUAL_RESERVE_0X18 =                0x1818 # 6168
    IS_PARTY_MEMBER_EQUAL_RESERVE_0X19 =                0x1819 # 6169
    IS_PARTY_MEMBER_EQUAL_CHOCOBO =                     0x181A # 6170
    IS_PARTY_MEMBER_EQUAL_BELIAS =                      0x181B # 6171
    IS_PARTY_MEMBER_EQUAL_MATEUS =                      0x181C # 6172
    IS_PARTY_MEMBER_EQUAL_ANDRAMMELECH =                0x181D # 6173
    IS_PARTY_MEMBER_EQUAL_HASHMAL =                     0x181E # 6174
    IS_PARTY_MEMBER_EQUAL_CÚCHULAINN =                  0x181F # 6175
    IS_PARTY_MEMBER_EQUAL_FAMFRIT =                     0x1820 # 6176
    IS_PARTY_MEMBER_EQUAL_ZALERA =                      0x1821 # 6177
    IS_PARTY_MEMBER_EQUAL_SHEMHAZAI =                   0x1822 # 6178
    IS_PARTY_MEMBER_EQUAL_CHAOS =                       0x1823 # 6179
    IS_PARTY_MEMBER_EQUAL_ZEROMUS =                     0x1824 # 6180
    IS_PARTY_MEMBER_EQUAL_EXODUS =                      0x1825 # 6181
    IS_PARTY_MEMBER_EQUAL_ULTIMA =                      0x1826 # 6182
    IS_PARTY_MEMBER_EQUAL_ZODIARK =                     0x1827 # 6183

    #========================= Equipped =========================#
        
    HAS_WEAPON_EQUIPPED =                               0x1A00 # 6656
    HAS_SHIELD_EQUIPPED =                               0x1A01 # 6657
    HAS_HELM_EQUIPPED =                                 0x1A02 # 6658
    HAS_ARMOR_EQUIPPED =                                0x1A03 # 6659
    HAS_ACCESSORY_EQUIPPED =                            0x1A04 # 6660
    HAS_DEFAULT_WEAPON_EQUIPPED =                       0x1A05 # 6661

    IS_WEAPON_TYPE_EQUAL_NONE =                         0x1C00 # 7168
    IS_WEAPON_TYPE_EQUAL_UNARMED =                      0x1C01 # 7169
    IS_WEAPON_TYPE_EQUAL_DAGGER =                       0x1C02 # 7170
    IS_WEAPON_TYPE_EQUAL_SWORD =                        0x1C03 # 7171
    IS_WEAPON_TYPE_EQUAL_GREATSWORD =                   0x1C04 # 7172
    IS_WEAPON_TYPE_EQUAL_KATANA =                       0x1C05 # 7173
    IS_WEAPON_TYPE_EQUAL_NINJA_SWORD =                  0x1C06 # 7174
    IS_WEAPON_TYPE_EQUAL_STAFF =                        0x1C07 # 7175
    IS_WEAPON_TYPE_EQUAL_MACE =                         0x1C08 # 7176
    IS_WEAPON_TYPE_EQUAL_NONE_0X09 =                    0x1C09 # 7177
    IS_WEAPON_TYPE_EQUAL_MEASURE =                      0x1C0A # 7178
    IS_WEAPON_TYPE_EQUAL_AXE =                          0x1C0B # 7179
    IS_WEAPON_TYPE_EQUAL_HAMMER =                       0x1C0C # 7180
    IS_WEAPON_TYPE_EQUAL_ROD =                          0x1C0D # 7181
    IS_WEAPON_TYPE_EQUAL_POLE =                         0x1C0E # 7182
    IS_WEAPON_TYPE_EQUAL_SPEAR =                        0x1C0F # 7183
    IS_WEAPON_TYPE_EQUAL_NONE_0X10 =                    0x1C10 # 7184
    IS_WEAPON_TYPE_EQUAL_BOW =                          0x1C11 # 7185
    IS_WEAPON_TYPE_EQUAL_CROSSBOW =                     0x1C12 # 7186
    IS_WEAPON_TYPE_EQUAL_NONE_0X13 =                    0x1C13 # 7187
    IS_WEAPON_TYPE_EQUAL_GUN =                          0x1C14 # 7188
    IS_WEAPON_TYPE_EQUAL_HAND_BOMB =                    0x1C15 # 7189
    IS_WEAPON_TYPE_EQUAL_UNARMED_BRAWLER =              0x1C16 # 7190
        
    #========================= Unused =========================#

    # UNUSED_0X1E00 =                                     0x1E00 # 7680

    #========================= Augments =========================#

    IS_AUGMENT_STABILITY_PRESENT =                      0x2000 # 8192
    IS_AUGMENT_STABILITY_MISSING =                      0x2100 # 8448

    IS_AUGMENT_SAFETY_PRESENT =                         0x2001 # 8193
    IS_AUGMENT_SAFETY_MISSING =                         0x2101 # 8449

    IS_AUGMENT_ACCURACY_BOOST_PRESENT =                 0x2002 # 8194
    IS_AUGMENT_ACCURACY_BOOST_MISSING =                 0x2102 # 8450

    IS_AUGMENT_SHIELD_BOOST_PRESENT =                   0x2003 # 8195
    IS_AUGMENT_SHIELD_BOOST_MISSING =                   0x2103 # 8451

    IS_AUGMENT_EVASION_BOOST_PRESENT =                  0x2004 # 8196
    IS_AUGMENT_EVASION_BOOST_MISSING =                  0x2104 # 8452

    IS_AUGMENT_LAST_STAND_PRESENT =                     0x2005 # 8197
    IS_AUGMENT_LAST_STAND_MISSING =                     0x2105 # 8453

    IS_AUGMENT_COUNTER_PRESENT =                        0x2006 # 8198
    IS_AUGMENT_COUNTER_MISSING =                        0x2106 # 8454

    IS_AUGMENT_COUNTER_BOOST_PRESENT =                  0x2007 # 8199
    IS_AUGMENT_COUNTER_BOOST_MISSING =                  0x2107 # 8455

    IS_AUGMENT_SPELLBREAKER_PRESENT =                   0x2008 # 8200
    IS_AUGMENT_SPELLBREAKER_MISSING =                   0x2108 # 8456

    IS_AUGMENT_BRAWLER_PRESENT =                        0x2009 # 8201
    IS_AUGMENT_BRAWLER_MISSING =                        0x2109 # 8457

    IS_AUGMENT_ADRENALINE_PRESENT =                     0x200A # 8202
    IS_AUGMENT_ADRENALINE_MISSING =                     0x210A # 8458

    IS_AUGMENT_FOCUS_PRESENT =                          0x200B # 8203
    IS_AUGMENT_FOCUS_MISSING =                          0x210B # 8459

    IS_AUGMENT_LOBBYING_PRESENT =                       0x200C # 8204
    IS_AUGMENT_LOBBYING_MISSING =                       0x210C # 8460

    IS_AUGMENT_COMBO_BOOST_PRESENT =                    0x200D # 8205
    IS_AUGMENT_COMBO_BOOST_MISSING =                    0x210D # 8461

    IS_AUGMENT_ITEM_BOOST_PRESENT =                     0x200E # 8206
    IS_AUGMENT_ITEM_BOOST_MISSING =                     0x210E # 8462

    IS_AUGMENT_MEDICINE_REVERSE_PRESENT =               0x200F # 8207
    IS_AUGMENT_MEDICINE_REVERSE_MISSING =               0x210F # 8463

    IS_AUGMENT_WEATHERPROOF_PRESENT =                   0x2010 # 8208
    IS_AUGMENT_WEATHERPROOF_MISSING =                   0x2110 # 8464

    IS_AUGMENT_THIEVERY_PRESENT =                       0x2011 # 8209
    IS_AUGMENT_THIEVERY_MISSING =                       0x2111 # 8465

    IS_AUGMENT_SABOTEUR_PRESENT =                       0x2012 # 8210
    IS_AUGMENT_SABOTEUR_MISSING =                       0x2112 # 8466

    IS_AUGMENT_MAGICK_LORE_1_PRESENT =                  0x2013 # 8211
    IS_AUGMENT_MAGICK_LORE_1_MISSING =                  0x2113 # 8467

    IS_AUGMENT_WARMAGE_PRESENT =                        0x2014 # 8212
    IS_AUGMENT_WARMAGE_MISSING =                        0x2114 # 8468

    IS_AUGMENT_MARTYR_PRESENT =                         0x2015 # 8213
    IS_AUGMENT_MARTYR_MISSING =                         0x2115 # 8469

    IS_AUGMENT_MAGICK_LORE_2_PRESENT =                  0x2016 # 8214
    IS_AUGMENT_MAGICK_LORE_2_MISSING =                  0x2116 # 8470

    IS_AUGMENT_HEADSMAN_PRESENT =                       0x2017 # 8215
    IS_AUGMENT_HEADSMAN_MISSING =                       0x2117 # 8471

    IS_AUGMENT_MAGICK_LORE_3_PRESENT =                  0x2018 # 8216
    IS_AUGMENT_MAGICK_LORE_3_MISSING =                  0x2118 # 8472

    IS_AUGMENT_TREASURE_HUNTER_PRESENT =                0x2019 # 8217
    IS_AUGMENT_TREASURE_HUNTER_MISSING =                0x2119 # 8473

    IS_AUGMENT_MAGICK_LORE_4_PRESENT =                  0x201A # 8218
    IS_AUGMENT_MAGICK_LORE_4_MISSING =                  0x211A # 8474

    IS_AUGMENT_DOUBLE_EXP_PRESENT =                     0x201B # 8219
    IS_AUGMENT_DOUBLE_EXP_MISSING =                     0x211B # 8475

    IS_AUGMENT_DOUBLE_LP_PRESENT =                      0x201C # 8220
    IS_AUGMENT_DOUBLE_LP_MISSING =                      0x211C # 8476

    IS_AUGMENT_NO_EXP_PRESENT =                         0x201D # 8221
    IS_AUGMENT_NO_EXP_MISSING =                         0x211D # 8477

    IS_AUGMENT_SPELLBOUND_PRESENT =                     0x201E # 8222
    IS_AUGMENT_SPELLBOUND_MISSING =                     0x211E # 8478

    IS_AUGMENT_PIERCING_MAGICK_PRESENT =                0x201F # 8223
    IS_AUGMENT_PIERCING_MAGICK_MISSING =                0x211F # 8479

    IS_AUGMENT_OFFERING_PRESENT =                       0x2020 # 8224
    IS_AUGMENT_OFFERING_MISSING =                       0x2120 # 8480

    IS_AUGMENT_MUFFLE_PRESENT =                         0x2021 # 8225
    IS_AUGMENT_MUFFLE_MISSING =                         0x2121 # 8481

    IS_AUGMENT_LIFE_CLOAK_PRESENT =                     0x2022 # 8226
    IS_AUGMENT_LIFE_CLOAK_MISSING =                     0x2122 # 8482

    IS_AUGMENT_BATTLE_LORE_1_PRESENT =                  0x2023 # 8227
    IS_AUGMENT_BATTLE_LORE_1_MISSING =                  0x2123 # 8483

    IS_AUGMENT_PARSIMONY_PRESENT =                      0x2024 # 8228
    IS_AUGMENT_PARSIMONY_MISSING =                      0x2124 # 8484

    IS_AUGMENT_TREAD_LIGHTLY_PRESENT =                  0x2025 # 8229
    IS_AUGMENT_TREAD_LIGHTLY_MISSING =                  0x2125 # 8485

    IS_AUGMENT_UNUSED_0X26_PRESENT =                    0x2026 # 8230
    IS_AUGMENT_UNUSED_0X26_MISSING =                    0x2126 # 8486

    IS_AUGMENT_EMPTINESS_PRESENT =                      0x2027 # 8231
    IS_AUGMENT_EMPTINESS_MISSING =                      0x2127 # 8487

    IS_AUGMENT_RESIST_PIERCING_DAMAGE_PRESENT =         0x2028 # 8232
    IS_AUGMENT_RESIST_PIERCING_DAMAGE_MISSING =         0x2128 # 8488

    IS_AUGMENT_ANTI_LIBRA_PRESENT =                     0x2029 # 8233
    IS_AUGMENT_ANTI_LIBRA_MISSING =                     0x2129 # 8489

    IS_AUGMENT_BATTLE_LORE_2_PRESENT =                  0x202A # 8234
    IS_AUGMENT_BATTLE_LORE_2_MISSING =                  0x212A # 8490

    IS_AUGMENT_BATTLE_LORE_3_PRESENT =                  0x202B # 8235
    IS_AUGMENT_BATTLE_LORE_3_MISSING =                  0x212B # 8491

    IS_AUGMENT_BATTLE_LORE_4_PRESENT =                  0x202C # 8236
    IS_AUGMENT_BATTLE_LORE_4_MISSING =                  0x212C # 8492

    IS_AUGMENT_BATTLE_LORE_5_PRESENT =                  0x202D # 8237
    IS_AUGMENT_BATTLE_LORE_5_MISSING =                  0x212D # 8493

    IS_AUGMENT_BATTLE_LORE_6_PRESENT =                  0x202E # 8238
    IS_AUGMENT_BATTLE_LORE_6_MISSING =                  0x212E # 8494

    IS_AUGMENT_BATTLE_LORE_7_PRESENT =                  0x202F # 8239
    IS_AUGMENT_BATTLE_LORE_7_MISSING =                  0x212F # 8495

    IS_AUGMENT_STONESKIN_PRESENT =                      0x2030 # 8240
    IS_AUGMENT_STONESKIN_MISSING =                      0x2130 # 8496

    IS_AUGMENT_ATTACK_BOOST_PRESENT =                   0x2031 # 8241
    IS_AUGMENT_ATTACK_BOOST_MISSING =                   0x2131 # 8497

    IS_AUGMENT_DOUBLE_EDGED_PRESENT =                   0x2032 # 8242
    IS_AUGMENT_DOUBLE_EDGED_MISSING =                   0x2132 # 8498

    IS_AUGMENT_SPELLSPRING_PRESENT =                    0x2033 # 8243
    IS_AUGMENT_SPELLSPRING_MISSING =                    0x2133 # 8499

    IS_AUGMENT_ELEMENTAL_SHIFT_PRESENT =                0x2034 # 8244
    IS_AUGMENT_ELEMENTAL_SHIFT_MISSING =                0x2134 # 8500

    IS_AUGMENT_CELERITY_PRESENT =                       0x2035 # 8245
    IS_AUGMENT_CELERITY_MISSING =                       0x2135 # 8501

    IS_AUGMENT_SWIFTCAST_PRESENT =                      0x2036 # 8246
    IS_AUGMENT_SWIFTCAST_MISSING =                      0x2136 # 8502

    IS_AUGMENT_ATTACK_IMMUNITY_PRESENT =                0x2037 # 8247
    IS_AUGMENT_ATTACK_IMMUNITY_MISSING =                0x2137 # 8503

    IS_AUGMENT_MAGICK_IMMUNITY_PRESENT =                0x2038 # 8248
    IS_AUGMENT_MAGICK_IMMUNITY_MISSING =                0x2138 # 8504

    IS_AUGMENT_STATUS_IMMUNITY_PRESENT =                0x2039 # 8249
    IS_AUGMENT_STATUS_IMMUNITY_MISSING =                0x2139 # 8505

    IS_AUGMENT_DAMAGE_SPIKES_PRESENT =                  0x203A # 8250
    IS_AUGMENT_DAMAGE_SPIKES_MISSING =                  0x213A # 8506

    IS_AUGMENT_SUICIDAL_PRESENT =                       0x203B # 8251
    IS_AUGMENT_SUICIDAL_MISSING =                       0x213B # 8507

    IS_AUGMENT_BATTLE_LORE_8_PRESENT =                  0x203C # 8252
    IS_AUGMENT_BATTLE_LORE_8_MISSING =                  0x213C # 8508

    IS_AUGMENT_BATTLE_LORE_9_PRESENT =                  0x203D # 8253
    IS_AUGMENT_BATTLE_LORE_9_MISSING =                  0x213D # 8509

    IS_AUGMENT_BATTLE_LORE_10_PRESENT =                 0x203E # 8254
    IS_AUGMENT_BATTLE_LORE_10_MISSING =                 0x213E # 8510

    IS_AUGMENT_BATTLE_LORE_11_PRESENT =                 0x203F # 8255
    IS_AUGMENT_BATTLE_LORE_11_MISSING =                 0x213F # 8511

    IS_AUGMENT_BATTLE_LORE_12_PRESENT =                 0x2040 # 8256
    IS_AUGMENT_BATTLE_LORE_12_MISSING =                 0x2140 # 8512

    IS_AUGMENT_BATTLE_LORE_13_PRESENT =                 0x2041 # 8257
    IS_AUGMENT_BATTLE_LORE_13_MISSING =                 0x2141 # 8513

    IS_AUGMENT_BATTLE_LORE_14_PRESENT =                 0x2042 # 8258
    IS_AUGMENT_BATTLE_LORE_14_MISSING =                 0x2142 # 8514

    IS_AUGMENT_BATTLE_LORE_15_PRESENT =                 0x2043 # 8259
    IS_AUGMENT_BATTLE_LORE_15_MISSING =                 0x2143 # 8515

    IS_AUGMENT_BATTLE_LORE_16_PRESENT =                 0x2044 # 8260
    IS_AUGMENT_BATTLE_LORE_16_MISSING =                 0x2144 # 8516

    IS_AUGMENT_MAGICK_LORE_5_PRESENT =                  0x2045 # 8261
    IS_AUGMENT_MAGICK_LORE_5_MISSING =                  0x2145 # 8517

    IS_AUGMENT_MAGICK_LORE_6_PRESENT =                  0x2046 # 8262
    IS_AUGMENT_MAGICK_LORE_6_MISSING =                  0x2146 # 8518

    IS_AUGMENT_MAGICK_LORE_7_PRESENT =                  0x2047 # 8263
    IS_AUGMENT_MAGICK_LORE_7_MISSING =                  0x2147 # 8519

    IS_AUGMENT_MAGICK_LORE_8_PRESENT =                  0x2048 # 8264
    IS_AUGMENT_MAGICK_LORE_8_MISSING =                  0x2148 # 8520

    IS_AUGMENT_MAGICK_LORE_9_PRESENT =                  0x2049 # 8265
    IS_AUGMENT_MAGICK_LORE_9_MISSING =                  0x2149 # 8521

    IS_AUGMENT_HP_PLUS_30_PRESENT =                     0x204A # 8266
    IS_AUGMENT_HP_PLUS_30_MISSING =                     0x214A # 8522

    IS_AUGMENT_HP_PLUS_70_PRESENT =                     0x204B # 8267
    IS_AUGMENT_HP_PLUS_70_MISSING =                     0x214B # 8523

    IS_AUGMENT_HP_PLUS_110_PRESENT =                    0x204C # 8268
    IS_AUGMENT_HP_PLUS_110_MISSING =                    0x214C # 8524

    IS_AUGMENT_HP_PLUS_150_PRESENT =                    0x204D # 8269
    IS_AUGMENT_HP_PLUS_150_MISSING =                    0x214D # 8525

    IS_AUGMENT_HP_PLUS_190_PRESENT =                    0x204E # 8270
    IS_AUGMENT_HP_PLUS_190_MISSING =                    0x214E # 8526

    IS_AUGMENT_HP_PLUS_230_PRESENT =                    0x204F # 8271
    IS_AUGMENT_HP_PLUS_230_MISSING =                    0x214F # 8527

    IS_AUGMENT_HP_PLUS_270_PRESENT =                    0x2050 # 8272
    IS_AUGMENT_HP_PLUS_270_MISSING =                    0x2150 # 8528

    IS_AUGMENT_HP_PLUS_310_PRESENT =                    0x2051 # 8273
    IS_AUGMENT_HP_PLUS_310_MISSING =                    0x2151 # 8529

    IS_AUGMENT_HP_PLUS_350_PRESENT =                    0x2052 # 8274
    IS_AUGMENT_HP_PLUS_350_MISSING =                    0x2152 # 8530

    IS_AUGMENT_HP_PLUS_390_PRESENT =                    0x2053 # 8275
    IS_AUGMENT_HP_PLUS_390_MISSING =                    0x2153 # 8531

    IS_AUGMENT_HP_PLUS_435_PRESENT =                    0x2054 # 8276
    IS_AUGMENT_HP_PLUS_435_MISSING =                    0x2154 # 8532

    IS_AUGMENT_HP_PLUS_500_PRESENT =                    0x2055 # 8277
    IS_AUGMENT_HP_PLUS_500_MISSING =                    0x2155 # 8533

    IS_AUGMENT_INQUISITOR_PRESENT =                     0x2056 # 8278
    IS_AUGMENT_INQUISITOR_MISSING =                     0x2156 # 8534

    IS_AUGMENT_MAGICK_LORE_10_PRESENT =                 0x2057 # 8279
    IS_AUGMENT_MAGICK_LORE_10_MISSING =                 0x2157 # 8535

    IS_AUGMENT_SHIELD_BLOCK_3_PRESENT =                 0x2058 # 8280
    IS_AUGMENT_SHIELD_BLOCK_3_MISSING =                 0x2158 # 8536

    IS_AUGMENT_SHIELD_BLOCK_2_PRESENT =                 0x2059 # 8281
    IS_AUGMENT_SHIELD_BLOCK_2_MISSING =                 0x2159 # 8537

    IS_AUGMENT_SHIELD_BLOCK_1_PRESENT =                 0x205A # 8282
    IS_AUGMENT_SHIELD_BLOCK_1_MISSING =                 0x215A # 8538

    IS_AUGMENT_CHANNELING_3_PRESENT =                   0x205B # 8283
    IS_AUGMENT_CHANNELING_3_MISSING =                   0x215B # 8539

    IS_AUGMENT_CHANNELING_2_PRESENT =                   0x205C # 8284
    IS_AUGMENT_CHANNELING_2_MISSING =                   0x215C # 8540

    IS_AUGMENT_CHANNELING_1_PRESENT =                   0x205D # 8285
    IS_AUGMENT_CHANNELING_1_MISSING =                   0x215D # 8541

    IS_AUGMENT_SWIFTNESS_3_PRESENT =                    0x205E # 8286
    IS_AUGMENT_SWIFTNESS_3_MISSING =                    0x215E # 8542

    IS_AUGMENT_SWIFTNESS_2_PRESENT =                    0x205F # 8287
    IS_AUGMENT_SWIFTNESS_2_MISSING =                    0x215F # 8543

    IS_AUGMENT_SWIFTNESS_1_PRESENT =                    0x2060 # 8288
    IS_AUGMENT_SWIFTNESS_1_MISSING =                    0x2160 # 8544

    IS_AUGMENT_MAGICK_LORE_11_PRESENT =                 0x2061 # 8289
    IS_AUGMENT_MAGICK_LORE_11_MISSING =                 0x2161 # 8545

    IS_AUGMENT_MAGICK_LORE_12_PRESENT =                 0x2062 # 8290
    IS_AUGMENT_MAGICK_LORE_12_MISSING =                 0x2162 # 8546

    IS_AUGMENT_MAGICK_LORE_13_PRESENT =                 0x2063 # 8291
    IS_AUGMENT_MAGICK_LORE_13_MISSING =                 0x2163 # 8547

    IS_AUGMENT_MAGICK_LORE_14_PRESENT =                 0x2064 # 8292
    IS_AUGMENT_MAGICK_LORE_14_MISSING =                 0x2164 # 8548

    IS_AUGMENT_MAGICK_LORE_15_PRESENT =                 0x2065 # 8293
    IS_AUGMENT_MAGICK_LORE_15_MISSING =                 0x2165 # 8549

    IS_AUGMENT_MAGICK_LORE_16_PRESENT =                 0x2066 # 8294
    IS_AUGMENT_MAGICK_LORE_16_MISSING =                 0x2166 # 8550

    IS_AUGMENT_SERENITY_PRESENT =                       0x2067 # 8295
    IS_AUGMENT_SERENITY_MISSING =                       0x2167 # 8551

    IS_AUGMENT_GAMBIT_SLOT_1_PRESENT =                  0x2068 # 8296
    IS_AUGMENT_GAMBIT_SLOT_1_MISSING =                  0x2168 # 8552

    IS_AUGMENT_GAMBIT_SLOT_2_PRESENT =                  0x2069 # 8297
    IS_AUGMENT_GAMBIT_SLOT_2_MISSING =                  0x2169 # 8553

    IS_AUGMENT_GAMBIT_SLOT_3_PRESENT =                  0x206A # 8298
    IS_AUGMENT_GAMBIT_SLOT_3_MISSING =                  0x216A # 8554

    IS_AUGMENT_GAMBIT_SLOT_4_PRESENT =                  0x206B # 8299
    IS_AUGMENT_GAMBIT_SLOT_4_MISSING =                  0x216B # 8555

    IS_AUGMENT_GAMBIT_SLOT_5_PRESENT =                  0x206C # 8300
    IS_AUGMENT_GAMBIT_SLOT_5_MISSING =                  0x216C # 8556

    IS_AUGMENT_GAMBIT_SLOT_6_PRESENT =                  0x206D # 8301
    IS_AUGMENT_GAMBIT_SLOT_6_MISSING =                  0x216D # 8557

    IS_AUGMENT_GAMBIT_SLOT_7_PRESENT =                  0x206E # 8302
    IS_AUGMENT_GAMBIT_SLOT_7_MISSING =                  0x216E # 8558

    IS_AUGMENT_GAMBIT_SLOT_8_PRESENT =                  0x206F # 8303
    IS_AUGMENT_GAMBIT_SLOT_8_MISSING =                  0x216F # 8559

    IS_AUGMENT_GAMBIT_SLOT_9_PRESENT =                  0x2070 # 8304
    IS_AUGMENT_GAMBIT_SLOT_9_MISSING =                  0x2170 # 8560

    IS_AUGMENT_GAMBIT_SLOT_10_PRESENT =                 0x2071 # 8305
    IS_AUGMENT_GAMBIT_SLOT_10_MISSING =                 0x2171 # 8561

    IS_AUGMENT_ESSENTIALS_PRESENT =                     0x2072 # 8306
    IS_AUGMENT_ESSENTIALS_MISSING =                     0x2172 # 8562

    IS_AUGMENT_UNUSED_0X73_PRESENT =                    0x2073 # 8307
    IS_AUGMENT_UNUSED_0X73_MISSING =                    0x2173 # 8563

    IS_AUGMENT_REMEDY_LORE_3_PRESENT =                  0x2074 # 8308
    IS_AUGMENT_REMEDY_LORE_3_MISSING =                  0x2174 # 8564

    IS_AUGMENT_REMEDY_LORE_2_PRESENT =                  0x2075 # 8309
    IS_AUGMENT_REMEDY_LORE_2_MISSING =                  0x2175 # 8565

    IS_AUGMENT_REMEDY_LORE_1_PRESENT =                  0x2076 # 8310
    IS_AUGMENT_REMEDY_LORE_1_MISSING =                  0x2176 # 8566

    IS_AUGMENT_POTION_LORE_3_PRESENT =                  0x2077 # 8311
    IS_AUGMENT_POTION_LORE_3_MISSING =                  0x2177 # 8567

    IS_AUGMENT_POTION_LORE_2_PRESENT =                  0x2078 # 8312
    IS_AUGMENT_POTION_LORE_2_MISSING =                  0x2178 # 8568

    IS_AUGMENT_POTION_LORE_1_PRESENT =                  0x2079 # 8313
    IS_AUGMENT_POTION_LORE_1_MISSING =                  0x2179 # 8569

    IS_AUGMENT_ETHER_LOR_3_PRESENT =                    0x207A # 8314
    IS_AUGMENT_ETHER_LOR_3_MISSING =                    0x217A # 8570

    IS_AUGMENT_ETHER_LOR_2_PRESENT =                    0x207B # 8315
    IS_AUGMENT_ETHER_LOR_2_MISSING =                    0x217B # 8571

    IS_AUGMENT_ETHER_LOR_1_PRESENT =                    0x207C # 8316
    IS_AUGMENT_ETHER_LOR_1_MISSING =                    0x217C # 8572

    IS_AUGMENT_PHOENIX_LORE_3_PRESENT =                 0x207D # 8317
    IS_AUGMENT_PHOENIX_LORE_3_MISSING =                 0x217D # 8573

    IS_AUGMENT_PHOENIX_LORE_2_PRESENT =                 0x207E # 8318
    IS_AUGMENT_PHOENIX_LORE_2_MISSING =                 0x217E # 8574

    IS_AUGMENT_PHOENIX_LORE_1_PRESENT =                 0x207F # 8319
    IS_AUGMENT_PHOENIX_LORE_1_MISSING =                 0x217F # 8575

    #========================= Miscellaneous =========================#

    HAS_PARTY_LEADER =                                  0x2200 # 8704
    IS_PLAYER_PARTY_LEADER =                            0x2201 # 8705
    IS_PARTY_LEADER =                                   0x2202 # 8706
    IS_GUEST =                                          0x2203 # 8707
    IS_ESPER =                                          0x2204 # 8708

    # UNUSED_0X2205 =                                     0x2205 # 8709
    # UNUSED_0X2206 =                                     0x2206 # 8710
    # UNUSED_0X2207 =                                     0x2207 # 8711

    IS_ENMITY_GREATER_EQUAL_P =                         0x2208 # 8712
    IS_GROUP_EQUAL_P =                                  0x2209 # 8713
    IS_STATUS_EFFECT_EQUAL_P =                          0x220A # 8714
    IS_CLASS_EQUAL_P =                                  0x220B # 8715
    IS_GENUS_EQUAL_P =                                  0x220C # 8716
    IS_HUNT_OR_BOSS =                                   0x220D # 8717

    # UNUSED_0X220E =                                     0x220E # 8718
    # UNUSED_0X220F =                                     0x220F # 8719

    IS_LEVEL_GREATER_EQUAL_P =                          0x2210 # 8720
    IS_SPAWN_POSITION_WITHIN_P_METERS =                 0x2211 # 8721
    IS_PARTY_MEMBER_WITHIN_P_METERS =                   0x2212 # 8722
    IS_PLAYER_PARTY_LEADER_WITHIN_P_METERS =            0x2213 # 8723
    IS_PARTY_LEADER_WITHIN_P_METERS =                   0x2214 # 8724
    IS_PLAYER_PARTY_LEADER_WITHIN_RADIUS_P_METERS =     0x2215 # 8725

    # UNUSED_0X2216 =                                     0x2216 # 8726
    # UNUSED_0X2217 =                                     0x2217 # 8727

    IS_TARGETING_LEADER =                               0x2218 # 8728
    IS_TARGETING_SELF =                                 0x2219 # 8729
    IS_TARGETING_ALLY =                                 0x221A # 8730
    IS_TARGETING_PARTY_MEMBER_P =                       0x221B # 8731
    IS_DIRECTLY_FACING_CASTER_WITHIN_RADIUS_P_METERS =  0x221C # 8732
    IS_CASTER_WITHIN_P_METERS =                         0x221D # 8733
    HAS_NEGATIVE_TEMPORARY_STATUS_EFFECT =              0x221E # 8734
    HAS_POSITIVE_TEMPORARY_STATUS_EFFECT =              0x221F # 8735
    HAS_RANGED_WEAPON_EQUIPPED =                        0x2220 # 8736

    #========================= Position =========================#

    IS_POSITION_1_WITHIN_P_METERS =                     0x2400 # 9216
    IS_POSITION_2_WITHIN_P_METERS =                     0x2401 # 9217
    IS_POSITION_3_WITHIN_P_METERS =                     0x2402 # 9218
    IS_POSITION_4_WITHIN_P_METERS =                     0x2403 # 9219
    IS_POSITION_5_WITHIN_P_METERS =                     0x2404 # 9220
    IS_POSITION_6_WITHIN_P_METERS =                     0x2405 # 9221
    IS_POSITION_7_WITHIN_P_METERS =                     0x2406 # 9222
    IS_POSITION_8_WITHIN_P_METERS =                     0x2407 # 9223
    IS_POSITION_9_WITHIN_P_METERS =                     0x2408 # 9224
    IS_POSITION_10_WITHIN_P_METERS =                    0x2409 # 9225
    IS_POSITION_11_WITHIN_P_METERS =                    0x240A # 9226
    IS_POSITION_12_WITHIN_P_METERS =                    0x240B # 9227
    IS_POSITION_13_WITHIN_P_METERS =                    0x240C # 9228
    IS_POSITION_14_WITHIN_P_METERS =                    0x240D # 9229
    IS_POSITION_15_WITHIN_P_METERS =                    0x240E # 9230
    IS_POSITION_16_WITHIN_P_METERS =                    0x240F # 9231
    IS_POSITION_17_WITHIN_P_METERS =                    0x2410 # 9232
    IS_POSITION_18_WITHIN_P_METERS =                    0x2411 # 9233
    IS_POSITION_19_WITHIN_P_METERS =                    0x2412 # 9234
    IS_POSITION_20_WITHIN_P_METERS =                    0x2413 # 9235
    IS_POSITION_21_WITHIN_P_METERS =                    0x2414 # 9236
    IS_POSITION_22_WITHIN_P_METERS =                    0x2415 # 9237
    IS_POSITION_23_WITHIN_P_METERS =                    0x2416 # 9238
    IS_POSITION_24_WITHIN_P_METERS =                    0x2417 # 9239
    IS_POSITION_25_WITHIN_P_METERS =                    0x2418 # 9240
    IS_POSITION_26_WITHIN_P_METERS =                    0x2419 # 9241
    IS_POSITION_27_WITHIN_P_METERS =                    0x241A # 9242
    IS_POSITION_28_WITHIN_P_METERS =                    0x241B # 9243
    IS_POSITION_29_WITHIN_P_METERS =                    0x241C # 9244
    IS_POSITION_30_WITHIN_P_METERS =                    0x241D # 9245
    IS_POSITION_31_WITHIN_P_METERS =                    0x241E # 9246
    IS_POSITION_32_WITHIN_P_METERS =                    0x241F # 9247
    IS_POSITION_33_WITHIN_P_METERS =                    0x2420 # 9248
    IS_POSITION_34_WITHIN_P_METERS =                    0x2421 # 9249
    IS_POSITION_35_WITHIN_P_METERS =                    0x2422 # 9250
    IS_POSITION_36_WITHIN_P_METERS =                    0x2423 # 9251
    IS_POSITION_37_WITHIN_P_METERS =                    0x2424 # 9252
    IS_POSITION_38_WITHIN_P_METERS =                    0x2425 # 9253
    IS_POSITION_39_WITHIN_P_METERS =                    0x2426 # 9254
    IS_POSITION_40_WITHIN_P_METERS =                    0x2427 # 9255
    IS_POSITION_41_WITHIN_P_METERS =                    0x2428 # 9256
    IS_POSITION_42_WITHIN_P_METERS =                    0x2429 # 9257
    IS_POSITION_43_WITHIN_P_METERS =                    0x242A # 9258
    IS_POSITION_44_WITHIN_P_METERS =                    0x242B # 9259
    IS_POSITION_45_WITHIN_P_METERS =                    0x242C # 9260
    IS_POSITION_46_WITHIN_P_METERS =                    0x242D # 9261
    IS_POSITION_47_WITHIN_P_METERS =                    0x242E # 9262
    IS_POSITION_48_WITHIN_P_METERS =                    0x242F # 9263
    IS_POSITION_49_WITHIN_P_METERS =                    0x2430 # 9264
    IS_POSITION_50_WITHIN_P_METERS =                    0x2431 # 9265
    IS_POSITION_51_WITHIN_P_METERS =                    0x2432 # 9266
    IS_POSITION_52_WITHIN_P_METERS =                    0x2433 # 9267
    IS_POSITION_53_WITHIN_P_METERS =                    0x2434 # 9268
    IS_POSITION_54_WITHIN_P_METERS =                    0x2435 # 9269
    IS_POSITION_55_WITHIN_P_METERS =                    0x2436 # 9270
    IS_POSITION_56_WITHIN_P_METERS =                    0x2437 # 9271
    IS_POSITION_57_WITHIN_P_METERS =                    0x2438 # 9272
    IS_POSITION_58_WITHIN_P_METERS =                    0x2439 # 9273
    IS_POSITION_59_WITHIN_P_METERS =                    0x243A # 9274
    IS_POSITION_60_WITHIN_P_METERS =                    0x243B # 9275
    IS_POSITION_61_WITHIN_P_METERS =                    0x243C # 9276
    IS_POSITION_62_WITHIN_P_METERS =                    0x243D # 9277
    IS_POSITION_63_WITHIN_P_METERS =                    0x243E # 9278
    IS_POSITION_64_WITHIN_P_METERS =                    0x243F # 9279
    IS_POSITION_65_WITHIN_P_METERS =                    0x2440 # 9280
    IS_POSITION_66_WITHIN_P_METERS =                    0x2441 # 9281
    IS_POSITION_67_WITHIN_P_METERS =                    0x2442 # 9282
    IS_POSITION_68_WITHIN_P_METERS =                    0x2443 # 9283
    IS_POSITION_69_WITHIN_P_METERS =                    0x2444 # 9284
    IS_POSITION_70_WITHIN_P_METERS =                    0x2445 # 9285
    IS_POSITION_71_WITHIN_P_METERS =                    0x2446 # 9286
    IS_POSITION_72_WITHIN_P_METERS =                    0x2447 # 9287
    IS_POSITION_73_WITHIN_P_METERS =                    0x2448 # 9288
    IS_POSITION_74_WITHIN_P_METERS =                    0x2449 # 9289
    IS_POSITION_75_WITHIN_P_METERS =                    0x244A # 9290
    IS_POSITION_76_WITHIN_P_METERS =                    0x244B # 9291
    IS_POSITION_77_WITHIN_P_METERS =                    0x244C # 9292
    IS_POSITION_78_WITHIN_P_METERS =                    0x244D # 9293
    IS_POSITION_79_WITHIN_P_METERS =                    0x244E # 9294
    IS_POSITION_80_WITHIN_P_METERS =                    0x244F # 9295
    IS_POSITION_81_WITHIN_P_METERS =                    0x2450 # 9296
    IS_POSITION_82_WITHIN_P_METERS =                    0x2451 # 9297
    IS_POSITION_83_WITHIN_P_METERS =                    0x2452 # 9298
    IS_POSITION_84_WITHIN_P_METERS =                    0x2453 # 9299
    IS_POSITION_85_WITHIN_P_METERS =                    0x2454 # 9300
    IS_POSITION_86_WITHIN_P_METERS =                    0x2455 # 9301
    IS_POSITION_87_WITHIN_P_METERS =                    0x2456 # 9302
    IS_POSITION_88_WITHIN_P_METERS =                    0x2457 # 9303
    IS_POSITION_89_WITHIN_P_METERS =                    0x2458 # 9304
    IS_POSITION_90_WITHIN_P_METERS =                    0x2459 # 9305
    IS_POSITION_91_WITHIN_P_METERS =                    0x245A # 9306
    IS_POSITION_92_WITHIN_P_METERS =                    0x245B # 9307
    IS_POSITION_93_WITHIN_P_METERS =                    0x245C # 9308
    IS_POSITION_94_WITHIN_P_METERS =                    0x245D # 9309
    IS_POSITION_95_WITHIN_P_METERS =                    0x245E # 9310
    IS_POSITION_96_WITHIN_P_METERS =                    0x245F # 9311
    IS_POSITION_97_WITHIN_P_METERS =                    0x2460 # 9312
    IS_POSITION_98_WITHIN_P_METERS =                    0x2461 # 9313
    IS_POSITION_99_WITHIN_P_METERS =                    0x2462 # 9314
    IS_POSITION_100_WITHIN_P_METERS =                   0x2463 # 9315
    IS_POSITION_101_WITHIN_P_METERS =                   0x2464 # 9316
    IS_POSITION_102_WITHIN_P_METERS =                   0x2465 # 9317
    IS_POSITION_103_WITHIN_P_METERS =                   0x2466 # 9318
    IS_POSITION_104_WITHIN_P_METERS =                   0x2467 # 9319
    IS_POSITION_105_WITHIN_P_METERS =                   0x2468 # 9320
    IS_POSITION_106_WITHIN_P_METERS =                   0x2469 # 9321
    IS_POSITION_107_WITHIN_P_METERS =                   0x246A # 9322
    IS_POSITION_108_WITHIN_P_METERS =                   0x246B # 9323
    IS_POSITION_109_WITHIN_P_METERS =                   0x246C # 9324
    IS_POSITION_110_WITHIN_P_METERS =                   0x246D # 9325
    IS_POSITION_111_WITHIN_P_METERS =                   0x246E # 9326
    IS_POSITION_112_WITHIN_P_METERS =                   0x246F # 9327
    IS_POSITION_113_WITHIN_P_METERS =                   0x2470 # 9328
    IS_POSITION_114_WITHIN_P_METERS =                   0x2471 # 9329
    IS_POSITION_115_WITHIN_P_METERS =                   0x2472 # 9330
    IS_POSITION_116_WITHIN_P_METERS =                   0x2473 # 9331
    IS_POSITION_117_WITHIN_P_METERS =                   0x2474 # 9332
    IS_POSITION_118_WITHIN_P_METERS =                   0x2475 # 9333
    IS_POSITION_119_WITHIN_P_METERS =                   0x2476 # 9334
    IS_POSITION_120_WITHIN_P_METERS =                   0x2477 # 9335
    IS_POSITION_121_WITHIN_P_METERS =                   0x2478 # 9336
    IS_POSITION_122_WITHIN_P_METERS =                   0x2479 # 9337
    IS_POSITION_123_WITHIN_P_METERS =                   0x247A # 9338
    IS_POSITION_124_WITHIN_P_METERS =                   0x247B # 9339
    IS_POSITION_125_WITHIN_P_METERS =                   0x247C # 9340
    IS_POSITION_126_WITHIN_P_METERS =                   0x247D # 9341
    IS_POSITION_127_WITHIN_P_METERS =                   0x247E # 9342
    IS_POSITION_128_WITHIN_P_METERS =                   0x247F # 9343
    IS_POSITION_129_WITHIN_P_METERS =                   0x2480 # 9344
    IS_POSITION_130_WITHIN_P_METERS =                   0x2481 # 9345
    IS_POSITION_131_WITHIN_P_METERS =                   0x2482 # 9346
    IS_POSITION_132_WITHIN_P_METERS =                   0x2483 # 9347
    IS_POSITION_133_WITHIN_P_METERS =                   0x2484 # 9348
    IS_POSITION_134_WITHIN_P_METERS =                   0x2485 # 9349
    IS_POSITION_135_WITHIN_P_METERS =                   0x2486 # 9350
    IS_POSITION_136_WITHIN_P_METERS =                   0x2487 # 9351
    IS_POSITION_137_WITHIN_P_METERS =                   0x2488 # 9352
    IS_POSITION_138_WITHIN_P_METERS =                   0x2489 # 9353
    IS_POSITION_139_WITHIN_P_METERS =                   0x248A # 9354
    IS_POSITION_140_WITHIN_P_METERS =                   0x248B # 9355
    IS_POSITION_141_WITHIN_P_METERS =                   0x248C # 9356
    IS_POSITION_142_WITHIN_P_METERS =                   0x248D # 9357
    IS_POSITION_143_WITHIN_P_METERS =                   0x248E # 9358
    IS_POSITION_144_WITHIN_P_METERS =                   0x248F # 9359
    IS_POSITION_145_WITHIN_P_METERS =                   0x2490 # 9360
    IS_POSITION_146_WITHIN_P_METERS =                   0x2491 # 9361
    IS_POSITION_147_WITHIN_P_METERS =                   0x2492 # 9362
    IS_POSITION_148_WITHIN_P_METERS =                   0x2493 # 9363
    IS_POSITION_149_WITHIN_P_METERS =                   0x2494 # 9364
    IS_POSITION_150_WITHIN_P_METERS =                   0x2495 # 9365
    IS_POSITION_151_WITHIN_P_METERS =                   0x2496 # 9366
    IS_POSITION_152_WITHIN_P_METERS =                   0x2497 # 9367
    IS_POSITION_153_WITHIN_P_METERS =                   0x2498 # 9368
    IS_POSITION_154_WITHIN_P_METERS =                   0x2499 # 9369
    IS_POSITION_155_WITHIN_P_METERS =                   0x249A # 9370
    IS_POSITION_156_WITHIN_P_METERS =                   0x249B # 9371
    IS_POSITION_157_WITHIN_P_METERS =                   0x249C # 9372
    IS_POSITION_158_WITHIN_P_METERS =                   0x249D # 9373
    IS_POSITION_159_WITHIN_P_METERS =                   0x249E # 9374
    IS_POSITION_160_WITHIN_P_METERS =                   0x249F # 9375
    IS_POSITION_161_WITHIN_P_METERS =                   0x24A0 # 9376
    IS_POSITION_162_WITHIN_P_METERS =                   0x24A1 # 9377
    IS_POSITION_163_WITHIN_P_METERS =                   0x24A2 # 9378
    IS_POSITION_164_WITHIN_P_METERS =                   0x24A3 # 9379
    IS_POSITION_165_WITHIN_P_METERS =                   0x24A4 # 9380
    IS_POSITION_166_WITHIN_P_METERS =                   0x24A5 # 9381
    IS_POSITION_167_WITHIN_P_METERS =                   0x24A6 # 9382
    IS_POSITION_168_WITHIN_P_METERS =                   0x24A7 # 9383
    IS_POSITION_169_WITHIN_P_METERS =                   0x24A8 # 9384
    IS_POSITION_170_WITHIN_P_METERS =                   0x24A9 # 9385
    IS_POSITION_171_WITHIN_P_METERS =                   0x24AA # 9386
    IS_POSITION_172_WITHIN_P_METERS =                   0x24AB # 9387
    IS_POSITION_173_WITHIN_P_METERS =                   0x24AC # 9388
    IS_POSITION_174_WITHIN_P_METERS =                   0x24AD # 9389
    IS_POSITION_175_WITHIN_P_METERS =                   0x24AE # 9390
    IS_POSITION_176_WITHIN_P_METERS =                   0x24AF # 9391
    IS_POSITION_177_WITHIN_P_METERS =                   0x24B0 # 9392
    IS_POSITION_178_WITHIN_P_METERS =                   0x24B1 # 9393
    IS_POSITION_179_WITHIN_P_METERS =                   0x24B2 # 9394
    IS_POSITION_180_WITHIN_P_METERS =                   0x24B3 # 9395
    IS_POSITION_181_WITHIN_P_METERS =                   0x24B4 # 9396
    IS_POSITION_182_WITHIN_P_METERS =                   0x24B5 # 9397
    IS_POSITION_183_WITHIN_P_METERS =                   0x24B6 # 9398
    IS_POSITION_184_WITHIN_P_METERS =                   0x24B7 # 9399
    IS_POSITION_185_WITHIN_P_METERS =                   0x24B8 # 9400
    IS_POSITION_186_WITHIN_P_METERS =                   0x24B9 # 9401
    IS_POSITION_187_WITHIN_P_METERS =                   0x24BA # 9402
    IS_POSITION_188_WITHIN_P_METERS =                   0x24BB # 9403
    IS_POSITION_189_WITHIN_P_METERS =                   0x24BC # 9404
    IS_POSITION_190_WITHIN_P_METERS =                   0x24BD # 9405
    IS_POSITION_191_WITHIN_P_METERS =                   0x24BE # 9406
    IS_POSITION_192_WITHIN_P_METERS =                   0x24BF # 9407
    IS_POSITION_193_WITHIN_P_METERS =                   0x24C0 # 9408
    IS_POSITION_194_WITHIN_P_METERS =                   0x24C1 # 9409
    IS_POSITION_195_WITHIN_P_METERS =                   0x24C2 # 9410
    IS_POSITION_196_WITHIN_P_METERS =                   0x24C3 # 9411
    IS_POSITION_197_WITHIN_P_METERS =                   0x24C4 # 9412
    IS_POSITION_198_WITHIN_P_METERS =                   0x24C5 # 9413
    IS_POSITION_199_WITHIN_P_METERS =                   0x24C6 # 9414
    IS_POSITION_200_WITHIN_P_METERS =                   0x24C7 # 9415
    IS_POSITION_201_WITHIN_P_METERS =                   0x24C8 # 9416
    IS_POSITION_202_WITHIN_P_METERS =                   0x24C9 # 9417
    IS_POSITION_203_WITHIN_P_METERS =                   0x24CA # 9418
    IS_POSITION_204_WITHIN_P_METERS =                   0x24CB # 9419
    IS_POSITION_205_WITHIN_P_METERS =                   0x24CC # 9420
    IS_POSITION_206_WITHIN_P_METERS =                   0x24CD # 9421
    IS_POSITION_207_WITHIN_P_METERS =                   0x24CE # 9422
    IS_POSITION_208_WITHIN_P_METERS =                   0x24CF # 9423
    IS_POSITION_209_WITHIN_P_METERS =                   0x24D0 # 9424
    IS_POSITION_210_WITHIN_P_METERS =                   0x24D1 # 9425
    IS_POSITION_211_WITHIN_P_METERS =                   0x24D2 # 9426
    IS_POSITION_212_WITHIN_P_METERS =                   0x24D3 # 9427
    IS_POSITION_213_WITHIN_P_METERS =                   0x24D4 # 9428
    IS_POSITION_214_WITHIN_P_METERS =                   0x24D5 # 9429
    IS_POSITION_215_WITHIN_P_METERS =                   0x24D6 # 9430
    IS_POSITION_216_WITHIN_P_METERS =                   0x24D7 # 9431
    IS_POSITION_217_WITHIN_P_METERS =                   0x24D8 # 9432
    IS_POSITION_218_WITHIN_P_METERS =                   0x24D9 # 9433
    IS_POSITION_219_WITHIN_P_METERS =                   0x24DA # 9434
    IS_POSITION_220_WITHIN_P_METERS =                   0x24DB # 9435
    IS_POSITION_221_WITHIN_P_METERS =                   0x24DC # 9436
    IS_POSITION_222_WITHIN_P_METERS =                   0x24DD # 9437
    IS_POSITION_223_WITHIN_P_METERS =                   0x24DE # 9438
    IS_POSITION_224_WITHIN_P_METERS =                   0x24DF # 9439
    IS_POSITION_225_WITHIN_P_METERS =                   0x24E0 # 9440
    IS_POSITION_226_WITHIN_P_METERS =                   0x24E1 # 9441
    IS_POSITION_227_WITHIN_P_METERS =                   0x24E2 # 9442
    IS_POSITION_228_WITHIN_P_METERS =                   0x24E3 # 9443
    IS_POSITION_229_WITHIN_P_METERS =                   0x24E4 # 9444
    IS_POSITION_230_WITHIN_P_METERS =                   0x24E5 # 9445
    IS_POSITION_231_WITHIN_P_METERS =                   0x24E6 # 9446
    IS_POSITION_232_WITHIN_P_METERS =                   0x24E7 # 9447
    IS_POSITION_233_WITHIN_P_METERS =                   0x24E8 # 9448
    IS_POSITION_234_WITHIN_P_METERS =                   0x24E9 # 9449
    IS_POSITION_235_WITHIN_P_METERS =                   0x24EA # 9450
    IS_POSITION_236_WITHIN_P_METERS =                   0x24EB # 9451
    IS_POSITION_237_WITHIN_P_METERS =                   0x24EC # 9452
    IS_POSITION_238_WITHIN_P_METERS =                   0x24ED # 9453
    IS_POSITION_239_WITHIN_P_METERS =                   0x24EE # 9454
    IS_POSITION_240_WITHIN_P_METERS =                   0x24EF # 9455
    IS_POSITION_241_WITHIN_P_METERS =                   0x24F0 # 9456
    IS_POSITION_242_WITHIN_P_METERS =                   0x24F1 # 9457
    IS_POSITION_243_WITHIN_P_METERS =                   0x24F2 # 9458
    IS_POSITION_244_WITHIN_P_METERS =                   0x24F3 # 9459
    IS_POSITION_245_WITHIN_P_METERS =                   0x24F4 # 9460
    IS_POSITION_246_WITHIN_P_METERS =                   0x24F5 # 9461
    IS_POSITION_247_WITHIN_P_METERS =                   0x24F6 # 9462
    IS_POSITION_248_WITHIN_P_METERS =                   0x24F7 # 9463
    IS_POSITION_249_WITHIN_P_METERS =                   0x24F8 # 9464
    IS_POSITION_250_WITHIN_P_METERS =                   0x24F9 # 9465
    IS_POSITION_251_WITHIN_P_METERS =                   0x24FA # 9466
    IS_POSITION_252_WITHIN_P_METERS =                   0x24FB # 9467
    IS_POSITION_253_WITHIN_P_METERS =                   0x24FC # 9468
    IS_POSITION_254_WITHIN_P_METERS =                   0x24FD # 9469
    IS_POSITION_255_WITHIN_P_METERS =                   0x24FE # 9470
    IS_POSITION_256_WITHIN_P_METERS =                   0x24FF # 9471

    IS_VAAN_WITHIN_P_METERS =                           0x2600 # 9728
    IS_ASHE_WITHIN_P_METERS =                           0x2601 # 9729
    IS_FRAN_WITHIN_P_METERS =                           0x2602 # 9730
    IS_BALTHIER_WITHIN_P_METERS =                       0x2603 # 9731
    IS_BASCH_WITHIN_P_METERS =                          0x2604 # 9732
    IS_PENELO_WITHIN_P_METERS =                         0x2605 # 9733
    IS_REKS_WITHI_P_METERS =                            0x2606 # 9734
    IS_AMALIA_WITHIN_P_METERS =                         0x2607 # 9735
    IS_BASCH_PRISONER_WITHIN_P_METERS =                 0x2608 # 9736
    IS_BASCH_DARK_SUIT_WITHIN_P_METERS =                0x2609 # 9737
    IS_LAMONT_WITHIN_P_METERS =                         0x260A # 9738
    IS_VOSSLER_IMPERIAL_WITHIN_P_METERS =               0x260B # 9739
    IS_VOSSLER_RESISTANCE_WITHIN_P_METERS =             0x260C # 9740
    IS_LARSA_WITHIN_P_METERS =                          0x260D # 9741
    IS_REDDAS_WITHIN_P_METERS =                         0x260E # 9742

    # IS_RESERVE_0X0F_WITHIN_P_METERS =                   0x260F # 9743
    # IS_RESERVE_0X10_WITHIN_P_METERS =                   0x2610 # 9744
    # IS_RESERVE_0X11_WITHIN_P_METERS =                   0x2611 # 9745
    # IS_RESERVE_0X12_WITHIN_P_METERS =                   0x2612 # 9746
    # IS_RESERVE_0X13_WITHIN_P_METERS =                   0x2613 # 9747
    # IS_RESERVE_0X14_WITHIN_P_METERS =                   0x2614 # 9748
    # IS_RESERVE_0X15_WITHIN_P_METERS =                   0x2615 # 9749
    # IS_RESERVE_0X16_WITHIN_P_METERS =                   0x2616 # 9750
    # IS_RESERVE_0X17_WITHIN_P_METERS =                   0x2617 # 9751
    # IS_RESERVE_0X18_WITHIN_P_METERS =                   0x2618 # 9752
    # IS_RESERVE_0X19_WITHIN_P_METERS =                   0x2619 # 9753

    IS_CHOCOBO_WITHIN_P_METERS =                        0x261A # 9754
    IS_BELIAS_WITHIN_P_METERS =                         0x261B # 9755
    IS_MATEUS_WITHIN_P_METERS =                         0x261C # 9756
    IS_ANDRAMMELECH_WITHIN_P_METERS =                   0x261D # 9757
    IS_HASHMAL_WITHIN_P_METERS =                        0x261E # 9758
    IS_CUCHULAINN_WITHIN_P_METERS =                     0x261F # 9759
    IS_FAMFRIT_WITHIN_P_METERS =                        0x2620 # 9760
    IS_ZALERA_WITHIN_P_METERS =                         0x2621 # 9761
    IS_SHEMHAZAI_WITHIN_P_METERS =                      0x2622 # 9762
    IS_CHAOS_WITHIN_P_METERS =                          0x2623 # 9763
    IS_ZEROMUS_WITHIN_P_METERS =                        0x2624 # 9764
    IS_EXODUS_WITHIN_P_METERS =                         0x2625 # 9765
    IS_ULTIMA_WITHIN_P_METERS =                         0x2626 # 9766
    IS_ZODIARK_WITHIN_P_METERS =                        0x2627 # 9767