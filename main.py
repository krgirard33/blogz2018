from flask import Flask, request, redirect, render_template, flash
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://build-a-blog:ChinaIsADog@localhost:8889/build-a-blog'
app.config['SQLALCHEMY_ECHO'] = True
db = SQLAlchemy(app)
app.secret_key='OICU812-WadUthink?'
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


@app.route('/blog', methods=['POST', 'GET'])
def blog_total():
    if request.method == 'GET' and request.args.get('id'):
        id = request.args.get('id')
        all_posts = Blog.query.filter_by(id=id).all()
        return render_template('allpost.html', all_posts=all_posts)
    else:
        all_posts=Blog.query.order_by(Blog.id).all()
        return render_template('allpost.html', all_posts=all_posts)

@app.route('/newpost')
def display_newpost_form():
    title=''
    body=''
    return render_template('newpost.html',title=title,body=body)

@app.route('/newpost', methods=['POST', 'GET'])
def new_post():
    if request.method == 'POST':
        title = request.form['title']
        body = request.form['body']
        if title and body:
            title = title
            body = body
            new_post = Blog(title, body)
            db.session.add(new_post)
            db.session.commit()
            flash("New post added")
            # all_posts = Blog.query.order_by(id).all()
            id = new_post.id
            all_posts = Blog.query.filter_by(id=id).all()
            id = str(id)
            return redirect('/blog?id='+id)
        else:
            flash("We need a title and text in the body of the post")
            return render_template('newpost.html',title=title,body=body)


@app.route('/singlepost', methods=['GET','POST'])
def single_post():
    # TODO: Look at delete_task in get-it-done
    post_ided = Blog.query.get(id)
    print(post_ided)
    singlepost="?id="+ post_ided
    print(singlepost)
    return redirect('/blog{singlepost}' .format(singlepost=singlepost))

if __name__ == '__main__':
    app.run()