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
    html.H1('Welcome to kheagans dash'),
    html.H3('An easy way to do stats. Not tested.')
], style= homeLayout)
