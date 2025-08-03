import database, models, passwordHashing, hidden, schemas

from datetime import timedelta, datetime
from sqlalchemy.orm import Session
from jose import jwt, JWTError
from fastapi import Depends, HTTPException, status

db = database.get_db

def get_user(db: Session, username: str):
    return db.query(models.User).filter(models.User.username == username).first()

def authenticate_user(db: Session, username: str, password: str):
    user = get_user(db, username)
    print(user)
    if not user:
        return False
    if not passwordHashing.Hash.verify(user.password, password):
        return False
    return user

def create_access_token(data: dict, expires_delta: timedelta or None = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)

    to_encode.update({"exp": expire})

    encode_jwt = jwt.encode(to_encode, hidden.SECRET_KEY, algorithm=hidden.ALGORITHM)

    return encode_jwt

async def get_current_user(token: str = Depends(hidden.oauth_2_scheme), db: Session = Depends(database.get_db)):
    credential_exceptions = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Could not validate credentials", headers={"WWW-Authenticate": "Bearer"})

    try: 
        payload = jwt.decode(token, hidden.SECRET_KEY, algorithms=[hidden.ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credential_exceptions
        
        token_data = schemas.TokenData(username=username)

    except JWTError:
        raise credential_exceptions
    
    user = get_user(db, username=token_data.username)
    if user is None:
        raise credential_exceptions
    
    return user

async def get_current_active_user(current_user: models.User = Depends(get_current_user)):
    if current_user.disabled: 
        raise HTTPException(status_code=400, detail="Inactive User")
    return current_user