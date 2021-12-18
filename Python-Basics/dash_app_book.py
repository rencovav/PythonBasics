import dash
from dash import dcc
from dash import html
import plotly.graph_objs as go
from dash.dependencies import Input, Output

app = dash.Dash("Aplikace")
app.layout = html.Div(children=[
    html.Div([
        html.Label('Hello, what do you like to do in your free time?')],
        style = {
    'display': 'inline-block', 'vertical-align': 'middle',
    'textAlign': 'center', 'font-size': '1.6em', 'width':
        '40%'
    }),
    html.Div([
        "Input: ",
        dcc.Input(id='my-input', value='initial value', type='text')
    ]),
    html.Div([
        "Output: ",
        html.Div(id='my-output')

    ]),

    dcc.Dropdown(
    id='example-dropdown',
     options=[
     {'label': 'Read books', 'value': 'read'},
     {'label': 'Bake cakes', 'value': 'bake'},
    ],
    value=''
    ),

    dcc.Graph(
        id='example-plot',
        figure={
            'data': [
                go.Bar(x=[1], y=[628], name='Paperback'),
                go.Bar(x=[1], y=[796], name='Hard book')
            ],
            'layout': {
                'title': 'Book weight in grams'
            }
        }
    )
])


@app.callback(
    Output(component_id='my-output', component_property='children'),
    [Input(component_id='my-input', component_property='value')]
)

def update_output_div(input_value):
    return 'You wrote"{}"'.format(input_value)


def update_plot(choice):
    if choice == "Read books":
        data: [
            go.Bar(x=[1], y=[628], name='Paperback'),
            go.Bar(x=[1], y=[123], name='Hard book')
        ]
    else:
        data: [
            go.Bar(x=[2], y=[123], name='Paperback'),
            go.Bar(x=[1], y=[796], name='Hard book')
        ]
    return data

if __name__ == '__main__':
    app.run_server(debug=True)

