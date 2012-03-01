from django.conf.urls.defaults import patterns, include, url
import views

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'face.views.home', name='home'),
    # url(r'^face/', include('face.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    ('^$', views.index),
    ('^login$', views.index),
    ('^about$', views.about),
#    ('account/create$', views.create_account),
    ('account/logout$', views.logout),
    ('^build-acct$', views.build_acct),
    ('dash$', views.dash),
    ('^how$', views.howitworks),
    ('question/check$', views.check_q),
    ('question/files/(\d+)', views.get_question_file),
    ('question/view/(\d+)', views.view_question),
    ('question/view/all$', views.list_questions),
    ('question/status/(\d+)', views.question_status),
#    ('suggest$', views.suggest_q),
#    ('suggest/submit$', views.submit_suggestion),
    ('community$', views.community),
    ('community/add$', views.community_add),
    ('communty/add/submit$', views.submit_community_q),
    ('community/(\d+)', views.community_view),
    ('ajax/feedback/like/(\d+)/(\d+)', views.feedback_like),
    ('ajax/feedback/challenge/(\d+)/(\d+)', views.feedback_challenge),
    ('ajax/hints/basic/(\d+)', views.get_all_hints),
    ('ajax/hints/get/(\d+)/([a-z0-9]+)', views.get_hint_details),
    ('ajax/hints/submit/(\d+)', views.submit_hint),
    ('ajax/hints/vote/yes/([a-f0-9]+)', views.tally_vote, { 'vote' : True }),
    ('ajax/hints/vote/no/([a-f0-9]+)', views.tally_vote, { 'vote' : False }),
    ('^questions/list$', views.list_questions_with_api),
    ('^questions/(\d+)$', views.view_question_with_api),
    ('^questions', views.questions_unknown), # Redirect to /questions/list
    ('^api/questions/list$', views.api_questions_list),
    ('^api/questions/([0-9]+)$', views.api_questions_get),
    ('^api/hints/list/([0-9]+)$', views.api_hints_list),
    ('^api/hints/([0-9]+)/vote$', views.api_hints_vote),
    ('^api/hints/([0-9]+)$', views.api_hints_get),
    ('^api/questions/([0-9]+)/attempts/insert$', views.api_attempts_insert),
    ('^api/attempts/([0-9]+)$', views.api_attempts_get),
    ('^api/questions/([0-9]+)/attempts/list$', views.api_attempts_list),
    ('^api/community/questions/insert$', views.api_community_questions_insert),
    ('^api/community/questions/list$', views.api_community_questions_list),
    ('^api/community/questions/([0-9]+)$', views.api_community_questions_get),
    ('^system/tests/run$', views.system_tests_run),
    url(r'', include('social_auth.urls')),
)
