from odoo import http
from odoo.http import request


class WebsiteSaleReorder(http.Controller):

    @http.route(['/shop/reorder/<int:order_id>'], type='http', auth="user", website=True)
    def reorder_from_sale_order(self, order_id):
        sale_order = request.env['sale.order'].sudo().browse(order_id)

        if not sale_order or sale_order.partner_id.id != request.env.user.partner_id.id:
            return request.redirect('/my/orders')

        # Add products to current website cart.
        for line in sale_order.order_line:
            request.website.sale_get_order(force_create=True)._cart_update(
                product_id=line.product_id.id,
                add_qty=line.product_uom_qty,
                set_qty=False
            )

        return request.redirect('/shop/cart')
