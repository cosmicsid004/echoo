import hidden
import models, database, schemas, passwordHashing, authentication

from fastapi import FastAPI, Depends, HTTPException, status

from sqlalchemy.orm import Session

from datetime import timedelta

app = FastAPI()

models.Base.metadata.create_all(database.engine)

@app.post("/user")
def UserCreation(request: schemas.UserCreate, db: Session = Depends(database.get_db)):
    new_user = models.User(username = request.username, name = request.name, email = request.email, password = passwordHashing.Hash.bcrypt(request.password))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

@app.get("/user/{id}", response_model=schemas.ShowUser)
def getUser(id: int, db: Session = Depends(database.get_db), current_user: models.User = Depends(authentication.get_current_user)):
    user = db.query(models.User).filter(models.User.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    return user

@app.post("/eecho/")
def CreateEecho(request: schemas.EechoCreate, db: Session = Depends(database.get_db), current_user: models.User = Depends(authentication.get_current_user)):
    new_eecho = models.Eecho(body = request.body, user_id = current_user.id)
    db.add(new_eecho)
    db.commit()
    db.refresh(new_eecho)
    return new_eecho

@app.post("/token", response_model=schemas.Token)
async def login_for_access_token(from_data: hidden.OAuth2PasswordRequestForm = Depends(), db: Session = Depends(database.get_db)):
    user = authentication.authenticate_user(db, from_data.username, from_data.password)
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Incorrect Username or Password", headers={"WWW-Authenticate": "Bearer"})
    
    access_token_expires = timedelta(minutes=hidden.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = authentication.create_access_token(data={"sub": user.username}, expires_delta=access_token_expires)

    return {"access_token": access_token, "token_type": "bearer"}

