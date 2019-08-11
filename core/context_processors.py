from gp.models import *


def context(request):
    return {
        # 'languages': Language.objects.all(),
        # 'servicesTypes': ServiceType.objects.all(),
        # 'workCites': WorkCity.objects.all(),
        # 'attendanceTypes': AttendanceType.objects.all(),
        # 'paymentTypes': PaymentType.objects.all(),
        # 'placeAccepteds': PlaceAccepted.objects.all(),
        'ethnicitys': ChoicesEthnicity.objects.all(),
    }