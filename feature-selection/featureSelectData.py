import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import chi2

data = pd.read_csv("train.csv")
X = data.iloc[:, 0:20]  # independent columns
y = data.iloc[:, -1]    # target column i.e price range
# apply SelectKBest class to extract top 10 best features

bestFeatures = SelectKBest(score_func=chi2, k=10)
fit = bestFeatures.fit(X, y)
dfScores = pd.DataFrame(fit.scores_)
dfColumns = pd.DataFrame(X.columns)

# concat two dataframes for better visualization

featureScores = pd.concat([dfColumns, dfScores], axis=1)
featureScores.columns = ['Specs', 'Score']  # naming the dataframe columns
# print(featureScores.nlargest(10, 'Score'))  # print 10 best features

X = data.iloc[:,0:20]  #independent columns
y = data.iloc[:,-1]    #target column i.e price range

from sklearn.ensemble import ExtraTreesClassifier
import matplotlib.pyplot as plt
model = ExtraTreesClassifier()
model.fit(X,y)
print(model.feature_importances_) #use inbuilt class feature_importances of tree based classifiers
#plot graph of feature importances for better visualization
feat_importances = pd.Series(model.feature_importances_, index=X.columns)
feat_importances.nlargest(10).plot(kind='barh')
plt.show()