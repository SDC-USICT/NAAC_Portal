import json

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods

from awards.models import Awards
from extra_activities.models import Extra
from guest_lecturer.models import GuestLecturer
from moab.models import Membership
from patents.models import *
from professional_details.models import *
from project.models import *
from publication_details.models import *
from subjects_taken.models import *
from workshop.models import *  # add rebase--continue

@csrf_exempt
@require_http_methods(["GET", "POST"])
def schools(request):
    schools = [
        'usict',
        'uslls',
        'usct',
        'usbt'
    ]

    return JsonResponse(schools, safe=False)

@csrf_exempt
@require_http_methods(["GET", "POST"])
def sections(request):
    sections = [
        'Awards',
        'Extra Activities',
        'Guest Lecturer',
        'MOAB',
        'Patents',
        'PhD Students',
        'Professional Details',
        'Projects',
        'Publication Details',
        'Subjects Taken'
    ]

    return JsonResponse(sections, safe=False)


@csrf_exempt
@require_http_methods(["GET", "POST"])
def login(request):
    request = json.loads(request.body.decode('utf-8'))
    username = request['empid']
    password = request['password']

    try:
        e = Employee.objects.get(instructor_id=username)
        a, created = Employee.objects.get(instructor_id=e, password=password)
        a.save()
        res = {
            'success' : 'true',
        }
    except Exception:
        res = {
            'error' : 'true'
        }

    return JsonResponse(res, safe=False)


@csrf_exempt
@require_http_methods(["GET", "POST"])
def awards(request):
    request = json.loads(request.body.decode('utf-8'))
    username = request['empid']
    title = request['title']
    org = request['organisation']
    month = request['month']
    year = request['year']

    try:
        e = Employee.objects.get(instructor_id=username)
        a, created = Awards.objects.update_or_create(instructor_id=e,title= title, organisation= org, month= month, year= year)
        a.save()
        res = {
            'success' : 'true',
        }
    except Exception:
        res = {
            'error' : 'true'
        }
    return JsonResponse(res, safe=False)


@csrf_exempt
@require_http_methods(["GET", "POST"])
def employee(request):
    request = json.loads(request.body.decode('utf-8'))
    username = request['empid']
    name = request['name']
    email = request['email']
    phone = request['phone']
    designation = request['designation']
    date_join = request['date_of_joining']
    romm = request['room_no']
    school = request['school']
    password = request['password']

    try:
        e = Employee.objects.get(instructor_id=username)
        a, created = Employee.objects.update_or_create(instructor_id=e,name= name, email= email, phone= phone, designation= designation,date_of_joining=date_join,room_no=romm,school=school,password=password)
        a.save()
        res = {
            'success' : 'true',
        }
    except Exception:
        res = {
            'error' : 'true'
        }
    return JsonResponse(res, safe=False)

@csrf_exempt
@require_http_methods(["GET", "POST"])
def extra(request):
    request = json.loads(request.body.decode('utf-8'))
    username = request['empid']
    name = request['name']
    dept = request['department']
    details = request['details']
    year = request['year']

    try:
        e = Employee.objects.get(instructor_id=username)
        a, created = Extra.objects.update_or_create(instructor_id=e,name= name, department= dept, details= details, year= year)
        a.save()
        res = {
            'success' : 'true',
        }
    except Exception:
        res = {
            'error' : 'true'
        }
    return JsonResponse(res, safe=False)


@csrf_exempt
@require_http_methods(["GET", "POST"])
def guest(request):
    request = json.loads(request.body.decode('utf-8'))
    username = request['empid']
    nature = request['nature']
    inst = request['institute']
    date = request['date']
    topic = request['topic']

    try:
        e = Employee.objects.get(instructor_id=username)
        a, created = GuestLecturer.objects.update_or_create(instructor_id=e,nature= nature, institute= inst, date= date, topic= topic)
        a.save()
        res = {
            'success' : 'true',
        }
    except Exception:
        res = {
            'error' : 'true'
        }
    return JsonResponse(res, safe=False)


@csrf_exempt
@require_http_methods(["GET", "POST"])
def moab(request):
    request = json.loads(request.body.decode('utf-8'))
    username = request['empid']
    type = request['type']
    acad_body = request['academic_body']
    univ = request['university_agency']

    try:
        e = Employee.objects.get(instructor_id=username)
        a, created = Membership.objects.update_or_create(instructor_id=e,type= type, academic_body= acad_body, university_agency= univ)
        a.save()
        res = {
            'success' : 'true',
        }
    except Exception:
        res = {
            'error' : 'true'
        }
    return JsonResponse(res, safe=False)


@csrf_exempt
@require_http_methods(["POST"])
def professional(request):
    request = json.loads(request.encode('utf-8'))

    empid_id = request['empid']
    academic_experience_id = request['academic_experience']
    industrial_exp_id = request['industrial_exp']
    qualification_before = request['qualification_before']
    qualification_after =  request['qualification_after']
    phds_id = request['phds']
    pursuing_id = request['pursuing']
    submitted_id = request['submitted']
    awarded_id = request['awarded']
    year_id = request['year']

    try:
        e = Employee.objects.get(instructor_id=empid_id)
        a, created = Professional.objects.update_or_create(instructor_id=e,academic_experience= academic_experience_id,
                                                         industrial_exp= industrial_exp_id, qualification_before= qualification_before,
                                                         qualification_after=qualification_after,phds=phds_id,pursuing=pursuing_id,
                                                         submitted=submitted_id,awarded=awarded_id,year= year_id)
        a.save()
        res = {
            'success' : 'true',
        }
    except Exception:
        res = {
            'error' : 'true'
        }
    return JsonResponse(res, safe=False)


@csrf_exempt
@require_http_methods(["POST"])
def workshop(request):
    request = json.loads(request.encode('utf-8'))

    empid_id = request['empid']
    name_id = request['name']
    date_id = request['date']
    duration_id = request['duration']
    organization_id =  request['organization']

    try:
        e = Employee.objects.get(instructor_id=empid_id)
        a, created = Workshop.objects.update_or_create(instructor_id=e,name= name_id,
                                                         date= date_id, duration= duration_id,
                                                         organisation=organization_id)
        a.save()
        res = {
            'success' : 'true',
        }
    except Exception:
        res = {
            'error' : 'true'
        }
    return JsonResponse(res, safe=False)


@csrf_exempt
@require_http_methods(["POST"])
def projects(request):
    request = json.loads(request.encode('utf-8'))

    username = request['empid']
    title_id = request['title']
    pi_id = request['pi']
    copi_id = request['copi']
    sponsors_id = request['sponsors']
    date_of_award_id =  request['date_of_award']
    date_completed_id =  request['date_completed']
    amnt_sanctioned_id =  request['amnt_sanctioned']
    status_id =  request['status']

    try:
        e = Employee.objects.get(instructor_id=username)
        a, created = Projects.objects.update_or_create(instructor_id=e,title=title_id,pi=pi_id,
                                              copi=copi_id,sponsors=sponsors_id,date_of_award=date_of_award_id,
                                              date_completed=date_completed_id,amnt_sanctioned=amnt_sanctioned_id,
                                              status=status_id)
        a.save()
        res = {
            'success' : 'true'
        }
    except Exception:
        res = {
            'error' : 'true'
        }
    return JsonResponse(res, safe=False)


@csrf_exempt
@require_http_methods(["POST"])
def patents(request):
    request = json.loads(request.encode('utf-8'))

    username = request['empid']
    name_id = request['name']
    patenting_agency_id = request['patenting_agency']
    year_application_id = request['year_application']
    year_grant_id =  request['year_grant']


    try:
        e = Employee.objects.get(instructor_id=username)
        a, created = Patents.objects.update_or_create(instructor_id=e,name=name_id,patenting_agency=patenting_agency_id,
                                             year_application=year_application_id,year_grant=year_grant_id)
        a.save()
        res = {
            'success' : 'true'
        }
    except Exception:
        res = {
            'error' : 'true'
        }
    return JsonResponse(res, safe=False)


@csrf_exempt
@require_http_methods(["POST"])
def subject(request):
    request = json.loads(request.encode('utf-8'))

    name = request['name']
    code = request['code']
    credit = request['credit']


    try:
        a, created = Subject.objects.update_or_create(name=name,code=code,credit=credit)
        a.save()
        res = {
            'success' : 'true'
        }
    except Exception:
        res = {
            'error' : 'true'
        }
    return JsonResponse(res, safe=False)


@csrf_exempt
@require_http_methods(["POST"])
def subjectTaken(request):
    request = json.loads(request.encode('utf-8'))

    username = request['empid']
    subjects = request['subjects']
    year = request['year']
    school = request['school']


    try:
        e = Employee.objects.get(instructor_id=username)
        a, created = SubjectsTaken.objects.update_or_create(instructor_id=e,subjects=subjects,year=year,school=school)
        a.save()
        res = {
            'success' : 'true'
        }
    except Exception:
        res = {
            'error' : 'true'
        }
    return JsonResponse(res, safe=False)


@csrf_exempt
@require_http_methods(["POST"])
def JournalPaper(request):
    request = json.loads(request.encode('utf-8'))

    username = request['empid']
    title_of_paper = request['title_of_paper']
    name_and_publisher = request['name_and_publisher']
    volume_no = request['volume_no']
    issn_isbn = request['issn_isbn']
    indexing = request['indexing']
    year = request['year']
    month = request['month']
    author = request['author']

    try:
        e = Employee.objects.get(instructor_id=username)
        a, created = JournalPapers.objects.update_or_create(instructor_id=e,title_of_paper=title_of_paper,
                                                            name_and_publisher=name_and_publisher,volume_no=volume_no,
                                                            issn_isbn=issn_isbn,indexing=indexing,year=year,month=month,author=author)
        a.save()
        res = {
            'success' : 'true'
        }
    except Exception:
        res = {
            'error' : 'true'
        }
    return JsonResponse(res, safe=False)


@csrf_exempt
@require_http_methods(["POST"])
def Conference(request):
    request = json.loads(request.encode('utf-8'))

    username = request['empid']
    title_of_paper = request['title_of_paper']
    name_and_publisher = request['name_and_publisher']
    volume_no = request['volume_no']
    issn_isbn = request['issn_isbn']
    indexing = request['indexing']
    year = request['year']
    month = request['month']
    author = request['author']
    international_national = request['international_national']

    try:
        e = Employee.objects.get(instructor_id=username)
        a, created = Conference.objects.update_or_create(instructor_id=e,title_of_paper=title_of_paper,
                                                            name_and_publisher=name_and_publisher,volume_no=volume_no,
                                                            issn_isbn=issn_isbn,indexing=indexing,year=year,month=month,
                                                            international_national=international_national,author=author)
        a.save()
        res = {
            'success' : 'true'
        }
    except Exception:
        res = {
            'error' : 'true'
        }
    return JsonResponse(res, safe=False)


@csrf_exempt
@require_http_methods(["POST"])
def BookChapter(request):
    request = json.loads(request.encode('utf-8'))

    username = request['empid']
    title_of_paper = request['title_of_paper']
    book_title_and_publisher = request['book_title_and_publisher']
    page_no = request['page_no']
    isbn = request['isbn']
    indexing = request['indexing']
    year = request['year']
    month = request['month']
    author = request['author']

    try:
        e = Employee.objects.get(instructor_id=username)
        a, created = BookChapters.objects.update_or_create(instructor_id=e,title_of_paper=title_of_paper,
                                                            book_title_and_publisher=book_title_and_publisher,page_no=page_no,
                                                            isbn=isbn,indexing=indexing,year=year,month=month,author=author)
        a.save()
        res = {
            'success' : 'true'
        }
    except Exception:
        res = {
            'error' : 'true'
        }
    return JsonResponse(res, safe=False)


@csrf_exempt
@require_http_methods(["POST"])
def BookChapter(request):
    request = json.loads(request.encode('utf-8'))

    username = request['empid']
    title_of_paper = request['title_of_paper']
    isbn = request['isbn']
    year = request['year']

    try:
        e = Employee.objects.get(instructor_id=username)
        a, created = Book.objects.update_or_create(instructor_id=e,title_of_paper=title_of_paper,isbn=isbn,year=year,)
        a.save()
        res = {
            'success' : 'true'
        }
    except Exception:
        res = {
            'error' : 'true'
        }
    return JsonResponse(res, safe=False)