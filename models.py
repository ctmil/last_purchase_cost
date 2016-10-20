from openerp import models, fields, api, _
from openerp.osv import osv
from openerp.exceptions import except_orm, ValidationError
from StringIO import StringIO
import urllib2, httplib, urlparse, gzip, requests, json
import openerp.addons.decimal_precision as dp
import logging
import datetime
from openerp.fields import Date as newdate

#Get the logger
_logger = logging.getLogger(__name__)

class purchase_order(models.Model):
	_inherit = 'purchase.order'


	@api.multi
	def write(self, vals):
		purchase_state = vals.get('state','')
		res = super(purchase_order,self).write(vals)
		if purchase_state in ['purchase','done']:
			for line in self.order_line:
				pricelist_id = self.env['product.supplierinfo'].search([\
					('name','=',self.partner_id.id),\
					('product_tmpl_id','=',line.product_id.product_tmpl_id.id)])
				vals = {
					'name': self.partner_id.id,
					'product_tmpl_id': line.product_id.product_tmpl_id.id,
					'min_qty': 0,
					'price': line.price_unit
					}
				if not pricelist_id:
					pricelist_id = self.env['product.supplierinfo'].create(vals)
				else:
					pricelist_id.write(vals)
class account_invoice(models.Model):
	_inherit = 'account.invoice'


	@api.multi
	def write(self, vals):
		invoice_state = vals.get('state','')
		res = super(account_invoice,self).write(vals)
		if invoice_state in ['open']:
			for line in self.invoice_line_ids:
				pricelist_id = self.env['product.supplierinfo'].search([\
					('name','=',self.partner_id.id),\
					('product_tmpl_id','=',line.product_id.product_tmpl_id.id)])
				vals = {
					'name': self.partner_id.id,
					'product_tmpl_id': line.product_id.product_tmpl_id.id,
					'min_qty': 0,
					'price': line.price_unit
					}
				if not pricelist_id:
					pricelist_id = self.env['product.supplierinfo'].create(vals)
				else:
					pricelist_id.write(vals)
				vals_product_tmpl = {
					'standard_price': line.price_unit
					}
				product_tmpl = line.product_id.product_tmpl_id
				product_tmpl.write(vals_product_tmpl)
