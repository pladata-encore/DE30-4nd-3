from flask import Blueprint

whitezoneAnalysis_bp = Blueprint('whitezoneAnalysis', __name__)

from . import views
