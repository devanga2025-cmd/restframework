from django.http import JsonResponse
import asyncio

async def student(request):
    await asyncio.sleep(2)

    return JsonResponse({
        "message": "Async API Working"
    })