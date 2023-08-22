from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
# from django.template.loader import render_to_string


# Create your views here.
# def index(request):
#     list_items = " "
#     months = list(monthly_challange.keys())

#     for month in months:
#         caps_month = month.capitalize
#         month_path = reverse("month_challange", args=[month])
#         list_items += f"<li><a href=\"{month_path}\">{caps_month}</a></li>"

#     response_data = f"<ul>{list_items} </ul>"

#     return HttpResponse(response_data )

monthly_challange = {
    'january': "Jan Page",
    "february": "Feb Page",
    "march": "This works for march",
    "april": "This works for april",
    "may": "This works for may",
    "june": None,
    "july": "This works for july",
    "august": "This works for august",
    "september": "This works for september",
    "october": "This works for october",
    "november": "This works for november",
    "december": None,
}



def index(request):
    list_items=" "
    months =list(monthly_challange.keys())
    # for month in months:
    #     capitalized_month = month.capitalize()
    #     month_path = reverse("month-challange", args=[month]) 
    #     list_items  +=   f"<li><a href=\"{month_path}\">{capitalized_month}</a></li>"
    # response_data = f"<ul>{list_items}</ul>"
    # return HttpResponse(response_data)
    return render(request, "challanges/index.html", {
        "months": months
    })



def monthly_challanges_by_number(request, month):
    months = list(monthly_challange.keys())

    if month > len(months):
        return HttpResponseNotFound("Invalid Month")
    redirect_month = months[month-1]
    redirect_path = reverse("month-challange", args=[redirect_month])
    return HttpResponseRedirect(redirect_path)


def monthy_challanges_by_string(request, month):
    challange_text = None
    try:
        challange_text = monthly_challange[month]
        # response_data = render_to_string("challanges/challange.html")

        # return HttpResponse(response_data)
        return render(request, "challanges/challange.html", {
            "month_value": month,
            "text": challange_text
        })

    except:
        return HttpResponseNotFound("<h1>This month is not supported</h1>")
