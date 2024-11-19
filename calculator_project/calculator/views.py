from django.shortcuts import render

# Create your views here.


from django.shortcuts import render

def index(request):
    if request.method == "POST":
        num1 = request.POST.get('num1')
        num2 = request.POST.get('num2')
        operator = request.POST.get('operator')
        
        try:
            num1 = float(num1)
            num2 = float(num2)
            
            if operator == '+':
                result = num1 + num2
            elif operator == '-':
                result = num1 - num2
            elif operator == '*':
                result = num1 * num2
            elif operator == '/':
                result = num1 / num2 if num2 != 0 else 'Cannot divide by zero'
            else:
                result = 'Invalid operator'
        except ValueError:
            result = 'Invalid input'
            
        context = {
            'result': result,
            'num1': num1,
            'num2': num2,
            'operator': operator
        }
        
        return render(request, 'index.html', context)
    else:
        return render(request, 'index.html')
