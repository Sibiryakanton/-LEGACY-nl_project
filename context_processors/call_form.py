from main_site.forms import CallForm
from main_site.models import ReferralUrl

def call_form(request):
	form = CallForm()
	return {'CallForm': form}

def referal_tag(request):
	referal_objects = ReferralUrl.objects.all()
	return {'referal_objects':referal_objects}