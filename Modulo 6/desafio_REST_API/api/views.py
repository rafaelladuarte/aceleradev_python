from rest_framework.decorators import api_view
from rest_framework.response import Response
from collections import Counter


# Create your views here.

# @api_view(['POST', 'GET'])
@api_view(['POST'])
def lambda_function(request):
    '''
     if request.method == 'GET':
        return Response({'Error': 'somente é aceito o método POST'})

    if request.method == ' POST':
    '''
        request_data = request.data.get('question')

        counter = Counter()
        for number in request_data:
            counter[number] += 1

        solution = []
        for item in counter.most_common():
            for _ in range(item[1]):
                solution.append(item[0])

        return Response({'solution': solution})
