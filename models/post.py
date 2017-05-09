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
import user
from utils import *
from google.appengine.ext import db



# Setting databank properties for Post databank
class Post(db.Model):


    subject = db.StringProperty(required=True)
    content = db.TextProperty(required=True)
    authorid = db.IntegerProperty(required=True)
    author = db.StringProperty(required=True)
    comment = db.StringListProperty()
    likedby = db.StringListProperty()
    created = db.DateTimeProperty(auto_now_add=True)
    last_modified = db.DateTimeProperty(auto_now=True)


    @property
    def likes(self):
        return self.likecount


    # Function in order to render posts appropriately
    def render(self):
        self._render_text = self.content.replace("\n", "<br>")
        return render_str("renderpost.html", p=self)

    # Function in order to render comments appropriately
    # Post.comment is list with: [user, comment, user, comment ...]
    def renderc(self):
        comment = range(len(self.comment))
        for i in range(1, len(self.comment), 2):
            comment[i - 1] = self.comment[i - 1]
            comment[i] = self.comment[i].replace("\n", "<br>")
        return comment