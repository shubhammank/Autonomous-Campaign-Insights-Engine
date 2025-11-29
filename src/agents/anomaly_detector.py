import numpy as np
def anomaly_detector(values):
    mean=np.mean(values); std=np.std(values)
    anomaly=values[-1]>mean+2*std
    return {"anomaly": bool(anomaly)}
