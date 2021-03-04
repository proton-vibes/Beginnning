import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def parameter_formatting_data(filename):
    user_col = ['PiezoZ[um]', 'PiezoX[um]', 'M(V)', "Phase(')", 'IS(A)', "Phase(')", 'Ref(V)', "Phase(')" ]
    readfile = pd.read_csv(filename, delim_whitespace= 1, skiprows=79, names=user_col)
    readfile = readfile.drop(["Phase(')", "Phase(').1","Phase(').2"], axis =1)
    return readfile

