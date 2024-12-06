from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404
from .models import Students, StudentsPNo, Subject, Scores
import json

@csrf_exempt
def students_api(request, id=None):
    if request.method == 'GET':
        if id:  # GET a single student by ID
            student = get_object_or_404(Students, id=id)
            return JsonResponse({'id': student.id, 'roll_no': student.roll_no, 'name': student.name})
        else:  # GET all students
            students = list(Students.objects.values())
            return JsonResponse(students, safe=False)

    elif request.method == 'POST':
        data = json.loads(request.body)
        student = Students.objects.create(roll_no=data['roll_no'], name=data['name'])
        return JsonResponse({'id': student.id, 'roll_no': student.roll_no, 'name': student.name}, status=201)

    elif request.method == 'PUT':
        if id:  # Update the student with the provided ID
            data = json.loads(request.body)
            student = get_object_or_404(Students, id=id)
            student.roll_no = data['roll_no']
            student.name = data['name']
            student.save()
            return JsonResponse({'id': student.id, 'roll_no': student.roll_no, 'name': student.name})

    elif request.method == 'PATCH':  # Handle partial updates
        if id:  # Partial update of student by ID
            data = json.loads(request.body)
            student = get_object_or_404(Students, id=id)
            if 'roll_no' in data:  # Update only if provided
                student.roll_no = data['roll_no']
            if 'name' in data:  # Update only if provided
                student.name = data['name']
            student.save()
            return JsonResponse({'id': student.id, 'roll_no': student.roll_no, 'name': student.name})

    elif request.method == 'DELETE':
        if id:  # Delete the student with the provided ID
            student = get_object_or_404(Students, id=id)
            student.delete()
            return JsonResponse({'message': 'Student deleted successfully'})

@csrf_exempt
def students_pno_api(request):
    if request.method == 'GET':
        if 'id' in request.GET:  # Get phone numbers for a specific student
            student_id = request.GET['id']
            student = get_object_or_404(Students, id=student_id)
            students_pno = list(StudentsPNo.objects.filter(student=student).values())
            return JsonResponse(students_pno, safe=False)
        else:  # Get all phone numbers
            students_pno = list(StudentsPNo.objects.values())
            return JsonResponse(students_pno, safe=False)

    elif request.method == 'POST':
        data = json.loads(request.body)
        student = get_object_or_404(Students, id=data['id'])
        pno = StudentsPNo.objects.create(student=student, pno=data['pno'])
        return JsonResponse({'pno_id': pno.id, 'id': pno.student.id, 'pno': pno.pno}, status=201)

    elif request.method == 'PUT':
        data = json.loads(request.body)
        pno = get_object_or_404(StudentsPNo, id=data['pno_id'])
        pno.pno = data['pno']
        pno.save()
        return JsonResponse({'message': 'PNo updated successfully'})

    elif request.method == 'PATCH':  # Handle partial updates for phone numbers
        data = json.loads(request.body)
        if 'pno_id' in data:
            pno = get_object_or_404(StudentsPNo, id=data['pno_id'])
            if 'pno' in data:  # Update the phone number if provided
                pno.pno = data['pno']
                pno.save()
                return JsonResponse({'message': 'PNo updated successfully', 'pno_id': pno.id, 'pno': pno.pno})
            else:
                return JsonResponse({'error': 'Phone number not provided in request'}, status=400)
        else:
            return JsonResponse({'error': 'PNo ID not provided in request'}, status=400)

    elif request.method == 'DELETE':
        data = json.loads(request.body)
        pno = get_object_or_404(StudentsPNo, id=data['pno_id'])
        pno.delete()
        return JsonResponse({'message': 'PNo deleted successfully'})


@csrf_exempt
def subject_api(request, id=None):
    if request.method == 'GET':
        if id:  # Get single subject by ID
            subject = get_object_or_404(Subject, id=id)
            return JsonResponse({'id': subject.id, 'subject_name': subject.subject_name})
        else:  # Get all subjects
            subjects = list(Subject.objects.values())
            return JsonResponse(subjects, safe=False)

    elif request.method == 'POST':
        data = json.loads(request.body)
        subject = Subject.objects.create(subject_name=data['subject_name'])
        return JsonResponse({'id': subject.id, 'subject_name': subject.subject_name}, status=201)

    elif request.method == 'PUT':
        if id:
            data = json.loads(request.body)
            subject = get_object_or_404(Subject, id=id)
            subject.subject_name = data['subject_name']
            subject.save()
            return JsonResponse({'id': subject.id, 'subject_name': subject.subject_name})

    elif request.method == 'PATCH':
        if id:
            data = json.loads(request.body)
            subject = get_object_or_404(Subject, id=id)
            if 'subject_name' in data:
                subject.subject_name = data['subject_name']
            subject.save()
            return JsonResponse({'id': subject.id, 'subject_name': subject.subject_name})

    elif request.method == 'DELETE':
        if id:
            subject = get_object_or_404(Subject, id=id)
            subject.delete()
            return JsonResponse({'message': 'Subject deleted successfully'})


@csrf_exempt
def scores_api(request, id=None):
    if request.method == 'GET':
        if id:  # Get a single score by ID
            score = get_object_or_404(Scores, id=id)
            return JsonResponse({
                'id': score.id,
                'student': score.student.id,
                'subject': score.subject.id,
                'marks': score.marks
            })
        else:  # Get all scores
            scores = list(Scores.objects.values())
            return JsonResponse(scores, safe=False)

    elif request.method == 'POST':
        data = json.loads(request.body)
        student = get_object_or_404(Students, id=data['student_id'])
        subject = get_object_or_404(Subject, id=data['subject_id'])
        score = Scores.objects.create(student=student, subject=subject, marks=data['marks'])
        return JsonResponse({
            'id': score.id,
            'student': score.student.id,
            'subject': score.subject.id,
            'marks': score.marks
        }, status=201)

    elif request.method == 'PUT':
        if id:
            data = json.loads(request.body)
            score = get_object_or_404(Scores, id=id)
            student = get_object_or_404(Students, id=data['student_id'])
            subject = get_object_or_404(Subject, id=data['subject_id'])
            score.student = student
            score.subject = subject
            score.marks = data['marks']
            score.save()
            return JsonResponse({
                'id': score.id,
                'student': score.student.id,
                'subject': score.subject.id,
                'marks': score.marks
            })

    elif request.method == 'PATCH':
        if id:
            data = json.loads(request.body)
            score = get_object_or_404(Scores, id=id)
            if 'student_id' in data:
                score.student = get_object_or_404(Students, id=data['student_id'])
            if 'subject_id' in data:
                score.subject = get_object_or_404(Subject, id=data['subject_id'])
            if 'marks' in data:
                score.marks = data['marks']
            score.save()
            return JsonResponse({
                'id': score.id,
                'student': score.student.id,
                'subject': score.subject.id,
                'marks': score.marks
            })

    elif request.method == 'DELETE':
        if id:
            score = get_object_or_404(Scores, id=id)
            score.delete()
            return JsonResponse({'message': 'Score deleted successfully'})
