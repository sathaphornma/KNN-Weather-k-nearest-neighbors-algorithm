import numpy as np

def today(now):
    x = np.array([[31.7, 25.7, 18.53], [33.2, 24.9, 25.95], [31, 26, 31.51], [25.6, 23, 35.21], [26.2, 22.9, 35.21],
                  [25.6, 21.7, 2.3], [25.9, 23.2, 22.24],
                  [27.8, 22, 22.24], [25.7, 22.4, 22.24], [31.5, 24.4, 3.7]])
    y = np.array([0.1, 0, 4.2, 4.8, 3.1, 4.7, 0.1, 9.4, 7.9, 0])

    # print(len(x), len(y))

    p = np.array(now)
    d = np.zeros(len(y))

    for i, dataX in enumerate(x):
        d[i] = np.sqrt(np.sum((p - dataX) ** 2))

    minD = np.min(d)
    indexMin = np.argmin(d)
    pre = y[indexMin]

    return pre


knn = today(now=[30, 22, 22])

if knn <= 0:
    print("วันนี้ไม่มีฝน")
else:
    print("วันนี้ฝนตก มีปริมาณฝน : ", knn)
