import dash_html_components as html



homeLayout = dict(
    width= '100%',
    height = '500px',
    display = 'flex',
    flexDirection = 'column',
    justifyContent = 'center',
    alignItems = 'center'
)


layout = html.Div([
    html.H1('Welcome to our dash!'),
    html.H3('This is an easy way to do stats')
], style= homeLayout)
