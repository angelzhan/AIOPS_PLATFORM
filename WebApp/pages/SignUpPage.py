'''
    SignUpPage.py Lib
    Written By Kyle Chen
    Version 20190401v1
'''

# import buildin pkgs
from flask_restful import Resource
from flask_login import login_user
from flask import redirect, request, \
                    render_template, Response, \
                    url_for

## import priviate pkgs
from SignUpForm import SignUpForm

## Sign Up Class
class SignUpPage(Resource):
    ## get method
    def get(self):
        form = SignUpForm()
        return(Response(render_template('SignUp.html', title="Sign Up", form = form)))

    ## post method
    def post(self):
        form = SignUpForm()
        if form.validate_on_submit():
            user_name = request.form.get('username', None)
            password1 = request.form.get('password1', None)
            password2 = request.form.get('password2', None)

        if password1 == password2:
            ## STOPPED HERE
            pass