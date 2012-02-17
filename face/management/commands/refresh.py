import face.models.models as regis
import face.offline.QuestionParser as qp
import face.offline.ParserTools.ParserTools as ParserTools

import json, datetime

from django.core.management.base import BaseCommand, CommandError

class Command(BaseCommand):
    args = 'none'
    help = 'Wipes out all instances of a particular template so that they can be regenerated by the parseall script.'

    def handle(self, *args, **options):
        template = regis.QuestionTemplate.objects.get(id=args[0])
        questions = regis.Question.objects.filter(template=template).exclude(status='solved')
        
        print 'Purging all unsolved instances of %s...' % template.title
        print '  %d target instances found.' % len(questions)

        for question in questions:
            question.status = 'retired'
            question.save()
            
        print 'Done.'