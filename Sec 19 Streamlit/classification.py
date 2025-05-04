import streamlit as st
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier

@st.cache_data
def load_data():
      iris = load_iris()
      df = pd.DataFrame(iris.data, columns=iris.feature_names)
      df['species'] = iris.target
      return df, iris.target_names

df, target_name = load_data()

model = RandomForestClassifier()
model.fit(df.iloc[:, :-1], df['species'])

st.sidebar.title("Input features")
sepal_length = st.sidebar.slider("Sepal Length (cm)", 
                               float(df['sepal length (cm)'].min()), 
                               float(df['sepal length (cm)'].max()),
                               float(df['sepal length (cm)'].mean()))

sepal_width = st.sidebar.slider("Sepal Width (cm)", 
                              float(df['sepal width (cm)'].min()), 
                              float(df['sepal width (cm)'].max()),
                              float(df['sepal width (cm)'].mean()))

petal_length = st.sidebar.slider("Petal Length (cm)", 
                               float(df['petal length (cm)'].min()), 
                               float(df['petal length (cm)'].max()),
                               float(df['petal length (cm)'].mean()))

petal_width = st.sidebar.slider("Petal Width (cm)", 
                              float(df['petal width (cm)'].min()), 
                              float(df['petal width (cm)'].max()),
                              float(df['petal width (cm)'].mean()))

# Display input parameters
st.subheader('User Input Parameters')
input_data = pd.DataFrame({
    'sepal length (cm)': [sepal_length],
    'sepal width (cm)': [sepal_width],
    'petal length (cm)': [petal_length],
    'petal width (cm)': [petal_width]
})
st.write(input_data)

# Prediction
prediction = model.predict(input_data)
predicted_species = target_name[prediction[0]]

st.subheader('Prediction')
st.write(f"The predicted species is: **{predicted_species}**")

# # Show prediction probabilities
# prediction_proba = model.predict_proba(input_data)
# st.subheader('Prediction Probability')
# proba_df = pd.DataFrame(prediction_proba, columns=target_name)
# st.write(proba_df)