from django.http import JsonResponse
from core.models import SDGGoal, Project
from django.db.models import Q


def get_sdg(request):
    # Get the 'tags' parameter from the query string (allows multiple tags)
    tags = request.GET.getlist('tags')  # ?tags=income inequality&tags=education&tags=health

    if not tags:
        return JsonResponse({'error': 'No tags provided in the query parameters.'}, status=400)

    try:
        # Fetch all SDG data
        all_sdgs = SDGGoal.objects.all()

        # Filter the SDGs where any tag is found in the name, case-insensitive
        matching_sdgs = []
        for sdg in all_sdgs:
            for tag in tags:
                if tag.lower() in sdg.name.lower():
                    matching_sdgs.append({'name': sdg.name, 'code': sdg.code})
                    break  # Avoid duplicates if multiple tags match the same SDG

        if not matching_sdgs:
            return JsonResponse({'error': 'No matching SDGs found.'}, status=404)

        return JsonResponse({'sdgs': matching_sdgs}, status=200)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)


def get_projects_by_sdgs(request):
    # Get the SDG values from query parameters
    sdgs = request.GET.getlist('sdgs')  # Example: ?sdgs=sdg_1&sdgs=sdg_4&sdgs=sdg_13

    if not sdgs:
        return JsonResponse({'error': 'No SDGs provided in the query parameters.'}, status=400)

    # Ensure the SDGs provided match valid column names in the model
    valid_sdgs = [f"sdg_{i}" for i in range(1, 18)]
    invalid_sdgs = [sdg for sdg in sdgs if sdg not in valid_sdgs]
    
    if invalid_sdgs:
        return JsonResponse({'error': f"Invalid SDGs provided: {invalid_sdgs}"}, status=400)

    try:
        # Build a Q object to dynamically filter projects where any of the SDG fields are True
        query = Q()
        for sdg in sdgs:
            query |= Q(**{sdg: True})

        # Fetch matching projects
        projects = Project.objects.filter(query).values(
            'id',
            'project_name',
            'organization__name',
            'source_name',
            'project_website',
            *sdgs  # Include the requested SDG fields in the response
        )

        if not projects:
            return JsonResponse({'error': 'No matching projects found.'}, status=404)

        return JsonResponse({'projects': list(projects)}, status=200)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)
