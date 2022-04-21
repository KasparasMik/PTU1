import unittest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from create_db import Base, Projektas

#####  Tikrinam kai SQL tuscias, darbo pradzioj, nes istrina viska tikrinant ar viskas veikia be klaidu #####

class Test_query(unittest.TestCase):
    
    engine = create_engine('sqlite:///pilotai.db')  
    Session = sessionmaker(bind=engine)
    session = Session()
    
    def setUp(self):
        Base.metadata.create_all(self.engine)
        self.projektas = Projektas("Test", "Test", "Test", 1, "Test")
        self.session.add(self.projektas)
        self.session.commit()

    def tearDown(self):
        Base.metadata.drop_all(self.engine)

    def test_query_panel(self):
        expected = [self.projektas]
        result = self.session.query(Projektas).all()
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()