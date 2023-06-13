from django.shortcuts import render
from django.view.generic import TemplateView

class HomePageView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["snacks"] = [
            {
                "image_url": "https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.pxfuel.com%2Fen%2Ffree-photo-qpxti&psig=AOvVaw3vvUGH2QX-2ZK22juW_xPz&ust=1686716204971000&source=images&cd=vfe&ved=2ahUKEwiApZLTsb__AhUZu4kEHS3CBvcQjRx6BAgAEAw",
                "title": "Cookies",
                "description": "A circular morsel of far too many calories",
                "reference_url": "https://en.wikipedia.org/wiki/Cookie"
            }, {
                "image_url": "https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.istockphoto.com%2Fphoto%2Fsalted-mini-pretzels-snack-gm1138805670-304170335&psig=AOvVaw11BI4h32ZW6oSaS5qxmxy6&ust=1686716440390000&source=images&cd=vfe&ved=2ahUKEwj0lrPDsr__AhVyookEHYqQDrcQjRx6BAgAEAw",
                "title": "Pretzels",
                "description": "A salty, crunchy snack",
                "reference_url": "https://en.wikipedia.org/wiki/Pretzel"
            }, {
                "image_url": "https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.nonsprecare.it%2Fricetta-biscotti-alla-cannella&psig=AOvVaw2HuQTAQ6aku3mxQYBZtYuc&ust=1686716433029000&source=images&cd=vfe&ved=0CBAQjRxqFwoTCNi8h8Cyv_8CFQAAAAAdAAAAABAO",
                "title": "Biscotti",
                "description": "A dog biscuit that has grown stale to the point of it being unsuitable for pet consumption",
                "reference_url": "https://en.wikipedia.org/wiki/Biscotti"
            }

        ]

        return context
    
class AboutView(TemplateView):
    template_name = 'about.html'
