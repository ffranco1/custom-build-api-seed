import os
from flask import Flask, url_for, jsonify, request
from flask import make_response
from flask.ext.sqlalchemy import SQLAlchemy

#basedir = os.path.abspath(os.path.dirname(__file__))
#db_path = os.path.join(basedir, '../data.sqlite')

app = Flask(__name__)
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + db_path
#connecting flask application to sql
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://localhost/mydb'
db = SQLAlchemy(app)


class ValidationError(ValueError):
    pass


class Student(db.Model):
    __tablename__ = 'students'
    id = db.Column(db.Integer, primary_key=True)
    score = db.Column(db.Integer)
    title = db.Column(db.String(500))
    author = db.Column(db.String(500))
    ups = db.Column(db.String(500))
    downs = db.Column(db.String(500))
    comments = db.Column(db.String(500))
    link = db.Column(db.String(500))

    def get_url(self):
        return url_for('get_student', id=self.id, _external=True)

    def export_data(self):
        return {
            'self_url': self.get_url(),
            'score':self.score,
            'title':self.title,
            'author':self.author,
            'ups':self.ups,
            'downs':self.downs,
            'comments':self.comments,
            'link':self.link

        }

    def import_data(self, data):
        try:
            self.score = data['score']
            self.title = data['title']
            self.author = data['author']
            self.ups = data['ups']
            self.downs = data['downs']
            self.comments = data['comments']
            self.link = data['link']
        except KeyError as e:
            raise ValidationError('Invalid student: missing ' + e.args[0])
        return self

@app.route('/students/', methods=['GET'])
def get_students():
    return jsonify({'students': [student.get_url() for student in
        Student.query.all()]})

@app.route('/students/<int:id>', methods=['GET'])
def get_student(id):
    return jsonify(Student.query.get_or_404(id).export_data())  


@app.route('/students/<int:id>', methods=['DELETE'])
def delete_student(id):
    user1 = Student.query.get_or_404(id).export_data
    db.session.delete(user1)
    db.session.commit()
    return jsonify({})

@app.route('/students/favoritepost', methods=['GET'])
def getfavoritepost():
    myquery = Student.query.order_by(Student.score.desc()).first()
    return jsonify(myquery.export_data())

    

@app.route('/students/franco')
def index():
    print ("this me debugging\n")
    return "whats up francisco\n"

@app.route('/students/', methods=['POST'])
def new_student():
    student = Student()
    student.import_data(request.json)
    db.session.add(student)
    db.session.commit()
    return jsonify({}), 201#,{'Location': student.get_url()}


@app.route('/students/<int:id>', methods=['PUT'])
def edit_student(id):
    student = Student.query.get_or_404(id)
    student.import_data(request.json)
    db.session.add(student)
    db.session.commit()
    return jsonify({})

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error':'Not found'}), 404)    


if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)


