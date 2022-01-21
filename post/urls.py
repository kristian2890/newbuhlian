from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from post.views import * #index, bloghome, contact, blogpost, contact, portfolio, project, resume #,services  blogpost, bloghome_alt


urlpatterns = [
    path('', index, name='post-list'),
    path('post/<id>/<title>', blogpost, name='post-detail'),
    path('bloghome/', bloghome, name='bloghome'),
    path('contact/', contact, name='contact'),
    path('portfolio/', portfolio, name='portfolio'),
    path('resume/', resume, name='resume'),
    path('tinymce/', include('tinymce.urls')),
    path('project/', project, name='project'),
    path('portfolio/project/cro-pdp-few-left-product-tags', project0, name='project0'),
    path('portfolio/project/cro-voucher-test', project1, name='project1'),
    path('portfolio/project/cro-pdp-sticky-cta', project2, name='project2'),
    path('portfolio/project/web-data-privacy-engineering', project3, name='project3'),
    path('portfolio/project/datascience-cac-cltc', project4, name='project4'),
    path('portfolio/project/datascience-nps-lifetime', project5, name='project5'),
    path('portfolio/project/datascience-nps-drivers', project6, name='project6'),
    path('portfolio/project/datascience-product-descriptions', project7, name='project7'),
    path('portfolio/project/datascience-on-the-fence-users-popup', project8, name='project8'),
    path('portfolio/project/cro-checkout-urgency-message', project13, name='project13'),
    path('portfolio/project/cro-a2r-recommendation-popup', project15, name='project15'),

]  

