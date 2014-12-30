from app import db

class Sumary(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    
    summary = db.Column(db.String)
    
    email = db.Column(db.String)

    is_send = db.Column(db.Boolean)
    

    def to_dict(self):
        return dict(
            summary = self.summary,
            email = self.email,
            is_send = self.is_send,
            id = self.id
        )

    def __repr__(self):
        return '<Sumary %r>' % (self.id)
