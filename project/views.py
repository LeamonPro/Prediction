from django.shortcuts import render
from django.shortcuts import render
import pandas as pd
# Create your views here.



def home(request):
    df = pd.read_csv("project\predictions.csv")
    context = {
        "table_data": df.to_dict(orient="records"),
        "column_names": df.columns.tolist(),
    }
    print(context["table_data"])
    return render(request, "index.html",context)