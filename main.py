# Import necessary libraries
import streamlit as st

st.title("Curvas de aprendizaje y Simulación Montecarlo")
st.write("[Ver el diseño del a aplicación](https://excalidraw.com/#room=5a1eb83a9c0ba4ee278b,j6-eKhrIdcLkM9BnRxtAgg)")

learning_tab, montecarlo_tab = st.tabs(["Curvas de aprendizaje", "Simulación Montecarlo"])
with learning_tab:
    # Get user input for error percentage
    error_percentage = st.text_input("Enter Error Percentage:")

    # Get user input for amount of iterations
    iterations = st.text_input("Enter Amount of Iterations:")

    # Button to display the inputs
    if st.button("Submit"):
        # Basic input validation
        try:
            error = float(error_percentage)
            iters = int(iterations)

            st.write(f"You entered {error}% error percentage.")
            st.write(f"You entered {iters} iterations.")
        except ValueError:
            st.write("Please enter valid values.")

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