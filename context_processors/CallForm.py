from main_site.forms import Call_Form
from main_site.models import ReferralUrl
def CallForm(request):
	form = Call_Form()
	return {'CallForm': form}

def referal_tag(request):
	referal_objects = ReferralUrl.objects.all()
	return {'referal_objects':referal_objects}