from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404
from .models import Students, StudentsPNo
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
