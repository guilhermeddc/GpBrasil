from client.models import *


def context(request):
    return {
        # 'languages': Language.objects.all(),
        # 'servicesTypes': ServiceType.objects.all(),
        # 'workCites': WorkCity.objects.all(),
        # 'attendanceTypes': AttendanceType.objects.all(),
        # 'paymentTypes': PaymentType.objects.all(),
        # 'placeAccepteds': PlaceAccepted.objects.all(),
        'ethnicitys': Ethnicity.objects.all(),
        'loiras': Client.objects.filter(ethnicity_id=2),
        'morenas': Client.objects.filter(ethnicity_id=1),
        'mulatas': Client.objects.filter(ethnicity_id=2),
        'asiaticas': Client.objects.filter(ethnicity_id=2),
        'ruivas': Client.objects.filter(ethnicity_id=2),
        'negras': Client.objects.filter(ethnicity_id=2),
        'plus_size': Client.objects.filter(ethnicity_id=2),
    }