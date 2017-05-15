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
from google.appengine.ext import ndb


# Setting databank properties for Post databank
class Comment(ndb.Model):

    content = ndb.TextProperty(required=True)
    authorid = ndb.KeyProperty(required=True)
    postid = ndb.KeyProperty(required=True)
    likedby = ndb.StringProperty(repeated=True)
    created = ndb.DateTimeProperty(auto_now_add=True)
    last_modified = ndb.DateTimeProperty(auto_now=True)

    @property
    def likes(self):
        likes = len(self.likedby)
        return likes

    # Function in order to render comments appropriately
    def render(self):
        self._render_text = self.content.replace("\n", "<br>")
        return self._render_text
