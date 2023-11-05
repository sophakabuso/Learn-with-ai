from flask import Blueprint
quizzes = Blueprint('quizzes', __name__)

@quizzes.route('/quiz')
def quiz():
    return "Quiz Page"