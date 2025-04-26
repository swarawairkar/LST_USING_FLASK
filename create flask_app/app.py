from flask import Flask, render_template, jsonify, request
import pandas as pd
import numpy as np
import json
import os
from datetime import datetime
from flask_app.data_processing import (
    get_temperature_data, 
    get_monthly_temperature_data,
    get_annual_trend_data,
    get_ndvi_data,
    get_district_list,
    generate_temperature_map_html
)

app = Flask(__name__, 
            static_folder="../static",
            template_folder="../templates")

# Initialize session state values
DEFAULT_YEAR = 2024
DEFAULT_MONTH = 4
DEFAULT_DISTRICT = "All"
DEFAULT_TIME = "Daytime"
DEFAULT_VARIABLE = "LST"

@app.route('/')
def index():
    """Render the main dashboard page"""
    return render_template('index.html')

@app.route('/api/districts')
def get_districts():
    """Return list of districts"""
    return jsonify(get_district_list())

@app.route('/api/temperature_map')
def temperature_map():
    """Generate temperature map for a given year, month, and time of day"""
    year = int(request.args.get('year', DEFAULT_YEAR))
    month = int(request.args.get('month', DEFAULT_MONTH))
    district = request.args.get('district', DEFAULT_DISTRICT)
    time_of_day = request.args.get('time_of_day', DEFAULT_TIME)
    
    map_html = generate_temperature_map_html(year, month, district, time_of_day)
    return map_html

@app.route('/api/temperature_data')
def temperature_data():
    """Get temperature data for districts"""
    year = int(request.args.get('year', DEFAULT_YEAR))
    month = int(request.args.get('month', DEFAULT_MONTH))
    time_of_day = request.args.get('time_of_day', DEFAULT_TIME)
    
    data = get_temperature_data(year, month, time_of_day)
    return jsonify(data.to_dict(orient='records'))

@app.route('/api/monthly_data')
def monthly_data():
    """Get monthly temperature data for a district"""
    year = int(request.args.get('year', DEFAULT_YEAR))
    district = request.args.get('district', DEFAULT_DISTRICT)
    
    data = get_monthly_temperature_data(year, district)
    return jsonify(data.to_dict(orient='records'))

@app.route('/api/annual_trend')
def annual_trend():
    """Get annual temperature trend data"""
    start_year = int(request.args.get('start_year', 2000))
    end_year = int(request.args.get('end_year', 2024))
    district = request.args.get('district', DEFAULT_DISTRICT)
    
    data = get_annual_trend_data(start_year, end_year, district)
    return jsonify(data.to_dict(orient='records'))

@app.route('/api/ndvi_data')
def ndvi_data():
    """Get vegetation index (NDVI) data"""
    year = int(request.args.get('year', DEFAULT_YEAR))
    month = int(request.args.get('month', DEFAULT_MONTH))
    district = request.args.get('district', DEFAULT_DISTRICT)
    
    data = get_ndvi_data(year, month, district)
    return jsonify(data)

@app.route('/spatial-analysis')
def spatial_analysis():
    """Render the spatial analysis page"""
    return render_template('spatial_analysis.html')

@app.route('/temporal-analysis')
def temporal_analysis():
    """Render the temporal analysis page"""
    return render_template('temporal_analysis.html')

@app.route('/vegetation-analysis')
def vegetation_analysis():
    """Render the vegetation analysis page"""
    return render_template('vegetation_analysis.html')

@app.route('/urban-heat-analysis')
def urban_heat_analysis():
    """Render the urban heat analysis page"""
    return render_template('urban_heat_analysis.html')

@app.route('/about')
def about():
    """Render the about page"""
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
