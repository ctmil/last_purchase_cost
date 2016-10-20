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

	@api.onchange('state')
	def _check_state(self):
		if self.state in ['purchase','done']:
			import pdb;pdb.set_trace()
			for line in self.order_line:
				pricelist_id = self.env['product.supplierinfo'].search([\
					('name','=',self.partner_id.id),\
					('product_tmpl_id','=',self.product_id.product_tmpl_id.id)])
				vals = {
					'name': self.partner_id,
					'product_tmpl_id': self.product_id.product_tmpl_id.id,
					'min_qty': 0,
					'price': line.price_unit
					}
				if not pricelist_id:
					pricelist_id = self.env['product.supplierinfo'].create(vals)
				else:
					pricelist_id.write(vals)
