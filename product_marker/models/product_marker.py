# -*- encoding: utf-8 -*-
##############################################################################
#
#    Copyright (C) 2016 ICTSTUDIO (<http://www.ictstudio.eu>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

import logging

from openerp import models, fields

_logger = logging.getLogger(__name__)

class ProductMarker(models.Model):
    _name = "product.marker"

    name = fields.Char(
            string="Marker",
            required=True,
            size=128
    )
    product_ids = fields.Many2many(
            comodel_name="product.product",
            relation="product_product_marker_rel",
            column1="marker_id",
            column2="product_id",
            string="Products"
    )
