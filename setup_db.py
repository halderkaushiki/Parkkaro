from app import app, db, User

def create_admin_user():
    with app.app_context():
        db.create_all()

        admin_exists = User.query.filter_by(username='admin').first()

        if admin_exists:
            print("Admin user already exists.")
        else:
            admin_user = User(
                username='admin',
                email='admin@gmail.com',
                password='admin',
                is_admin=True
            )
            db.session.add(admin_user)
            db.session.commit()
            print("Admin user created successfully.")

create_admin_user()
