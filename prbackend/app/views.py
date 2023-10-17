from django.shortcuts import render
from rest_framework.views import APIView
from .models import *
from rest_framework.response import Response
from .serializers import *
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.db.models import Q

# Create your views here.


@api_view(['GET'])
def getData(request):
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def postData(request):
    serializer = UserSerializer(data=request.data)
    # print("________________",request.data.username)
    if serializer.is_valid():
        serializer.save()
        return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
    else:
        return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)



# @api_view(['POST'])
# def LoginAPIView(request):
#     username = request.data.get('username')
#     password = request.data.get('password')
#
#     user = authenticate(request, username=username, password=password)
#     if user is not None:
#         login(request, user)
#         serializer = UserSerializer(user)
#         return Response(serializer.data, status=status.HTTP_200_OK)
#     else:
#         return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)


@api_view(['POST'])
def LoginAPIView(request):
    if request.method == 'POST':
        data = request.data
        username = data.get("username")
        password = data.get("password")

        # user = authenticate(request, username=username, password=password)
        user = User.objects.filter(username=username, password=password)
        if user:
            for x in user:
                # request.session['id'] = x.id
                role = x.role

            return Response({"status": "success","role":role})
        else:
            return Response({"status": "error", "message": "Invalid username or password."}, status=status.HTTP_401_UNAUTHORIZED)
    else:
        return Response({"status": "error", "message": "Invalid request method."}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def Listprojects(request):
    projects = Projects.objects.all()
    serializer = PojectSerializer(projects, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def Listemployees(request):
    employees = User.objects.all().filter(role='employee')
    serializer = UserSerializer(employees, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getemployee_updates(request, id):
    employees = User.objects.all().filter(id=id)
    serializer = UserSerializer(employees, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def Listemployees_projectassign(request, projectId):
    projects = Members.objects.all().filter(projectID=projectId)
    user_ids = [item.userID.values_list('id', flat=True) for item in projects]
    user_ids = [id for ids in user_ids for id in ids]
    print("user_ids", user_ids)
    # employees = User.objects.exclude(id__in=user_ids)
    employees = User.objects.exclude(Q(id__in=user_ids) | Q(role='Manager') | Q(role='HR'))
    serializer = UserSerializer(employees, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def AddprojectData(request):
    project_name = request.data.get('project_name')
    existing_project = Projects.objects.filter(project_name=project_name).first()
    if existing_project:
        # If a project with the same name already exists, return an error response
        return Response({"status": "error", "message": "Project name already exists"},
                        status=status.HTTP_400_BAD_REQUEST)

    serializer = PojectSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
    else:
        return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def AddemployeeData(request):
    data = request.data
    existing_employee = User.objects.filter(empID=data['empID']).first()
    if existing_employee:
        serializer = UserSerializer(existing_employee)
        return Response({"status": "error", "data": "EmployeeID already exists"}, status=status.HTTP_409_CONFLICT)

    serializer = UserSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
    else:
        return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
@api_view(['DELETE'])
def deleteproject(request, projectId):
    data = request.data
    Projects.objects.filter(id=projectId).delete()
    return Response({"status": "success"})

@api_view(['DELETE'])
def deleteuser(request, userID):
    data = request.data
    User.objects.filter(id=userID).delete()
    return Response({"status": "success"})

@api_view(['GET'])
def projectdetailview(request, projectId):
    project_data = Projects.objects.filter(id=projectId)
    serializer = PojectSerializer(project_data, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def assignedemployeedata(request, projectId):
    employees = Members.objects.filter(projectID=projectId)
    serializer = MemberSerializer(employees, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def Assignproject_team(request):
    print("POstttttt",request.data)
    serializer = MemberSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
    else:
        return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
def UpdateUser(request, id):
    try:
        user = User.objects.get(id=id)
    except User.DoesNotExist:
        return Response({"status": "error", "detail": "User not found"}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        serializer = UserSerializer(user, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

