from django.shortcuts import render
from datetime import datetime
from dateutil.relativedelta import relativedelta
from ControlVehiculos.models import Expense
from django.db.models import Sum

def dashboard(request):
    # Obtener la fecha actual
    fecha_actual = datetime.now()
    
    # Especificar el número de meses que quieres iterar hacia atrás
    meses_atras = 10
    
    # Lista de nombres de los meses en español
    nombres_meses = ["Ene", "Feb", "Mar", "Abr", "May", "Jun", "Jul", "Agos", "Sep", "Oct", "Nov", "Dic"]
    
    # Generar las etiquetas de los meses y años
    etiquetas = []
    gastos_por_mes = []
    
    for i in range(meses_atras):
        fecha_iteracion = fecha_actual - relativedelta(months=i)
        mes_nombre = nombres_meses[fecha_iteracion.month - 1]
        año = fecha_iteracion.year
        etiquetas.append(f"{mes_nombre}-{año}")
        
        # Obtener el total de gastos para el mes y año específicos
        total_gastos = Expense.route.get_object.filter(
            fecha__year=año,
            fecha__month=fecha_iteracion.month
        ).aggregate(total=Sum('monto'))['total'] or 0
        
        gastos_por_mes.append(total_gastos)
    
    etiquetas.reverse()
    gastos_por_mes.reverse()
    
    context = {
        "etiquetas": etiquetas,
        "gastos_por_mes": gastos_por_mes
    }
    
    return render(request, 'dashboard/dashboard.html', context)
