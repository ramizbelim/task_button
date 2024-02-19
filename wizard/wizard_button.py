from odoo import models, fields, api
class WizardButton(models.TransientModel):
    _name = 'wizard.button'

    test = fields.Boolean(string="Test")

    def button1(self):
        pass
    def button2(self):
        pass
    def button3(self):
        pass
    @api.model
    def default_get(self,vals):
        res = super(WizardButton, self).default_get(vals)
        print("5555555",self.env.context)
        print("5555555",self._context)
        return res


