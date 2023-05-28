from models import Dog

def create_table(base, engine):
    # 2 arguments passed from test || without engine include following
    # import => from sqlalchemy import create_engine   
    # in create_table => engine = create_engine('sqlite:///:memory:')
    base.metadata.create_all(engine)

def save(session, dog):
    session.add(dog)
    session.commit()

def get_all(session):
    dogs = session.query(Dog).all()
    return dogs

def find_by_name(session, name):
    dogs_name = session.query(Dog.name).filter(Dog.name.like(f"%{name}%")).all()
    return dogs_name[0]

def find_by_id(session, id):
    dogs_id = session.query(Dog.name, Dog.id, Dog.breed).filter(Dog.id.like(f"%{id}%")).all()
    return dogs_id[0]

def find_by_name_and_breed(session, name, breed):
    dogs_name_breed = session.query(Dog.name, Dog.breed).filter(Dog.name.like(f"%{name}%")).filter(Dog.breed.like(f"%{breed}%")).all()
    return dogs_name_breed[0]

def update_breed(session, dog, breed):
    dog.breed = breed
    session.commit()