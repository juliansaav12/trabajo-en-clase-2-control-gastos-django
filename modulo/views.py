from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.core.paginator import Paginator
from .models import Gasto
from .forms import GastoForm


def lista_gastos(request):
    gastos = Gasto.objects.all()

    q = request.GET.get('q', '')
    cat = request.GET.get('categoria', '')
    pag = request.GET.get('pagado', '')

    if q:
        gastos = gastos.filter(descripcion__icontains=q)
    if cat:
        gastos = gastos.filter(categoria=cat)
    if pag in ['True', 'False']:
        gastos = gastos.filter(pagado=(pag == 'True'))

    paginator = Paginator(gastos, 4)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
        'categorias': Gasto.CATEGORIAS,
        'q': q,
        'categoria_filtro': cat,
        'pagado_filtro': pag,
    }
    return render(request, 'modulo/gasto_list.html', context)


def detalle_gasto(request, pk):
    gasto = get_object_or_404(Gasto, pk=pk)
    return render(request, 'modulo/gasto_detail.html', {'gasto': gasto})


def crear_gasto(request):
    if request.method == 'POST':
        form = GastoForm(request.POST)
        if form.is_valid():
            nuevo_gasto = form.save(commit=False)
            nuevo_gasto.usuario = request.user
            nuevo_gasto.save()
            messages.success(request, "Gasto registrado con éxito.")
            return redirect('lista_gastos')
    else:
        form = GastoForm()
    return render(request, 'modulo/gasto_form.html', {'form': form, 'titulo': 'Registrar Gasto'})


def editar_gasto(request, pk):
    gasto = get_object_or_404(Gasto, pk=pk)
    if request.method == 'POST':
        form = GastoForm(request.POST, instance=gasto)
        if form.is_valid():
            form.save()
            messages.success(request, "Gasto actualizado con éxito.")
            return redirect('detalle_gasto', pk=gasto.pk)
    else:
        form = GastoForm(instance=gasto)
    return render(request, 'modulo/gasto_form.html', {'form': form, 'titulo': 'Editar Gasto'})


def eliminar_gasto(request, pk):
    gasto = get_object_or_404(Gasto, pk=pk)
    if request.method == 'POST':
        gasto.delete()
        messages.success(request, "Gasto eliminado con éxito.")
        return redirect('lista_gastos')
    return render(request, 'modulo/gasto_confirm_delete.html', {'gasto': gasto})