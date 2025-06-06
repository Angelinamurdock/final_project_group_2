from flask import Flask, render_template, request
import pandas as pd
import plotly.express as px
import plotly.io as pio

app = Flask(__name__)
data = pd.read_csv("Resources/future_home_value_predictions.csv")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/plot", methods=["GET", "POST"])
def plot():
    selected_min_year = request.form.get("min_year")
    selected_max_year = request.form.get("max_year")
    selected_neighborhood = request.form.get("neighborhood")
    min_price = request.form.get("min_price")
    max_price = request.form.get("max_price")

    filtered = data.copy()

    if selected_min_year:
        filtered = filtered[filtered["Year"] >= int(selected_min_year)]
    if selected_max_year:
        filtered = filtered[filtered["Year"] <= int(selected_max_year)]
    if selected_neighborhood and selected_neighborhood != "All":
        filtered = filtered[filtered["Neighborhood"] == selected_neighborhood]
    if min_price:
        filtered = filtered[filtered["Predicted Home Value"] >= float(min_price)]
    if max_price:
        filtered = filtered[filtered["Predicted Home Value"] <= float(max_price)]

    fig = px.scatter(
        filtered,
        x="Predicted Home Value",
        y="Year",
        size="Predicted Home Value",
        color="Year",
        hover_name="Neighborhood",
        title="Top Investment Neighborhoods by Year",
        color_continuous_scale="Viridis"
    )

    # Save interactive plot to an HTML file
    fig.write_html("plot.html")
    



    plot_html = pio.to_html(fig, full_html=False)

    years = sorted(data["Year"].unique())
    neighborhoods = ["All"] + sorted(data["Neighborhood"].unique())

    return render_template(
        "plot.html",
        plot_html=plot_html,
        years=years,
        neighborhoods=neighborhoods,
        selected_min_year=selected_min_year,
        selected_max_year=selected_max_year,
        selected_neighborhood=selected_neighborhood,
        min_price=min_price,
        max_price=max_price
    )

@app.route("/table")
def table():
    # Filter to just 2024 and 2035 predictions
    data_2024 = data[data['Year'] == 2024][['RegionID', 'Neighborhood', 'City', 'Predicted Home Value']].rename(columns={'Predicted Home Value': 'Value_2024'})
    data_2035 = data[data['Year'] == 2035][['RegionID', 'Neighborhood', 'City', 'Predicted Home Value']].rename(columns={'Predicted Home Value': 'Value_2035'})

    # Merge and calculate growth
    merged = pd.merge(data_2024, data_2035, on=['RegionID', 'Neighborhood', 'City'])
    merged['Growth ($)'] = merged['Value_2035'] - merged['Value_2024']
    merged['Growth (%)'] = (merged['Growth ($)'] / merged['Value_2024']) * 100

    # Format numbers with commas and no decimal for display
    merged['Value_2024'] = merged['Value_2024'].map('{:,.0f}'.format)
    merged['Value_2035'] = merged['Value_2035'].map('{:,.0f}'.format)
    merged['Growth ($)'] = merged['Growth ($)'].map('{:,.0f}'.format)
    merged['Growth (%)'] = merged['Growth (%)'].map('{:,.2f}%'.format)

    top_growth = merged.sort_values(by='Growth ($)', ascending=False).head(10)

    return render_template("table.html", tables=[top_growth.to_html(classes='table table-striped', index=False, escape=False)])

if __name__ == "__main__":
    app.run(debug=True)
