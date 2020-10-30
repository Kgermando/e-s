from django.urls import path

from documentations.views import doc_view, doc_view_detail

app_name = 'docs'

urlpatterns = [
    path('', doc_view, name='docs'),
    path('doc_detail/<slug:slug>/', doc_view_detail, name='doc_detail'),
]
