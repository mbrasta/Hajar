from flask import Flask, render_template
import requests
import plotly.graph_objects as go

app = Flask(__name__)

# Fetching real-time earthquake data
def fetch_earthquake_data():
    url = "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_hour.geojson"
    response = requests.get(url)
    data = response.json()
    return data

@app.route('/')
def index():
    # Generate Plotly 3D Earth globe
    data = fetch_earthquake_data()
    earthquakes = data['features']

    latitudes = []
    longitudes = []
    magnitudes = []
    locations = []

    for eq in earthquakes:
        lat = eq['geometry']['coordinates'][1]
        lon = eq['geometry']['coordinates'][0]
        mag = eq['properties']['mag']
        place = eq['properties']['place']

        latitudes.append(lat)
        longitudes.append(lon)
        magnitudes.append(mag)
        locations.append(place)

    # Create Plotly globe visualization
    trace = go.Scattergeo(
        locationmode='ISO-3',
        locations=latitudes,
        text=locations,
        hoverinfo='text',
        mode='markers',
        marker=dict(
            size=8,
            color=magnitudes,
            colorscale='Reds',
            showscale=True
        )
    )

    layout = go.Layout(
        geo=dict(
            projection=dict(
                type='orthographic'
            ),
            showland=True,
            landcolor='lightgreen',
            showocean=True,
            oceancolor='lightblue'
        )
    )

    fig = go.Figure(data=[trace], layout=layout)
    graph_html = fig.to_html(full_html=False)

    return render_template('index.html', plot_html=graph_html)

if __name__ == '__main__':
    app.run(debug=True)
