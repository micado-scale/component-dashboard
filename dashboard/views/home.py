from flask import Blueprint, render_template, current_app
from flask_menu import register_menu

home = Blueprint("home", __name__, url_prefix="/")

@home.route("/")
@home.route("/dashboard")
@home.route("/prometheus")
@home.route("/dashboard/prometheus")
@register_menu(home, '.', "Home", order=0)
@register_menu(home, '.prometheus', "Prometheus", order=0)
def home_prometheus():
    return render_template("prometheus.html",
        frontend_ip=current_app.config["FRONTEND_IP"])


@home.route("/grafana")
@home.route("/dashboard/grafana")
@register_menu(home, '.grafana', "Grafana", order=0)
def home_grafana():
    return render_template("grafana.html",
        frontend_ip=current_app.config["FRONTEND_IP"])


@home.route("/kubernetes")
@home.route("/dashboard/kubernetes")
@register_menu(home, '.kubernetes-dashboard', "Kubernetes Dashboard", order=0)
def home_docker_visualizer():
    return render_template("kubernetes-dashboard.html",
        frontend_ip=current_app.config["FRONTEND_IP"])


@home.route("/logout")
@register_menu(home, '.logout', "Log out", order=1)
def home_logout():
    return "Logging you out"
