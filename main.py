# Import necessary libraries
import streamlit as st

def main():
    st.title("Curvas de aprendizaje y Simulación Montecarlo")
    st.write("[https://excalidraw.com/#room=5a1eb83a9c0ba4ee278b,j6-eKhrIdcLkM9BnRxtAgg](Ver el diseño del a aplicación)")


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

if __name__ == '__main__':
    main()
