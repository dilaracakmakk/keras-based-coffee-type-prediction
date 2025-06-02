import tkinter as tk
from tkinter import ttk, messagebox
import pandas as pd
import tensorflow as tf
from tensorflow.keras.models import load_model
from profile_manager import update_user_profile, get_user_profile

model = tf.keras.models.load_model("coffee_model.keras")
X_columns = pd.read_csv("coffee_model_columns.csv")["columns"].tolist()
y_labels = pd.read_csv("coffee_model_labels.csv")["labels"].tolist()

root = tk.Tk()
root.title("Your Coffee Assistant")
root.geometry("500x600")
root.configure(padx=20, pady=20)

tk.Label(root, text="Your Name").pack()
username_entry = tk.Entry(root)
username_entry.pack(pady=5)

tk.Label(root, text="Time (8-22)").pack()
time_entry = tk.Entry(root)
time_entry.pack(pady=5)

tk.Label(root, text="Mood").pack()
mood_cb = ttk.Combobox(root, values=["tired", "normal", "energetic", "relaxed"])
mood_cb.pack(pady=5)

tk.Label(root, text="Weather").pack()
weather_cb = ttk.Combobox(root, values=["cold", "hot", "sunny", "rainy", "snowy"])
weather_cb.pack(pady=5)

tk.Label(root, text="Previous Choice").pack()
prev_cb = ttk.Combobox(root, values=[
    "filter-coffee", "ice-latte", "cappucino", "espresso", "mocha", 
    "ice-flat-white", "caramel-frappucino", "frappe", "ice-matcha-latte",
    "hot-chocolate", "chai-tea-latte"
])
prev_cb.pack(pady=5)

tk.Label(root, text="Sugar Choice").pack()
sugar_cb = ttk.Combobox(root, values=["sugar", "non-sugar"])
sugar_cb.pack(pady=5)

tk.Label(root, text="Milk Choice").pack()
milk_cb = ttk.Combobox(root, values=["milk", "non-milk", "almond-milk", "oat-milk", "lactose-free-milk"])
milk_cb.pack(pady=5)

def öner():
    try:
        username = username_entry.get()
        time_val = int(time_entry.get())

        sample = {
            "time": time_val,
            "mood": mood_cb.get(),
            "weather_status": weather_cb.get(),
            "previous_choice": prev_cb.get(),
            "sugar_request": sugar_cb.get(),
            "milk_choice": milk_cb.get()
        }

        df = pd.DataFrame([sample])
        df = pd.get_dummies(df)

        for col in X_columns:
            if col not in df.columns:
                df[col] = 0
        df = df[X_columns]
        df = df.astype("float32")

        print("\n--- DEBUG ---")
        print("Input DataFrame to Model:\n", df)
        print("X_columns uyumu:", list(df.columns) == X_columns)
        
        prediction = model.predict(df)
        print("Raw prediction output:\n", prediction)
        top_indices = prediction[0].argsort()[::-1][:3] 
        top_labels = [y_labels[i] for i in top_indices]
        top_probs = [prediction[0][i] for i in top_indices]

        top_3_text = "Top 3 Suggestions:\n"
        for lbl, prob in zip(top_labels, top_probs):
            top_3_text += f"{lbl}: {prob:.2%}\n"  

        messagebox.showinfo("Recommended Coffee", top_3_text)


        

        predicted_label = y_labels[prediction.argmax()]
        print("Predicted label:", predicted_label)
        print("--- END DEBUG ---\n")

        messagebox.showinfo("Recommended Coffee", f"{predicted_label}")

        update_user_profile(username, predicted_label, time_val)
        profile = get_user_profile(username)

        if profile:
            last = profile.get("last_choice", "N/A")
            most = max(profile["total_choices"], key=profile["total_choices"].get) if profile["total_choices"] else "N/A"
            profile_text = f"Last Coffee: {last}\nMost Drunk: {most}"
            profile_label.config(text=profile_text)

    except Exception as e:
        messagebox.showerror("Error!", str(e))

tk.Button(root, text="Recommend", command=öner).pack(pady=15)

tk.Label(root, text="User Profile", font=("Arial", 14, "bold")).pack(pady=(20, 5))
profile_label = tk.Label(root, text="No data", justify="left")
profile_label.pack()

root.mainloop()
