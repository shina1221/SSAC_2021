#%load util.py

# %%writefile 파일경로 - cell의 내용을 파일로 저장한다. 반드시 첫줄에 작성한다.

import numpy as np
from sklearn.metrics import (accuracy_score,
                            recall_score,
                            precision_score,
                            f1_score,
                            mean_squared_error,
                            r2_score)

def print_metrics(y, pred, title=None):
    acc = accuracy_score(y, pred)
    recall = recall_score(y, pred)
    precision = precision_score(y, pred)
    f1 = f1_score(y, pred)   
    
    if title:
        print(title)
    print('정확도: {acc}, recall: {recall}, Precision: {precision}, f1점수: {f1}'.format(acc, recall, precision, f1))
    
def print_regression_metrics(y, y_pred, title=None):
    mse = mean_squared_error(y, y_pred)
    rmse = np.sqrt(mse)
    r2 = r2_score(y, y_pred)
    if title:
        print(title)
    #print(f"MSE:{mse}, RMSE:{rmse}, R Square:{r2}")
    print("MSE:{mse}, RMSE:{rmse}, R Square:{r2}".format(mse, rmse, r2))