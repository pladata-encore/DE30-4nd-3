def register_blueprints(app):
    from app.blueprints.whitezoneAnalysis import whitezoneAnalysis_bp
    app.register_blueprint(whitezoneAnalysis_bp, url_prefix='/whitezoneAnalysis')
