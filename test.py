import tkinter as tk
from tkinter import *
import numpy as np
import joblib
import codecs
from sklearn.tree import DecisionTreeClassifier

# Create a tkinter window
root = tk.Tk()
root.geometry('600x600')
root.title('Transportation Prediction')
bg = tk.PhotoImage(file = "C:\\Users\\kolipaka akhila\\Desktop\\ml project\\space.png")
img = tk.Label(root, i=bg)
img.pack()
# Create input labels and entry boxes


home_planet_label = tk.Label(root, text='Home Planet: ', font=('Comic Sans MS', 10, 'bold'))
home_planet_entry = tk.Entry(root)
home_planet_label.place(x=150, y=10)
home_planet_entry.place(x=350, y=10)

cryo_sleep_label = tk.Label(root, text='Cryo Sleep (True/False)', font=('Comic Sans MS', 10, 'bold'))
cryo_sleep_label.place(x=150, y=40)
cryo_sleep_entry = tk.Entry(root)
cryo_sleep_entry.place(x=350, y=40)

destination_label = tk.Label(root, text='Destination:', font=('Comic Sans MS', 10, 'bold'))
destination_label.place(x=150, y=70)
destination_entry = tk.Entry(root)
destination_entry.place(x=350, y=70)

vip_label = tk.Label(root, text='VIP (True/False):', font=('Comic Sans MS', 10, 'bold'))
vip_label.place(x=150, y=100)
vip_entry = tk.Entry(root)
vip_entry.place(x=350, y=100)

child_label = tk.Label(root, text='Child (True/False):', font=('Comic Sans MS', 10, 'bold'))
child_label.place(x=150, y=130)
child_entry = tk.Entry(root)
child_entry.place(x=350, y=130)

youth_label = tk.Label(root, text='Youth (True/False):', font=('Comic Sans MS', 10, 'bold'))
youth_label.place(x=150, y=160)
youth_entry = tk.Entry(root)
youth_entry.place(x=350, y=160)

cabin_deck_label = tk.Label(root, text='Cabin Deck:', font=('Comic Sans MS', 10, 'bold'))
cabin_deck_label.place(x=150, y=190)
cabin_deck_entry = tk.Entry(root)
cabin_deck_entry.place(x=350, y=190)

r2_label = tk.Label(root, text='CabinNum < 600(0 / 1):', font=('Comic Sans MS', 10, 'bold'))
r2_label.place(x=150, y=220) 
r2_entry = tk.Entry(root)
r2_entry.place(x=350, y=220)

r3_label = tk.Label(root, text='CabinNum < 1100(0 / 1):', font=('Comic Sans MS', 10, 'bold'))
r3_label.place(x=150, y=250)
r3_entry = tk.Entry(root)
r3_entry.place(x=350, y=250)

r4_label = tk.Label(root, text='CabinNum < 1200(0 / 1):', font=('Comic Sans MS', 10, 'bold'))
r4_label.place(x=150, y=280)
r4_entry = tk.Entry(root)
r4_entry.place(x=350, y=280)

r6_label = tk.Label(root, text='CabinNum < 1800(0 / 1):', font=('Comic Sans MS', 10, 'bold'))
r6_label.place(x=150, y=310)
r6_entry = tk.Entry(root)
r6_entry.place(x=350, y=310)

r7_label = tk.Label(root, text='CabinNum > 1800(0 / 1):', font=('Comic Sans MS', 10, 'bold'))
r7_label.place(x=150, y=340)
r7_entry = tk.Entry(root)
r7_entry.place(x=350, y=340)

dicti={'Europa': 0, 'Earth': 1, 'Mars': 2, FALSE: 0, TRUE: 1, 'TRAPPIST-1e': 0, 'PSO J318.5-22': 1,'55 Cancri e': 2, 'B': 0, 'F': 1, 'A': 2, 'G': 3,'E': 4, 'C': 5, 'D': 6}
# Create a function to predict using a trained model
def predict():
    features = [dicti[str(home_planet_entry.get())], dicti[bool(cryo_sleep_entry.get())], dicti[str(destination_entry.get())],
                dicti[bool(vip_entry.get())], dicti[bool(child_entry.get())], dicti[bool(youth_entry.get())],
                dicti[str(cabin_deck_entry.get())], r2_entry.get(), (r3_entry.get()),
                r4_entry.get(), r6_entry.get(), r7_entry.get()]
    X = np.array(features).reshape(1, -1)
    model = joblib.load("C:\\Users\\kolipaka akhila\\Desktop\\ml project\\decision_tree.joblib")
    #model.fit(X, [0, 1])
    prediction=model.predict(X)    
    return "Transported" if prediction[0] == 1 else "Not Transported"

# Create a function to update the output label
def update_output():
    prediction = predict()
    if(prediction[0] == 'T'):
        output_label.config(text=f'Prediction: Transported')
    else:
        output_label.config(text=f'Prediction: Not Transported')

# Create a button to trigger the prediction function
predict_button = tk.Button(root, text='Predict', font=('Comic Sans MS', 10, 'bold'), command=update_output)
predict_button.place(x=300, y=380)

# Create an output label to display the predicted value
output_label = tk.Label(root, text='Prediction: ', font=('Comic Sans MS', 10, 'bold'))
output_label.place(x=250, y=430)

#Decoded features
homePlanet_decode1 = tk.Label(root, text='HomePlanet: ', font=('Comic Sans MS', 10, 'bold'))
homePlanet_decode2 = tk.Label(root, text='[Europa, Earth, Mars]', font=('Comic Sans MS', 10, 'bold'))
homePlanet_decode1.place(x=80, y=460)
homePlanet_decode2.place(x=200, y=460)


destination_decode1 = tk.Label(root, text='Destination: ', font=('Comic Sans MS', 10, 'bold'))
destination_decode2 = tk.Label(root, text='[TRAPPIST-1e, PSO J318.5-22, 55 Cancri e]', font=('Comic Sans MS', 10, 'bold'))
destination_decode1.place(x=80, y=490)
destination_decode2.place(x=200, y=490)

deck_decode1 = tk.Label(root, text='Cabin Deck: ', font=('Comic Sans MS', 10, 'bold'))
deck_decode2 = tk.Label(root, text='[B, F, A, G, E, C, D]', font=('Comic Sans MS', 10, 'bold'))
deck_decode1.place(x=80, y=520)
deck_decode2.place(x=200, y=520)
root.mainloop()