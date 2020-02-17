from colorScheme import color

### css styles
style_graph_grid = dict(
    backgroundColor = color['background'],
    display = 'flex',
    flexDirection = 'row',
    alignItems = 'space-evenly',
    justifyContent = 'space-evenly', 
    width = '100%',   
    margin = '20px' 
)


style_line = dict(
    borderColor = color['trim']
)

style_layout = dict(
    backgroundColor = color['background'],
    color = color['text'],
    display = 'flex',
    flexDirection = 'column',
    alignItems = 'center',
    justifyContent = 'center'
)

style_button = dict(
    borderColor = color['trim'],
    color = color['trim']
)

style_input = dict(
    display = 'flex',
    flexDirection = 'column',
    alignItems = 'center'
)
