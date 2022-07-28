from datacenter.models import Passcard
from datacenter.models import Visit, format_duration
from django.shortcuts import render, get_object_or_404


def passcard_info_view(request, passcode):
    this_passcard_visits = []
    passcard = get_object_or_404(Passcard.objects, passcode=passcode)
    visits = Visit.objects.filter(passcard=passcard)

    for visit in visits:
        duration = visit.get_duration()
        this_passcard_visits.append(
        {
            'entered_at': visit.entered_at,
            'duration': format_duration(duration),
            'is_strange': visit.is_visit_long(minutes=60)
        }
        )

    context = {
        'passcard': passcard,
        'this_passcard_visits': this_passcard_visits
    }
    return render(request, 'passcard_info.html', context)
