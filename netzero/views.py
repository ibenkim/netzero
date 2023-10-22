from django.shortcuts import render

# Create your views here.

def index(request):
    if request.POST.get('calc_process', ''):
        drive_mile = request.POST["drive_mile"]
        light_count = request.POST["light_count"]
        light_time = request.POST["light_time"]
        paper_count = request.POST["paper_count"]
        air_time = request.POST["air_time"]
        bottle_count = request.POST["bottle_count"]
        elev_count = request.POST["elev_count"]

        print('drive_mile: {}, light_count: {}, light_time: {}, paper_count: {}, air_time: {}, bottle_count: {}, elev_count: {}'.format(
              drive_mile, light_count, light_time, paper_count, air_time, bottle_count, elev_count))

        carbon_footprint = 0.0

        if drive_mile:
            carbon_footprint += float(drive_mile) * 262.2;
        if light_count and light_time:
            carbon_footprint += float(light_count) * float(light_time) * 17.7;
        if paper_count:
            carbon_footprint += float(paper_count) * 8.64;
        if air_time:
            carbon_footprint += float(air_time) * 669.4;
        if bottle_count:
            carbon_footprint += float(bottle_count) * 16.69;
        if elev_count:
            carbon_footprint += float(elev_count) * 14;

        carbon_footprint = '{0:,.2f}'.format(carbon_footprint)
        print('generated carbon footproint: {}'.format(carbon_footprint))
        gotodiv = 'calc-res'
    else:
        carbon_footprint = ''
        gotodiv = ''

    context = {
        "generated_carbon_footprint": carbon_footprint,
        "gotodiv": gotodiv,
    }
    return render(request, 'index.html', context)

def calculate(request):
    drive_time = request.POST["drive_time"]
    light_count = request.POST["light_count"]
    light_time = request.POST["light_time"]
    paper_count = request.POST["paper_count"]
    air_time = request.POST["air_time"]
    bottle_count = request.POST["bottle_count"]
    elev_time = request.POST["elev_time"]

    carbon_footprint = 32

    context = {
        "generated_carbon_footprint": carbon_footprint,
    }
    return render(request, 'index.html', context)