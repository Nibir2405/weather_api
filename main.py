from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

stations = pd.read_csv("weather_data\stations.txt", skiprows=17)
stations = stations[["STAID","STANAME                                 "]]

@app.route("/")
def home():
    return render_template("home.html", data=stations.to_html())

@app.route("/about/")
def about():
    return render_template("about.html")

@app.route("/api/v1/<stationid>/<date>")
def get_data(stationid, date):
    filename =f"weather_data/TG_STAID{str(stationid).zfill(6)}.txt"
    df = pd.read_csv(filename, skiprows=20, parse_dates=["    DATE"])
    temperature = df.loc[df["    DATE"]== date]["   TG"].squeeze() / 10
    return {"Date": date,
            "Station": stationid,
            "Temperature": temperature}
@app.route("/api/v1/<stationid>")
def all_data(stationid):
    filename =f"weather_data/TG_STAID{str(stationid).zfill(6)}.txt"
    df = pd.read_csv(filename, skiprows=20, parse_dates=["    DATE"])
    results = df.to_dict(orient="records")
    return results

@app.route("/api/v1/yearly/<stationid>/<year>")
def yearly(stationid,year):
    filename =f"weather_data/TG_STAID{str(stationid).zfill(6)}.txt"
    df = pd.read_csv(filename, skiprows=20)
    df["    DATE"] = df["    DATE"].astype(str)
    results = df[df["    DATE"].str.startswith(str(year))].to_dict(orient="records")
    return results
    

if __name__ == "__main__":
    app.run(debug=True)