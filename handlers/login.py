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


# Handler for Login submissions
class Login(BlogHandler):
    def get(self):
        uid = (self.read_secure_cookie("user_id"))
        self.render("login.html", uid=uid)

    def post(self):
        uid = (self.read_secure_cookie("user_id"))
        username = self.request.get('username')
        password = self.request.get('password')

        # If login correct redirect to Welcome page else rerender page
        u = User.login(username, password)
        if u:
            self.login(u)
            self.redirect("/blog/welcome")
        else:
            msg = "Invalid login"
            self.render(
                "login.html",
                uid=uid,
                username=username,
                error=msg)
