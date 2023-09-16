# from folderName import className
from BioModules import StatisticsList

# Main
# -----------------------------------------------------------------------------
if __name__ == "__main__":
    
    # Construim 2 llistes diferents i apliquem els mateixos mètodes.

    llistaNotes22 = [5, 10, 8, 1, 7, 3, 6, 8, 9, 10]
    stats_marks = StatisticsList(llistaNotes22)
    print(stats_marks)
    print(f'Sumatori notes =',stats_marks.sumatori())