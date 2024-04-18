import streamlit as st
import plotly.graph_objs as go

def main():
    st.title("Simple Plotting with Plotly")

    # Generate some sample data
    x_values = [1, 2, 3, 4, 5]
    y_values = [10, 20, 15, 25, 30]

    # Create a Plotly figure
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=x_values, y=y_values, mode='lines+markers'))

    # Update layout
    fig.update_layout(title='Sample Plot', xaxis_title='X-axis', yaxis_title='Y-axis')

    # Display the plot using Streamlit
    #https://project-heszqmysob5vqsdb7go9v6.streamlit.app/
    st.plotly_chart(fig)

if __name__ == "__main__":
    main()
