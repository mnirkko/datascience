# Import required libraries
import os
import pandas as pd
import dash
from dash import html
from dash import dcc
from dash.dependencies import Input, Output
import plotly.express as px

# Read the airline data into pandas dataframe
input_file = os.path.join(os.path.dirname(__file__), 'spacex_launch_dash.csv')
spacex_df = pd.read_csv(input_file, index_col='Unnamed: 0')
max_payload = spacex_df['Payload Mass (kg)'].max()
min_payload = spacex_df['Payload Mass (kg)'].min()

# Build a list of dictionaries containing launch sites (for the dropdown menu)
launch_sites = spacex_df['Launch Site'].unique()
ls_dropdown_options = [{'label': 'All Sites', 'value': 'ALL'}]
for ls in launch_sites: ls_dropdown_options.append({'label': ls, 'value': ls})

# Create a dash application
app = dash.Dash(__name__)

# Create an app layout
app.layout = html.Div(
    children = [
        html.H1('SpaceX Launch Records Dashboard',
            style={
                'textAlign': 'center',
                'color': '#503D36',
                'font-size': 40
            }
        ),

        # TASK 1: Add a dropdown list to enable Launch Site selection
        # The default select value is for ALL sites
        dcc.Dropdown(
            id          = 'site-dropdown', 
            options     = ls_dropdown_options,
            value       = 'ALL',
            placeholder = 'Select a Launch Site here',
            searchable  = True
        ),
        html.Br(),

        # TASK 2: Add a pie chart to show the total successful launches count for all sites
        # If a specific launch site was selected, show the Success vs. Failed counts for the site
        html.Div(dcc.Graph(id='success-pie-chart')),
        html.Br(),

        # TASK 3: Add a slider to select payload range
        html.P("Payload range (Kg):"),
        dcc.RangeSlider(
            id      = 'payload-slider',
            min     = 0,
            max     = 10000,
            step    = 1000,
            value   = [min_payload, max_payload]
        ),

        # TASK 4: Add a scatter chart to show the correlation between payload and launch success
        html.Div(dcc.Graph(id='success-payload-scatter-chart')),
    ]
)

# TASK 2: Add a callback function for `site-dropdown` as input, `success-pie-chart` as output
@app.callback(Output(component_id='success-pie-chart', component_property='figure'),
              Input(component_id='site-dropdown', component_property='value'))
def get_pie_chart(entered_site: str):
    if entered_site == 'ALL':
        filtered_df = spacex_df.groupby('Launch Site')['class'].count().reset_index()
        fig = px.pie(filtered_df,
                     values='class',
                     names='Launch Site',
                     title='Total successful launches by site'
                    )
        return fig
    else:
        # return the outcomes piechart for a selected site
        filtered_df = spacex_df[spacex_df['Launch Site']==entered_site]['class'].value_counts()
        fig = px.pie(filtered_df,
                     values='class',
                     names=filtered_df.index,
                     title=f'Successful launches for site {entered_site}'
                    )
        return fig

# TASK 4: Add a callback function for `site-dropdown` and `payload-slider` as inputs, `success-payload-scatter-chart` as output
@app.callback(Output(component_id='success-payload-scatter-chart', component_property='figure'),
              [Input(component_id='site-dropdown', component_property='value'),
               Input(component_id="payload-slider", component_property="value")])
def get_scatter_chart(entered_site: str, payload_range: list):
    if entered_site == 'ALL':
        fig = px.scatter(spacex_df, 
                         x='Payload Mass (kg)',
                         y='class',
                         color='Booster Version Category',
                         title='Correlation between Payload and Success for all sites'
                        )
        fig.update_xaxes(range=payload_range)
        return fig
    else:
        # return the outcomes piechart for a selected site
        filtered_df = spacex_df[spacex_df['Launch Site']==entered_site]
        fig = px.scatter(filtered_df,
                         x='Payload Mass (kg)',
                         y='class',
                         color='Booster Version Category',
                         title=f'Correlation between Payload and Success for site {entered_site}'
                        )
        fig.update_xaxes(range=payload_range)
        return fig

# Run the app
if __name__ == '__main__':
    app.run_server()
