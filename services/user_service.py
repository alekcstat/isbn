from repositories.user_repository import UserRepository

class UserService:
    
    @staticmethod
    def create_user_service(data):

        company = data['company']
        line = data['line']

        return UserRepository.create_user_repository(company, line)