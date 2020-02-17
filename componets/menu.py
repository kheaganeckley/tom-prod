import dash_core_components as dcc
import dash_html_components as html
from colorScheme import color


MenuStyle = dict(
    width = '100%',
    height = '50px',
    display = 'flex',
    flexDirection = 'row',
    backgroundColor = color['trim'],
)



MenuBox =  dict(
         flex = '30%',
         height = '100%',
         width = '100%',
         display = 'flex',
         justifyContent = 'center',
         alignItems = 'center'
       )


MenuBox2=  dict(
         flex = '70%',
         height = '100%',
         width = '100%',
         display = 'flex',
         justifyContent = ' flex-start',
         alignItems = 'center'
       )

TitleText = dict(
  fontSize= '30px',
  color = 'white',
  textDecoration = 'none'
)

LinkStyle = dict(
    margin = '5px',
    marginRight = '40px',
    textDecoration = 'none',
    color = 'white',
)


def menu(MenuArray):
   return html.Div([
     html.Div(
       dcc.Link(id = 'titletag', children = "Thompson's dash", href='/', style=TitleText),
       style=MenuBox
     ),
     html.Div(
       [dcc.Link(id= item['link'], children = item['name'], href = item['link'], style = LinkStyle) for item in MenuArray],
       style= MenuBox2
     )
   ],
   style = MenuStyle)
    
    