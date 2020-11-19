# -*- coding: utf-8 -*-

from openerp import models, fields, api

class StockInventoryExtended(models.Model):
    _inherit = 'stock.inventory.line'
    
    variance = fields.Integer(string="Variance", compute='_stock_difference')

    # calculate variance
    @api.one
    @api.depends('theoretical_qty', 'product_qty')
    def _stock_difference(self):
        self.variance = self.theoretical_qty - self.product_qty
    
    # trigger report
    @api.multi
    def print_stock_variance_report(self):
        return self.env['report'].get_action(
            self, 'stock_take_variance.report_stock_variance')
        
