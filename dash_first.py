{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "import plotly.graph_objects as go\n",
    "import dash\n",
    "import dash_html_components as html\n",
    "import numpy as np\n",
    "import pandas as pd\n",
    "import dash_core_components as dcc"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [],
   "source": [
    "my_sample_data = np.random.random_sample([10,3])\n",
    "cat_g = [\"good\",\"bad\",\"worst\"]\n",
    "sample_cat= [cat_g[np.random.randint(0,3)] for i in range(10)]\n",
    "base_data= pd.DataFrame(my_sample_data,columns = [\"val_1\",\"val_2\",\"val_3\"])\n",
    "base_data[\"sample_cat\"]=sample_cat\n",
    "#base_data.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Dropdown(options=[{'label': 'New York City', 'value': 'NYC'}, {'label': 'Montréal', 'value': 'MTL'}, {'label': 'San Francisco', 'value': 'SF'}], value='MTL')"
      ]
     },
     "execution_count": 3,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "dcc.Dropdown(\n",
    "    options=[\n",
    "        {'label': 'New York City', 'value': 'NYC'},\n",
    "        {'label': 'Montréal', 'value': 'MTL'},\n",
    "        {'label': 'San Francisco', 'value': 'SF'}\n",
    "    ],\n",
    "    value='MTL'\n",
    ")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 29,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Dropdown(None)"
      ]
     },
     "execution_count": 29,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "dcc.Dropdown()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array(['good', 'bad', 'worst'], dtype=object)"
      ]
     },
     "execution_count": 4,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "base_data[\"sample_cat\"].unique()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Dropdown(options=[{'label': 'good', 'value': 'good'}, {'label': 'bad', 'value': 'bad'}, {'label': 'worst', 'value': 'worst'}], value='good')"
      ]
     },
     "execution_count": 5,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "options_list =[]\n",
    "for i in cat_g:\n",
    "    options_list.append({'label':i,'value':i})\n",
    "    \n",
    "dcc.Dropdown(options=options_list , value='good')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      " * Serving Flask app \"__main__\" (lazy loading)\n",
      " * Environment: production\n",
      "   WARNING: This is a development server. Do not use it in a production deployment.\n",
      "   Use a production WSGI server instead.\n",
      " * Debug mode: off\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      " * Running on http://127.0.0.1:8050/ (Press CTRL+C to quit)\n",
      "127.0.0.1 - - [19/Apr/2020 17:44:07] \"GET / HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [19/Apr/2020 17:44:08] \"GET /_dash-component-suites/dash_core_components/dash_core_components-shared.v1_9_0m1586773415.js HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [19/Apr/2020 17:44:08] \"GET /_dash-component-suites/dash_core_components/dash_core_components.v1_9_0m1586773415.min.js HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [19/Apr/2020 17:44:08] \"GET /_dash-layout HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [19/Apr/2020 17:44:08] \"GET /_dash-dependencies HTTP/1.1\" 200 -\n"
     ]
    }
   ],
   "source": [
    "app = dash.Dash()\n",
    "\n",
    "app.layout= html.Div(children=[html.Div(\"WELCOME to DASH\",style={\n",
    "                                              \"color\": \"white\",\n",
    "                                              \"text-align\": \"center\",\"background-color\":\"lightblue\",\n",
    "                                              \"border-style\":\"dotted\",\"display\":\"inline-block\",\n",
    "                                              \"width\":\"80%\"\n",
    "                                            }),\n",
    "                                html.Div(dcc.Dropdown(options=options_list , value='good'),style={\n",
    "                                              \"color\": \"red\",\n",
    "                                              \"text-align\": \"center\",\"background-color\":\"lightblue\",\n",
    "                                              \"border-style\":\"dotted\",\"display\":\"inline-block\",\n",
    "                                              \"width\":\"40%\"\n",
    "                                            }),\n",
    "                               html.Div(\"how are you\",style={\"color\": \"black\",\n",
    "                                              \"text-align\": \"center\",\"background-color\":\"lightblue\",\n",
    "                                              \"border-style\":\"dotted\",\"display\":\"inline-block\",\n",
    "                                              \"width\":\"40%\"})])\n",
    "\n",
    "if __name__== '__main__':\n",
    "    app.run_server()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
