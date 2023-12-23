from dash import Dash,dcc,html,Input,Output,dash_table
import plotly.express as px
import pandas as pd

df=pd.read_csv("processed_data.csv")
app=Dash(__name__)

app.layout=html.Div([
    html.H2("Rainfall data of Albury"),
    dash_table.DataTable(data=df.to_dict('records'),page_size=10),
    html.H4("Animated Graphs for Rainfall Analysis"),
    html.P("Select Animation"),
    dcc.RadioItems(
        id='selection',
        options=['Rainfall Analysis','Humidity Variations','Temperature Variations','Effects of Wind Direction','Effect of Temperature on Rainfall','Effect of Humidity on Rainfall','Effect of Pressure on Rainfall'],
        value='Rainfall Analysis'
    ),
    dcc.Loading(dcc.Graph(id='graph'),type='cube')
    
])

@app.callback(
Output('graph','figure'),
Input('selection','value')
)
def display_animated_graph(selection):
    animations={
        "Rainfall Analysis":px.bar(df,x='Rainfall',y='RainToday'),
        "Humidity Variations":px.bar(df,x='Humidity3pm',y='RainToday'),
        "Temperature Variations":px.bar(df,x='MaxTemp',y='RainToday'),
        "Effects of Wind Direction":px.bar(df,x='WindGustDir',y='RainToday'),
        "Effect of Temperature on Rainfall":px.scatter(df,x='Temp9am',y='Temp3pm',color='RainToday'),
        "Effect of Humidity on Rainfall":px.scatter(df,x='Humidity9am',y='Humidity3pm',color='RainToday'),
        "Effect of Pressure on Rainfall":px.scatter(df,x='Pressure9am',y='Pressure3pm',color='RainToday')
    }
    return animations[selection]

if __name__=='__main__':
    app.run(debug=True)