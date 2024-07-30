class Event(db.Model):
    __tablename__ = 'events'

    id= db.Column(db.Integer, primary_key= True)
    name= db.Column(db.String, nullable=False)
    venue= db.Column(db.String, nullable= False)
    date= db.Column(db.Date, nullable=False)
    start_time= db.Column(db.Integer, nullable=False)
    ticket_price= db.Column(db.Integer, nullable=False)

class User(db.Model):
    __tablename__= 'users'

    id= db.Column(db.Integer, primary_key= True)
    username= db.Column(db.String, nullable=False)
    password=db.Column(db.String, unique=True, nullable=False)
    email= db.Column(db.String, unique=True, nullable=False)

class Performance(db.Model):
    __tablename__ = 'performances'

    id= db.Column(db.Integer, primary_key= True)
    musician_name= db.Column(db.String, nullable=False)
    start_time= db.column(db.Integer, nullable=False)
    end__time= db.column(db.Integer, nullable=False)
    event_id= db.Column(db.Integer, db.ForeignKey('events.id'), nullable=False)

    #Relationship
    event= db.relationship('Event', back_populates='performances')


