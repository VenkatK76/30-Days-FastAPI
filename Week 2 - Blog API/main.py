from fastapi import FastAPI
from data import posts
from model import Post

app = FastAPI(title="Week-2 Blog API")

@app.get("/")
def root():
    return {"message": "Welcome to Blog API"}

@app.post("/posts")
def create_post(post: Post):
    post_id = len(posts) + 1
    new_post = post.dict()
    new_post["id"] = post_id
    posts.append(new_post)
    return {"message": "Post created successfully", "post": new_post}


