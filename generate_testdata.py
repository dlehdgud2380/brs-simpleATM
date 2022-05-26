import module.model as db
import module.account as account
from module.model import Card
from sqlalchemy.orm import Session
from sqlalchemy import create_engine

# database generate
db.create_db()

# User Genrate
newuser1 = account.Register("hello", "hello123", "watson")
newuser1.user()
newuser1.card("1234")
for _ in range(3):
    newuser1.account()
    
newuser2 = account.Register("world", "world456", "justin")
newuser2.user()
newuser2.card("5678")
for _ in range(3):
    newuser2.account()
    
newuser3 = account.Register("foo", "foo789", "steve")
newuser3.user()
newuser3.card("1357")
for _ in range(3):
    newuser3.account()
    
newuser4 = account.Register("bar", "bar135", "endrew")
newuser4.user()
newuser4.card("2468")
for _ in range(3):
    newuser4.account()
    
# make cardlist.txt
engine = create_engine("sqlite:///account.db", echo=False, future=True)
session = Session(engine)

f = open('cardlist.txt', 'w')
f.write("[card List] - Input cardnum, pin for atm_run.py\n\n")
for card in session.query(Card).all():
    data: str = f'{card.owner}: {card.serial}(num) - {card.pin}(pin)\n'
    f.write(data)
f.close()