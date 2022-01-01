from dash import dcc
import plotly.express as px
import pandas as pd
import dash
from dash import html
from plotly import graph_objs as go
import plotly
from plotly import graph_objs as go


#Lecture de "covid_19_2020.csv"
covid = pd.read_csv('covid_19_2020.csv')

#Création de la 1ère carte

map1 = px.scatter_mapbox(covid, lat="Lat", lon="Long", hover_name="Country",hover_data=["Country","Date", "Confirmed","Recovered", "Deaths", "Active"],color="Confirmed",size="Confirmed", zoom=2, height=800,color_continuous_scale=px.colors.sequential.Inferno,title="Distribution of confirmed cases worldwide")
map1.update_layout(
    mapbox_style="white-bg",
    mapbox_layers=[
        {
            "below": 'traces',
            "sourcetype": "raster",
            "sourceattribution": "Distribution of confirmed cases worldwide",
            "source": [
                "https://basemap.nationalmap.gov/arcgis/rest/services/USGSImageryOnly/MapServer/tile/{z}/{y}/{x}"
            ]
        }
      ],title_x=0.5,title_y=0.98,titlefont={ "size": 35, "color":'#1C2840' })

map1.update_layout(margin={"l": 0, "r": 0, "b": 0, "t": 50})

# Création de la 2ème carte
map2 = px.scatter_mapbox(covid, lat="Lat", lon="Long", hover_name="Country",hover_data=["Country","Date","Deaths"],color_discrete_sequence=["red"], zoom=2, height=800,title="Distribution of deaths worldwide")

map2.update_layout(
    mapbox_style="white-bg",
    mapbox_layers=[
        {
            "below": 'traces',
            "sourcetype": "raster",
            "sourceattribution": "Distribution of deaths worldwide",
            "source": [
                "https://basemap.nationalmap.gov/arcgis/rest/services/USGSImageryOnly/MapServer/tile/{z}/{y}/{x}"
            ]
        }
      ],title_x=0.5,title_y=0.98,titlefont={ "size": 35, "color":'#1C2840' })

map2.update_layout(margin={"l": 0, "r": 0, "b": 0, "t": 50})

#Création des Graphiques

#Création du graphe en fromage

#Organisation des données pour n'avoir aucune donnée nulle pour faire le pourcentage
confirm=covid.loc[covid['Confirmed']>0].count()[0]
dead=covid.loc[covid['Deaths']>0].count()[0]
recov=covid.loc[covid['Recovered']>0].count()[0]
active=covid.loc[covid['Active']>0].count()[0]

#Définition des différentes parties du fromage

labels=['Death','Cared for','Active']
values = [dead,recov,active]

#Couleurs des différentes parties du fromage

colors = ['#384b7e', '#122425', '#223565']

#Création du graphique fromage 

cheese = go.Figure(data=[go.Pie(labels=labels, values=values, textinfo='label+percent',marker_colors=colors, hole=.1,insidetextorientation='radial',textfont_size=25)])

#Ajout d'une couleur de fond au graphique, taille, titre
cheese.layout.paper_bgcolor = '#8e8e8e'
cheese.update_layout(title_text="Distribution of the type of confirmed cases",titlefont={ "size": 35, "color":"#FFFFFF" },hoverlabel={"bgcolor":"white","font_size":30,"font_family":"Rockwell"})

#Création de l'histogramme représentant les cas du Covid confirmés en fonction de la date 

fig1 = px.histogram(covid, x="Date",y="Confirmed", color="Country",title='Evolution of confirmed cases over time',template='plotly')
fig1.update_layout(titlefont={ "size": 25 })

#Création de l'histogramme représentant les morts du Covid confirmés en fonction de la date 

fig2 = px.histogram(covid, x="Date",y="Deaths",color="Country",title='Evolution of deceased cases over time',template='plotly')
fig2.update_layout(titlefont={ "size": 25 })

#Création du graphique représentant le nombre de cas confirmé par pays

fig3 = px.scatter(covid, x="Country", y="Confirmed", color="Country", title="Number of confirmed cases by country",template='plotly')
fig3.update_layout(titlefont={ "size": 25 })

#Création du graphique représentant le nombre de morts par pays

fig4 = px.scatter(covid, x="Country", y="Deaths", title='Number of deaths by country',template='plotly', color="Country")
fig4.update_layout(titlefont={ "size": 25 })

#Création du graphique représentant le nombre de cas confirmé par pays en fonction du temps

fig5 = px.scatter(covid, x="Date", y="Confirmed", color="Country",title='Number of confirmed cases per country as a function of time',template='plotly')
fig5.update_layout(titlefont={ "size": 25 })

#Création du graphique représentant le nombre de morts par pays en fonction du temps

fig6 = px.scatter(covid, x="Date", y="Deaths", color="Country", title='Number of deaths by country as a function of time',template='plotly')
fig6.update_layout(titlefont={ "size": 25 })

#Création du graphique représentant le nombre de morts en fonction des cas confirmés

fig8 = px.histogram(covid, x="Confirmed",y="Deaths", color="Country",title='Number of deaths according to confirmed cases',template='plotly_white')
fig8.update_layout(titlefont={ "size": 25 })

#Création du graphique représentant l'évolution du nombre de morts par pays dans le temps

fig7 = px.bar(covid,x="Country",y="Confirmed",title='Evolution of the number of deaths by country over time',animation_group="Country",animation_frame="Date",range_y=[0,14000000], height=800,template='plotly')
fig7.update_layout(titlefont={ "size": 25 })

fig7.layout.updatemenus[0].buttons[0].args[1]['frame']['duration'] = 5
fig7.layout.updatemenus[0].buttons[0].args[1]['transition']['duration'] = 5

#########################################################################################################################################################################################################################################


# Création du DASHBOARD

dashboard= dash.Dash(__name__) # Créer le dashboard
# Générer le code HTML
dashboard.layout = html.Div(style={'background-color':'#191970'},children=[

                        html.H1("COVID-19 data around the world", style={'text-align': 'center', 'color':'white', 'padding-top':'2vh','padding-bottom':'2vh'}),

                        html.Br(),
                        #Dessin de l'élément dans le dashboard

                        #Création de la carte des répartitions des cas confirmés dans le monde
                        dcc.Graph(id='map1',figure=map1),
                        
                        #Création de la carte des répartitions des cas morts dans le monde
                        dcc.Graph(id='map2',figure=map2),

                        #Création de l'histogramme représentant les cas du Covid confirmés en fonction de la date
                        dcc.Graph(id='graph1',figure=fig1),

                        #Création de l'histogramme représentant les morts du Covid confirmés en fonction de la date 
                        dcc.Graph(id='graph2',figure=fig2),

                        #Création du graphique représentant le nombre de cas confirmé par pays
                        dcc.Graph(id='graph3',figure=fig3), 

                        #Création du graphique représentant le nombre de morts par pays
                        dcc.Graph(id='graph4',figure=fig4),  

                        #Création du graphique représentant le nombre de cas confirmé par pays en fonction du temps
                        dcc.Graph(id='graph5',figure=fig5),

                        #Création du graphique représentant le nombre de morts par pays en fonction du temps
                        dcc.Graph(id='graph6',figure=fig6),

                        #Création du graphique représentant le nombre de morts en fonction des cas confirmés
                        dcc.Graph(id='graph8',figure=fig8),
                        
                        #Création du graphique représentant l'évolution du nombre de morts par pays dans le temps                                                     
                        dcc.Graph(id='graph7',figure=fig7),

                        #Création du graphique fromage 
                        dcc.Graph(id='cheese',figure=cheese,style={'height': '90vh', 'display': 'block', 'margin-left': 'auto', 'margin-right': 'auto'})
])        
        

#########################################################################################################################################################################################################################################

#Lance le Dashboard

if __name__ == '__main__':
    dashboard.run_server(debug=False, use_reloader=False)