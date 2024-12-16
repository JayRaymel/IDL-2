import dash
from dash import dcc, html
import plotly.graph_objects as go

# Datos 
ventas = [1200, 1500, 1100, 2000, 2200, 1800, 2500, 1900, 1600, 2100, 2400, 2300]
meses = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre']

# Función para asignar colores según las ventas
def asignar_color(venta):
    if venta < 1500:
        return 'red'   # Rojo para ventas bajas
    elif venta < 2000:
        return 'yellow'  # Amarillo para ventas medias
    else:
        return 'green'  # Verde para ventas altas

# Colores de las barras
colores = [asignar_color(venta) for venta in ventas]

# Crear el gráfico de barras
fig = go.Figure(data=[
    go.Bar(
        x=meses,
        y=ventas,
        marker=dict(color=colores)
    )
])

# Diseño del gráfico
fig.update_layout(
    title="Ventas Mensuales del Año",
    xaxis_title="Meses",
    yaxis_title="Ventas (en unidades)",
    plot_bgcolor='white',
)

# Crear la app Dash
app = dash.Dash(__name__)

# Diseño del dashboard
app.layout = html.Div([
    html.H1("Dashboard de Ventas Mensuales", style={'text-align': 'center'}),
    dcc.Graph(figure=fig)
])

# Ejecutar el servidor
if __name__ == '__main__':
    app.run_server(debug=True)

