import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def parameter_formatting_WL(filename):
    user_col = ['Wavelength(nm)', 'Repeat[x]', 'M(V)', "Phase(')", 'IS(A)', "Phase(')", 'R(V)', "Phase(')" ]
    readfile = pd.read_csv(filename, delim_whitespace= 1, skiprows=77, names=user_col)
    return readfile