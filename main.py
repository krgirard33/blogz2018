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
    return render_template('allpost.html', all_posts=all_posts)

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
        # flash('New post added')
    
    return redirect('/blog')

@app.route('/singlepost', methods=['GET','POST'])
def single_post():
    # TODO: Look at delete_task in get-it-done
    post_ided = Blog.query.get(id)
    singlepost="?id="+ post_ided
    print(singlepost)
    return redirect('/blog{singlepost}' .format(singlepost=singlepost))

if __name__ == '__main__':
    app.run()