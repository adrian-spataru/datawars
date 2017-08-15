import pandas as pd
import numpy as np
from sklearn.metrics import accuracy_score

"""
returns the score of a submission
"""
def accuracy_score_private(true, sub):
    true = np.array([x for x in true.split(";") ])
    sub = np.array([x for x in sub.split(";") ])
    return accuracy_score(true, sub)

def accuracy_score_public(true, sub, public_ids):
    public_ids = [int(x) for x  in public_ids.split(";")] 
    true = np.array([x for x in true.split(";") ])
    sub = np.array([x for x in sub.split(";") ])
    return accuracy_score(true[public_ids], sub[public_ids])

   



