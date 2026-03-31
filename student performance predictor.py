
#   Tanmay soni
#   25BAI111463
#   Project Fumdamental AI & ML


import tkinter as tk
from sklearn.linear_model import LinearRegression
import numpy as np

# ---------------- ML MODEL ---------------- #

# Sample dataset 
# [study_hours, attendance, previous_marks]
X = np.array([
    [2, 60, 50],
    [3, 65, 55],
    [4, 70, 60],
    [5, 75, 65],
    [6, 80, 70],
    [7, 85, 75],
    [8, 90, 80],
    [9, 95, 85]
])

# Final marks
y = np.array([52, 57, 63, 68, 72, 78, 83, 88])

# Train model
model = LinearRegression()
model.fit(X, y)

# ---------------- GUI ---------------- #

root = tk.Tk()
root.title("Student Performance Predictor")
root.geometry("400x400")

tk.Label(root, text="Enter Study Hours").pack()
entry_hours = tk.Entry(root)
entry_hours.pack()

tk.Label(root, text="Enter Attendance (%)").pack()
entry_attendance = tk.Entry(root)
entry_attendance.pack()

tk.Label(root, text="Enter Previous Marks").pack()
entry_marks = tk.Entry(root)
entry_marks.pack()

result_label = tk.Label(root, text="Prediction: ", font=("Arial", 14))
result_label.pack(pady=20)

def predict():
    try:
        hours = float(entry_hours.get())
        attendance = float(entry_attendance.get())
        marks = float(entry_marks.get())

        # Prediction
        prediction = model.predict([[hours, attendance, marks]])

        result_label.config(text=f"Predicted Marks: {prediction[0]:.2f}")

    except:
        result_label.config(text="Invalid Input!")

tk.Button(root, text="Predict", command=predict).pack()

root.mainloop()