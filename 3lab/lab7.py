import matplotlib.pyplot as plt
import pandas as pd
import sns as sns
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
import warnings
warnings.filterwarnings("ignore", category=FutureWarning)

LogisticRegression(solver='lbfgs')

data_train = pd.read_csv('student-mat.csv', delimiter=",")
data_test = pd.read_csv('student-mat.csv', delimiter=",")

data_train.shape
data_test.shape

train, validation = train_test_split(data_train, test_size=0.2)

arr_name = []
arr_train = []
arr_val = []
cols_x = ['health', 'age', 'sex', 'Walc', "Dalc", 'G1']
col_y = ['G3']


def get_statistics():
    data_train_rain_today = data_train[data_train['G3'] > 10].shape[0]
    data_train_without_rain = data_train[data_train['G3'] <= 10].shape[0]

    print("Количество человек у которых оценка больше 10 = {}, количество людей у которых оценка меньше 10 = {}.\
      Всего = {}, это означает, что наша выборка будет состоять из этого количества значений. " \
          .format(data_train_rain_today, data_train_without_rain,
                  data_train_rain_today + data_train_without_rain))

    data_train_count = data_train.shape[0]
    data_train_percent_rain = data_train_rain_today / data_train_count
    data_train_percent_without_rain = data_train_without_rain / data_train_count

    print("Процент единиц = {}, а процент нулей = {}." \
          .format(round(data_train_percent_rain * 100, 2),
                  round(data_train_percent_without_rain * 100, 2)))


def get_corr():
    sns.heatmap(data_train.corr())


def test_classifier(classifier, classifier_name):
    classifier.fit(train[cols_x], train[col_y].values.ravel())
    y_train = classifier.predict(train[cols_x])
    y_train_acc = accuracy_score(train[col_y], y_train)

    y_val = classifier.predict(validation[cols_x])
    y_val_acc = accuracy_score(validation[col_y], y_val)

    arr_name.append(classifier_name)
    arr_train.append(y_train_acc)
    arr_val.append(y_val_acc)

    print('Точность для алгоритма {} на обучаещей выборке = {},\
     на валидационной выборке = {}' \
          .format(classifier_name, \
                  round(y_train_acc, 3),
                  round(y_val_acc, 3)))
    return classifier


if __name__ == '__main__':
    get_statistics()
     #get_corr()
    classifier = test_classifier(KNeighborsClassifier(), 'KNN')
    classifier = test_classifier(LogisticRegression(), 'LR')
    classifier = test_classifier(SVC(), 'SVM')
    classifier = test_classifier(DecisionTreeClassifier(), 'Tree')
    for col, i in zip(cols_x, classifier.feature_importances_):
        print(col, ": ", i)

    classifier = test_classifier(GradientBoostingClassifier(), 'GB')
    for col, i in zip(cols_x, classifier.feature_importances_):
        print(col, ": ", i)

    x = range(len(arr_train))
    plt.plot(x, arr_train)
    plt.plot(x, arr_val)
    plt.xticks(x, arr_name)
    plt.ylabel('Точность алгоритма')
    plt.legend(['обучение', 'валидация'], loc='lower left')
    plt.show()

    cols_x = ['health', 'age', 'sex', 'Walc', "Dalc", 'G1']
    col_y = 'G3'
    clf = DecisionTreeClassifier()
    clf.fit(data_train[cols_x], data_train[col_y])

    occupancy_predicted = clf.predict(data_test[cols_x])
    data_test['value'] = occupancy_predicted
    data_test.to_csv('base_solution.csv')
