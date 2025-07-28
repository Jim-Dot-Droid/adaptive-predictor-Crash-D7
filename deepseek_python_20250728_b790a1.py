try:
    import plotly.express as px
    import plotly.graph_objects as go
    PLOTLY_AVAILABLE = True
except ImportError:
    PLOTLY_AVAILABLE = False
    st.warning("Plotly not available - using simple text display")

# Rest of your imports
import streamlit as st
import requests
import pandas as pd
import numpy as np
from datetime import datetime

# ... [rest of your existing code] ...

# Replace all plotting code with this conditional:
if PLOTLY_AVAILABLE:
    fig = px.line(...)
    st.plotly_chart(fig)
else:
    st.write("Multiplier data:", df.head(num_games)[['timestamp', 'multiplier']])