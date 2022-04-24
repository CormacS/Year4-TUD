#Cormac Smith C17723185

import pandas as pd
import csv

#Reading in CSV file
df = pd.read_csv("./data/dataset.csv", header=None, na_values = '?', sep="\s*,\s*", engine="python")

headings = []

#Reading feature names from file
with open("./data/feature_names.txt", 'r') as fo:
    for line in fo:
        if line !='\n':
            headings.append(line.strip())
df.columns = headings

#Deciding which features are continuous and categiorical
continuous = ['age', 'fnlwgt', 'education-num', 'capital-gain', 'capital-loss', 'hours-per-week']
categorical = ['workclass', 'education', 'marital-status', 'occupation', 'relationship', 'race', 'sex',
               'native-country', 'target']

#The structure for each of the tables
continuousStructure = ['Feature Name','Count','% Miss','Card','Min','1st Qrt','Mean','Median','3rd Qrt','Max','Std Dev']
categoricalStructure = ['Feature Name','Count','% Miss','Card','Mode','Mode Freq','Mode %','2nd Mode','2nd Mode Freq','2nd Mode %']


#Getting the data for the continuous dataset

#Making a dictionary with the keys of the continous table
conDict = dict.fromkeys(continuousStructure)
conDict['Feature Name'] = continuous

conDict['Count'] = df[continuous].count()

#Getting total that are missing and then divide and multply by 100 to get percent
conDict['% Miss'] = df[continuous].isna().sum() / len(df[continuous])*100

conDict['Card'] = df[continuous].nunique()

conDict['Min'] = df[continuous].min()

conDict['1st Qrt'] = df[continuous].quantile(0.25)

conDict['Mean'] = df[continuous].mean()

conDict['Median'] = df[continuous].median()

conDict['3rd Qrt'] = df[continuous].quantile(0.75)

conDict['Max'] = df[continuous].max()

conDict['Std Dev'] = df[continuous].std()

#Turning dictionary into dataframe and converting to csv
d1 = pd.DataFrame(conDict)
d1.to_csv('./data/C17723185CONT.csv', index=False)

#Getting the data for the categorical dataset

#Making a dictionary with the keys of the continous table
catDict = dict.fromkeys(categoricalStructure)
catDict['Feature Name'] = categorical

#Count wasn't including missing values so had to add them after
catDict['Count'] = df[categorical].count() + df[categorical].isna().sum()

catDict['% Miss'] = df[categorical].isna().sum() / len(df[categorical])*100

catDict['Card'] = df[categorical].nunique()

catDict['Mode'] = df[categorical].value_counts().index[0]

#Need forloop to prevent getting the name rather than the value
modeFreq = []
for cat in categorical:
    modeFreq.append(df[cat].value_counts()[0])
catDict['Mode Freq'] = modeFreq

#Was getting an issue where it was printing the feature aswell so need to use an array to select the number instead
modeFreqPercent = []
total = df[categorical].count() + df[categorical].isna().sum()
for cat in categorical:
    modeFreqPercent.append(df[cat].value_counts()[0] / total[0] *100)
catDict['Mode %'] = modeFreqPercent

secondMode = []
for cat in categorical:
    secondMode.append(df[cat].value_counts().index[1])
catDict['2nd Mode'] = secondMode

#Same reasoning as with mode frequency
secondModeFreq = []
for cat in categorical:
    secondModeFreq.append(df[cat].value_counts()[1])

catDict['2nd Mode Freq'] = secondModeFreq
secondModeFreqPercent = []

#Same reasoning for the for loop as mode frequency percentage
total = df[categorical].count() + df[categorical].isna().sum()
for cat in categorical:
    secondModeFreqPercent.append(df[cat].value_counts()[1] / total[0] *100)
catDict['2nd Mode %'] = secondModeFreqPercent

#Turning dictionary into dataframe and converting to csv
d2 = pd.DataFrame(catDict)
d2.to_csv('./data/C17723185CAT.csv', index=False)