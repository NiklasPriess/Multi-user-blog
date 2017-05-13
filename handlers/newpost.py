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


# Handler in order to submit new Posts
class NewPost(BlogHandler):
    def get(self):
        if self.user:
            self.render("newpost.html", user=self.user)
        else:
            self.redirect("/blog/login")

    def post(self):
        content = self.request.get("content")
        subject = self.request.get("subject")

        # Save user entry in Post databank and redirect to permalink
        # If subject or content is missing rerender the page with errormessage
        if subject and content:
            p = Post(
                subject=subject,
                content=content,
                authorid=User.get_by_id(self.uid).key)
            p.put()

            self.redirect("/blog/%s" % str(p.key.id()))
        else:
            error = "subject and content please!"
            self.render(
                "newpost.html",
                user=self.user,
                subject=subject,
                content=content,
                error=error)
