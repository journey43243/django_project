from cart.forms import CartAddProductForm


class DataMixin():
    extra_context = {}
    title_page = None

    def __init__(self):
        if 'cart_product_form' not in self.extra_context:
            self.extra_context['cart_product_form'] = CartAddProductForm()

        if self.title_page:
            self.extra_context['title'] = self.title_page

    def get_mixin_context(self, context, **kwargs):
        if self.title_page:
            context['title'] = self.title_page
        context.update(kwargs)
        return context