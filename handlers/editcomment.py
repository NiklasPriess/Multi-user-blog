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
from models import Comment
from bloghandler import BlogHandler



# Handler in order to submit blog commment edits/deletes
class EditComment(BlogHandler):
    @user_logged_in
    @comment_exists
    @user_owns_comment
    def get(self, comment_id, uid, comment):
        self.render(
            "editcomment.html",
            comment=comment,
            uid=uid)

    @user_logged_in
    @comment_exists
    @user_owns_comment
    def post(self, comment_id, uid, comment):
        content = self.request.get("content")
        action = self.request.get("action")

        # Depending on user submission either edit the post, delete the post
        # or cancel the edit
        if action == "submit":

            # Update Post databank with edited post and redirect to permalink
            if content:
                comment.content = content
                comment.put()
                self.redirect("/")
            else:
                error = "Content please!"
                self.render(
                    "editcomment.html",
                    comment=comment,
                    content=content,
                    error=error)

        # Cancel edit and redirect to MainPage
        if action == "cancel":
            self.redirect("/")

        # Delete post
        if action == "delete":
            post = comment.postid.get()
            post.comments.remove(comment.key)
            post.put()
            comment.key.delete()
            time.sleep(0.2)
            self.redirect("/")
