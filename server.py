from flask import Flask, render_template, request
from forms import SignUpForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'finlab'

@app.route('/')
def home():
    return render_template('home.html', author="Rasyid", sunny=False)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/blog')
def blog():
    posts = [{'title':'Flask Introduction', 'author':'Avi'},
            {'title':'Learn Geopandas', 'author':'Lathif'}]
    return render_template('blog.html', posts=posts)

@app.route('/blog/<string:blog_id>')
def blogpost(blog_id):
    return 'This is blog post number ' + blog_id

@app.route('/admin', methods=['GET','POST'])
def signin():
    form = SignUpForm()
    if form.is_submitted():
        result = request.form
        return render_template('dashboard.html', result=result)
    return render_template('admin.html', form=form)

if __name__ == '__main__':
    app.run()
