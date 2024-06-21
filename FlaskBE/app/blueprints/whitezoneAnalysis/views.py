from flask import jsonify, request, abort
from . import whitezoneAnalysis_bp
from .models import *
from app.extensions import db


phase_models = [Phase1, Phase2, Phase3, Phase4,
                Phase5, Phase6, Phase7, Phase8]

phase_models_dict = {
    'phase1': Phase1,
    'phase2': Phase2,
    'phase3': Phase3,
    'phase4': Phase4,
    'phase5': Phase5,
    'phase6': Phase6,
    'phase7': Phase7,
    'phase8': Phase8
}


@whitezoneAnalysis_bp.route('/phases', methods=['GET'])
def get_phases():
    phases = {}
    for idx, phase in enumerate(phase_models, 1):
        phase_data = phase.query.all()
        phases[f'Phase{idx}'] = [
            {
                'match_id': p.match_id,
                'user_geometry_center_x': p.user_geometry_center_x,
                'user_geometry_center_y': p.user_geometry_center_y,
                'white_zone_center_x': p.white_zone_center_x,
                'white_zone_center_y': p.white_zone_center_y
            } for p in phase_data
        ]
    return jsonify(phases)


@whitezoneAnalysis_bp.route('/phase/<int:phase_number>', methods=['GET'])
def get_dist_phases(phase_number):
    phases = {}
    phase_data = phase_models[phase_number - 1].query.all()
    phases[f'Phase{phase_number}'] = [
        {
            'match_id': p.match_id,
            'user_geometry_center_x': p.user_geometry_center_x,
            'user_geometry_center_y': p.user_geometry_center_y,
            'white_zone_center_x': p.white_zone_center_x,
            'white_zone_center_y': p.white_zone_center_y
        } for p in phase_data
    ]
    return jsonify(phases)


@whitezoneAnalysis_bp.route('/insert/phase', methods=['POST'])
def create_phase():
    # 400 error1
    if not request.json:
        # data가 json형식이 아닌경우
        abort(400, description="Request body must be JSON")
    # body의 내용 불러오기
    data = request.json
    print(data)

    if 'table' not in data or 'data' not in data:
        abort(400, description="Request must include 'table' and 'data'")
    # 400 error2
    if 'match_id' not in data['data'] or 'user_geometry_center_x' not in data['data'] or 'user_geometry_center_y' not in \
            data['data'] or 'white_zone_center_x' not in data['data'] or 'white_zone_center_y' not in data['data']:
        abort(400, description="Missing Data Fields")

    # 400 error3
    required_fields = ['match_id', 'user_geometry_center_x', 'user_geometry_center_y', 'white_zone_center_x',
                       'white_zone_center_y']

    table_name = data['table']
    if table_name not in phase_models_dict:
        abort(400, description="Invalid table name")

    Model = phase_models_dict[table_name]
    print(Model)
    record_data = data['data']
    for field in required_fields:
        if field not in record_data:
            abort(400, description=f"Missing Data Field: {field}")

    new_phase = Model(
        match_id=record_data['match_id'],
        user_geometry_center_x=record_data['user_geometry_center_x'],
        user_geometry_center_y=record_data['user_geometry_center_y'],
        white_zone_center_x=record_data['white_zone_center_x'],
        white_zone_center_y=record_data['white_zone_center_y']
    )
    db.session.add(new_phase)
    db.session.commit()

    # 데이터가 잘 들어갔는지 쿼리하여 확인
    inserted_phase = Model.query.filter_by(match_id=record_data['match_id']).first()
    if inserted_phase:
        print(f"Data inserted: {inserted_phase.to_dict()}")

    return '', 204  # 204 No Content 상태 코드 반환
