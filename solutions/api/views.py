from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from solutions.models import Entreprise_solution, Artisans_solution, Consultance_solution
from solutions.serializers import EntrepriseSolutionSerializer, ArtisansSolutionSerializer, ConsultanceSolutionserializer


from django.core.files.storage import default_storage

# Create your views here.
@csrf_exempt
def entrepriseSolutionApi(request, id=0):
    if request.method=='GET':
        entrepriseSolution = Entreprise_solution.objects.all()
        entrepriseSolution_serializer = EntrepriseSolutionSerializer(entrepriseSolution, many=True)
        return JsonResponse(entrepriseSolution_serializer.data, safe=False)

    elif request.method=='POST':
        entrepriseSolution_data=JSONParser().parse(request)
        entrepriseSolution_serializer = EntrepriseSolutionSerializer(data=entrepriseSolution_data)
        if entrepriseSolution_serializer.is_valid():
            entrepriseSolution_serializer.save()
            return JsonResponse("Added Successfully!!" , safe = False)
        return JsonResponse("Failed to Add.",safe=False)

    elif request.method=='PUT':
        entrepriseSolution_data = JSONParser().parse(request)
        entrepriseSolution = Entreprise_solution.objects.get(id = entrepriseSolution_data['id'])
        entrepriseSolution_serializer = EntrepriseSolutionSerializer(entrepriseSolution, data = entrepriseSolution_data)
        if entrepriseSolution_serializer.is_valid():
            entrepriseSolution_serializer.save()
            return JsonResponse("Updated Successfully!!", safe = False)
        return JsonResponse("Failed to Update.", safe=False)

    elif request.method=='DELETE':
        entrepriseSolution = Entreprise_solution.objects.get(id = id)
        entrepriseSolution.delete()
        return JsonResponse("Deleted Succeffully!!", safe = False)


@csrf_exempt
def artisansSolutionApi(request, id=0):
    if request.method=='GET':
        artisanSolution = Artisans_solution.objects.all()
        artisansSolutionSerializer = ArtisansSolutionSerializer(artisanSolution, many=True)
        return JsonResponse(artisansSolutionSerializer.data, safe = False)
    
    elif request.method == 'POST':
        artisanSolution_data = JSONParser().parse(request)
        artisansSolutionSerializer = ArtisansSolutionSerializer(data = artisanSolution_data)
        if artisansSolutionSerializer.is_valid():
            artisansSolutionSerializer.save()
            return JsonResponse('Add success!', safe=False)
        return JsonResponse("Failed to add.", safe=False)
    
    elif request.method=='PUT':
        artisanSolution_data = JSONParser().parse(request)
        artisanSolution = Artisans_solution.objects.get(id = artisanSolution_data['id'])
        artisansSolutionSerializer = ArtisansSolutionSerializer(artisanSolution, data= artisanSolution_data)
        if artisansSolutionSerializer.is_valid():
            artisansSolutionSerializer.save()
            return JsonResponse("Updated Successfully!!", safe = False)
        return JsonResponse("Failed to Update.", safe=False)

    elif request.method=='DELETE':
        artisanSolution = Artisans_solution.objects.get(id= id)
        artisanSolution.delete()
        return JsonResponse("Deleted Succeffully!!", safe = False)


@csrf_exempt
def consultantSolutionApi(request, id=0):
    if request.method=='GET':
        consultantSolution = Consultance_solution.objects.all()
        consultantSolutionSerializer = ConsultanceSolutionserializer(consultantSolution, many=True)
        return JsonResponse(consultantSolutionSerializer.data, safe=False)

    elif request.method == 'POST':
        consutantSolution_data = JSONParser().parse(request)
        consultantSolutionSerializer = ConsultanceSolutionserializer(data = consutantSolution_data)
        if artisansSolutionSerializer.is_valid():
            artisansSolutionSerializer.save()
            return JsonResponse('Add success!', safe=False)
        return JsonResponse("Failed to add.", safe=False)
    
    elif request.method=='PUT':
        consutantSolution_data = JSONParser().parse(request)
        consultantSolution = Consultance_solution.objects.get(id = consutantSolution_data['id'])
        consultantSolutionSerializer = ConsultanceSolutionserializer(consultantSolution, data= consutantSolution_data)
        if consultantSolutionSerializer.is_valid():
            consultantSolutionSerializer.save()
            return JsonResponse("Updated Successfully!!", safe=False)
        return JsonResponse("Failed to Update.", safe=False)

    elif request.method=='DELETE':
        consultantSolution = Consultance_solution.objects.get(id= id)
        consultantSolution.delete()
        return JsonResponse("Deleted Succeffully!!", safe = False)

@csrf_exempt
def SaveFile(request):
    file=request.FILES['uploadedFile']
    file_name = default_storage.save(file.name,file)

    return JsonResponse(file_name,safe=False)