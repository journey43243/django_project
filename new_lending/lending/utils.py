from .models import Tags

class DataMixin:
    extra_content = {
        'tags' : Tags.objects.all()
    }

    # def __init__(self) -> None:
    #     if self


    # def get_mixin_context(self, **kwargs):
        