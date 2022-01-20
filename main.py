import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
from app.ui import (
    header,
    contact_modal,
)
from app import tab_map, tab_stats, tab_compare
from dash import State
from config import strings, constants
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
import plotly.io as plt_io

from dash_extensions import Lottie       # pip install dash-extensions
import plotly.express as px              # pip install plotly                    # pip install pandas
from datetime import date
import calendar
import numpy as np
import plotly.graph_objects as go
import textwrap
import dash_daq as daq
from dash_bootstrap_templates import ThemeSwitchAIO
from pandas import read_excel
from plotly.subplots import make_subplots




url_theme1 = dbc.themes.FLATLY
url_theme2 = dbc.themes.DARKLY

plt_io.templates["custom_light"] = plt_io.templates["plotly_dark"]

# set the paper_bgcolor and the plot_bgcolor to a new color
plt_io.templates["custom_light"]['layout']['paper_bgcolor'] = '#303030'
plt_io.templates["custom_light"]['layout']['plot_bgcolor'] = '#303030'

# you may also want to change gridline colors if you are modifying background
plt_io.templates['custom_light']['layout']['yaxis']['gridcolor'] = '#4f687d'
plt_io.templates['custom_light']['layout']['xaxis']['gridcolor']  = '#4f687d'


plt_io.templates["custom_dark"] = plt_io.templates["plotly"]

# set the paper_bgcolor and the plot_bgcolor to a new color
plt_io.templates["custom_dark"]['layout']['paper_bgcolor'] = '#E7E7E7'
plt_io.templates["custom_dark"]['layout']['plot_bgcolor'] = '#E7E7E7'

# you may also want to change gridline colors if you are modifying background
plt_io.templates['custom_dark']['layout']['yaxis']['gridcolor'] = '#4f687d'
plt_io.templates['custom_dark']['layout']['xaxis']['gridcolor']  = '#4f687d'

custom_light = "custom_light"
custom_dark = "custom_dark"



# Lottie by Emil - https://github.com/thedirtyfew/dash-extensions
url_application = "https://assets2.lottiefiles.com/packages/lf20_tgj5soqx.json"
url_intake = "https://assets6.lottiefiles.com/private_files/lf30_aQeqzz.json"
url_respondent = "https://assets7.lottiefiles.com/packages/lf20_uky0mc6u.json"
url_coonections = "https://assets3.lottiefiles.com/packages/lf20_DMgKk1.json"
url_companies = "https://assets9.lottiefiles.com/packages/lf20_EzPrWM.json"
url_msg_in = "https://assets9.lottiefiles.com/packages/lf20_8wREpI.json"
url_student = "https://assets3.lottiefiles.com/private_files/lf30_cyQ8b1.json"
url_reactions = "https://assets2.lottiefiles.com/packages/lf20_nKwET0.json"
options = dict(loop=True, autoplay=True, rendererSettings=dict(preserveAspectRatio='xMidYMid slice'))

# Import App data from csv sheets **************************************
df = pd.read_csv("All.csv")


# EXTERNAL SCRIPTS AND STYLES
external_scripts = ["https://kit.fontawesome.com/0bb0d79500.js"]
external_stylesheets = [
    "https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css"
]

app = dash.Dash(
    __name__,
    meta_tags=[{"name": "viewport", "content": "width=device-width, initial-scale=1"}],
    external_scripts=external_scripts,
    external_stylesheets=external_stylesheets,
)
app.title = strings.APP_NAME
app.config["suppress_callback_exceptions"] = True
server = app.server

#STYLE
CONTENT_STYLE = {
    'margin-left': '23%',
    'margin-right': '5%',
    'padding': '20px 10p'
}

HIDE_STYLE = {
    'display': 'none',
}
SHOW_STYLE = {
    'display': 'show',
}

SIDEBAR_STYLE = {
    'position': 'fixed',
    'margin-left': '1%',
    'background-color':'#2a2b30',
    'margin-top': '10%',
    'color': '#FFFFFF',
    'box-shadow':'6px 0px 6px 0px rgba(0,0,0,0.95)'
}

MODE_STYLE = {
    'position': 'fixed',
    'margin-left': '1%',
    'background-color':'#2a2b30',
    'color': '#FFFFFF',
    'box-shadow':'6px 0px 6px 0px rgba(0,0,0,0.95)',
}

YEAR_STYLE = {
    'position': 'fixed',
    'margin-left': '1%',
    'background-color':'#2a2b30',
    'color': '#FFFFFF',
    'margin-top': '28%',
    'box-shadow':'6px 0px 6px 0px rgba(0,0,0,0.95)',
}

lightstyle = {  'textAlign':'center',
               'background-color': '#E7E7E7', 
               'border-radius': '20px','color': '#000000',
               }
               
darkstyle = {  'textAlign':'center',
               'background-color': '#303030', 
               'border-radius': '20px','color': '#FFFFFF',
               } 
               

lightgraph= {  'border-radius': '20px','background-color': '#E7E7E7', 'margin': '1px','height': '91.9%'
               }
               
darkgraph = {  'border-radius': '20px','background-color': '#303030', 'margin': '1px','height': '91.9%'
               }    

lightgraph2= {  'border-radius': '20px','background-color': '#E7E7E7', 'margin': '1px','height': '96%'
               }
               
darkgraph2 = {  'border-radius': '20px','background-color': '#303030', 'margin': '1px','height': '96%'
               }   
lightgraph3= {   'border-radius': '20px','background-color': '#E7E7E7', 'margin': '1px','height': '97%','float': 'left'
               }
               
darkgraph3 = {  'border-radius': '20px','background-color': '#303030', 'margin': '1px','height': '97%','float': 'left'
               }  
lighthome= {  'border-radius': '20px','background-color': '#E7E7E7', 'margin': '1px','height': '80%'
               }
               
darkhome = {  'border-radius': '20px','background-color': '#303030', 'margin': '1px','height': '80%'
               } 
modallight = {  
               'background-color': '#E7E7E7', 
               
               }
               
modaldark = {  
               'background-color': '#303030', 
              
               }                



# CONTENT LAYOUT
content_first_row = dbc.Row([
dbc.Col([
      
            dbc.Card([
             
                Lottie(options=options, width="13%", height="13%", url=url_coonections)
                ,
                dbc.CardBody([
                    html.H6('Total Program'),
                    html.H3(id='content-connections', children="000")
                ], )
            ], id="card1",style=lightstyle),
        ], width=4),
        dbc.Col([
            dbc.Card([
               Lottie(options=options, width="13%", height="13%", url=url_student)
                ,
                dbc.CardBody([
                    html.H6('Total Admission'),
                    html.H3(id='content-companies', children="000")
                ],)
            ], id="card2",style=lightstyle),
        ], width=4),
         dbc.Col([
            dbc.Card([
                Lottie(options=options, width="17%", height="17%", url=url_companies)
                ,
                dbc.CardBody([
                    html.H6('Total Department'),
                    html.H3(id='content-department', children="000")
                ],)
            ], id="card3",style=lightstyle),
        ] , width=4 ),
        
        
    
        
], )


content_second_row = dbc.Row(
    [
   
    
           dbc.Col([
      
                 dbc.Card([
                  
                dbc.CardBody([
                    html.Img(id="open-dismiss",src=app.get_asset_url('full.png'), style={'height':'4%', 'width':'5%'}),
                    dcc.Graph(id='graph_5', figure={}), 
                    
                ],)
            ],id='cardgraph_5',style=lightgraph),

        ], width=5),
        
       dbc.Col([
       
       
             dbc.Card([
                dbc.CardBody([
                 html.Img(id="open-dismiss1",src=app.get_asset_url('full.png'), style={'height':'4%', 'width':'4%'}),
                 dcc.Graph(id='graph_3', figure={}), 
                ],)
            ],id='cardgraph_3',style=lightgraph2),
      
           
        ], className='mb-4', width=7),
    ]
)


content_third_row = dbc.Row(
    [
    
     dbc.Col([
     
              dbc.Card([
                dbc.CardBody([
               
                     dbc.Row(
               [
                dbc.Col(
                  [
                   html.Img(id="open-dismiss2",src=app.get_asset_url('full.png'), style={'height':'50%', 'width':'150%'}),
                  ],width=1
                 ),
                  dbc.Col(
                  [
                 dcc.Dropdown(id='dprtmn', options=[],value=['SCIENCE,  MATHEMATICS AND  COMPUTING'], multi=True,
                 style={'width':'100%', 'font-size' : '90%','color': '#000000','display': 'inline-block'}),   
                  ],width=11
                 )    
               ]
             ),
                
                
                
                   dcc.Graph(id='graph_6', figure={}), 
                ],)
            ],id='cardgraph_6',style=lightgraph2),
           
               
                   
                   
                     
              
           
        ], width=5),
    
           dbc.Col([
      
                dbc.Card([
                dbc.CardBody([
                html.Img(id="open-dismiss3",src=app.get_asset_url('full.png'), style={'height':'4%', 'width':'4%'}),
                  dcc.Graph(id='graph_4', figure={}),
                ],)
            ],id='cardgraph_4',style=lightgraph2),
                   
                    
                     
              
    
        ], width=7),
    ] , className='mb-4'
)


content_fifth_row = dbc.Row(
    [
       
          dbc.Col([
           
       dbc.Card([
                dbc.CardBody([
                
            dbc.Row(
               [
                dbc.Col(
                  [
                   html.Img(id="open-dismiss4",src=app.get_asset_url('full.png'), style={'display': 'inline-block','height':'60%', 'width':'10%'}),
                  ],width=3
                 ),
                  dbc.Col(
                  [
                 dcc.Dropdown(id='category', options=[],value=['Computer science'], multi=True,
                 style={'width':'100%', 'font-size' : '90%','color': '#000000','display': 'inline-block'}),   
                  ],width=7
                 )    
               ]
             ),
               
                  dcc.Graph(id='graph_7', figure={}), 
                ],)
            ],id='cardgraph_7',style=lightgraph3),
                  
           
        ], width=12),
      
    ] 
)



controls = html.Div([

    dbc.Row(
         [

         ],id="rowlevel" ,style={'z-index':1}  
    ),
      html.Br(),
        dbc.Row(
         [
        dbc.Label("Select University"),
             html.Br(),
            dcc.Dropdown(
                    id='jantina', 
                    clearable=False,
                     value="Universiti Teknologi MARA",
                     style={'width':'100%', 'font-size' : '90%','color': '#000000','z-index': 1},
                       options=[]
                       ),
           
         ],style={'z-index':1} 
    ),
    
    html.Br(),
    
     dbc.Row(
         [
      
           
         ],id='rowyear',style={'z-index':1} 
    ),

    
   
] ,className='box',  style=SIDEBAR_STYLE)

side = html.Div([

    dbc.Row(
        [
            dbc.Col(
                [
                    dbc.Label("Light/Dark Mode"),
                    ThemeSwitchAIO(aio_id="theme", themes=[url_theme1, url_theme2],),
                   
                ]
            )
        ],style={'z-index':-1}
    ),

   
   
] ,className='box',  style=MODE_STYLE)


yearside = dbc.Row(
        [
            dbc.Col(
                [
                     dbc.Label("Select Year"),
                        html.Br(),
                    dcc.Dropdown(id='tahun',  clearable=False,value='2020', options=[],
                    style={'width':'100%', 'font-size' : '90%','color': '#000000','display': 'inline-block'}),   
                   
                ]
            )
        ],style={'z-index':-1}
    )
    
levelhome = dbc.Row(
        [
            dbc.Col(
                [
                      dbc.Label("Select Education Level"),
                    html.Br(),
                dbc.RadioItems(
                id="level",
                options=[{"label": i, "value": i} for i in sorted(df.LEVEL.unique())],
                value="DEGREE",
            ), 
                   
                ]
            )
        ],style={'z-index':-1}
    )    
       




content = html.Div(
    [
        
        content_first_row,
        content_second_row,
        content_third_row,
        content_fifth_row
    ],
    style=CONTENT_STYLE,
    
)
modal = html.Div(
    [
        dbc.Modal(
            [
             
                dbc.ModalBody(
                   dcc.Graph(id='graph_99', figure={},),
                                     
                ),  
                dbc.ModalFooter(dbc.Button("Close", id="close-dismiss")),
            ],
            
            id="modal-dismiss",
            keyboard=False,
            size="xl",
            backdrop="static",
        ),
          dbc.Modal(
            [
              
                dbc.ModalBody(
                   dcc.Graph(id='graph_91', figure={},), 
                ),
                dbc.ModalFooter(dbc.Button("Close", id="close-dismiss1")),
            ],
            
            id="modal-dismiss1",
            keyboard=False,
            size="xl",
            backdrop="static",
        ),
          dbc.Modal(
            [
             
                dbc.ModalBody(
                   dcc.Graph(id='graph_92', figure={},), 
                ),
                dbc.ModalFooter(dbc.Button("Close", id="close-dismiss2")),
            ],
            
            id="modal-dismiss2",
            keyboard=False,
            size="xl",
            backdrop="static",
        ),
          dbc.Modal(
            [
             
                dbc.ModalBody(
                   dcc.Graph(id='graph_93', figure={},), 
                ),
                dbc.ModalFooter(dbc.Button("Close", id="close-dismiss3")),
            ],
            
            id="modal-dismiss3",
            keyboard=False,
            size="xl",
            backdrop="static",
        ),
          dbc.Modal(
            [
             
                dbc.ModalBody(
              
                 
                dcc.Graph(id='graph_971', figure={},), 
                   
                ),
                dbc.ModalFooter(dbc.Button("Close", id="close-dismiss4")),
                
            ],
            
            id="modal-dismiss4",
            keyboard=False,
            size="xl",
            backdrop="static",
        ),
    ],
)



# HOME LAYOUT *****************************************************


home_second_row = dbc.Row(
    [
    
    
   
    
           dbc.Col([
      
                 dbc.Card([
                  
                dbc.CardBody([
                
                 html.Img(id="home-dismiss",src=app.get_asset_url('full.png'), style={'height':'4%', 'width':'5%'}),

                   
                    dcc.Graph(id='home_5', figure={}), 
                    
                ],)
            ],id='cardhome_51',style=lighthome),

        ], className='mb-4', width=5),
        
       dbc.Col([
       
       
             dbc.Card([
                dbc.CardBody([
                 html.Img(id="home-dismiss1",src=app.get_asset_url('full.png'), style={'height':'4%', 'width':'4%'}),
                 dcc.Graph(id='home_3', figure={}), 
                ],)
            ],id='cardhome_3',style=lightgraph2),
      
           
        ], className='mb-4', width=7),
    ]
)

home_first_row = dbc.Row([
dbc.Col([
            dbc.Card([
                Lottie(options=options, width="13%", height="13%", url=url_application)
                ,
                dbc.CardBody([
                    html.H6('Total Application'),
                    html.H3(id='home-connections', children="000")
                ], )
            ],id='homecard',style=lightstyle),
        ], width=4),
        dbc.Col([
            dbc.Card([
               Lottie(options=options, width="13%", height="13%", url=url_intake)
                ,
                dbc.CardBody([
                    html.H6('Total Intake'),
                    html.H3(id='home-companies', children="000")
                ],)
            ],id='homecard2',style=lightstyle),
        ], width=4),
         dbc.Col([
            dbc.Card([
                Lottie(options=options, width="13%", height="13%", url=url_student)
                ,
                dbc.CardBody([
                    html.H6('Total Graduate'),
                    html.H3(id='home-department', children="000")
                ],)
            ],id='homecard3',style=lightstyle),
        ] , width=4 ),
    
        
], )

home = html.Div(
    [
        
        home_first_row,
        home_second_row,
        
    ],
    style=CONTENT_STYLE,
    
)

lebel = dbc.Row(
        [
            dbc.Col(
                [
                      dbc.Label("Select Education Level"),
                      html.Br(),
                      dbc.RadioItems(
                      options=[{"label": "ALL", "value": "ALL"}],
                      value="ALL",
            ),   
                   
                ]
            )
        ]
    )




# HOME LAYOUT *****************************************************

# GRADUAN LAYOUT *****************************************************
graduan_first_row = dbc.Row([
dbc.Col([
            dbc.Card([
                dbc.CardBody([
                    html.H6('Respondent'),
                    html.H3(id='graduan-connections', children="000")
                ], )
            ],id='graduancard',style=lightstyle),
        ], width=4),
        
], )

graduan_second_row = dbc.Row(
    [
    
    
   
    
           dbc.Col([
      
                 dbc.Card([
                  
                dbc.CardBody([
                
                    html.Img(id="graduan-dismiss",src=app.get_asset_url('full.png'), style={'height':'4%', 'width':'5%'}),
                   
                    dcc.Graph(id='graduan_5', figure={}), 
                    
                ],)
            ],id='cardgraduan_51',style=lighthome),

        ], className='mb-4', width=5),
        
       dbc.Col([
       
       
             dbc.Card([
                dbc.CardBody([
                 html.Img(id="graduan-dismiss1",src=app.get_asset_url('full.png'), style={'height':'4%', 'width':'4%'}),
                 dcc.Graph(id='graduan_3', figure={}), 
                ],)
            ],id='cardgraduan_3',style=lightgraph2),
      
           
        ], className='mb-4', width=7),
    ]
)


graduan = html.Div(
    [
        graduan_first_row,
        graduan_second_row,
        
    ],
    style=CONTENT_STYLE,
    
)



# GRADUAN LAYOUT *****************************************************


# GENERAL LAYOUT
app.layout = html.Div(
    [
        header.make_header(),
        side,
        controls,
        html.Div(
            children=[
                html.Div(id="main-area"),
             
            ],
        ),
        

    ]
)

  

# TAB RENDERER
@app.callback(Output("main-area", "children"),
             [Input("navigation-tabs", "value"),]
             )
def render_tab(tab):
    
    if tab == "tab-port-stats":
        return [
            html.Div(
                children=[
                        
                        content,
                        modal,
                       
                    
                ],
            )
        ]
        
    elif tab == "tab-port-map":
      return [
            html.Div(
                children=[
                        
                        home,
                       
                      
                ],
            )
        ]
    elif tab == "tab-port-graduan":
      return [
            html.Div(
                children=[
                      
                      graduan,
                ],
            )
        ]
        
@app.callback(Output("rowlevel", "children"),
             [Input("navigation-tabs", "value"),]
             )
def render_tab(tab):
    
    if tab == "tab-port-stats":
        return [
            html.Div(
                children=[
                        
                        levelhome, 
                    
                ],
            )
        ]
        
    elif tab == "tab-port-map":
      return [
            html.Div(
                children=[
                        levelhome, 
                ],
            )
        ]
    elif tab == "tab-port-graduan":
      return [
            html.Div(
                children=[
                        
                        lebel,
                      
                ],
            )
        ]
  
  
        
@app.callback(Output("rowyear", "children"),
              [Input("navigation-tabs", "value")])
def render_tab(tab):
    
 
    if tab == "tab-port-map":
      return [
            html.Div(
                children=[
                        
                        yearside,
                      
                ],
            )
        ]

        
        
        


@app.callback(
    Output('jantina', 'options'),
    Input('level', 'value'),
)

def set_cities_options(chosen_state):
    dff = df[df.LEVEL==chosen_state]
    return [{'label': c, 'value': c} for c in sorted(dff.INSTITUSI.unique())]
    
@app.callback(
    Output('dprtmn', 'options'),
    Input('jantina', 'value'),
)

def set_cities_options(chosen_state):
    dff = df[df.INSTITUSI==chosen_state]
    return [{'label': c, 'value': c} for c in sorted(dff.NEC_BROAD.unique())]

# Updating the 5 number cards ******************************************
@app.callback(
    Output('content-connections','children'),
    Output('content-companies','children'),
    Output('content-department','children'),
    Output('card1', 'style'),
    Output('card2', 'style'),
    Output('card3', 'style'),
    Input('jantina','value'),
    Input('level','value'),
    Input(ThemeSwitchAIO.ids.switch("theme"), "value"),
    Input(ThemeSwitchAIO.ids.switch("theme"), "value"),
    Input(ThemeSwitchAIO.ids.switch("theme"), "value"),
 
)
def update_small_cards(animal_chosen,level,toggle,toggle1,toggle2):

    template = lightstyle if toggle else darkstyle
    template1 = lightstyle if toggle1 else darkstyle
    template2 = lightstyle if toggle2 else darkstyle
    # Connections
    dt = df[df["INSTITUSI"]==animal_chosen]
    dff = dt[dt["LEVEL"]==level]
    conctns_num = len(dff)
    compns_num = len(dff['PROGRAM'].unique())

    # Reactions
    dt = df[df["INSTITUSI"]==animal_chosen]
    dff = dt[dt["LEVEL"]==level]
    reactns_num = len(dff)
    
    # Department
    dt = df[df["INSTITUSI"]==animal_chosen]
    dff = dt[dt["LEVEL"]==level]
    depart_num = len(dff['NEC_BROAD'].unique())

    return  compns_num, reactns_num, depart_num,template,template1,template2
    
    # Pie Chart ************************************************************   
    

    
@app.callback(

    Output('graph_5','figure'),
    Output('cardgraph_5','style'),
    Input('jantina','value'),
    Input('level','value'),
    Input(ThemeSwitchAIO.ids.switch("theme"), "value"),
)
def update_pie(animal_chosen,level,toggle):
    template = lightgraph if toggle else darkgraph
    template2 = custom_dark if toggle else custom_light
    
    dt = df[df["LEVEL"]==level]
    dff = dt[dt["INSTITUSI"]==animal_chosen]
    fig_pie = px.pie(dff, names="JANTINA", title="Total Admission by Gender" , hole=.4 ,color='JANTINA',
             color_discrete_map={'Lelaki':'#FF8888',
                                 'Perempuan':'#57CCC5'})
    fig_pie.update_traces(textinfo="value+percent").update_layout(title_x=0.5)
    fig_pie.layout.template = template2
    
   
    return fig_pie,template

# Bar Chart ************************************************************
def customwrap2(s,width=30):
    return textwrap.shorten(text=s, width=width)   
@app.callback(
    Output('graph_4','figure'),
    Output('cardgraph_4','style'),
    Input('jantina','value'),
    Input('level','value'),
    Input(ThemeSwitchAIO.ids.switch("theme"), "value"),
   

)
def update_bar(animal_chosen,level,toggle):
    template = lightgraph2 if toggle else darkgraph2
    template2 = custom_dark if toggle else custom_light
    
    dt = df[df["LEVEL"]==level]
    df_hist = dt[dt["INSTITUSI"]==animal_chosen]
    
    xr = df_hist.groupby(['NEC_BROAD',],as_index=False)[['RECORD_NUM']].count()
    xr.sort_values("RECORD_NUM", axis = 0, ascending = False, inplace = True, na_position ='first')


        



    fig = go.Figure(go.Bar(
    
    x=xr['RECORD_NUM'],
    y=xr['NEC_BROAD'].map(customwrap2),
    marker=dict(
        color='rgba(87, 204, 197, 1.0)',
        
    ),
    orientation='h',
    
    ))

    fig.update_layout(
                title = 'The Number of Admission By Department',

                hovermode = 'closest',
               
                xaxis = dict(title = '<b>Number of Admission</b>',
                           
                             showline = True,
                             showgrid = True,
                             showticklabels = True,
                             linecolor = 'black',
                             linewidth = 1,
                             ticks = 'outside',
                            ),

                yaxis = dict(title = '<b></b>',
                             autorange = 'reversed',
                           
                             showline = False,
                             showgrid = False,
                             showticklabels = True,
                             linecolor = 'black',
                             linewidth = 1,
                             ticks = 'outside',
                          

                             ),

              
            )
    
  
    fig.layout.template = template2


    return fig,template

# Bar age ************************************************************

@app.callback(
    Output('graph_3','figure'),
    Output('cardgraph_3','style'),
    Input('jantina','value'),
    Input('level','value'),
    Input(ThemeSwitchAIO.ids.switch("theme"), "value"),
  
)
def update_bar(animal_chosen,level,toggle):
    template = lightgraph2 if toggle else darkgraph2
    template2 = custom_dark if toggle else custom_light
    ages = pd.read_csv("All.csv")
    ages = pd.DataFrame(ages)
    ages = ages[ages['LEVEL']==level]
    ages = ages[ages['INSTITUSI']==animal_chosen]
    bins= [15,25,35,45,55,65,75]
    labels = ['15-24','25-34','35-44','45-54','55-64', '65+']
    ages['AgeGroup'] = pd.cut(ages['UMUR'], bins=bins, labels=labels, right=False)
    ages = ages.groupby(['AgeGroup','JANTINA',],as_index=False)[['RECORD_NUM']].count()
    print (ages)


    barchart = px.bar(
        data_frame=ages,
        x="AgeGroup",
        y="RECORD_NUM",
        template='plotly',
        color="JANTINA",  
        # differentiate color of marks
        opacity=1,                  # set opacity of markers (from 0 to 1)
        color_discrete_map={'Lelaki':'#FF8888',
                                 'Perempuan':'#57CCC5'},         # 'v','h': orientation of the marks
        barmode='group',
        orientation='v',
         labels={"RECORD_NUM":"Total Admission",
        "JANTINA":"JANTINA"},           # map the labels of the figure
        title='Total Admission by Group of Age ', # figure title
        
     
    )
  
    barchart.layout.template = template2
    

    return barchart,template
    
# treemap program ************************************************************

@app.callback(
    Output('graph_6','figure'),
    Output('cardgraph_6','style'),
    Input('jantina','value'),
    Input('dprtmn','value'),
    Input('level','value'),
    Input(ThemeSwitchAIO.ids.switch("theme"), "value"),
   
)
def update_bar(animal_chosen,deparment,level,toggle):
    template = lightgraph2 if toggle else darkgraph2
    template2 = custom_dark if toggle else custom_light
    data_url = 'All.csv'
    df = pd.read_csv(data_url)
    df = df[(df['INSTITUSI']==animal_chosen) & (df['NEC_BROAD'].isin(deparment))]
    df = df[df['LEVEL']==level]

    df = df.groupby(['PROGRAM','NEC_DETAIL',],as_index=False)[['RECORD_NUM']].count()



    tree = px.treemap(df, path=[px.Constant("All"),  'NEC_DETAIL', 'PROGRAM'], values=df["RECORD_NUM"],
                 
                  color_continuous_scale='RdBu',
                  color_continuous_midpoint=np.average(df["RECORD_NUM"], weights=df["RECORD_NUM"]))
    tree.layout.template = template2
    tree.update_layout(margin = dict(t=50, l=25, r=25, b=25),title="Total Program by Deparment")
    tree.update_traces(root_color="lightgrey")

    return tree,template

# pyramic program ************************************************************  

@app.callback(
    Output('category', 'options'),
    Input('jantina', 'value'),
    
  
)
def set_cities_options(chosen_state):
  
    dff = df[df['INSTITUSI']==chosen_state]
    return [{'label': c, 'value': c} for c in sorted(dff['NEC_DETAIL'].unique())]
# pyramic program ************************************************************  


# populate initial values of counties dropdown

def customwrap(s,width=60):
    return textwrap.shorten(text=s, width=width)
@app.callback(
    Output('graph_7','figure'),
    Output('cardgraph_7','style'),
    Input('category','value'),
    Input('jantina','value'),
    Input('level','value'),
    Input(ThemeSwitchAIO.ids.switch("theme"), "value"),
    
   
)
def update_bargne(selected_counties, selected_state,level,toggle):
    template = lightgraph3 if toggle else darkgraph3
    template2 = custom_dark if toggle else custom_light
    if len(selected_counties) == 0:
        return dash.no_update
    else:
        df = pd.read_csv("All.csv")
        dff = df[(df['INSTITUSI']==selected_state) & (df['NEC_DETAIL'].isin(selected_counties))]
        dff = dff[dff['LEVEL']==level]
        x_M = dff.loc[dff['JANTINA'] == 'Lelaki']

        x_F = dff.loc[dff['JANTINA'] == 'Perempuan'] 


        xr = x_M.groupby(['JANTINA','PROGRAM',],as_index=False)[['RECORD_NUM']].count()
        xt = x_F.groupby(['JANTINA','PROGRAM',],as_index=False)[['RECORD_NUM']].count()
            
    
        x_age = xr['PROGRAM']
        y_age = xt['PROGRAM']
        

# Creating instance of the figure
        pyr = go.Figure()
  
# Adding Male data to the figure
        pyr.add_trace(go.Bar(y=x_age , x =xr['RECORD_NUM'], 
                     name = 'Male', 
                     orientation = 'h',
                     hoverinfo='y',
                     marker=dict(color='#FF8888')))
# Adding Female data to the figure
        pyr.add_trace(go.Bar(y =y_age , x=-1 * xt['RECORD_NUM'],
                     name = 'Female', orientation = 'h',
                     hoverinfo='x',
                     marker=dict(color='#57CCC5')))
    
  
# Updating the layout for our graph
        pyr.update_layout(
                  title = 'Programme Distribution By Gender',
                  xaxis=go.layout.XAxis(
                     title='Number of Admission',
                     ),
                  yaxis=go.layout.YAxis(
                   
                       title='Programme'),
                       barmode='overlay',   
                       height=600,
                  
                   bargap=0.2)
                   
        pyr.layout.template = template2

        return pyr,template
        
        
# HOME PAGE ************************************************************  
# Updating the 5 number cards ******************************************
@app.callback(
    Output('home-connections','children'),
    Output('home-companies','children'),
    Output('home-department','children'),
    Output('homecard', 'style'),
    Output('homecard2', 'style'),
    Output('homecard3', 'style'),
    Input('jantina','value'),
    Input('level','value'),
    Input(ThemeSwitchAIO.ids.switch("theme"), "value"),
    Input(ThemeSwitchAIO.ids.switch("theme"), "value"),
    Input(ThemeSwitchAIO.ids.switch("theme"), "value"),
    Input('tahun','value'),
 
)
def update_small_cards(animal_chosen,level,toggle,toggle1,toggle2,tahun):

    template = lightstyle if toggle else darkstyle
    template1 = lightstyle if toggle1 else darkstyle
    template2 = lightstyle if toggle2 else darkstyle
    
    my_sheet = level # change it to your sheet name, you can find your sheet name at the bottom left of your excel file
    file_name = 'data2.xlsx' # change it to the name of your excel file
    dfs = read_excel(file_name, sheet_name = my_sheet)
    
    cover = int(tahun)

    # Connections
    dt = dfs[dfs["INSTITUSI"]==animal_chosen]
    ds = dt.loc[dt['YEAR'] == cover]
    compns_num = ds['Kemasukan Jumlah']

    # Reactions
    dt1 = dfs[dfs["INSTITUSI"]==animal_chosen]
    ds1 = dt1.loc[dt['YEAR'] == cover]
    reactns_num = ds1['Enrolmen Jumlah']
    
    # Department
    dt2 = dfs[dfs["INSTITUSI"]==animal_chosen]
    ds2 = dt2.loc[dt['YEAR'] == cover]
    depart_num = ds2['Keluaran Jumlah']

    return  compns_num, reactns_num, depart_num,template,template1,template2
    
  #*************************************************
  
@app.callback(
    Output('tahun', 'options'),
    Input('level', 'value'),
    Input('jantina', 'value'),
    
  
)
def set_cities_options(level,chosen_state):
    my_sheet = level # change it to your sheet name, you can find your sheet name at the bottom left of your excel file
    file_name = 'data2.xlsx' # change it to the name of your excel file
    dt = read_excel(file_name, sheet_name = my_sheet)
  
    dt = dt[dt['INSTITUSI']==chosen_state]
    return [{'label': c, 'value': c} for c in sorted(dt['YEAR'].unique())]

@app.callback(
    Output('home_5','figure'),
    Output('cardhome_51', 'style'),
    Input('jantina','value'),
    Input('level','value'),
    Input(ThemeSwitchAIO.ids.switch("theme"), "value"),
    Input('tahun','value'),
  
)
def update_bar(animal_chosen,level,toggle,tahun):
    template = lightgraph3 if toggle else darkgraph3
    template2 = custom_dark if toggle else custom_light

    
    my_sheet = level # change it to your sheet name, you can find your sheet name at the bottom left of your excel file
    file_name = 'data2.xlsx' # change it to the name of your excel file
    dt = read_excel(file_name, sheet_name = my_sheet)
 
    dt = dt[dt['INSTITUSI']==animal_chosen]
    
    cover = int(tahun)

    ds = dt.loc[dt['YEAR'] == cover]
    print(ds)
   

   

    k = ds.iloc[0]['Kemasukan Lelaki']
    k1= ds.iloc[0]['Kemasukan Perempuan']

    s = ds.iloc[0]['Enrolmen Lelaki']
    s1 = ds.iloc[0]['Enrolmen Perempuan']

    w = ds.iloc[0]['Keluaran Lelaki']
    w1 =ds.iloc[0]['Keluaran Perempuan']


    l = [k,s,w]

    ls = [k1,s1,w1]



    # Creating instance of the figure
    pyr = go.Figure()
  
    # Adding Male data to the figure
    pyr.add_trace(go.Bar(y=l, x =['Application','Intake','Graduate'], 
                     name = 'Male', 
                     orientation = 'v',
                     hoverinfo='y',
                     marker=dict(color='#FF8888')))
    # Adding Female data to the figure
    pyr.add_trace(go.Bar(y =ls , x=['Application','Intake','Graduate'],
                     name = 'Female', orientation = 'v',
                     hoverinfo='y',
                     marker=dict(color='#57CCC5')))
    # Adding Female data to the figure
    
  
    # Updating the layout for our graph
    pyr.update_layout(
                  xaxis=go.layout.XAxis(
                     title='Program',
                     ),
                  yaxis=go.layout.YAxis(
                   
                       title='Number'),
                       barmode='group',
                      
                  
                   bargap=0.2)
    
    pyr.layout.template = template2
                   
    return pyr,template

# Bar age ************************************************************

@app.callback(
    Output('home_3','figure'),
    Output('cardhome_3', 'style'),
    Input('jantina','value'),
    Input('level','value'),
    Input(ThemeSwitchAIO.ids.switch("theme"), "value"),
  
)
def update_lines(animal_chosen,level,toggle):
    template = lightgraph3 if toggle else darkgraph3
    template2 = custom_dark if toggle else custom_light
    
    my_sheet = level # change it to your sheet name, you can find your sheet name at the bottom left of your excel file
    file_name = 'data2.xlsx' # change it to the name of your excel file
    df = read_excel(file_name, sheet_name = my_sheet)

    df = df[df['INSTITUSI']==animal_chosen]

    year = df['YEAR'].unique()
    k = df['Kemasukan Jumlah']
    e = df['Enrolmen Jumlah']
    l= df['Keluaran Jumlah']




    # Create traces
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=year, y=k,
                    mode='lines+markers',
                    name='Application'))
    fig.add_trace(go.Scatter(x=year, y=e,
                    mode='lines+markers',
                    name='Intake'))
    fig.add_trace(go.Scatter(x=year, y=l,
                    mode='lines+markers', name='Graduate'))
    fig.update_layout(
                  xaxis=go.layout.XAxis(
                     title='Year',
                     ),
                  yaxis=go.layout.YAxis(
                   
                       title='Number'),
                       barmode='group',
                      
                  
                   bargap=0.2)
    
    fig.layout.template = template2

    return fig,template
    
# GRADUAN ***********************************************************
@app.callback(
    Output('graduan-connections','children'),
    Output('graduancard', 'style'),
    Input('jantina','value'),
    Input(ThemeSwitchAIO.ids.switch("theme"), "value"),
 
)
def update_small_cards(animal_chosen,toggle):

    template = lightstyle if toggle else darkstyle

    
   

    # Connections
    df = pd.read_csv("statuspekerjaan2016.csv")
    df = df[df['UA']==animal_chosen]
    compns_num = df['Jumlah responden']

    return  compns_num, template
    
    
@app.callback(
    Output('graduan_5','figure'),
    Output('cardgraduan_51', 'style'),
    Input('jantina','value'),
    Input(ThemeSwitchAIO.ids.switch("theme"), "value"),
    
)
def update_bar(animal_chosen,toggle):

    dakis = '#303030'
    lighty = '#E7E7E7'
    template = lightgraph3 if toggle else darkgraph3
    template2 = custom_dark if toggle else custom_light
    colorst = lighty if toggle else dakis

    
    df = pd.read_csv("statuspekerjaan2016.csv")
    df = df[df['UA']==animal_chosen]
    k = df.iloc[0]['Bekerja']
    w= df.iloc[0]['Melanjutkan pengajian']
    m = df.iloc[0]['Meningkatkan kemahiran']
    n = df.iloc[0]['Menunggu penempatan pekerjaan']
    o = df.iloc[0]['Belum bekerja']

    categories = [
        {"name": "Bekerja", "value": k},
        {"name": "Melanjutkan pengajian", "value": w},
        {"name": "Meningkatkan kemahiran", "value": m},
        {"name": "Menunggu penempatan pekerjaan", "value": n},
        {"name": "Belum bekerja", "value": o},
    ]
    
    def get_name(categories):
        return categories.get('name')


    def get_age(categories):
        return categories.get('value')



    categories.sort(key=get_name, reverse=True)


# sort by Age (Ascending order)
    categories.sort(key=get_age, reverse=True)  


    subplots = make_subplots(
        rows=len(categories),
        cols=1,
        subplot_titles=[x["name"] for x in categories],
        shared_xaxes=True,
        print_grid=False,
        vertical_spacing=(0.45 / len(categories)),
        )
    _   = subplots['layout'].update(
        width=550,
        plot_bgcolor=colorst,
        paper_bgcolor=colorst,
        )
        
    for k, x in enumerate(categories):
        subplots.add_trace(dict(
            type='bar',
            orientation='h',
       
            x=[x["value"]],
            text=[x["value"]],
            hoverinfo='text',
            textposition='auto',
            marker=dict(
            color="#7030a0",
            ),
        ), k+1, 1)
    
    subplots['layout'].update(
        showlegend=False,
    )
    for x in subplots["layout"]['annotations']:
        x['x'] = 0
        x['xanchor'] = 'left'
        x['align'] = 'left'
        x['font'] = dict(
        size=12,
    )
    
    for axis in subplots['layout']:
        if axis.startswith('yaxis') or axis.startswith('xaxis'):
            subplots['layout'][axis]['visible'] = False
        
    subplots['layout']['margin'] = {
        'l': 15,
        'r': 0,
        't': 80,
        'b': 0,
    }
    height_calc = 45 * len(categories)
    height_calc = max([height_calc, 350])
    subplots['layout']['height'] = height_calc
    subplots['layout']['width'] = height_calc
    subplots.update_layout(
    title='Employment Status of Graduates',
    )
    subplots.layout.template = template2
    
    
    

    
                   
    return subplots,template
    

@app.callback(
    Output('graduan_3','figure'),
    Output('cardgraduan_3', 'style'),
    Input('jantina','value'),
    Input(ThemeSwitchAIO.ids.switch("theme"), "value"),
    
)
def update_pie(animal_chosen,toggle):

    dakis = '#303030'
    lighty = '#E7E7E7'
    template = lightgraph3 if toggle else darkgraph3
    template2 = custom_dark if toggle else custom_light
    colorst = lighty if toggle else dakis

    
    df = pd.read_csv("statuspekerjaan2016.csv")
    df = df[df['UA']==animal_chosen]
    k = df.iloc[0]['Bekerja']
    w= df.iloc[0]['Melanjutkan pengajian']
    m = df.iloc[0]['Meningkatkan kemahiran']
    n = df.iloc[0]['Menunggu penempatan pekerjaan']
    o = df.iloc[0]['Belum bekerja']

    
    labels = ['Bekerja','Melanjutkan pengajian','Meningkatkan kemahiran','Menunggu penempatan pekerjaan','Belum bekerja']
    values = [k, w, m, n,o]

# pull is given as a fraction of the pie radius
    fig = go.Figure(data=[go.Pie(labels=labels, values=values, pull=[0, 0, 0.2, 0])])
    fig.update_layout(
                title="Employment Status of Graduates"
              
            )
            
    fig.layout.template = template2  
    
    return fig,template
# GRADUAN ***********************************************************

# MODAL ************************************************************
@app.callback(

    Output('graph_99','figure'),
    Input('jantina','value'),
    Input('level','value'),
    Input(ThemeSwitchAIO.ids.switch("theme"), "value"),
)
def update_pie1(animal_chosen,level,toggle):
    template2 = custom_dark if toggle else custom_light
    dt = df[df["LEVEL"]==level]
    dff = dt[dt["INSTITUSI"]==animal_chosen]
    fig_pie = px.pie(dff, names="JANTINA", template='plotly', title="Total Admission by Gender" , hole=.4 ,color='JANTINA',
             color_discrete_map={'Lelaki':'#FF8888',
                                 'Perempuan':'#57CCC5'})
    fig_pie.update_traces(textinfo="value+percent").update_layout(title_x=0.5)
    fig_pie.layout.template = template2
    
   
    return fig_pie
    
    
# Bar Chart ************************************************************
@app.callback(
    Output('graph_91','figure'),
    Input('jantina','value'),
    Input('level','value'),
    Input(ThemeSwitchAIO.ids.switch("theme"), "value"),
  
)
def update_bar(animal_chosen,level,toggle):
    template2 = custom_dark if toggle else custom_light
    ages = pd.read_csv("All.csv")
    ages = pd.DataFrame(ages)
    ages = ages[ages['LEVEL']==level]
    ages = ages[ages['INSTITUSI']==animal_chosen]
    bins= [15,25,35,45,55,65,75]
    labels = ['15-24','25-34','35-44','45-54','55-64', '65+']
    ages['AgeGroup'] = pd.cut(ages['UMUR'], bins=bins, labels=labels, right=False)
    ages = ages.groupby(['AgeGroup','JANTINA',],as_index=False)[['RECORD_NUM']].count()
    print (ages)


    barchart = px.bar(
        data_frame=ages,
        x="AgeGroup",
        y="RECORD_NUM",
        template='plotly',
        color="JANTINA",  
        # differentiate color of marks
        opacity=1,                  # set opacity of markers (from 0 to 1)
        color_discrete_map={'Lelaki':'#FF8888',
                                 'Perempuan':'#57CCC5'},         # 'v','h': orientation of the marks
        barmode='group',
        orientation='v',
         labels={"RECORD_NUM":"Total Admission",
        "JANTINA":"JANTINA"},           # map the labels of the figure
        title='Total Admission by Group of Age ', # figure title
        
     
    )
  
    barchart.layout.template = template2
    

    return barchart

def customwrap2(s,width=30):
    return textwrap.shorten(text=s, width=width)   
@app.callback(
    Output('graph_93','figure'),
    Input('jantina','value'),
    Input('level','value'),
    Input(ThemeSwitchAIO.ids.switch("theme"), "value"),
   

)
def update_bar2(animal_chosen,level,toggle):
    template2 = custom_dark if toggle else custom_light
    dt = df[df["LEVEL"]==level]
    df_hist = dt[dt["INSTITUSI"]==animal_chosen]
    
    xr = df_hist.groupby(['NEC_BROAD',],as_index=False)[['RECORD_NUM']].count()
    xr.sort_values("RECORD_NUM", axis = 0, ascending = False, inplace = True, na_position ='first')


        



    fig = go.Figure(go.Bar(
    
    x=xr['RECORD_NUM'],
    y=xr['NEC_BROAD'].map(customwrap2),
    marker=dict(
        color='rgba(87, 204, 197, 1.0)',
        
    ),
    orientation='h',
    
    ))

    fig.update_layout(
                title = 'The Number of Admission By Department',

                hovermode = 'closest',
               
                xaxis = dict(title = '<b>Number of Admission</b>',
                           
                             showline = True,
                             showgrid = True,
                             showticklabels = True,
                             linecolor = 'black',
                             linewidth = 1,
                             ticks = 'outside',
                            ),

                yaxis = dict(title = '<b></b>',
                             autorange = 'reversed',
                           
                             showline = False,
                             showgrid = False,
                             showticklabels = True,
                             linecolor = 'black',
                             linewidth = 1,
                             ticks = 'outside',
                          

                             ),

              
            )
    
  
    fig.layout.template = template2


    return fig
    
# treemap program ************************************************************

@app.callback(
    Output('graph_92','figure'),
    Input('jantina','value'),
    Input('dprtmn','value'),
    Input('level','value'),
    Input(ThemeSwitchAIO.ids.switch("theme"), "value"),
   
)
def update_bar3(animal_chosen,deparment,level,toggle):
    template2 = custom_dark if toggle else custom_light
    data_url = 'All.csv'
    df = pd.read_csv(data_url)
    df = df[(df['INSTITUSI']==animal_chosen) & (df['NEC_BROAD'].isin(deparment))]
    df = df[df['LEVEL']==level]

    df = df.groupby(['PROGRAM','NEC_DETAIL',],as_index=False)[['RECORD_NUM']].count()



    tree = px.treemap(df, path=[px.Constant("All"),  'NEC_DETAIL', 'PROGRAM'], values=df["RECORD_NUM"],
                 
                  color_continuous_scale='RdBu',
                  color_continuous_midpoint=np.average(df["RECORD_NUM"], weights=df["RECORD_NUM"]))
    tree.layout.template = template2
    tree.update_layout(margin = dict(t=50, l=25, r=25, b=25),title="Total Program by Deparment")
    tree.update_traces(root_color="lightgrey")

    return tree
    
    

@app.callback(
    Output('graph_971','figure'),
    Input('category','value'),
    Input('jantina','value'),
    Input('level','value'),
    Input(ThemeSwitchAIO.ids.switch("theme"), "value"),
    
)
def update_bargne1(selected_counties, selected_state,level,toggle):
    template2 = custom_dark if toggle else custom_light
    if len(selected_counties) == 0:
        return dash.no_update
    else:
        df = pd.read_csv("All.csv")
        dff = df[(df['INSTITUSI']==selected_state) & (df['NEC_DETAIL'].isin(selected_counties))]
        dff = dff[dff['LEVEL']==level]
        x_M = dff.loc[dff['JANTINA'] == 'Lelaki']

        x_F = dff.loc[dff['JANTINA'] == 'Perempuan'] 


        xr = x_M.groupby(['JANTINA','PROGRAM',],as_index=False)[['RECORD_NUM']].count()
        xt = x_F.groupby(['JANTINA','PROGRAM',],as_index=False)[['RECORD_NUM']].count()
            
    
        x_age = xr['PROGRAM']
        y_age = xt['PROGRAM']
        

# Creating instance of the figure
        pyr = go.Figure()
  
# Adding Male data to the figure
        pyr.add_trace(go.Bar(y=x_age , x =xr['RECORD_NUM'], 
                     name = 'Male', 
                     orientation = 'h',
                     hoverinfo='y',
                     marker=dict(color='#FF8888')))
# Adding Female data to the figure
        pyr.add_trace(go.Bar(y =y_age , x=-1 * xt['RECORD_NUM'],
                     name = 'Female', orientation = 'h',
                     hoverinfo='x',
                     marker=dict(color='#57CCC5')))
    
  
# Updating the layout for our graph
        pyr.update_layout(
                  xaxis=go.layout.XAxis(
                     title='Program',
                     ),
                  yaxis=go.layout.YAxis(
                   
                       title='Number'),
                       barmode='overlay',
                       height=600,
                  
                   bargap=0.2)
                   
        pyr.layout.template = template2

        return pyr



# pyramic program ************************************************************  



@app.callback(
    Output("modal-dismiss", "is_open"),
    [Input("open-dismiss", "n_clicks"), Input("close-dismiss", "n_clicks")],
    [State("modal-dismiss", "is_open")],
)
def toggle_modal(n_open, n_close, is_open):
    if n_open or n_close:
        return not is_open
    return is_open
    
@app.callback(
    Output("modal-dismiss1", "is_open"),
    [Input("open-dismiss1", "n_clicks"), Input("close-dismiss1", "n_clicks")],
    [State("modal-dismiss1", "is_open")],
)
def toggle_modal1(n_open, n_close, is_open):
    if n_open or n_close:
        return not is_open
    return is_open

@app.callback(
    Output("modal-dismiss2", "is_open"),
    [Input("open-dismiss2", "n_clicks"), Input("close-dismiss2", "n_clicks")],
    [State("modal-dismiss2", "is_open")],
)
def toggle_modal2(n_open, n_close, is_open):
    if n_open or n_close:
        return not is_open
    return is_open

@app.callback(
    Output("modal-dismiss3", "is_open"),
    [Input("open-dismiss3", "n_clicks"), Input("close-dismiss3", "n_clicks")],
    [State("modal-dismiss3", "is_open")],
)
def toggle_modal3(n_open, n_close, is_open):
    if n_open or n_close:
        return not is_open
    return is_open

@app.callback(
    Output("modal-dismiss4", "is_open"),
    [Input("open-dismiss4", "n_clicks"), Input("close-dismiss4", "n_clicks")],
    [State("modal-dismiss4", "is_open")],
)
def toggle_modal4(n_open, n_close, is_open):
    if n_open or n_close:
        return not is_open
    return is_open


# CLOSEMODAL ************************************************************





if __name__ == '__main__':
    app.run_server(debug=False)
