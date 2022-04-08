import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

def main():
    coredata_df = pd.read_csv('data/CoreData.csv', sep=';')
    mentalhealth_df = pd.read_csv('data/MentalHealth.csv', sep=';')

    joined_df = pd.merge(coredata_df, mentalhealth_df, on='Participant.ID', how='left')

    return


if __name__ == '__main__':
    main()
