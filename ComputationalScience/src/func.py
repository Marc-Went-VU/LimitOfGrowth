from math import floor

def drange(start, stop, step):
    r = start
    while r < stop:
        yield r
        r += step
def get_unprecise_index(table, index):
    return table[index] if index in table else table[min(table.keys(), key=lambda k: abs(k-index))]

def get_table_value(table, lower_value, upper_value, step_size, inp):
    if inp < lower_value:
        inp = lower_value
    elif inp > upper_value:
        inp = upper_value
        
    index = floor(inp/step_size)*step_size; #rounding is done by floor(inp*(1/step_size))/(1/step_size). For example step_size 0.1 requires rounding to one digit
    
    
    if index == inp:
        return table[index]
    else:
        frac = inp - index
        return (1 - frac) * get_unprecise_index(table, index) + frac * get_unprecise_index(table, index+step_size)

def f4(inp): #mortality0To14
    table = {20: 0.0567,
            30: 0.0366,
            40: 0.0243,
            50: 0.0155,
            60: 0.0082,
            70: 0.0023,
            80: 0.0010,
            }
    
    return get_table_value(table, 20, 80, 10, inp)

def f8(inp): #mortality15To44
    table = {20: 0.0266,
            30: 0.0171,
            40: 0.0110,
            50: 0.0065,
            60: 0.0040,
            70: 0.0016,
            80: 0.0008,
            }
    
    return get_table_value(table, 20, 80, 10, inp)

def f12(inp): #mortality45To64
    table = {20: 0.0562,
            30: 0.0373,
            40: 0.0252,
            50: 0.0171,
            60: 0.0118,
            70: 0.0083,
            80: 0.0060,
            }
    
    return get_table_value(table, 20, 80, 10, inp)

def f16(inp): #mortality65AndOver
    table = {20: 0.13,
            30: 0.11,
            40: 0.09,
            50: 0.07,
            60: 0.06,
            70: 0.05,
            80: 0.04,
            }
    
    return get_table_value(table, 20, 80, 10, inp)

def f20(inp): #lifetimeMultiplierFromFood
    table = {0: 0,
            1: 1,
            2: 1.2,
            3: 1.3,
            4: 1.35,
            5: 1.4,
            }
    
    return get_table_value(table, 0, 5, 1, inp)

def f21(inp): #healthServicesAllocationsPerCapita
    table = {0: 0,
            250: 20,
            500: 50,
            750: 95,
            1000: 140,
            1250: 175,
            1500: 200,
            1750: 220,
            2000: 230,
            }
    
    return get_table_value(table, 0, 2000, 250, inp)

def f24(inp): #lifetimeMultiplierFromHealthServicesBefore
    table = {0: 1,
            20: 1.1,
            40: 1.4,
            60: 1.6,
            80: 1.7,
            100: 1.8,
            }
    
    return get_table_value(table, 0, 100, 20, inp)

def f25(inp): #lifetimeMultiplierFromHealthServicesAfter
    table = {0: 1,
            20: 1.4,
            40: 1.6,
            60: 1.8,
            80: 1.95,
            100: 2.0,
            }
    
    return get_table_value(table, 0, 100, 20, inp)

def f26(inp): #fractionOfPopulationUrban
    table = {0: 0,
            2000000000: 0.2,
            4000000000: 0.4,
            6000000000: 0.5,
            8000000000: 0.58,
            10000000000: 0.65,
            12000000000: 0.72,
            14000000000: 0.78,
            16000000000: 0.80,
            }
    
    return get_table_value(table, 0, 16000000000, 2000000000, inp)

def f27(inp): #crowdingMultiplierFromIndustrialization
    table = {0: 0.5,
            200: 0.05,
            400: -0.1,
            600: -0.08,
            800: -0.02,
            1000: 0.05,
            1200: 0.1,
            1400: 0.15,
            1600: 0.2,
            }
    
    return get_table_value(table, 0, 1600, 200, inp)

def f29(inp): #lifetimeMultiplierFromPollution
    table = {0: 1.0,
            10: 0.99,
            20: 0.97,
            30: 0.95,
            40: 0.90,
            50: 0.85,
            60: 0.75,
            70: 0.65,
            80: 0.55,
            90: 0.40,
            100: 0.20,
            }
    
    return get_table_value(table, 0, 100, 10, inp)

def f34(inp): #fecundityMultiplier
    table = {0: 0.0,
            10: 0.2,
            20: 0.4,
            30: 0.6,
            40: 0.8,
            50: 0.9,
            60: 1.0,
            70: 1.05,
            80: 1.1,
            }
    
    return get_table_value(table, 0, 80, 10, inp)

def f36(inp): #compensatoryMultiplierFromPerceivedLifeExpectancy
    table = {0: 3.0,
            10: 2.1,
            20: 1.6,
            30: 1.4,
            40: 1.3,
            50: 1.2,
            60: 1.1,
            70: 1.05,
            80: 1.0,
            }
    
    return get_table_value(table, 0, 80, 10, inp)

def f39(inp): #socialFamilySizeNorm
    table = {0: 1.25,
            200: 1,
            400: 0.9,
            600: 0.8,
            800: 0.75,
            }
    
    return get_table_value(table, 0, 800, 200, inp)

def f41(inp): #familyResponseToSocialNorm
    table = {-0.2: 0.5,
            -0.1: 0.6,
            0: 0.7,
            0.1: 0.85,
            0.2: 1.0,
            }
    
    return get_table_value(table, -0.2, 0.2, 0.1, inp)

def f45(inp): #fertilityControlEffectiveness
    table = {0: 0.75,
            0.5: 0.85,
            1: 0.90,
            1.5: 0.95,
            2: 0.98,
            2.5: 0.99,
            3: 1.0,
            }
    
    return get_table_value(table, 0, 3, 0.5, inp)

def f48(inp): #fractionOfServicesAllocatedToFertilityControl
    table = {0: 0.0,
            2: 0.005,
            4: 0.015,
            6: 0.025,
            8: 0.030,
            10: 0.035,
            }
    
    return get_table_value(table, 0, 10, 2, inp)

def f59(inp): #fractionOfIndustrialOutputAllocatedToConsumptionVariable
    table = {0: 0.3,
            0.2: 0.32,
            0.4: 0.34,
            0.6: 0.36,
            0.8: 0.38,
            1: 0.43,
            1.2: 0.73,
            1.4: 0.77,
            1.6: 0.81,
            1.8: 0.82,
            2: 0.83,
            }
    
    return get_table_value(table, 0, 2, 0.2, inp)

def f61(inp): #indicatedServiceOutputPerCapitaBefore
    table = {0: 40,
            200: 300,
            400: 640,
            600: 1000,
            800: 1220,
            1000: 1450,
            1200: 1650,
            1400: 1800,
            1600: 2000,
            }
    
    return get_table_value(table, 0, 1600, 200, inp)

def f62(inp): #indicatedServiceOutputPerCapitaAfter
    table = {0: 40,
            200: 300,
            400: 640,
            600: 1000,
            800: 1220,
            1000: 1450,
            1200: 1650,
            1400: 1800,
            1600: 2000,
            }
    
    return get_table_value(table, 0, 1600, 200, inp)

def f64(inp): #fractionOfIndustrialOutputAllocatedToServicesBefore
    table = {0: 0.3,
            0.5: 0.2,
            1: 0.1,
            1.5: 0.05,
            2: 0,
            }
    
    return get_table_value(table, 0, 2, 0.5, inp)

def f65(inp): #fractionOfIndustrialOutputAllocatedToServicesAfter
    table = {0: 0.3,
            0.5: 0.2,
            1: 0.1,
            1.5: 0.05,
            2: 0,
            }
    
    return get_table_value(table, 0, 2, 0.5, inp)

def f75(inp): #jobsPerIndustrialCapitalUnit
    table = {50: 0.00037,
            200: 0.00018,
            350: 0.00012,
            500: 0.00009,
            650: 0.00007,
            800: 0.00006,
            }
    
    return get_table_value(table, 50, 800, 150, inp)

def f77(inp): #jobsPerServiceCapitalUnit
    table = {50: .0011,
            200: 0.0006,
            350: 0.00035,
            500: 0.0002,
            650: 0.00015,
            800: 0.00015,
            }
    
    return get_table_value(table, 50, 800, 150, inp)

def f79(inp): #jobsPerHectare
    table = {2: 2,
            6: 0.5,
            10: 0.4,
            14: 0.3,
            18: 0.27,
            22: 0.24,
            26: 0.2,
            30: 0.2,
            }
    
    return get_table_value(table, 2, 30, 4, inp)

def f83(inp): #capitalUtilizationFraction
    table = {1: 1.0,
            3: 0.9,
            5: 0.7,
            7: 0.3,
            9: 0.1,
            11: 0.1,
            }
    
    return get_table_value(table, 1, 11, 2, inp)

def f90(inp): #indicatedFoodPerCapitaBefore
    table = {0: 230,
            200: 480,
            400: 690,
            600: 850,
            800: 970,
            1000: 1070,
            1200: 1150,
            1400: 1210,
            1600: 1250,
            }
    
    return get_table_value(table, 0, 1600, 200, inp)

def f91(inp): #indicatedFoodPerCapitaAfter
    table = {0: 230,
            200: 480,
            400: 690,
            600: 850,
            800: 970,
            1000: 1070,
            1200: 1150,
            1400: 1210,
            1600: 1250,
            }
    
    return get_table_value(table, 0, 1600, 200, inp)

def f94(inp): #fractionOfIndustrialOutputAllocatedToAgricultureBefore
    table = {0: 0.4,
            0.5: 0.2,
            1: 0.1,
            1.5: 0.025,
            2: 0,
            2.5: 0,
            }
    
    return get_table_value(table, 0, 2.5, 0.5, inp)

def f95(inp): #fractionOfIndustrialOutputAllocatedToAgricultureAfter
    table = {0: 0.4,
            0.5: 0.2,
            1: 0.1,
            1.5: 0.025,
            2: 0,
            2.5: 0,
            }
    
    return get_table_value(table, 0, 2.5, 0.5, inp)

def f97(inp): #developmentCostPerHectare
    table = {0: 100000,
            0.1: 7400,
            0.2: 5200,
            0.3: 3500,
            0.4: 2400,
            0.5: 1500,
            0.6: 750,
            0.7: 300,
            0.8: 150,
            0.9: 75,
            1: 50,
            }
    
    return get_table_value(table, 0, 1, 0.1, inp)

def f102(inp): #landYieldMultiplierFromCapital
    table = {0: 1,
            40: 3,
            80: 3.8,
            120: 4.4,
            160: 4.9,
            200: 5.4,
            240: 5.7,
            280: 6,
            320: 6.3,
            360: 6.6,
            400: 6.9,
            440: 7.2,
            480: 7.4,
            520: 7.6,
            560: 7.8,
            600: 8,
            640: 8.2,
            680: 8.4,
            720: 8.6,
            760: 8.8,
            800: 9,
            840: 9.2,
            880: 9.4,
            920: 9.6,
            960: 9.8,
            1000: 10,
            }
    
    return get_table_value(table, 0, 1000, 40, inp)

def f106(inp): #landYieldMultiplierFromAirPollutionBefore
    table = {0: 1,
            10: 1,
            20: 0.7,
            30: 0.4,
            }
    
    return get_table_value(table, 0, 30, 10, inp)

def f107(inp): #landYieldMultiplierFromAirPollutionAfter
    table = {0: 1,
            10: 1,
            20: 0.7,
            30: 0.4,
            }
    
    return get_table_value(table, 0, 30, 10, inp)

def f108(inp): #fractionOfInputsAllocatedToLandDevelopment
    table = {0: 0,
            0.25: 0.05,
            0.5: 0.15,
            0.75: 0.30,
            1: 0.50,
            1.25: 0.70,
            1.5: 0.85,
            1.75: 0.95,
            2: 1,
            }
    
    return get_table_value(table, 0, 2, 0.25, inp)

def f111(inp): #marginalLandYieldMultiplierFromCapital
    table = {0: 0.075,
            40: 0.03,
            80: 0.015,
            120: 0.011,
            160: 0.009,
            200: 0.008,
            240: 0.007,
            280: 0.006,
            320: 0.005,
            360: 0.005,
            400: 0.005,
            440: 0.005,
            480: 0.005,
            520: 0.005,
            560: 0.005,
            600: 0.005,
            }
    
    return get_table_value(table, 0, 600, 40, inp)

def f114(inp): #landLifeMultiplierFromYieldBefore
    table = {0: 1.2,
            1: 1,
            2: 0.63,
            3: 0.36,
            4: 0.16,
            5: 0.055,
            6: 0.04,
            7: 0.025,
            8: 0.015,
            9: 0.01,
            }
    
    return get_table_value(table, 0, 9, 1, inp)

def f115(inp): #landLifeMultiplierFromYieldAfter
    table = {0: 1.2,
            1: 1,
            2: 0.63,
            3: 0.36,
            4: 0.16,
            5: 0.055,
            6: 0.04,
            7: 0.025,
            8: 0.015,
            9: 0.01,
            }
    
    return get_table_value(table, 0, 9, 1, inp)

def f117(inp): #urbanIndustrialLandPerCapita
    table = {0: 0.005,
            200: 0.008,
            400: 0.15,
            600: 0.025,
            800: 0.04,
            1000: 0.055,
            1200: 0.07,
            1400: 0.08,
            1600: 0.09,
            }
    
    return get_table_value(table, 0, 1600, 200, inp)

def f122(inp): #landFertilityDegradationRate
    table = {0: 0,
            10: 0.1,
            20: 0.3,
            30: 0.5,
            }
    
    return get_table_value(table, 0, 30, 10, inp)

def f125(inp): #landFertilityRegenerationTime
    table = {0: 20,
            0.02: 13,
            0.04: 8,
            0.06: 4,
            0.08: 2,
            0.1: 2,
            }
    
    return get_table_value(table, 0, 0.1, 0.02, inp)

def f126(inp): #fractionOfInputsAllocatedToLandMaintenance
    table = {0: 0,
            1: 0.04,
            2: 0.07,
            3: 0.09,
            4: 0.10,
            }
    
    return get_table_value(table, 0, 4, 1, inp)

def f132(inp): #perCapitaResourceUsageMultiplier
    table = {0: 0,
            200: 0.85,
            400: 2.6,
            600: 4.4,
            800: 5.4,
            1000: 6.2,
            1200: 6.8,
            1400: 7,
            1600: 7,
            }
    
    return get_table_value(table, 0, 1600, 200, inp)

def f135(inp): #fractionOfCapitalAllocatedToObtainingResourcesBefore
    table = {0: 1,
            0.1: 0.9,
            0.2: 0.7,
            0.3: 0.5,
            0.4: 0.2,
            0.5: 0.1,
            0.6: 0.05,
            0.7: 0.05,
            0.8: 0.05,
            0.9: 0.05,
            1: 0.05,
            }
    
    return get_table_value(table, 0, 1, 0.1, inp)

def f136(inp): #fractionOfCapitalAllocatedToObtainingResourcesAfter
    table = {0: 1,
            0.1: 0.9,
            0.2: 0.7,
            0.3: 0.5,
            0.4: 0.2,
            0.5: 0.1,
            0.6: 0.05,
            0.7: 0.05,
            0.8: 0.05,
            0.9: 0.05,
            1: 0.05,
            }
    
    return get_table_value(table, 0, 1, 0.1, inp)

def f145(inp): #assimilationHalfLifeMultiplier
    table = {1: 1,
            251: 11,
            501: 21,
            751: 31,
            1001: 41,
            }
    
    return get_table_value(table, 1, 1001, 250, inp)