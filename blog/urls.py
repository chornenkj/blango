
# other imports
from django.urls import path

import blog.views

urlpatterns = [
    # other patterns
    path('', blog.views.index),
    path('samples/', blog.views.samples, name='blog-samples'),
    path('post/<slug>/', blog.views.post_detail, name="blog-post-detail"),
]