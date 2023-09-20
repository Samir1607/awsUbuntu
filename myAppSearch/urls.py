from django.urls import path
from .views import StudentsAPI, StudentAPI, StudentsSearch 
""", StudentsSearchN, search_models"""

urlpatterns = [
    path("student/", StudentsAPI.as_view(), name="students"),
    path("student/<int:id>/", StudentAPI.as_view(), name="student"),
    path("students/", StudentsSearch.as_view(), name="studentsearch"),
    # path("students/slug/<slug:slug>", StudentBySlugAPI.as_view(), name="studentSlug"),
    # path("student/search/", StudentsSearchN.as_view(), name="studentsearchN"),
    # path('search/', search_models, name='search_models'),
]
