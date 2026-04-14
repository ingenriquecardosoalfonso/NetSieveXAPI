from extensions import db
import uuid

class Feature(db.Model):
    __tablename__ = 'features'

    id          = db.Column('id',db.Integer,  primary_key=True)
    feature_key          = db.Column('feature_key',db.String(100))
    feature_name             = db.Column('feature_name', db.String(150))
    description             = db.Column('description', db.String(1000))
    predicted_class             = db.Column('predicted_class', db.String(5100))
    description_positive             = db.Column('description_positive',             db.String(1000))
    description_negative             = db.Column('description_negative',             db.String(1000))
    state             = db.Column('state',             db.Boolean())
    def __repr__(self):
        return f'<Feature feature_key={self.feature_key} feature_name={self.feature_name} description={self.description} predicted_class={self.predicted_class} description_positive={self.description_positive} description_negative={self.description_negative} state={self.state}>'