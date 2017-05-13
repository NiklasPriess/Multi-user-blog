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


# Handler in order to like blog posts
class LikePost(BlogHandler):

    @post_exists
    def get(self, post_id, post):

        # Increase likes in databank +1 if user is logged in, has not liked
        # the post yet and is not the author of the blogpost
        if self.user:
            name = self.user.name
            if name not in post.likedby and self.uid != post.authorid.id():
                post.likedby = post.likedby + [name]
                post.put()
                time.sleep(0.2)
        else:
            self.redirect("/blog/login")

        self.render("permalink.html", post=post, user=self.user, uid=self.uid)
