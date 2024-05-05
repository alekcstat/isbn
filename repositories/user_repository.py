from models.user import User, db

class UserRepository:

    @staticmethod
    def create_user_repository(company, line):

        user = User(company=company, line=line)
        
        db.session.add(user)
        db.session.commit()

        return user