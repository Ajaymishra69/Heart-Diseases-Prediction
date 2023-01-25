{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "4ebd3fcd",
   "metadata": {},
   "outputs": [
    {
     "ename": "",
     "evalue": "",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31mRunning cells with 'c:\\Users\\Ajay\\AppData\\Local\\Programs\\Python\\Python310\\python.exe' requires ipykernel package.\n",
      "\u001b[1;31mRun the following command to install 'ipykernel' into the Python environment. \n",
      "\u001b[1;31mCommand: 'c:/Users/Ajay/AppData/Local/Programs/Python/Python310/python.exe -m pip install ipykernel -U --user --force-reinstall'"
     ]
    }
   ],
   "source": [
    "import pandas as pd\n",
    "data=pd.read_csv('heart.csv')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "1c927d67",
   "metadata": {},
   "outputs": [
    {
     "ename": "",
     "evalue": "",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31mRunning cells with 'c:\\Users\\Ajay\\AppData\\Local\\Programs\\Python\\Python310\\python.exe' requires ipykernel package.\n",
      "\u001b[1;31mRun the following command to install 'ipykernel' into the Python environment. \n",
      "\u001b[1;31mCommand: 'c:/Users/Ajay/AppData/Local/Programs/Python/Python310/python.exe -m pip install ipykernel -U --user --force-reinstall'"
     ]
    }
   ],
   "source": [
    "data"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "4931ddec",
   "metadata": {},
   "outputs": [
    {
     "ename": "",
     "evalue": "",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31mRunning cells with 'c:\\Users\\Ajay\\AppData\\Local\\Programs\\Python\\Python310\\python.exe' requires ipykernel package.\n",
      "\u001b[1;31mRun the following command to install 'ipykernel' into the Python environment. \n",
      "\u001b[1;31mCommand: 'c:/Users/Ajay/AppData/Local/Programs/Python/Python310/python.exe -m pip install ipykernel -U --user --force-reinstall'"
     ]
    }
   ],
   "source": [
    "data.shape"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "1e28bc9c",
   "metadata": {},
   "outputs": [
    {
     "ename": "",
     "evalue": "",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31mRunning cells with 'c:\\Users\\Ajay\\AppData\\Local\\Programs\\Python\\Python310\\python.exe' requires ipykernel package.\n",
      "\u001b[1;31mRun the following command to install 'ipykernel' into the Python environment. \n",
      "\u001b[1;31mCommand: 'c:/Users/Ajay/AppData/Local/Programs/Python/Python310/python.exe -m pip install ipykernel -U --user --force-reinstall'"
     ]
    }
   ],
   "source": [
    "data.describe()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "24def13a",
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "ename": "",
     "evalue": "",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31mRunning cells with 'c:\\Users\\Ajay\\AppData\\Local\\Programs\\Python\\Python310\\python.exe' requires ipykernel package.\n",
      "\u001b[1;31mRun the following command to install 'ipykernel' into the Python environment. \n",
      "\u001b[1;31mCommand: 'c:/Users/Ajay/AppData/Local/Programs/Python/Python310/python.exe -m pip install ipykernel -U --user --force-reinstall'"
     ]
    }
   ],
   "source": [
    "data.isnull().sum()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "0b2ae3c7",
   "metadata": {},
   "outputs": [
    {
     "ename": "",
     "evalue": "",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31mRunning cells with 'c:\\Users\\Ajay\\AppData\\Local\\Programs\\Python\\Python310\\python.exe' requires ipykernel package.\n",
      "\u001b[1;31mRun the following command to install 'ipykernel' into the Python environment. \n",
      "\u001b[1;31mCommand: 'c:/Users/Ajay/AppData/Local/Programs/Python/Python310/python.exe -m pip install ipykernel -U --user --force-reinstall'"
     ]
    }
   ],
   "source": [
    "#dataset is clean and has no missing values"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "9b11f7b6",
   "metadata": {},
   "outputs": [
    {
     "ename": "",
     "evalue": "",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31mRunning cells with 'c:\\Users\\Ajay\\AppData\\Local\\Programs\\Python\\Python310\\python.exe' requires ipykernel package.\n",
      "\u001b[1;31mRun the following command to install 'ipykernel' into the Python environment. \n",
      "\u001b[1;31mCommand: 'c:/Users/Ajay/AppData/Local/Programs/Python/Python310/python.exe -m pip install ipykernel -U --user --force-reinstall'"
     ]
    }
   ],
   "source": [
    "data['target'].value_counts()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "23b55089",
   "metadata": {},
   "source": [
    "### dataset is balanced"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "f6d964d5",
   "metadata": {},
   "outputs": [
    {
     "ename": "",
     "evalue": "",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31mRunning cells with 'c:\\Users\\Ajay\\AppData\\Local\\Programs\\Python\\Python310\\python.exe' requires ipykernel package.\n",
      "\u001b[1;31mRun the following command to install 'ipykernel' into the Python environment. \n",
      "\u001b[1;31mCommand: 'c:/Users/Ajay/AppData/Local/Programs/Python/Python310/python.exe -m pip install ipykernel -U --user --force-reinstall'"
     ]
    }
   ],
   "source": [
    "data.info()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "cbe20dae",
   "metadata": {},
   "outputs": [
    {
     "ename": "",
     "evalue": "",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31mRunning cells with 'c:\\Users\\Ajay\\AppData\\Local\\Programs\\Python\\Python310\\python.exe' requires ipykernel package.\n",
      "\u001b[1;31mRun the following command to install 'ipykernel' into the Python environment. \n",
      "\u001b[1;31mCommand: 'c:/Users/Ajay/AppData/Local/Programs/Python/Python310/python.exe -m pip install ipykernel -U --user --force-reinstall'"
     ]
    }
   ],
   "source": [
    "#All data are numerical"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "72d75bcb",
   "metadata": {},
   "outputs": [
    {
     "ename": "",
     "evalue": "",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31mRunning cells with 'c:\\Users\\Ajay\\AppData\\Local\\Programs\\Python\\Python310\\python.exe' requires ipykernel package.\n",
      "\u001b[1;31mRun the following command to install 'ipykernel' into the Python environment. \n",
      "\u001b[1;31mCommand: 'c:/Users/Ajay/AppData/Local/Programs/Python/Python310/python.exe -m pip install ipykernel -U --user --force-reinstall'"
     ]
    }
   ],
   "source": [
    "#let's transform categorical values into dummies/Convert categorical variable into dummy/indicator variables.\n",
    "\n",
    "data = pd.get_dummies(data, columns = ['sex', 'cp', 'fbs', 'restecg', 'exang', 'slope', 'ca', 'thal'])\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "fc488f7f",
   "metadata": {},
   "outputs": [
    {
     "ename": "",
     "evalue": "",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31mRunning cells with 'c:\\Users\\Ajay\\AppData\\Local\\Programs\\Python\\Python310\\python.exe' requires ipykernel package.\n",
      "\u001b[1;31mRun the following command to install 'ipykernel' into the Python environment. \n",
      "\u001b[1;31mCommand: 'c:/Users/Ajay/AppData/Local/Programs/Python/Python310/python.exe -m pip install ipykernel -U --user --force-reinstall'"
     ]
    }
   ],
   "source": [
    "data"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "31d72878",
   "metadata": {},
   "outputs": [
    {
     "ename": "",
     "evalue": "",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31mRunning cells with 'c:\\Users\\Ajay\\AppData\\Local\\Programs\\Python\\Python310\\python.exe' requires ipykernel package.\n",
      "\u001b[1;31mRun the following command to install 'ipykernel' into the Python environment. \n",
      "\u001b[1;31mCommand: 'c:/Users/Ajay/AppData/Local/Programs/Python/Python310/python.exe -m pip install ipykernel -U --user --force-reinstall'"
     ]
    }
   ],
   "source": [
    "#We will test some classification algorithms: Logistic regression, svm, stochastic gradient descent , decision tree, random forest."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "eaa51455",
   "metadata": {},
   "outputs": [
    {
     "ename": "",
     "evalue": "",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31mRunning cells with 'c:\\Users\\Ajay\\AppData\\Local\\Programs\\Python\\Python310\\python.exe' requires ipykernel package.\n",
      "\u001b[1;31mRun the following command to install 'ipykernel' into the Python environment. \n",
      "\u001b[1;31mCommand: 'c:/Users/Ajay/AppData/Local/Programs/Python/Python310/python.exe -m pip install ipykernel -U --user --force-reinstall'"
     ]
    }
   ],
   "source": [
    "from sklearn.linear_model import LogisticRegression\n",
    "from sklearn import svm\n",
    "from sklearn.linear_model import SGDClassifier\n",
    "from sklearn import tree\n",
    "from sklearn.ensemble import RandomForestClassifier\n",
    "from sklearn.metrics import accuracy_score\n",
    "from sklearn.model_selection import train_test_split\n",
    "\n",
    "y = data['target']\n",
    "\n",
    "X = data.drop('target',axis=1)\n",
    "X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.3,random_state=0)\n",
    "LR_classifier = LogisticRegression(random_state=0)\n",
    "clf = svm.SVC()\n",
    "sgd=SGDClassifier()\n",
    "forest=RandomForestClassifier(n_estimators=20, random_state=12,max_depth=6)\n",
    "treee = tree.DecisionTreeClassifier(criterion = 'entropy',random_state=0,max_depth = 6)\n",
    "LR_classifier.fit(X_train, y_train)\n",
    "clf.fit(X_train, y_train)\n",
    "sgd.fit(X_train, y_train)\n",
    "treee.fit(X_train, y_train)\n",
    "forest.fit(X_train, y_train)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "6233d08b",
   "metadata": {},
   "outputs": [
    {
     "ename": "",
     "evalue": "",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31mRunning cells with 'c:\\Users\\Ajay\\AppData\\Local\\Programs\\Python\\Python310\\python.exe' requires ipykernel package.\n",
      "\u001b[1;31mRun the following command to install 'ipykernel' into the Python environment. \n",
      "\u001b[1;31mCommand: 'c:/Users/Ajay/AppData/Local/Programs/Python/Python310/python.exe -m pip install ipykernel -U --user --force-reinstall'"
     ]
    }
   ],
   "source": [
    "print(forest)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "2c551508",
   "metadata": {},
   "outputs": [
    {
     "ename": "",
     "evalue": "",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31mRunning cells with 'c:\\Users\\Ajay\\AppData\\Local\\Programs\\Python\\Python310\\python.exe' requires ipykernel package.\n",
      "\u001b[1;31mRun the following command to install 'ipykernel' into the Python environment. \n",
      "\u001b[1;31mCommand: 'c:/Users/Ajay/AppData/Local/Programs/Python/Python310/python.exe -m pip install ipykernel -U --user --force-reinstall'"
     ]
    }
   ],
   "source": [
    "#traing accuracy\n",
    "y_pred=LR_classifier.predict(X_train)\n",
    "y_predsvm=clf.predict(X_train)\n",
    "y_predsgd=sgd.predict(X_train)\n",
    "y_predtree=treee.predict(X_train)\n",
    "y_predforest=forest.predict(X_train)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "62c20953",
   "metadata": {},
   "outputs": [
    {
     "ename": "",
     "evalue": "",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31mRunning cells with 'c:\\Users\\Ajay\\AppData\\Local\\Programs\\Python\\Python310\\python.exe' requires ipykernel package.\n",
      "\u001b[1;31mRun the following command to install 'ipykernel' into the Python environment. \n",
      "\u001b[1;31mCommand: 'c:/Users/Ajay/AppData/Local/Programs/Python/Python310/python.exe -m pip install ipykernel -U --user --force-reinstall'"
     ]
    }
   ],
   "source": [
    "print(accuracy_score(y_train, y_pred))\n",
    "print(accuracy_score(y_train, y_predsvm))\n",
    "print(accuracy_score(y_train, y_predsgd))\n",
    "print(accuracy_score(y_train, y_predtree))\n",
    "print(accuracy_score(y_train, y_predforest))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "bf427c13",
   "metadata": {},
   "outputs": [
    {
     "ename": "",
     "evalue": "",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31mRunning cells with 'c:\\Users\\Ajay\\AppData\\Local\\Programs\\Python\\Python310\\python.exe' requires ipykernel package.\n",
      "\u001b[1;31mRun the following command to install 'ipykernel' into the Python environment. \n",
      "\u001b[1;31mCommand: 'c:/Users/Ajay/AppData/Local/Programs/Python/Python310/python.exe -m pip install ipykernel -U --user --force-reinstall'"
     ]
    }
   ],
   "source": [
    "#test accuracy\n",
    "y_pred=LR_classifier.predict(X_test)\n",
    "y_predsvm=clf.predict(X_test)\n",
    "y_predsgd=sgd.predict(X_test)\n",
    "y_predtree=treee.predict(X_test)\n",
    "y_predforest=forest.predict(X_test)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "7bdb31ae",
   "metadata": {},
   "outputs": [
    {
     "ename": "",
     "evalue": "",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31mRunning cells with 'c:\\Users\\Ajay\\AppData\\Local\\Programs\\Python\\Python310\\python.exe' requires ipykernel package.\n",
      "\u001b[1;31mRun the following command to install 'ipykernel' into the Python environment. \n",
      "\u001b[1;31mCommand: 'c:/Users/Ajay/AppData/Local/Programs/Python/Python310/python.exe -m pip install ipykernel -U --user --force-reinstall'"
     ]
    }
   ],
   "source": [
    "print(accuracy_score(y_test, y_pred))\n",
    "print(accuracy_score(y_test, y_predsvm))\n",
    "print(accuracy_score(y_test, y_predsgd))\n",
    "print(accuracy_score(y_test, y_predtree))\n",
    "print(accuracy_score(y_test, y_predforest))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "0f29a459",
   "metadata": {},
   "outputs": [
    {
     "ename": "",
     "evalue": "",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31mRunning cells with 'c:\\Users\\Ajay\\AppData\\Local\\Programs\\Python\\Python310\\python.exe' requires ipykernel package.\n",
      "\u001b[1;31mRun the following command to install 'ipykernel' into the Python environment. \n",
      "\u001b[1;31mCommand: 'c:/Users/Ajay/AppData/Local/Programs/Python/Python310/python.exe -m pip install ipykernel -U --user --force-reinstall'"
     ]
    }
   ],
   "source": [
    "#best model is randomForest"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "656d373c",
   "metadata": {},
   "outputs": [
    {
     "ename": "",
     "evalue": "",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31mRunning cells with 'c:\\Users\\Ajay\\AppData\\Local\\Programs\\Python\\Python310\\python.exe' requires ipykernel package.\n",
      "\u001b[1;31mRun the following command to install 'ipykernel' into the Python environment. \n",
      "\u001b[1;31mCommand: 'c:/Users/Ajay/AppData/Local/Programs/Python/Python310/python.exe -m pip install ipykernel -U --user --force-reinstall'"
     ]
    }
   ],
   "source": [
    "import pickle\n",
    "pickle.dump(forest, open('Random_forest_model.pkl', 'wb'))"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.10.6 (tags/v3.10.6:9c7b4bd, Aug  1 2022, 21:53:49) [MSC v.1932 64 bit (AMD64)]"
  },
  "vscode": {
   "interpreter": {
    "hash": "655401cce18542ff0291ac6d94e1b051649840c8aedd95e513915aaaddbfd6e8"
   }
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
