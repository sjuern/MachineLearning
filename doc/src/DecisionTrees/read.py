# Common imports
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.tree import export_graphviz
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from IPython.display import Image 
from pydot import graph_from_dot_data
import os

# Where to save the figures and data files
PROJECT_ROOT_DIR = "Results"
FIGURE_ID = "Results/FigureFiles"
DATA_ID = "DataFiles/"

if not os.path.exists(PROJECT_ROOT_DIR):
    os.mkdir(PROJECT_ROOT_DIR)

if not os.path.exists(FIGURE_ID):
    os.makedirs(FIGURE_ID)

if not os.path.exists(DATA_ID):
    os.makedirs(DATA_ID)

def image_path(fig_id):
    return os.path.join(FIGURE_ID, fig_id)

def data_path(dat_id):
    return os.path.join(DATA_ID, dat_id)

def save_fig(fig_id):
    plt.savefig(image_path(fig_id) + ".png", format='png')

infile = open(data_path("ride.csv"),'r')

# Read the experimental data with Pandas
from IPython.display import display
ridedata = pd.read_csv(infile,names = ('Outlook','Temperature','Humidity','Wind','Ride'))
ridedata = pd.DataFrame(ridedata)
display(ridedata)
# Features and targets
X = ridedata.loc[:, ridedata.columns != 'Ride'].values
display(X)
y = ridedata.loc[:, ridedata.columns == 'Ride'].values
display(y)
# Categorical variables to one-hot's
onehotencoder = OneHotEncoder(categories="auto")

X = ColumnTransformer([("", onehotencoder)]).fit_transform(X)
y.shape

display(X)
display(y)


"""
X = pd.DataFrame(ridedata.data, columns=ridedata.feature_names)
y = pd.Categorical.from_codes(ridedata.target, ridedata.target_names)
y = pd.get_dummies(y)


tree_clf = DecisionTreeClassifier(max_depth=2)
tree_clf.fit(X, y)


export_graphviz(
    tree_clf,
    out_file="ride.dot",
    feature_names=tree_clf.feature_names,
    class_names=tree_clf.target_names,
    rounded=True,
    filled=True
)
"""

