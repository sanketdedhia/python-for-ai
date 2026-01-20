class APIConfig():
    def __init__(self, api_key, model = 'gpt-3.5-turbo', max_tokens = 100):
        self.api_key = api_key
        self.model = model
        self.max_tokens = max_tokens
        self.base_url = "https://api.openai.com"

#---------------------------------------

devconfig = APIConfig('sk-dev-key',max_tokens = 50)

prod_config = APIConfig('sk-prog-key',model = 'gpt-4',max_tokens = 200)

print(devconfig.model)
print(prod_config.model)

#--------------------
class DataValidator():
    def __init__(self):
        self.errors = []

    def is_valid_email(self,email):
        if not '@' in email:
            self.errors.append(f'The email {email} is not valid.')
            return False
        return True
    
    def get_errors(self):
        return self.errors
    

validator = DataValidator()
validator.is_valid_email('sanket.com')
print(validator.get_errors())