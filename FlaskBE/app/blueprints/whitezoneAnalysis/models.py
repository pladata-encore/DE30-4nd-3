from app.extensions import db


class Phase1(db.Model):
    __tablename__ = 'phase1'
    match_id = db.Column(db.String(50), primary_key=True, nullable=False)
    user_geometry_center_x = db.Column(db.REAL, nullable=False)
    user_geometry_center_y = db.Column(db.REAL, nullable=False)
    white_zone_center_x = db.Column(db.REAL, nullable=False)
    white_zone_center_y = db.Column(db.REAL, nullable=False)

    def to_dict(self):
        return {
            'match_id': self.match_id,
            'user_geometry_center_x': self.user_geometry_center_x,
            'user_geometry_center_y': self.user_geometry_center_y,
            'white_zone_center_x': self.white_zone_center_x,
            'white_zone_center_y': self.white_zone_center_x
        }


class Phase2(db.Model):
    __tablename__ = 'phase2'
    match_id = db.Column(db.String(50), primary_key=True, nullable=False)
    user_geometry_center_x = db.Column(db.REAL, nullable=False)
    user_geometry_center_y = db.Column(db.REAL, nullable=False)
    white_zone_center_x = db.Column(db.REAL, nullable=False)
    white_zone_center_y = db.Column(db.REAL, nullable=False)

    def to_dict(self):
        return {
            'match_id': self.match_id,
            'user_geometry_center_x': self.user_geometry_center_x,
            'user_geometry_center_y': self.user_geometry_center_y,
            'white_zone_center_x': self.white_zone_center_x,
            'white_zone_center_y': self.white_zone_center_x
        }


class Phase3(db.Model):
    __tablename__ = 'phase3'
    match_id = db.Column(db.String(50), primary_key=True, nullable=False)
    user_geometry_center_x = db.Column(db.REAL, nullable=False)
    user_geometry_center_y = db.Column(db.REAL, nullable=False)
    white_zone_center_x = db.Column(db.REAL, nullable=False)
    white_zone_center_y = db.Column(db.REAL, nullable=False)

    def to_dict(self):
        return {
            'match_id': self.match_id,
            'user_geometry_center_x': self.user_geometry_center_x,
            'user_geometry_center_y': self.user_geometry_center_y,
            'white_zone_center_x': self.white_zone_center_x,
            'white_zone_center_y': self.white_zone_center_x
        }


class Phase4(db.Model):
    __tablename__ = 'phase4'
    match_id = db.Column(db.String(50), primary_key=True, nullable=False)
    user_geometry_center_x = db.Column(db.REAL, nullable=False)
    user_geometry_center_y = db.Column(db.REAL, nullable=False)
    white_zone_center_x = db.Column(db.REAL, nullable=False)
    white_zone_center_y = db.Column(db.REAL, nullable=False)

    def to_dict(self):
        return {
            'match_id': self.match_id,
            'user_geometry_center_x': self.user_geometry_center_x,
            'user_geometry_center_y': self.user_geometry_center_y,
            'white_zone_center_x': self.white_zone_center_x,
            'white_zone_center_y': self.white_zone_center_x
        }


class Phase5(db.Model):
    __tablename__ = 'phase5'
    match_id = db.Column(db.String(50), primary_key=True, nullable=False)
    user_geometry_center_x = db.Column(db.REAL, nullable=False)
    user_geometry_center_y = db.Column(db.REAL, nullable=False)
    white_zone_center_x = db.Column(db.REAL, nullable=False)
    white_zone_center_y = db.Column(db.REAL, nullable=False)

    def to_dict(self):
        return {
            'match_id': self.match_id,
            'user_geometry_center_x': self.user_geometry_center_x,
            'user_geometry_center_y': self.user_geometry_center_y,
            'white_zone_center_x': self.white_zone_center_x,
            'white_zone_center_y': self.white_zone_center_x
        }


class Phase6(db.Model):
    __tablename__ = 'phase6'
    match_id = db.Column(db.String(50), primary_key=True, nullable=False)
    user_geometry_center_x = db.Column(db.REAL, nullable=False)
    user_geometry_center_y = db.Column(db.REAL, nullable=False)
    white_zone_center_x = db.Column(db.REAL, nullable=False)
    white_zone_center_y = db.Column(db.REAL, nullable=False)

    def to_dict(self):
        return {
            'match_id': self.match_id,
            'user_geometry_center_x': self.user_geometry_center_x,
            'user_geometry_center_y': self.user_geometry_center_y,
            'white_zone_center_x': self.white_zone_center_x,
            'white_zone_center_y': self.white_zone_center_x
        }


class Phase7(db.Model):
    __tablename__ = 'phase7'
    match_id = db.Column(db.String(50), primary_key=True, nullable=False)
    user_geometry_center_x = db.Column(db.REAL, nullable=False)
    user_geometry_center_y = db.Column(db.REAL, nullable=False)
    white_zone_center_x = db.Column(db.REAL, nullable=False)
    white_zone_center_y = db.Column(db.REAL, nullable=False)

    def to_dict(self):
        return {
            'match_id': self.match_id,
            'user_geometry_center_x': self.user_geometry_center_x,
            'user_geometry_center_y': self.user_geometry_center_y,
            'white_zone_center_x': self.white_zone_center_x,
            'white_zone_center_y': self.white_zone_center_x
        }


class Phase8(db.Model):
    __tablename__ = 'phase8'
    match_id = db.Column(db.String(50), primary_key=True, nullable=False)
    user_geometry_center_x = db.Column(db.REAL, nullable=False)
    user_geometry_center_y = db.Column(db.REAL, nullable=False)
    white_zone_center_x = db.Column(db.REAL, nullable=False)
    white_zone_center_y = db.Column(db.REAL, nullable=False)

    def to_dict(self):
        return {
            'match_id': self.match_id,
            'user_geometry_center_x': self.user_geometry_center_x,
            'user_geometry_center_y': self.user_geometry_center_y,
            'white_zone_center_x': self.white_zone_center_x,
            'white_zone_center_y': self.white_zone_center_x
        }
