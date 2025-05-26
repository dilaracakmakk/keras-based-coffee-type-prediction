import pandas as pd
from tensorflow.keras.models import Sequential 
from tensorflow.keras.layers import Dense

df=pd.read_csv("augmented_dataset.csv")

categorical_cols=["mood","weather_status" ,"previous_choice", "sugar_request", "milk_choice"]
df=pd.get_dummies(df, columns=categorical_cols)

y=pd.get_dummies(df["coffee_recommendation"])
X=df.drop("coffee_recommendation", axis=1)


X = X.astype("float32")
y = y.astype("float32") 

model=Sequential()
model.add(Dense(32, activation='relu', input_shape=(X.shape[1],)))
model.add(Dense(32, activation='relu'))
model.add(Dense(y.shape[1], activation='softmax'))



model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
model.fit(X,y, epochs=30, verbose=1)

model.save("coffee_model.keras")
pd.DataFrame({"columns": X.columns}).to_csv("coffee_model_columns.csv", index=False)
pd.DataFrame({"labels": y.columns}).to_csv("coffee_model_labels.csv", index=False)