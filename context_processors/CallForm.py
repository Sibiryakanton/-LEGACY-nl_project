from main_site.forms import Call_Form

def CallForm(request):
	form = Call_Form()
	return {'CallForm': form}