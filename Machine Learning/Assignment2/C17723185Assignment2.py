import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_score
from sklearn.naive_bayes import GaussianNB

#Read in both files
df = pd.read_csv("trainingset.txt", header=None)
df2 = pd.read_csv("queries.txt", header=None)

#create columns for the data frame and add them.
columns = ['ID', 'Age', 'Job', 'Marital', 'Education', 'Default', 'Balance', 'Housing', 'Loan', 'Contact','Day','Month','Duration','Campaign','Pdays','Previous','Poutcome','Target']
df.columns = columns
df2.columns = columns

#Changing both the training and testing data at the same time.

#Replace all yes and no columns with 1 or 0
df.Housing.replace(('yes', 'no'), (1, 0), inplace=True)
df.Default.replace(('yes', 'no'), (1, 0), inplace=True)
df.Loan.replace(('yes', 'no'), (1, 0), inplace=True)
df2.Housing.replace(('yes', 'no'), (1, 0), inplace=True)
df2.Default.replace(('yes', 'no'), (1, 0), inplace=True)
df2.Loan.replace(('yes', 'no'), (1, 0), inplace=True)


#Drop target from the training and query data.
#Then add it to own variable for later
trainingData = df.drop('Target',axis='columns')
target = df.Target
testingData = df2.drop('Target',axis='columns')

#Converting categorical values into columns of 1s and 0s
#Also drop them from the table since we will have the new seperated ones
dummiesTrain = pd.get_dummies(df.Job)
dummiesTest = pd.get_dummies(df2.Job)
trainingData = pd.concat([trainingData,dummiesTrain],axis='columns')
testingData = pd.concat([testingData,dummiesTest],axis='columns')
trainingData.drop(['Job'],axis='columns',inplace=True)
testingData.drop(['Job'],axis='columns',inplace=True)

#Converting categorical values into columns of 1s and 0s
#Also drop them from the table since we will have the new seperated ones
dummiesTrain = pd.get_dummies(df.Marital)
dummiesTest = pd.get_dummies(df2.Marital)
trainingData = pd.concat([trainingData,dummiesTrain],axis='columns')
testingData = pd.concat([testingData,dummiesTest],axis='columns')
trainingData.drop(['Marital'],axis='columns',inplace=True)
testingData.drop(['Marital'],axis='columns',inplace=True)

#Converting categorical values into columns of 1s and 0s
#Also drop them from the table since we will have the new seperated ones
dummiesTrain = pd.get_dummies(df.Education)
dummiesTest = pd.get_dummies(df2.Education)
trainingData = pd.concat([trainingData,dummiesTrain],axis='columns')
testingData = pd.concat([testingData,dummiesTest],axis='columns')
trainingData.drop(['Education'],axis='columns',inplace=True)
testingData.drop(['Education'],axis='columns',inplace=True)

#Converting categorical values into columns of 1s and 0s
#Also drop them from the table since we will have the new seperated ones
dummiesTrain = pd.get_dummies(df.Contact)
dummiesTest = pd.get_dummies(df2.Contact)
trainingData = pd.concat([trainingData,dummiesTrain],axis='columns')
testingData = pd.concat([testingData,dummiesTest],axis='columns')
trainingData.drop(['Contact'],axis='columns',inplace=True)
testingData.drop(['Contact'],axis='columns',inplace=True)


#Converting categorical values into columns of 1s and 0s
#Also drop them from the table since we will have the new seperated ones
dummiesTrain = pd.get_dummies(df.Month)
dummiesTest = pd.get_dummies(df2.Month)
trainingData = pd.concat([trainingData,dummiesTrain],axis='columns')
testingData = pd.concat([testingData,dummiesTest],axis='columns')
trainingData.drop(['Month'],axis='columns',inplace=True)
testingData.drop(['Month'],axis='columns',inplace=True)


#Converting categorical values into columns of 1s and 0s
#Also drop them from the table since we will have the new seperated ones
dummiesTrain = pd.get_dummies(df.Poutcome)
dummiesTest = pd.get_dummies(df2.Poutcome)
trainingData = pd.concat([trainingData,dummiesTrain],axis='columns')
testingData = pd.concat([testingData,dummiesTest],axis='columns')
trainingData.drop(['Poutcome'],axis='columns',inplace=True)
testingData.drop(['Poutcome'],axis='columns',inplace=True)

#Take the test data ids. Then drop from data table since they arent needed for training.
testIDS = testingData.ID
trainingData.drop(['ID'],axis='columns',inplace=True)
testingData.drop(['ID'],axis='columns',inplace=True)

#Split the table with an 75/25 split 75 for training and 25 for testing the model.
#Then used the GaussianNB model and got a score for the model
dataToTrain, dataForTest, outcomeForTrain, outcomeForTest = train_test_split(trainingData,target,test_size=0.25)
model = GaussianNB()
model.fit(dataToTrain,outcomeForTrain)
print(model.score(dataForTest,outcomeForTest))

#Taking the predictions from the testing data
modelPredictions = model.predict(testingData)

#Print out predictions into appropriate style txt file
counter = 0
file1 = open("predictions.txt","w")
for i in testIDS:
    if counter < len(testIDS) - 1:
        file1.write(i + "," + '"'+modelPredictions[counter]+'"'+"\n") 
    else:
        file1.write(i + "," + '"'+modelPredictions[counter]+'"') 
    counter = counter + 1

file1.close()