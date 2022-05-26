import module.model as db
import module.account as account

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