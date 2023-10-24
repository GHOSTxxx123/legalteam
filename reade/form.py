from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, IntegerField, SubmitField, BooleanField, PasswordField, SelectField, MultipleFileField
from flask_wtf.file import FileField, FileAllowed, FileRequired
from wtforms.validators import DataRequired, Length, NumberRange, ValidationError, Email

class BookForm(FlaskForm):
    title = StringField('Название', validators=[DataRequired(),
                                             Length(min=5, max=100)])
    author = StringField('Автор', validators=[DataRequired(),
                                             Length(min=5, max=100)])
    genre = StringField('Жанр', validators=[DataRequired(),
                                             Length(min=5, max=20)])
    cover = FileField('Обложка книги', validators=[FileAllowed(['jpg', 'png'])])
    bookpdf = FileField('Файл книги (pdf)', validators=[DataRequired(),
                                                            FileAllowed(['pdf'])])
    rating = IntegerField('Моя оценка', validators=[DataRequired(), NumberRange(min=1, max=5)])
    description = TextAreaField('Сюжет',
                                validators=[DataRequired(),
                                            Length(max=500)])
    notes = TextAreaField('Заметки',
                                validators=[DataRequired(),
                                            Length(max=500)])
    submit = SubmitField('Добавить')


