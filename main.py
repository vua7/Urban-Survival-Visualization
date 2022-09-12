import dash
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import dash_core_components as dcc
import dash_bootstrap_components as dbc
import dash_html_components as html
from dash.dependencies import Input, Output


def main():
    crime_bar = get_crime(1)
    crime_line = get_crime(2)
    education_bar = get_education(1)
    employment_bar = get_employment(1)
    employment_line = get_employment(2)
    health_bar = get_health(1)
    housing_bar = get_housing(1)
    housing_line = get_housing(2)
    income_bar = get_income(1)
    income_line = get_income(2)
    population_bar = get_population(1)
    population_line = get_population(2)
    tax_bar = get_tax(1)

    criteria_checklist = dcc.Checklist(
        id='criteria_checklist',
        options=[
            {'label': 'Crime', 'value': 'crime'},
            {'label': 'Education', 'value': 'education'},
            {'label': 'Employment', 'value': 'employment'},
            {'label': 'Healthcare', 'value': 'healthcare'},
            {'label': 'Housing', 'value': 'housing'},
            {'label': 'Income', 'value': 'income'},
            {'label': 'Population', 'value': 'population'},
            {'label': 'Tax', 'value': 'tax'}],
        value=['crime', 'education', 'employment', 'healthcare', 'housing', 'income', 'population', 'tax'],
        labelStyle={'display': 'block'},
        style={'display': 'block'}
    )

    # checklist for provinces
    province_checklist = dcc.Checklist(
        id='province_checklist',
        options=[
            {'label': 'Alberta', 'value': 'Alberta'},
            {'label': 'British Columbia', 'value': 'British Columbia'},
            {'label': 'Manitoba', 'value': 'Manitoba'},
            {'label': 'New Brunswick', 'value': 'New Brunswick'},
            {'label': 'Newfoundland and Labrador', 'value': 'Newfoundland and Labrador'},
            {'label': 'Northwest Territories', 'value': 'Northwest Territories'},
            {'label': 'Nova Scotia', 'value': 'Nova Scotia'},
            {'label': 'Nunavut', 'value': 'Nunavut'},
            {'label': 'Ontario', 'value': 'Ontario'},
            {'label': 'Prince Edward Island', 'value': 'Prince Edward Island'},
            {'label': 'Quebec', 'value': 'Quebec'},
            {'label': 'Saskatchewan', 'value': 'Saskatchewan'},
            {'label': 'Yukon', 'value': 'Yukon'}],
        value=['Alberta', 'British Columbia', 'Manitoba', 'New Brunswick', 'Newfoundland and Labrador', 'Northwest Territories', 'Nova Scotia', 'Nunavut', 'Ontario', 'Prince Edward Island', 'Quebec', 'Saskatchewan', 'Yukon'],
        labelStyle={'display': 'block'},
        style={'display': 'block'}
    )

    # Style for every graph, (width, border, border color, etc..)
    graph_style = {'textAlign': 'center', 'color': 'black', 'border': '1px grey solid'}
    app = dash.Dash()
    app.layout = html.Div(
        [
            dbc.Row(
                [
                html.Div(html.H1('Urban Survival Visualization', style={'textAlign': 'center'}))
            ]),
            dbc.Row(
                [
                    html.Div([criteria_checklist], style={'display': 'inline-block', 'width': '25%', 'verticalAlign': 'top'}),
                    html.Div([dcc.Graph(id='crime_bar', figure=crime_bar, style=graph_style)], style={'width': '25%', 'display': 'inline-block'}),
                    html.Div([dcc.Graph(id='crime_line', figure=crime_line, style=graph_style)], style={'width': '25%', 'display': 'inline-block'}),
                    html.Div([dcc.Graph(id='education_bar', figure=education_bar, style=graph_style)], style={'width': '25%', 'display': 'inline-block'}),
                ]
            ),
            dbc.Row(
                [
                    html.Div([province_checklist], style={'display': 'inline-block', 'width': '25%', 'verticalAlign': 'top'}),
                    html.Div([dcc.Graph(id='employment_bar', figure=employment_bar, style=graph_style)], style={'width': '25%', 'display': 'inline-block'}),
                    html.Div([dcc.Graph(id='employment_line', figure=employment_line, style=graph_style)], style={'width': '25%', 'display': 'inline-block'}),
                    html.Div([dcc.Graph(id='health_bar', figure=health_bar, style=graph_style)], style={'width': '25%', 'display': 'inline-block'}),
                ]
            ),
            dbc.Row(
                [
                    html.Div([dcc.Graph(id='housing_bar', figure=housing_bar, style=graph_style)], style={'width': '25%', 'display': 'inline-block'}),
                    html.Div([dcc.Graph(id='housing_line', figure=housing_line, style=graph_style)], style={'width': '25%', 'display': 'inline-block'}),
                    html.Div([dcc.Graph(id='income_bar', figure=income_bar, style=graph_style)], style={'width': '25%', 'display': 'inline-block'}),
                    html.Div([dcc.Graph(id='income_line', figure=income_line, style=graph_style)], style={'width': '25%', 'display': 'inline-block'}),
                ]
            ),
            dbc.Row(
                [
                    html.Div([dcc.Graph(id='population_bar', figure=population_bar, style=graph_style)], style={'width': '25%', 'display': 'inline-block'}),
                    html.Div([dcc.Graph(id='population_line', figure=population_line, style=graph_style)], style={'width': '25%', 'display': 'inline-block'}),
                    html.Div([dcc.Graph(id='tax_bar', figure=tax_bar, style=graph_style)], style={'width': '25%', 'display': 'inline-block'})
                ]
            )
        ])

    #------ SHOW/HIDE BY CRITERIA ------#
    # show/hide crime_bar
    @app.callback(
        Output(component_id='crime_bar', component_property='style'),
        [Input(component_id='criteria_checklist', component_property='value')]
    )
    def hide_graph(criteria):
        if 'crime' in criteria:
            return graph_style
        else:
            return {'display': 'none'}

    # show/hide crime_line
    @app.callback(
        Output(component_id='crime_line', component_property='style'),
        [Input(component_id='criteria_checklist', component_property='value')]
    )
    def hide_graph(criteria):
        if 'crime' in criteria:
            return graph_style
        else:
            return {'display': 'none'}

        # ------ Show/hide education viz ------
        # show/hide education_bar

    @app.callback(
        Output(component_id='education_bar', component_property='style'),
        [Input(component_id='criteria_checklist', component_property='value')]
    )
    def hide_graph(criteria):
        if 'education' in criteria:
            return graph_style
        else:
            return {'display': 'none'}

    # ------ Show/hide employment viz ------
    # show/hide education_bar
    @app.callback(
        Output(component_id='employment_bar', component_property='style'),
        [Input(component_id='criteria_checklist', component_property='value')]
    )
    def hide_graph(criteria):
        if 'employment' in criteria:
            return graph_style
        else:
            return {'display': 'none'}

    # ------ Show/hide Education ---------
    # show/hide education_line
    @app.callback(
        Output(component_id='employment_line', component_property='style'),
        [Input(component_id='criteria_checklist', component_property='value')]
    )
    def hide_graph(criteria):
        if 'employment' in criteria:
            return graph_style
        else:
            return {'display': 'none'}

    # ----- Show/hide health -------
    # show/hide health_bar
    @app.callback(
        Output(component_id='health_bar', component_property='style'),
        [Input(component_id='criteria_checklist', component_property='value')]
    )
    def hide_graph(criteria):
        if 'healthcare' in criteria:
            return graph_style
        else:
            return {'display': 'none'}

    # ----- Show/hide housing -----
    # show/hide housing_line
    @app.callback(
        Output(component_id='housing_line', component_property='style'),
        [Input(component_id='criteria_checklist', component_property='value')]
    )
    def hide_graph(criteria):
        if 'housing' in criteria:
            return graph_style
        else:
            return {'display': 'none'}

    # show/hide housing_bar
    @app.callback(
        Output(component_id='housing_bar', component_property='style'),
        [Input(component_id='criteria_checklist', component_property='value')]
    )
    def hide_graph(criteria):
        if 'housing' in criteria:
            return graph_style
        else:
            return {'display': 'none'}

    # ------ Show/hide Income -----
    # show/hide income_bar
    @app.callback(
        Output(component_id='income_bar', component_property='style'),
        [Input(component_id='criteria_checklist', component_property='value')]
    )
    def hide_graph(criteria):
        if 'income' in criteria:
            return graph_style
        else:
            return {'display': 'none'}

    # show/hide income_line
    @app.callback(
        Output(component_id='income_line', component_property='style'),
        [Input(component_id='criteria_checklist', component_property='value')]
    )
    def hide_graph(criteria):
        if 'income' in criteria:
            return graph_style
        else:
            return {'display': 'none'}

    # show/hide population bar
    @app.callback(
        Output(component_id='population_bar', component_property='style'),
        [Input(component_id='criteria_checklist', component_property='value')]
    )
    def hide_graph(criteria):
        if 'population' in criteria:
            return graph_style
        else:
            return {'display': 'none'}

    # show/hide population line
    @app.callback(
        Output(component_id='population_line', component_property='style'),
        [Input(component_id='criteria_checklist', component_property='value')]
    )
    def hide_graph(criteria):
        if 'population' in criteria:
            return graph_style
        else:
            return {'display': 'none'}

    # show/hide tax bar
    @app.callback(
        Output(component_id='tax_bar', component_property='style'),
        [Input(component_id='criteria_checklist', component_property='value')]
    )
    def hide_graph(criteria):
        if 'tax' in criteria:
            return graph_style
        else:
            return {'display': 'none'}

    #------ SHOW/HIDE BY PROVINCE ------#

    @app.callback(
        Output(component_id='crime_bar', component_property='figure'),
        [Input(component_id='province_checklist', component_property='value')]
    )
    def edit_graph(province):
        crime_bar = get_crime(1, province)
        return crime_bar

    @app.callback(
        Output(component_id='crime_line', component_property='figure'),
        [Input(component_id='province_checklist', component_property='value')]
    )
    def edit_graph(province):
        crime_line = get_crime(2, province)
        return crime_line

    @app.callback(
        Output(component_id='education_bar', component_property='figure'),
        [Input(component_id='province_checklist', component_property='value')]
    )
    def edit_graph(province):
        education_bar = get_education(1, province)
        return education_bar

    @app.callback(
        Output(component_id='employment_bar', component_property='figure'),
        [Input(component_id='province_checklist', component_property='value')]
    )
    def edit_graph(province):
        employment_bar = get_employment(1, province)
        return employment_bar

    @app.callback(
        Output(component_id='employment_line', component_property='figure'),
        [Input(component_id='province_checklist', component_property='value')]
    )
    def edit_graph(province):
        employment_line = get_employment(2, province)
        return employment_line

    @app.callback(
        Output(component_id='health_bar', component_property='figure'),
        [Input(component_id='province_checklist', component_property='value')]
    )
    def edit_graph(province):
        health_bar = get_health(1, province)
        return health_bar

    @app.callback(
        Output(component_id='housing_bar', component_property='figure'),
        [Input(component_id='province_checklist', component_property='value')]
    )
    def edit_graph(province):
        housing_bar = get_housing(1, province)
        return housing_bar

    @app.callback(
        Output(component_id='housing_line', component_property='figure'),
        [Input(component_id='province_checklist', component_property='value')]
    )
    def edit_graph(province):
        housing_line = get_housing(2, province)
        return housing_line

    @app.callback(
        Output(component_id='income_bar', component_property='figure'),
        [Input(component_id='province_checklist', component_property='value')]
    )
    def edit_graph(province):
        income_bar = get_income(1, province)
        return income_bar

    @app.callback(
        Output(component_id='income_line', component_property='figure'),
        [Input(component_id='province_checklist', component_property='value')]
    )
    def edit_graph(province):
        income_line = get_income(2, province)
        return income_line

    @app.callback(
        Output(component_id='population_bar', component_property='figure'),
        [Input(component_id='province_checklist', component_property='value')]
    )
    def edit_graph(province):
        population_bar = get_population(1, province)
        return population_bar

    @app.callback(
        Output(component_id='population_line', component_property='figure'),
        [Input(component_id='province_checklist', component_property='value')]
    )
    def edit_graph(province):
        population_line = get_population(2, province)
        return population_line

    @app.callback(
        Output(component_id='tax_bar', component_property='figure'),
        [Input(component_id='province_checklist', component_property='value')]
    )
    def edit_graph(province):
        tax_bar = get_tax(1, province)
        return tax_bar

    app.run_server()
    return

def get_province():
    population = pd.read_csv('venv/Datasets/Population.csv')
    provinces = population['Geography']  # save provinces subset
    population = population.drop(columns=['Geography']).apply(lambda x: x.str.replace(',', '')).astype(int).join(provinces)
    populations = pd.Series(population['2021'].values, index=population['Geography']).to_dict()
    return populations

def get_crime(view, province=None):
    crime = pd.read_csv('venv/Datasets/Crime.csv')
    provinces = crime['Province']
    crime = crime.drop(columns=['Province']).apply(lambda x: x.str.replace(',', '')).astype(int).join(provinces)

    if province != None:
        crime = crime.query("Province == @province")

    if view == 1:
        crime = crime[['Province', '2018']]
        # crime.set_index('Province')
        populations = get_province()
        crime['Population'] = crime['Province'].map(populations)
        crime['Normalized'] = crime['2018'] / crime['Population'] * 1000
        crime_bar = px.bar(crime, x=crime['Normalized'], y=crime['Province'], title="Crimes Per Province (2018)", template='simple_white', labels={"Normalized": "Crimes (Per 1000 People)"})
        crime_bar.update_layout(showlegend=False, yaxis={'categoryorder': 'total ascending'}, title_x=0.5)
        crime_bar.update_xaxes(linecolor='lightgrey')
        crime_bar.update_yaxes(linecolor='lightgrey')
        return crime_bar

    elif view == 2:
            crime_line = px.line(crime.set_index('Province').T, title="Crimes Per Province", template='simple_white')
            crime_line.update_layout(showlegend=True, title_x=0.5)
            crime_line.update_xaxes(dtick=4, title="Year", linecolor='lightgrey')
            crime_line.update_yaxes(title="Crimes", linecolor='lightgrey')
            return crime_line


def get_education(view, province=None):
    education = pd.read_csv('venv/Datasets/Education.csv')
    education = education.rename(columns={"GEO": "Province", "VALUE": "Graduates"})

    if province != None:
        education = education.query("Province == @province")

    if view == 1:
        populations = get_province()
        education['Population'] = education['Province'].map(populations)
        education['Normalized'] = education['REF_DATE'] / education['Population'] * 1000
        education_bar = px.bar(education, y='Province', x='Normalized', title="Number of Graduates per Province (2015)", template='simple_white')
        education_bar.update_xaxes(title="Graduates (Per 1000 People)", linecolor='lightgrey')
        education_bar.update_yaxes(linecolor='lightgrey')
        education_bar.update_layout(showlegend=False, yaxis={'categoryorder': 'total ascending'}, title_x=0.5)
        return education_bar

    elif view == 2:
        education_table = go.Figure(data=[go.Table(
            header=dict(values=["Province", "Graduates"]),
            cells=dict(values=[education.Province, education.Graduates]))])
        return education_table

def get_employment(view, province=None):
    employment = pd.read_csv('venv/Datasets/Employment.csv')

    if province != None:
        employment = employment.query("Province == @province")

    if view == 1:
        employment_bar = px.bar(employment, y='Province', x='2021', title='Employment Rate (2021)', template='simple_white')
        employment_bar.update_xaxes(title='Employment Rate (%)', linecolor='lightgrey')
        employment_bar.update_yaxes(title='Province', linecolor='lightgrey')
        employment_bar.update_layout(showlegend=False, yaxis={'categoryorder': 'total ascending'}, title_x=0.5)
        return employment_bar

    elif view == 2:
        employment_line = px.line(employment.set_index('Province').T, title='Employment Rate', template='simple_white')
        employment_line.update_layout(showlegend=True, title_x=0.5)
        employment_line.update_xaxes(dtick=5, title='Year', linecolor='lightgrey')
        employment_line.update_yaxes(title='Employment Rate (%)', linecolor='lightgrey')
        return employment_line

def get_health(view, province=None):
    health = pd.read_csv('venv/Datasets/Health.csv')
    health_data = health.groupby('province').count().reset_index()
    health_data = health_data[['province', 'facility_name']]

    if province != None:
        health_data = health_data.query("province == @province")

    if view == 1:
        populations = get_province()
        health_data['Population'] = health_data['province'].map(populations)
        health_data['Normalized'] = health_data['facility_name'] / health_data['Population'] * 1000
        health_bar = px.bar(health_data, y='province', x='Normalized', title="Healthcare Facilities Per Province", labels={"province": "Province"}, template='simple_white')
        health_bar.update_yaxes(title="Provinces", linecolor='lightgrey')
        health_bar.update_xaxes(title="Healthcare Facilities (Per 1000 People)", linecolor='lightgrey')
        health_bar.update_layout(showlegend=False, yaxis={'categoryorder': 'total ascending'}, title_x=0.5)
        return health_bar

    elif view == 2:
        health_table = go.Figure(data=[go.Table(
            header=dict(values=["Province", "Number of Facilities"]),
            cells=dict(values=[health_data.province, health_data.facility_name]))])
        return health_table

def get_housing(view, province=None):
    housing = pd.read_csv('venv/Datasets/Housing.csv')
    housing = housing.query('GEO != "Canada"')

    if province != None:
        housing = housing.query("GEO == @province")

    if view == 1:
        housing = housing.query('REF_DATE == "2021-01"')  # take only latest january values
        housing_bar = px.bar(housing, y='GEO', x='VALUE',
                             title="Housing Value by Province (2021)",
                             labels={"GEO": "Province", "VALUE": "Housing Price Index"},
                             template='simple_white')
        housing_bar.update_layout(showlegend=False, yaxis={'categoryorder': 'total ascending'}, title_x=0.5)
        housing_bar.update_xaxes(linecolor='lightgrey')
        housing_bar.update_yaxes(linecolor='lightgrey')
        return housing_bar

    elif view == 2:
        housing = housing.query('REF_DATE.str.contains("-01")')  # take february value for each year
        housing_line = px.line(housing, x='REF_DATE', y='VALUE', color="GEO",
                               title="Housing Value by Province Per Year",
                               labels={"REF_DATE": "Year", "VALUE": "New Housing Price Index Values",
                                       "GEO": "Province"},
                               template='simple_white')
        housing_line.update_layout(showlegend=True, xaxis={'categoryorder': 'total descending'}, title_x=0.5)
        housing_line.update_xaxes(linecolor='lightgrey')
        housing_line.update_yaxes(linecolor='lightgrey')
        return housing_line

def get_income(view, province=None):
    income = pd.read_csv('venv/Datasets/Income.csv')

    if province != None:
        income = income.query("Province == @province")

    if view == 1:
        income = pd.melt(income, id_vars=['Province'], value_vars=['2017'],
                         var_name='Year', value_name='Income')
        income_bar = px.bar(income, y='Province', x='Income', template='simple_white')  # STACKED?? OR GROUPED?
        income_bar.update_layout(showlegend=False, title="Median Income Per Province", yaxis={'categoryorder': 'total ascending'}, title_x=0.5)
        income_bar.update_xaxes(linecolor='lightgrey')
        income_bar.update_yaxes(linecolor='lightgrey')
        return income_bar

    elif view == 2:
        income_line = px.line(income.set_index('Province').T, title="Median Income Per Province",
                              template='simple_white')
        income_line.update_layout(showlegend=True, title_x=0.5)
        income_line.update_xaxes(dtick=2, title="Year", linecolor='lightgrey')
        income_line.update_yaxes(title="Income", linecolor='lightgrey')
        return income_line

def get_population(view, province=None):
    population = pd.read_csv('venv/Datasets/Population.csv')
    provinces = population['Geography']  # save provinces subset
    population = population.drop(columns=['Geography']).apply(lambda x: x.str.replace(',', '')).astype(int).join(provinces)

    if province != None:
        population = population.query("Geography == @province")

    if view == 1:
        population = population[["Geography", "2021"]]  # take latest values
        population_bar = px.bar(population, y='Geography', x='2021',
                             title="Population by Province (2021)",
                             labels={"2021": "Population", "Geography": "Province"},
                             template='simple_white',
                             )
        population_bar.update_layout(showlegend=False, yaxis={'categoryorder': 'total ascending'}, title_x=0.5)
        population_bar.update_xaxes(title='Population', linecolor='lightgrey')
        population_bar.update_yaxes(linecolor='lightgrey')
        return population_bar

    elif view == 2:
        population_line = px.line(population.set_index('Geography').T, title="Population Per Province",
                                  labels={"Geography": "Province"}, template='simple_white')
        population_line.update_layout(showlegend=True, title_x=0.5)
        population_line.update_xaxes(dtick=5, title="Year", linecolor='lightgrey')
        population_line.update_yaxes(title="Population", linecolor='lightgrey')
        return population_line

def get_tax(view, province=None):
    tax = pd.read_csv('venv/Datasets/Tax.csv')

    if province != None:
        tax = tax.query("Province == @province")

    if view == 1:
        tax_bar = px.bar(tax, y='Province', x='Total (%)', title="Sales Tax by Province", template='simple_white')
        tax_bar.update_layout(showlegend=False, yaxis={'categoryorder': 'total ascending'}, title_x=0.5)
        tax_bar.update_xaxes(linecolor='lightgrey')
        tax_bar.update_yaxes(linecolor='lightgrey')
        return tax_bar

    elif view == 2:
        tax_line = px.scatter(tax, x='Province', y='Total (%)', title="Sales Tax by Province", template='simple_white')
        tax_line.update_layout(showlegend=False, xaxis={'categoryorder': 'total descending'}, title_x=0.5)
        tax_line.update_xaxes(tickangle=45, linecolor='lightgrey')
        tax_line.update_yaxes(linecolor='lightgrey')
        return tax_line

if __name__ == '__main__':
    main()
