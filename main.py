# Import necessary libraries
import streamlit as st
import matplotlib.pyplot as plt
import math 
import random

st.title("Curvas de aprendizaje y Simulación Montecarlo")
st.write("[Ver el diseño del a aplicación](https://excalidraw.com/#room=5a1eb83a9c0ba4ee278b,j6-eKhrIdcLkM9BnRxtAgg)")

learning_tab, montecarlo_tab = st.tabs(["📉  Curvas de aprendizaje", "🎲  Simulación Montecarlo"])
with learning_tab:
    p = st.number_input(label="% de aprendizaje", value=80.0, min_value=1.0, max_value=99.999)

    a = st.number_input(label="Tiempo para la primera unidad", value=800, min_value=1)

    X = st.number_input(label="Unidades requeridas",  value=16, min_value=2)
    
    try:
        p = float(p) / 100
        a = float(a)
        X = int(X)
        b = math.log(p) / math.log(2)
        
        y = a * math.pow(X, b)
        
        st.success(f"Cantidad de tiempo para producir la unidad **{X}** es: **{y:.2f}**", icon="📈")
        
        x_values = list(range(1, X + 1))
        y_values = [a * math.pow(x, b) for x in x_values]


        fig, ax = plt.subplots()
        ax.plot(x_values, y_values)
        
        ax.set_xlabel('Unidades')
        ax.set_ylabel('Tiempo')

        # Display the plot in the Streamlit app
        st.pyplot(fig)

    except ValueError as error:
        st.write("Ocurrió un error, por favor verifica los valores ingresados.")
        st.write(error)

with montecarlo_tab:
    st.info("El siguiente simulador se adecua al manejo de inventarios a través de drones sobre el cual se basa nuestra investigación", icon="ℹ️")

    n = st.number_input(label="#️⃣ Número de iteraciones", value=2500, min_value=1)

    cost = st.number_input(label="💰 Costo debido a errores", value=1200.00, min_value=1.0)

    route_a = st.number_input(label="🙅🏽‍♂️ Probabilidad (%) de error en la ruta A", value=18.00, min_value=0.0, max_value=100.0)

    route_b = st.number_input(label="🙅🏽‍♂️ Probabilidad (%) de error en la ruta B", value=15.00, min_value=0.0, max_value=100.0)

    route_c = st.number_input(label="🙅🏽‍♂️ Probabilidad (%) de error en la ruta C", value=10.00, min_value=0.0, max_value=100.0)


    total_cost = 0
    mean_cost = []
    if st.button("🏁 Simular"):
        try:
            for i in range(n):
                random_route = random.choices([route_a, route_b, route_c])

                error = random.choices([True, False], weights=[random_route[0], 100 - random_route[0]])

                if error[0]:
                    total_cost += cost
                
                mean_cost.append(total_cost / (i + 1))

            st.success(f"El costo medio debido a errores es: **{total_cost/n:.2f}**", icon="💰")

            fig, ax = plt.subplots()
            ax.hist(mean_cost)
            ax.set_title('Histograma de costos medios')
            ax.set_xlabel('Costo')
            ax.set_ylabel('Freccuencia')
            st.pyplot(fig)

        except ValueError as error:
            st.write("Ocurrió un error, por favor verifica los valores ingresados.")
            st.write(error)