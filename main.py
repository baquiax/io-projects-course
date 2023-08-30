# Import necessary libraries
import streamlit as st
import matplotlib.pyplot as plt
import math 

st.title("Curvas de aprendizaje y Simulación Montecarlo")
st.write("[Ver el diseño del a aplicación](https://excalidraw.com/#room=5a1eb83a9c0ba4ee278b,j6-eKhrIdcLkM9BnRxtAgg)")

learning_tab, montecarlo_tab = st.tabs(["📉  Curvas de aprendizaje", "⏳  Simulación Montecarlo"])
with learning_tab:
    p = st.number_input(label="% de aprendizaje", value=80.0, min_value=1.0, max_value=99.999)

    a = st.number_input(label="Tiempo para la primera unidad", value=800, min_value=1)

    X = st.number_input(label="Unidades requeridas",  value=16, min_value=2)
    
    # text_input(label="Unidades requeridas", value=16)
    
    # Button to display the inputs
    
        # Basic input validation
    try:
        p = float(p) / 100
        a = float(a)
        X = int(X)
        b = math.log(p) / math.log(2)
        
        y = a * math.pow(X, b)
        
        st.success(f"Cantidad de tiempo para producir **{X}** unidades: **{y:.2f}**", icon="📈")
        
        x_values = list(range(1, X + 1))
        y_values = [a * math.pow(x, b) for x in x_values]


        fig, ax = plt.subplots()
        ax.plot(x_values, y_values)
        
        ax.set_xlabel('Unidades')
        ax.set_ylabel('Tiempo')

        # Display the plot in the Streamlit app
        st.pyplot(fig)

    except ValueError as error:
        st.write("Please enter valid values.")
        st.write(error)

with montecarlo_tab:
    # Get user input for error percentage
    error_percentage = st.text_input("Enter Error Percentages:")

    # Get user input for amount of iterations
    iterations = st.text_input("Enter Amount of Iterationss:")

    # Button to display the inputs
    if st.button("Submits"):
        # Basic input validation
        try:
            error = float(error_percentage)
            iters = int(iterations)

            st.write(f"You entered {error}% error percentage.")
            st.write(f"You entered {iters} iterations.")
        except ValueError:
            st.write("Please enter valid values.")