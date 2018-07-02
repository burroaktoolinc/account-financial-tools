# -*- coding: utf-8 -*-
# Copyright 2017 ACSONE SA/NV
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import api, fields, models


class AccountMoveLine(models.Model):
    _inherit = 'account.move.line'

    is_tax_editable = fields.Boolean(
        string="Is tax data editable?", compute='_compute_is_tax_editable')
    move_state = fields.Selection(related="move_id.state", readonly=True)

    @api.multi
    @api.depends('move_state')
    def _compute_is_tax_editable(self):
        for rec in self:
            rec.is_tax_editable = rec._get_is_tax_editable()

    @api.multi
    def _get_is_tax_editable(self):
        self.ensure_one()
        return not self.move_id or self.move_id.state == 'draft'
