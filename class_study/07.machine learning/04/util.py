
# %%writefile 파일경로 - cell의 내용을 파일로 저장한다. 반드시 첫줄에 작성한다.

from sklearn.metrics import accuracy_score, recall_score, precision_score, f1_score
def print_metrics(y, pred, title=None):
    acc = accuracy_score(y, pred)
    recall = recall_score(y, pred)
    precision = precision_score(y, pred)
    f1 = f1_score(y, pred)   
    
    if title:
        print(title)
    print(f'정확도: {acc}, recall: {recall}, Precision: {precision}, f1점수: {f1}')
