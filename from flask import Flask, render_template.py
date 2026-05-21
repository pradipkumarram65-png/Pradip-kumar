from flask import Flask, render_template, request, redirect, url_for, session, jsonify
import json
import os
from datetime import datetime
 
app = Flask(__name__)
app.secret_key = "helpconnect_secret_2024"
 
# In-memory data store (replace with a real DB in production)
users = [
    {"id": 1, "name": "Aisha Sharma", "avatar": "AS", "location": "Kathmandu", "bio": "Love helping neighbours with groceries and errands.", "points": 420, "joined": "Jan 2024"},
    {"id": 2, "name": "Rohan KC", "avatar": "RK", "location": "Lalitpur", "bio": "Skilled in home repairs and teaching math.", "points": 310, "joined": "Feb 2024"},
    {"id": 3, "name": "Priya Thapa", "avatar": "PT", "location": "Bhaktapur", "bio": "Teacher and tutor, happy to help with studies.", "points": 280, "joined": "Mar 2024"},
]
 
posts = [
    {"id": 1, "user_id": 2, "user": "Rohan KC", "avatar": "RK", "type": "offer", "title": "Free math tutoring for students", "description": "I can help Grade 6–10 students with mathematics every Saturday morning. Completely free!", "category": "Education", "location": "Lalitpur", "time": "2 hours ago", "likes": 14, "comments": 3},
    {"id": 2, "user_id": 3, "user": "Priya Thapa", "avatar": "PT", "type": "request", "title": "Need help moving furniture", "description": "Moving to a new apartment this weekend. Need 2-3 people to help carry boxes and furniture. Will provide snacks!", "category": "Moving", "location": "Bhaktapur", "time": "5 hours ago", "likes": 7, "comments": 5},
    {"id": 3, "user_id": 1, "user": "Aisha Sharma", "avatar": "AS", "type": "offer", "title": "Grocery runs for elderly neighbours", "description": "I shop at Bhat-Bhateni every Thursday. Happy to pick up groceries for anyone nearby who finds it difficult to travel.", "category": "Errands", "location": "Kathmandu", "time": "1 day ago", "likes": 22, "comments": 8},
    {"id": 4, "user_id": 2, "user": "Rohan KC", "avatar": "RK", "type": "request", "title": "Looking for a plant-sitting volunteer", "description": "Travelling for 10 days. Need someone to water my plants once every 2 days. Easy task, I'll leave full instructions.", "category": "Pets & Plants", "location": "Lalitpur", "time": "1 day ago", "likes": 5, "comments": 2},
    {"id": 5, "user_id": 3, "user": "Priya Thapa", "avatar": "PT", "type": "offer", "title": "English speaking practice sessions", "description": "I run free weekly English conversation groups every Wednesday evening. Open to all levels. Great for building confidence!", "category": "Education", "location": "Bhaktapur", "time": "2 days ago", "likes": 31, "comments": 11},
]
 
categories = ["All", "Education", "Errands", "Moving", "Pets & Plants", "Tech Help", "Cooking", "Repairs"]
 
@app.route("/")
def index():
    return render_template("index.html", posts=posts, categories=categories, users=users)
 
@app.route("/api/posts")
def api_posts():
    category = request.args.get("category", "All")
    post_type = request.args.get("type", "all")
    filtered = posts
    if category != "All":
        filtered = [p for p in filtered if p["category"] == category]
    if post_type != "all":
        filtered = [p for p in filtered if p["type"] == post_type]
    return jsonify(filtered)
 
@app.route("/api/post/new", methods=["POST"])
def new_post():
    data = request.json
    new = {
        "id": len(posts) + 1,
        "user_id": 1,
        "user": "You",
        "avatar": "YO",
        "type": data.get("type", "offer"),
        "title": data.get("title", ""),
        "description": data.get("description", ""),
        "category": data.get("category", "Other"),
        "location": data.get("location", "Nepal"),
        "time": "Just now",
        "likes": 0,
        "comments": 0,
    }
    posts.insert(0, new)
    return jsonify({"success": True, "post": new})
 
@app.route("/api/post/<int:post_id>/like", methods=["POST"])
def like_post(post_id):
    for p in posts:
        if p["id"] == post_id:
            p["likes"] += 1
            return jsonify({"success": True, "likes": p["likes"]})
    return jsonify({"success": False}), 404
 
if __name__ == "__main__":
    app.run(debug=True, port=5000)