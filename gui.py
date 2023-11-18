import tkinter as tk
import numpy as np
import joblib
import codecs
from sklearn.tree import DecisionTreeClassifier

# Create a tkinter window
root = tk.Tk()
root.geometry('400x200')
root.title('Transportation Prediction')

# Create input labels and entry boxes
home_planet_label = tk.Label(root, text='Home Planet:')
home_planet_label.pack()
home_planet_entry = tk.Entry(root)
home_planet_entry.pack()
print(home_planet_entry)

cryo_sleep_label = tk.Label(root, text='Cryo Sleep (years):')
cryo_sleep_label.pack()
cryo_sleep_entry = tk.Entry(root)
cryo_sleep_entry.pack()

destination_label = tk.Label(root, text='Destination:')
destination_label.pack()
destination_entry = tk.Entry(root)
destination_entry.pack()

vip_label = tk.Label(root, text='VIP? (0 or 1):')
vip_label.pack()
vip_entry = tk.Entry(root)
vip_entry.pack()

child_label = tk.Label(root, text='Child? (0 or 1):')
child_label.pack()
child_entry = tk.Entry(root)
child_entry.pack()

youth_label = tk.Label(root, text='Youth? (0 or 1):')
youth_label.pack()
youth_entry = tk.Entry(root)
youth_entry.pack()

cabin_deck_label = tk.Label(root, text='Cabin Deck:')
cabin_deck_label.pack()
cabin_deck_entry = tk.Entry(root)
cabin_deck_entry.pack()

r2_label = tk.Label(root, text='Room on Deck 2? (0 or 1):')
r2_label.pack()
r2_entry = tk.Entry(root)
r2_entry.pack()

r3_label = tk.Label(root, text='Room on Deck 3? (0 or 1):')
r3_label.pack()
r3_entry = tk.Entry(root)
r3_entry.pack()

r4_label = tk.Label(root, text='Room on Deck 4? (0 or 1):')
r4_label.pack()
r4_entry = tk.Entry(root)
r4_entry.pack()

r6_label = tk.Label(root, text='Room on Deck 6? (0 or 1):')
r6_label.pack()
r6_entry = tk.Entry(root)
r6_entry.pack()

r7_label = tk.Label(root, text='Room on Deck 7? (0 or 1):')
r7_label.pack()
r7_entry = tk.Entry(root)
r7_entry.pack()



# Create a function to predict using a trained model
def predict():
    features = [home_planet_entry.get(), int(cryo_sleep_entry.get()), destination_entry.get(),
                int(vip_entry.get()), int(child_entry.get()), int(youth_entry.get()),
                int(cabin_deck_entry.get()), int(r2_entry.get()), int(r3_entry.get()),
                int(r4_entry.get()), int(r6_entry.get()), int(r7_entry.get())]
    X = np.array(features).reshape(1, -1)
    model = joblib.load("C:\\Users\\kolipaka akhila\\Downloads\\decision_tree.joblib")
    #model.fit(X, [0, 1])
    prediction=model.predict(X)    
    return "Transported" if prediction[0] == 1 else "Not Transported"
    '''model.fit(X, ['Not Transported', 'Transported'])
    return model.predict(X)'''

# Create a function to update the output label
def update_output():
    prediction = predict()
    if(prediction[0] == 'T'):
        output_label.config(text=f'Prediction: Transported')
    else:
        output_label.config(text=f'Prediction: Not Transported')

# Create a button to trigger the prediction function
predict_button = tk.Button(root, text='Predict', command=update_output)
predict_button.pack()

# Create an output label to display the predicted value
output_label = tk.Label(root, text='Prediction: ')
output_label.pack()

root.mainloop()