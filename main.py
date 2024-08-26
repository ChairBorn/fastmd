from fasthtml.common import *
 
app,rt = fast_app()
@rt('/')
def get_home():
    return Div(P('Hello World!'), hx_get="/change")

@rt('/change')
def get_change():
    return P('nice homie')

serve()