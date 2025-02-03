import streamlit as st

# App title
st.title("Water Pollution Treatment App")

# Sidebar navigation
st.sidebar.header("Navigation")
page = st.sidebar.radio("Go to", ["Home", "Types of Pollution", "Treatment Methods", "Upload Data"])

if page == "Home":
    st.header("Welcome to the Water Treatment App")
    st.write("This app provides insights into water pollution and different treatment methods.")
    st.image("https://upload.wikimedia.org/wikipedia/commons/2/2e/Polluted_Water.jpg", caption="Example of Polluted Water", use_column_width=True)

elif page == "Types of Pollution":
    st.header("Types of Water Pollution")
    st.write("1. **Chemical Pollution**: Industrial waste, pesticides, heavy metals.")
    st.write("2. **Biological Pollution**: Bacteria, viruses, parasites.")
    st.write("3. **Physical Pollution**: Plastics, sediments, debris.")
    st.image("https://upload.wikimedia.org/wikipedia/commons/3/3d/Water_Pollution.jpg", caption="Types of Pollution", use_column_width=True)

elif page == "Treatment Methods":
    st.header("Water Treatment Methods")
    st.write("### 1. Physical Treatment:")
    st.write("- Filtration")
    st.write("- Sedimentation")
    st.write("### 2. Chemical Treatment:")
    st.write("- Chlorination")
    st.write("- Coagulation and Flocculation")
    st.write("### 3. Biological Treatment:")
    st.write("- Bioremediation")
    st.write("- Aeration")
    st.image("https://upload.wikimedia.org/wikipedia/commons/1/19/Water_treatment_plant.jpg", caption="Water Treatment Plant", use_column_width=True)

elif page == "Upload Data":
    st.header("Upload Water Sample Data")
    uploaded_file = st.file_uploader("Upload a CSV file with water sample data", type=["csv"])
    if uploaded_file:
        import pandas as pd
        df = pd.read_csv(uploaded_file)
        st.write("### Uploaded Data:")
        st.dataframe(df)
        st.write("Further analysis can be performed on this data.")
