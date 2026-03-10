from sklearn.linear_model import LinearRegression
import numpy as np
x=np.array([[500],[800],[1200],[1500],[1800]])
y=np.array([150000,200000,280000,310000,360000])

model=LinearRegression()
model.fit(x,y)

size=np.array([[1400]])
prediction=model.predict(size)
print("Predicted size: ",prediction[0])