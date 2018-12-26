#from django.contrib import admin

# Register your models here.

#from .models import Question

#admin.site.register(Question)
# above line = originally loaded from tutorial 2
#==============================================================

from django.contrib import admin

from .models import Choice, Question

#============================================
#class QuestionAdmin(admin.ModelAdmin):
#    #fields = ['pub_date', 'question_text']
#    fieldsets = [
#        (None,               {'fields': ['question_text']}),
#        ('Date information', {'fields': ['pub_date']}),
#    ]
#admin.site.register(Question, QuestionAdmin)
#admin.site.register(Choice)

#inefficient way of adding choice and using foreign key
#===========================================

#class ChoiceInline(admin.StackedInline):
#Stackedinline is hard to read as it takes space
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']
    search_fields = ['question_text']


admin.site.register(Question, QuestionAdmin)
