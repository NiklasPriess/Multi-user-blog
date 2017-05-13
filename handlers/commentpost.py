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
from models import Comment
from bloghandler import BlogHandler


# Handler in order to submit comments on blog posts
class CommentPost(BlogHandler):

    @post_exists
    def get(self, post_id, post):
        self.render("comment.html", user=self.user)


    @post_exists
    def post(self, post_id, post):
        comment = self.request.get("comment")

        # Save comment and user Post.comment and redirect to MainPage
        # In case of no comment rerender the page with errormessage
        if comment:
            c = Comment(
                content=comment,
                authorid=User.get_by_id(self.uid).key,
                postid=post.key
                )
            c.put()
            print(c.key)
            post.comments = post.comments +[c.key]
            post.put()
            print(post.comments)
            time.sleep(0.2)
            self.redirect("/")
        else:
            error = "Enter comment please!"
            self.render(
                "comment.html",
                user=self.user,
                comment=comment,
                error=error)