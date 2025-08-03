from passlib.context import CryptContext
import hidden

class Hash():
    def bcrypt(password: str):
        hashedPassword = hidden.pwd_context.hash(password)
        return hashedPassword
    
    def verify(hashedPassword, plainPassword):
        return hidden.pwd_context.verify(plainPassword, hashedPassword)