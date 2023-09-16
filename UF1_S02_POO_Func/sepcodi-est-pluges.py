# Our imports
# from folderName import className
from BioModules import StatisticsList

# Main
# -----------------------------------------------------------------------------
if __name__ == "__main__":
    
    # Construim 2 llistes diferents i apliquem els mateixos mètodes.

    llistaPluges21 = [16.5, 0.0, 32.7, 6.5, 24.6, 15.7, 2.6, 0.0, 94.2, 65.5, 25.5, 9.2]
    stats_raining = StatisticsList(llistaPluges21)
    print(stats_raining)
    print(f'Sumatori precipitacions de l''any =',stats_raining.sumatori(),'L.')
