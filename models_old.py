# -*- encoding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from datetime import datetime
from openerp.osv import fields, osv
from openerp.tools import DEFAULT_SERVER_DATETIME_FORMAT, DEFAULT_SERVER_DATE_FORMAT
from openerp.tools.translate import _
import openerp.addons.decimal_precision as dp
from openerp.exceptions import UserError

class purchase_requisition(osv.osv):
	_inherit = "purchase.requisition"

	def _prepare_purchase_order_line(self, cr, uid, requisition, requisition_line, purchase_id, supplier, context=None):
		res = super(purchase_requisition, self)._prepare_purchase_order_line(\
			cr,uid,requisition,requisition_line,purchase_id,supplier,context)
		taxes_ids = res.get('taxes_id',False)
		if taxes_ids:
			if taxes_ids[0][2] == []:
				product_id = res.get('product_id',False)
				if product_id:
					product = self.pool.get('product.product').browse(cr,uid,product_id)
					if product.supplier_taxes_id:
						res['taxes_id'] = [(6,0,product.supplier_taxes_id.ids)]
		return res

purchase_requisition()

