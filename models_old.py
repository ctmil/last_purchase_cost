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
		import pdb;pdb.set_trace()
		return res

purchase_requisition()

