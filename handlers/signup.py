# Copyright 2016 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# Parts of this code have been taken from the udacity course material

# Import libraries
from utils import *
from models import User
from models import Post
from bloghandler import BlogHandler


# Handler for Signup submissions
class Signup(BlogHandler):
    def get(self):
        self.render("signup.html", user=self.user)

    def post(self):
        self.username = self.request.get("username")
        self.password = self.request.get("password")
        self.verify = self.request.get("verify")
        self.email = self.request.get("email")

        error = ""
        errorpw = ""
        erroremail = ""
        have_error = False

        if self.verify == self.password:
            errorverify = ""
        else:
            errorverify = "Passwords did not match"
            have_error = True

        # Display error message if validation of username, password or email
        # fails
        if valid_username(self.username) is None:
            error = "Invalid username"
            have_error = True

        if valid_pw(self.password) is None:
            errorpw = "Invalid password"
            have_error = True

        if valid_email(self.email) is None:
            erroremail = "Invalid email"
            have_error = True

        # if validation of all form submissions is correct redirect to Welcome
        # page
        if have_error:
            self.render(
                "signup.html",
                user=self.user,
                username=self.username,
                email=self.email,
                password=self.password,
                error=error,
                errorpw=errorpw,
                errorverify=errorverify,
                erroremail=erroremail)
        else:
            self.done()

    def done(self):
        # make sure the user doesn`t already exist
        # if it's a new user store his data in User databank and log him in
        u = User.by_name(self.username)
        if u:
            msg = "That user already exists."
            self.render(
                "signup.html",
                user=self.user,
                username=self.username,
                password=self.password,
                verify=self.verify,
                email=self.email,
                error=msg)
        else:
            u = User.register(self.username, self.password, self.email)
            u.put()

            self.login(u)
            self.redirect("/blog/welcome")