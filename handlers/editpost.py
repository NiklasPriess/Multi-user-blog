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

# Handler in order to submit blog post edits/deletes
class EditPost(BlogHandler):

    @post_exists
    def get(self, post_id, post):
        self.render(
            "editpost.html",
            post=post,
            user=self.user,
            uid=self.uid)

    @post_exists
    def post(self, post_id, post):
        content = self.request.get("content")
        subject = self.request.get("subject")
        action = self.request.get("action")

        # Depending on user submission either edit the post, delete the post
        # or cancel the edit
        if action == "submit":

            # Update Post databank with edited post and redirect to permalink
            if subject and content:
                post.content = content
                post.subject = subject
                post.put()
                self.redirect("/blog/%s" % str(post.key.id()))
            else:
                error = "subject and content please!"
                self.render(
                    "editpost.html",
                    post=post,
                    user=self.user,
                    subject=subject,
                    content=content,
                    error=error)

        # Cancel edit and redirect to MainPage
        if action == "cancel":
            self.redirect("/")

        # Delete post
        if action == "delete":
            post.key.delete()
            time.sleep(0.2)
            self.redirect("/")