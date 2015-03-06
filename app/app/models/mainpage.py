from app import db

class Mainpage(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    
    test = db.Column(db.String)
    

    def to_dict(self):
        return dict(
            test = self.test,
            id = self.id
        )

    def __repr__(self):
        return '<Mainpage %r>' % (self.id)
