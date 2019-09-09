from flask import Blueprint, render_template, current_app
from flask_menu import register_menu

home = Blueprint("home", __name__, url_prefix="/")

@home.route("/")
@home.route("/dashboard")
@home.route("/prometheus")
@home.route("/dashboard/prometheus")
@register_menu(home, '.', "Home", order=0)
@register_menu(home, '.prometheus', "Prometheus", order=2)
def home_prometheus():
    return render_template(['prometheus.html','base.html'],
        frontend_ip=current_app.config['FRONTEND_IP'], version=current_app.config['MICADO_VERSION'])

@home.route("/grafana")
@home.route("/dashboard/grafana")
@register_menu(home, '.grafana', "Grafana", order=1)
def home_grafana():
    return render_template(['grafana.html','base.html'],
        frontend_ip=current_app.config['FRONTEND_IP'], version=current_app.config['MICADO_VERSION'])

@home.route("/kubernetes")
@home.route("/dashboard/kubernetes")
@register_menu(home, '.kubernetes', "Kubernetes", order=0)
def home_kubernetes_dashboard():
    return render_template(['kubernetes.html','base.html'],
        frontend_ip=current_app.config['FRONTEND_IP'], version=current_app.config['MICADO_VERSION'])

@home.route("/optimizer")
@home.route("/dashboard/optimizer")
@register_menu(home, '.optimizer', "Optimizer", order=3)
def home_optimizer():
    return render_template(['optimizer.html','base.html'],
        frontend_ip=current_app.config['FRONTEND_IP'], version=current_app.config['MICADO_VERSION'])

@home.route("/logout")
@register_menu(home, '.logout', "Log out", order=4)
def home_logout():
    return "Logging you out"
