from flask import Blueprint, render_template, current_app
from flask_menu import register_menu

home = Blueprint("home", __name__, url_prefix='/')

#@home.route("/")
#def home_index():
#    return render_template("index.html")


@home.route("/")
@home.route("/prometheus")
@register_menu(home, '.', "Home", order=0)
@register_menu(home, '.prometheus', "Prometheus", order=0)
def home_prometheus():
    return render_template("prometheus.html",
        frontend_ip=current_app.config["FRONTEND_IP"])


@home.route("/grafana")
@register_menu(home, '.grafana', "Grafana", order=0)
def home_grafana():
    return render_template("grafana.html",
        frontend_ip=current_app.config["FRONTEND_IP"])


@home.route("/docker-visualizer")
@register_menu(home, '.docker-visualizer', "Docker Visualizer", order=0)
def home_docker_visualizer():
    return render_template("docker-visualizer.html",
        frontend_ip=current_app.config["FRONTEND_IP"])

