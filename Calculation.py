
glandType = "Piston"
MaxPistonGrooveOrRodDiameter = 4.653
MaxRingCrossSection = 0.1390
MaxRingInnerDiameter = 4.6090

def ReducedSealCrossSectionMax(glandType, MaxPistonGrooveOrRodDiameter, MaxRingCrossSection, MaxRingInnerDiameter):
    #   Piston
    if glandType == "Piston":
        if MaxRingInnerDiameter / MaxRingCrossSection > 2.95:
            X = (MaxPistonGrooveOrRodDiameter - MaxRingInnerDiameter) / (MaxRingInnerDiameter)
    
            if X <= 0:
                ReductionFactor = 0
            elif X > 0 & bool(X <= 0.03):
                ReductionFactor = 0.001 + 1.06 * X - 10 * X ** 2
            else:
                ReductionFactor = 0.0056 + 0.59 * X - 0.46 * X ** 2

            return MaxRingCrossSection - (MaxRingCrossSection * ReductionFactor)
       
        if MaxRingInnerDiameter / MaxRingCrossSection <= 2.95:
            X = (MaxPistonGrooveOrRodDiameter - MaxRingInnerDiameter) / (MaxRingInnerDiameter)
    
            if X <= 0:
                ReductionFactor = 0
            else:
                ReductionFactor = 100 * X / (315 * 2.718 ** (-MaxRingInnerDiameter / MaxRingCrossSection) + 165 + 100 * X)

            return MaxRingCrossSection - (MaxRingCrossSection * ReductionFactor)
    #   Bore

def ReducedSealCrossSectionMin(glandType, PistonGrooveOrRodDiameter, MinRingCrossSection, MinRingInnerDiameter):
    if glandType == "Piston":
        if MinRingInnerDiameter / MinRingCrossSection > 2.95:
            X = (PistonGrooveOrRodDiameter - MinRingInnerDiameter) / (MinRingInnerDiameter)
    
            if X <= 0:
                ReductionFactor = 0
            elif X > 0 & X <= 0.03:
                ReductionFactor = 0.001 + 1.06 * X - 10 * X ^ 2
            else:
                ReductionFactor = 0.0056 + 0.59 * X - 0.46 * X ^ 2

            return MinRingCrossSection - (MinRingCrossSection * ReductionFactor)

        if MinRingInnerDiameter / MinRingCrossSection <= 2.95:
            X = (PistonGrooveOrRodDiameter - MinRingInnerDiameter) / (MinRingInnerDiameter)
    
            if X <= 0:
                ReductionFactor = 0
            else:
                ReductionFactor = 100 * X / (315 * 2.718 ** (-MinRingInnerDiameter / MinRingCrossSection) + 165 + 100 * X)

            return MinRingCrossSection - (MinRingCrossSection * ReductionFactor)


if __name__ == '__main__':
    #   Ambient Temperature(75°F)
    #   Get dimension : Concentricity & eccentricity & BID_max & GOD_min & POD_min

    #   Gland Depth

    #   Ring Compression Absolute

    #   Reduced Cross Section

    #   Squeeze formulation

    #   output
    print("Reduced Seal Cross Section Nominal = " + str(ReducedSealCrossSectionMax("Piston", 4.653, 0.1390, 4.6090)))