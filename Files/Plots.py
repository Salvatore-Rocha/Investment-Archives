import pandas as pd
import plotly.graph_objects as go

# Month translation
months_map = {
    'Jan': 'Ene', 'Feb': 'Feb', 'Mar': 'Mar', 'Apr': 'Abr',
    'May': 'May', 'Jun': 'Jun', 'Jul': 'Jul', 'Aug': 'Ago',
    'Sep': 'Sep', 'Oct': 'Oct', 'Nov': 'Nov', 'Dec': 'Dic'
}
colors = ["#2E2B64","#872BAC","#272860", "#5C2D69", "#373871"]

# Load and clean data
data = pd.read_csv("Files/AG_Hist_Returns.csv")
data["Return"] = data["Return"].str.replace('%', '', regex=False).astype(float) / 100
data["Date"] = pd.to_datetime(data["Date"], format="%d-%m-%Y")
data["Date_Label"] = data["Date"].dt.strftime("%b-%Y").map(
    lambda x: months_map[x[:3]] + x[3:]
)

# Create bar chart with percentage labels
fig = go.Figure()

fig.add_trace(go.Bar(
    x=data["Date_Label"],
    y=data["Return"],
    text=data["Return"].apply(lambda x: f"{x*100:.1f}%"),
    textposition="outside",
    #marker_color='steelblue',
    marker_color=[colors[i % len(colors)] for i in range(len(data))]  # cyclic color assignment
))

fig.update_layout(
    title="Rendimientos Históricos",
    yaxis_tickformat=".1%",  # Keep axis in percentage
    xaxis=dict(
        tickmode='linear',
        tickangle=-45
    )
)

fig.show()