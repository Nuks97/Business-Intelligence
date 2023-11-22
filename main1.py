import dash
import dash_core_components as dcc
from dash import html
import plotly.express as px
import pandas as pd
import pyodbc

# Establish database connection
conn = pyodbc.connect("Driver={SQL Server};"
                      "Server=L417\SQLEXPRESS;"
                      "Database=DWAdventureWorks;"
                      "Trusted_Connection=yes;")

# Retrieve data from database
sql_query = """
SELECT [EmployeeID],
       [Jobtitle],
       [AgeOfEmployee],
       [MaritalStatus],
       [Gender],
       [SickLeaveHours],
       [VacationHours]
FROM [DWAdventureWorks].[dbo].[Employee_Dim]
"""
df = pd.read_sql(sql_query, conn)

# Create scatter plot using Plotly Express
fig = px.scatter(df, x="AgeOfEmployee", y="VacationHours",
                 color="Gender", size="SickLeaveHours",
                 hover_data=["EmployeeID", "Jobtitle", "MaritalStatus"],
                 title="Employee Data")

# Set the layout for the plot
fig.update_layout(title_x=0.5)

# Create the Dash app
app = dash.Dash(__name__)

# Define the layout for the app
app.layout = html.Div([
    html.H1("Employee Data Dashboard"),
    
    # Add a dropdown menu to filter the data by gender
    dcc.Dropdown(
        id="gender-dropdown",
      

        options=[
            {"label": "All", "value": "all"},
            {"label": "Male", "value": "male"},
            {"label": "Female", "value": "female"}
        ],
        value="all"
    ),
    
    # Add the scatter plot
    dcc.Graph(id="employee-plot", figure=fig)
])

# Define the callback to filter the data by gender
@app.callback(
    dash.dependencies.Output("employee-plot", "figure"),
    [dash.dependencies.Input("gender-dropdown", "value")]
)
def update_plot(gender):
    if gender == "all":
        filtered_df = df
    else:
        filtered_df = df[df["Gender"] == gender]
    
    updated_fig = px.scatter(filtered_df, x="AgeOfEmployee", y="VacationHours",
                             color="Gender", size="SickLeaveHours",
                             hover_data=["EmployeeID", "Jobtitle", "MaritalStatus"],
                             title="Employee Data")
    
    updated_fig.update_layout(title_x=0.5)
    
    return updated_fig



# Run the app
if __name__ == "__main__":
    app.run_server(debug=True)




