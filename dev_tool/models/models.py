# -*- coding: utf-8 -*-

from odoo import models, fields, api

class BaseModuleControl(models.TransientModel):
    _name = "base.module.control"
    _description = "Module controls"

    modules = fields.Text('Control modules')

    @api.one
    def install(self):
        names = self.modules.split('\n')
        self.env['ir.module.module'].search([('name', 'in', names), ('state', '=', 'uninstalled')]).button_immediate_install()
        return False

    @api.one
    def upgrade(self):
        names = self.modules.split('\n')
        self.env['ir.module.module'].search([('name', 'in', names), ('state', '=', 'installed')]).button_immediate_upgrade()
        return False

    @api.one
    def uninstall(self):
        names = self.modules.split('\n')
        self.env['ir.module.module'].search([('name', 'in', names), ('state', '=', 'installed')]).button_immediate_uninstall()
        return False
