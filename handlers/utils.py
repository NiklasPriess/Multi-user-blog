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
import os
import math
import re
import hashlib
import random
import hmac
import jinja2
import webapp2
import time
import utils
from string import letters
from google.appengine.ext import ndb
from functools import wraps


# Load jinja template
parent_dir = os.path.dirname(os.path.normpath(os.path.dirname(__file__)))
template_dir = os.path.join(parent_dir, 'template')
jinja_env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(template_dir),
    autoescape=True)

# Secret key for the HMAC
secret = "blobbyvolley"

# Validation of username, password and email
USER_RE = re.compile(r"^[a-zA-Z0-9_-]{3,20}$")
PW_RE = re.compile(r"^.{3,20}$")
Email_RE = re.compile(r"^[\S]+@[\S]+.[\S]+$")


def valid_username(username):
    return USER_RE.match(username)


def valid_pw(password):
    return PW_RE.match(password)


def valid_email(email):
    return not email or Email_RE.match(email)


# global functions
def render_str(template, **params):
    t = jinja_env.get_template(template)
    return t.render(params)


# functions to handle passwords and cookies (hashing and validation)
def make_secure_val(val):
    return '%s|%s' % (val, hmac.new(secret, val).hexdigest())


def check_secure_val(secure_val):
    val = secure_val.split('|')[0]
    if secure_val == make_secure_val(val):
        return val


def make_salt(length=5):
    return ''.join(random.choice(letters) for x in xrange(length))


def make_pw_hash(name, pw, salt=None):
    if not salt:
        salt = make_salt()
    h = hashlib.sha256(name + pw + salt).hexdigest()
    return '%s,%s' % (salt, h)


def valid_pw_hash(name, password, h):
    salt = h.split(',')[0]
    return h == make_pw_hash(name, password, salt)


# Decoraters in order to check if post/comment exists, if the user is
# logged in and if the user owns the post/comment
def post_exists(function):
    @wraps(function)
    def wrapper(self, *args, **kwargs):
        key = ndb.Key('Post', int(args[0]))
        post = key.get()
        if post:
            print(post)
            return function(self, args[0], post)
        else:
            self.error(404)
            return
    return wrapper