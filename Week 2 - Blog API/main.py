from fastapi import FastAPI, HTTPException
from data import posts
from model import Post, PostUpdate

app = FastAPI(title="Week-2 Blog API")

@app.get("/")
def root():
    return {"message": "Welcome to Blog API"}

@app.get("/posts")
def get_posts():
    return {"count": len(posts), "posts": posts}

@app.post("/posts")
def create_post(post: Post):
    post_id = len(posts) + 1
    new_post = post.dict()
    new_post["id"] = post_id
    posts.append(new_post)
    return {"message": "Post created successfully", "post": new_post}


@app.put("/posts/{post_id}")
def update_post(post_id: int, post_update: PostUpdate):
    for post in posts:
        if post["id"] == post_id:
            update_data = post_update.dict(exclude_unset=True)
            post.update(update_data)
            return {"message": "Post updated successfully", "post": post}
    raise HTTPException(status_code=404, detail="Post not found")


