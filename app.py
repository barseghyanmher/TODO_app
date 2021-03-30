from flask import Flask, render_template, request, redirect, url_for
from api import API
import datetime


app = Flask(__name__)
api = API()


@app.route("/")
def home():
    story_list = api.list_stories()
    return render_template("stories.html", story_list=story_list)


@app.route("/add", methods=["POST"])
def add():
    title = request.form.get("title")
    api.create_story(title)
    return redirect(url_for("home"))
 

@app.route("/story/<string:story>")
def story_more(story):
    return render_template("update_story.html", story=eval(story))


@app.route("/delete/<int:id>")
def delete(id):
    api.delete_story(id)
    return redirect(url_for("home"))


@app.route("/update_story/<int:id>", methods=["POST"])
def update_story(id):
    header = request.form.get("header")
    story_description = request.form.get("story_description")
    start_date = request.form.get("start_date")
    end_date = request.form.get("end_date")
    api.modify_story(id=id, header=header, story_description=story_description, 
                    start_date=start_date, end_date=end_date)
    return redirect(url_for("home"))


@app.route("/todos/<int:id>")
def todos(id):
    todo_list = api.list_todos(id)
    return render_template("todos.html", todo_list=todo_list, story_id=id)


@app.route("/add_todo/<int:id>", methods=["POST"])
def add_todo(id):
    title = request.form.get("title")
    api.create_to_do(story_id=id, header=title)
    return redirect(url_for("todos", id=id))


@app.route("/delete_todo/<int:story_id>/<int:id>")
def delete_todo(id,story_id):
    api.delete_to_do(id)
    return redirect(url_for("todos", id=story_id))


@app.route("/todo/<int:story_id>/<string:todo>")
def todo_more(story_id, todo):
    return render_template("update_todo.html", todo=eval(todo), story_id=story_id, statuses=api.status_dict)


@app.route("/update_todo/<int:story_id>/<int:id>", methods=["POST"])
def update_todo(id, story_id):
    header = request.form.get("header")
    to_do_description = request.form.get("to_do_description")
    start_date = request.form.get("start_date")
    end_date = request.form.get("end_date")
    to_do_status = request.form.get("to_do_status")
    api.modify_to_do(id=id, header=header, to_do_status=to_do_status, to_do_description=to_do_description, 
                    start_date=start_date, end_date=end_date)
    return redirect(url_for("todos", id=story_id))


if __name__ == "__main__":
    app.run(debug=True)
