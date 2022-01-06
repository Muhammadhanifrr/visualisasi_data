# -*- coding: utf-8 -*-
"""Tugas_Besar_Visualisasi_Data_1301160280_Muhammad Hanif  Rifki Rohman.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1lnVqrbRsAkv3AbBzScDe0-HabUI1d7KA
"""

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

from bokeh.io import output_notebook
from bokeh.plotting import figure, show
from bokeh.io import output_file
from bokeh.models import ColumnDataSource
from bokeh.layouts import row, column, gridplot
from bokeh.models.widgets import Tabs, Panel
from bokeh.models import HoverTool

datahanif=pd.read_csv('stock_market.csv') 
datahanif.head()

datahanif.info()

datahanif.describe()

sns.pairplot(datahanif, hue='Name')

datahanif['Index_Saham'] = datahanif.index + 1
datahanif.rename({'Adj Close': 'Adj_Close'}, axis=1, inplace=True)
datahanif.head()

"""**Level 1**"""

# Output to file
output_notebook()

# Isolate the data for the Rockets and Warriors
hs = datahanif[datahanif['Name'] == 'HANG SENG']
nk = datahanif[datahanif['Name'] == 'NIKKEI']
ns = datahanif[datahanif['Name'] == 'NASDAQ']

# Create a ColumnDataSource object for each team
hs_cds = ColumnDataSource(hs)
nk_cds = ColumnDataSource(nk)
ns_cds = ColumnDataSource(ns)

# Create and configure the figure
fig = figure(plot_height=300, plot_width=600,
             title='Adj Close',
             x_axis_label='Index', y_axis_label='Adj Close')

# Render the race as step lines
fig.circle('Index_Saham', 'Adj_Close', 
         color='red', legend_label='Hang Seng', 
         source=hs_cds)
fig.circle('Index_Saham', 'Adj_Close', 
         color='blue', legend_label='Nikkei', 
         source=nk_cds)
fig.circle('Index_Saham', 'Adj_Close', 
         color='black', legend_label='Nasdaq', 
         source=ns_cds)

# Move the legend to the upper left corner
fig.legend.location = 'top_left'


# Bokeh Library
from bokeh.models import HoverTool

# Format the tooltip
tooltips = [
            ('Nama Saham','@Name'),
            ('Adj Close', '@Adj_Close'),
            ('Volume', '@Volume'),
            ('Day Perc Change','@Day_Perc_Change'),
           ]

# Add the HoverTool to the figure
fig.add_tools(HoverTool(tooltips=tooltips))

# Visualize
show(fig)

"""Level 2"""

# Output to file
output_notebook()

# Isolate the data for the Rockets and Warriors
hs = datahanif[datahanif['Name'] == 'HANG SENG']
nk = datahanif[datahanif['Name'] == 'NIKKEI']
ns = datahanif[datahanif['Name'] == 'NASDAQ']

# Create a ColumnDataSource object for each team
hs_cds = ColumnDataSource(hs)
nk_cds = ColumnDataSource(nk)
ns_cds = ColumnDataSource(ns)

# Create and configure the figure
fig_a = figure(plot_height=300, plot_width=600,
             title='Adj Close',
             x_axis_label='Index', y_axis_label='Adj Close')

# Render the race as step lines
fig_a.circle('Index_Saham', 'Adj_Close', 
         color='red', legend_label='Hang Seng', 
         source=hs_cds)
fig_a.circle('Index_Saham', 'Adj_Close', 
         color='blue', legend_label='Nikkei', 
         source=nk_cds)
fig_a.circle('Index_Saham', 'Adj_Close', 
         color='black', legend_label='Nasdaq', 
         source=ns_cds)

# Move the legend to the upper left corner
fig_a.legend.location = 'top_left'


# Bokeh Library
from bokeh.models import HoverTool

# Format the tooltip
tooltips = [
            ('Nama Saham','@Name'),
            ('Adj Close', '@Adj_Close'),
            ('Volume', '@Volume'),
            ('Day Perc Change','@Day_Perc_Change'),
           ]

# Add the HoverTool to the figure
fig_a.add_tools(HoverTool(tooltips=tooltips))

# Visualize
show(fig_a)

#Volume

# Output to file
output_notebook()

# Isolate the data for the Rockets and Warriors
hs = datahanif[datahanif['Name'] == 'HANG SENG']
nk = datahanif[datahanif['Name'] == 'NIKKEI']
ns = datahanif[datahanif['Name'] == 'NASDAQ']

# Create a ColumnDataSource object for each team
hs_cds = ColumnDataSource(hs)
nk_cds = ColumnDataSource(nk)
ns_cds = ColumnDataSource(ns)

# Create and configure the figure
fig_b = figure(plot_height=300, plot_width=600,
             title='Volume',
             x_axis_label='Index', y_axis_label='Volume')

# Render the race as step lines
fig_b.circle('Index_Saham', 'Volume', 
         color='red', legend_label='Hang Seng', 
         source=hs_cds)
fig_b.circle('Index_Saham', 'Volume', 
         color='blue', legend_label='Nikkei', 
         source=nk_cds)
fig_b.circle('Index_Saham', 'Volume', 
         color='black', legend_label='Nasdaq', 
         source=ns_cds)

# Move the legend to the upper left corner
fig_b.legend.location = 'top_left'


# Bokeh Library
from bokeh.models import HoverTool

# Format the tooltip
tooltips = [
            ('Nama Saham','@Name'),
            ('Adj Close', '@Adj_Close'),
            ('Volume', '@Volume'),
            ('Day Perc Change','@Day_Perc_Change'),
           ]

# Add the HoverTool to the figure
fig_b.add_tools(HoverTool(tooltips=tooltips))

# Visualize
show(fig_b)

#Day Perc Change

# Output to file
output_notebook()

# Isolate the data for the Rockets and Warriors
hs = datahanif[datahanif['Name'] == 'HANG SENG']
nk = datahanif[datahanif['Name'] == 'NIKKEI']
ns = datahanif[datahanif['Name'] == 'NASDAQ']

# Create a ColumnDataSource object for each team
hs_cds = ColumnDataSource(hs)
nk_cds = ColumnDataSource(nk)
ns_cds = ColumnDataSource(ns)

# Create and configure the figure
fig_c = figure(plot_height=300, plot_width=600,
             title='Day_Perc_Change',
             x_axis_label='Index', y_axis_label='VDay_Perc_Change')

# Render the race as step lines
fig_c.circle('Index_Saham', 'Day_Perc_Change', 
         color='red', legend_label='Hang Seng', 
         source=hs_cds)
fig_c.circle('Index_Saham', 'Day_Perc_Change', 
         color='blue', legend_label='Nikkei', 
         source=nk_cds)
fig_c.circle('Index_Saham', 'Day_Perc_Change', 
         color='black', legend_label='Nasdaq', 
         source=ns_cds)

# Move the legend to the upper left corner
fig_c.legend.location = 'top_left'


# Bokeh Library
from bokeh.models import HoverTool

# Format the tooltip
tooltips = [
            ('Nama Saham','@Name'),
            ('Adj Close', '@Adj_Close'),
            ('Volume', '@Volume'),
            ('Day Perc Change','@Day_Perc_Change'),
           ]

# Add the HoverTool to the figure
fig_c.add_tools(HoverTool(tooltips=tooltips))

# Visualize
show(fig_c)

# Tab dan Panel

# Increase the plot widths
fig_a.plot_width = fig_b.plot_width = fig_c.plot_width = 900

# Create two panels, one for each conference
a_panel = Panel(child= fig_a, title='Adj Close')
b_panel = Panel(child= fig_b, title='Volume')
c_panel = Panel(child= fig_c, title='Day Perc Change')

# Assign the panels to Tabs
tabs = Tabs(tabs=[a_panel, b_panel, c_panel])

# Show the tabbed layout
show(tabs)

"""**Level 3**"""

#Hiding Selecting Legend
fig_a.legend.click_policy = 'hide'
fig_b.legend.click_policy = 'hide'
fig_c.legend.click_policy = 'hide'

# Increase the plot widths
fig_a.plot_width = fig_b.plot_width = fig_c.plot_width = 900

# Create two panels, one for each conference
a_panel = Panel(child= fig_a, title='Adj Close')
b_panel = Panel(child= fig_b, title='Volume')
c_panel = Panel(child= fig_c, title='Day Perc Change')

# Assign the panels to Tabs
tabs = Tabs(tabs=[a_panel, b_panel, c_panel])

# Show the tabbed layout
show(tabs)
