from fastapi import FastAPI
from pydantic import BaseModel
from typing_extensions import Text, Optional
from datetime import datetime
from uuid import uuid4 as uui
 

app = FastAPI()

# USAREMOS UN ARRAY PARA GUARDAR LOS DATOS, ESTE ARRAY GUARDARÁ POSTS
posts = []

# POST MODEL
class Post(BaseModel):
    #Es importante establecer el None para hacerle entender que aunque es opcional, no debe esperar que se ingrese
    #Si solo dejamos el Optional, entenderá que es opcional que sea string pero esperará que le ingresemos un dato.
    id: Optional[str] = None
    title: str
    author: str
    content: str
    created_at: datetime = datetime.now()
    published_at: Optional[datetime] = None
    published: bool = False

#########################################################---RUTAS---##############################################################

@app.get('/')
def read_root():
    return {"welcome": "Welcome to my REST API"}


####### RUTA GET, HTTP ########
@app.get('/posts')
def get_posts():
    return posts

####### RUTA POST, HTTP ########
@app.post('/posts')
def save_post(post: Post):
    #Guardamos un id generado
    post.id= str(uui())
    posts.append(post)
    #devolverá el último objeto ingresado
    return posts[-1]


####### RUTA GET POST BY ID, HTTP ########
@app.get('/posts/{post_id}')
def get_post(post_id : str):
    for post in posts:
        if post.id == post_id:
            return post
    #print(f"El id que ingresas es el: {post_id}")    
    return "Not found"

####### RUTA DELETE, HTTP ########
@app.delete('/posts/{post_id}')
def delete_post(post_id: str):
    for index,post in enumerate(posts):
       # print(post)
       # print(index)
       if post.id == post_id:
            posts.pop(index)
            return {"message:" "Post has been deleted succesfully"}
    return "Not found"
        
####### RUTA UPDATE, HTTP ########
@app.put('/posts/{post_id}')
#LOS PARÁMETROS DEL UPDATE SERÁN UN ID Y UN OBJETO POST, SERÁ EL QUE EDITAREMOS
def update_post(post_id: str, updatePost: Post):
    for index, post in enumerate(posts):
        #Si el post ingresado existe
        if post.id == post_id:
            posts[index].title = updatePost.title
            posts[index].author= updatePost.author
            posts[index].content = updatePost.content
            return {"message:" "Post has been updated succesfully"}
    return "Not found"
