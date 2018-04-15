from flask import Flask, request, redirect, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://build-a-blog:ChinaIsADog@localhost:8889/build-a-blog'
app.config['SQLALCHEMY_ECHO'] = True
db = SQLAlchemy(app)
secret_key='OICU812-WadUthink?'
# added the current time to use later on, might need an import
# current_time = datetime.datetime.utcnow()

class Blog(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120))
    body = db.Column(db.String(1200))
    # created = Column(DateTime, default=datetime.datetime.utcnow())
    

    def __init__(self, title, body):
        self.title = title
        self.body = body


@app.route('/blog', methods=['POST','GET'])
def blog_total():
    all_posts=Blog.query.order_by(Blog.id).all()
    print(all_posts)
    return render_template('allpost.html',all_posts=all_posts)

@app.route('/newpost')
def display_newpost_form():
    title=''
    body=''
    title_error=''
    body_error=''
    return render_template('newpost.html',title=title,body=body,title_error=title_error,
                body_error=body_error)

@app.route('/newpost', methods=['POST', 'GET'])
def new_post():
    '''title = request.form('title')
    body = request.form('body')
    title_error=''
    body_error=''
    '''

    if request.method == 'POST':
        title = request.form['title']
        body = request.form['body']
        new_post = Blog(title, body)
        db.session.add(new_post)
        db.session.commit()
    
    return redirect('/blog')

    @app.route('/blog?id=')
    def single_post():
        singlepost = Blog.get_by_id(int(id))
        return render_template('singlepost.html',singlepost=singlepost,title=title,body=body)


    '''
        if not title:
            title_error = 'Please give it a title'
        if not body:
            body_error = 'Please write something'
    
        if title_error or body_error:
            return render_template('newpost.html',title=title,body=body,title_error=title_error,
                body_error=body_error)
        else:
            title = request.form('title')
            body = request.form('body')
            new_post = Blog(title, body)
            db.session.add(new_post)
            db.session.commit()
        all_posts = Blog.query.order_by(id).all()
        return render_template('allpost.html')
        

    
    return render_template('newpost.html')
    '''

'''
@app.route('/', methods=['POST', 'GET'])
def index():

    if request.method == 'POST':
        task_name = request.form['task']
        new_task = Task(task_name)
        db.session.add(new_task)
        db.session.commit()

    tasks = Task.query.filter_by(completed=False).all()
    completed_tasks = Task.query.filter_by(completed=True).all()
    return render_template('todos.html',title="Get It Done!", 
        tasks=tasks, completed_tasks=completed_tasks)


@app.route('/delete-task', methods=['POST'])
def delete_task():

    task_id = int(request.form['task-id'])
    task = Task.query.get(task_id)
    task.completed = True
    db.session.add(task)
    db.session.commit()

    return redirect('/')
'''

if __name__ == '__main__':
    app.run()