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
import jinja2
import webapp2
from google.appengine.ext import db
from handlers import Welcome
from handlers import CommentPost
from handlers import EditPost
from handlers import LikePost
from handlers import Login
from handlers import Logout
from handlers import Signup
from handlers import MainPage
from handlers import NewPost
from handlers import PostPage
from models import User
from models import Post


app = webapp2.WSGIApplication([
    ("/", MainPage),
    ("/blog/welcome", Welcome),
    ("/blog/signup", Signup),
    ("/blog/([0-9]+)", PostPage),
    ("/blog/newpost", NewPost),
    ("/blog/login", Login),
    ("/blog/logout", Logout),
    ("/blog/editpost/([0-9]+)", EditPost),
    ("/blog/commentpost/([0-9]+)", CommentPost),
    ("/blog/likepost/([0-9]+)", LikePost),
], debug=True)
