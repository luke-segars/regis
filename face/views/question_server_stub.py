from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
from django.http import HttpResponse
from django.template.loader import get_template
from django.template import Context


import urllib2 # for Django requests to third party servers 
import json, datetime
import face.util.UserStats as UserStats
import face.models.models as models
import face.msg.msghub as msghub
import face.util.exceptions as exception
import face.util.QuestionManager as qm



QUESTION_SERVER = 'http://localhost:8080/question_server'

def questions(request):
    questions = []
    for x in xrange(10):
        questions.append( {
            "id" : x,
            "kind" : "question",
            "content" : "question%d" % x,
        } )
    return HttpResponse(json.dumps(questions), mimetype='application/json')



