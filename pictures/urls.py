from django.http import HttpResponse,Http404
from django.conf.urls import url
from . import views

urlpatterns=[
    url('^$', views.welcome,name='welcome'),
    url('^today/$',views.pictures_of_day,name='picturesToday'),
    url(r'^archives/(\d{4}-\d{2}-\d{2})/$',views.past_days_pictures,name = 'pastPictures')
]

#Conversion
def convert_dates(dates):

    # Function that gets the weekday number for the date.
    day_number = dt.date.weekday(dates)

    days = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday',"Sunday"]

    # Returning the actual day of the week
    day = days[day_number]
    return day

def pictures_of_day(request,):
    date = dt.date.today()

    # FUNCTION TO CONVERT DATE OBJECT TO FIND EXACT DAY
    day = convert_dates(date)
    html = f'''
        <html>
            <body>
                <h1>Pictures for {day} {date.day}-{date.month}-{date.year}</h1>
            </body>
        </html>
            '''
    return HttpResponse(html) 

