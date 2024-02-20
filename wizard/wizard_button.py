from odoo import models, fields, api
class WizardButton(models.TransientModel):
    _name = 'wizard.button'
    partner_new_id = fields.Many2one('res.partner',"Contact")
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
        context=self.env.context

        print("5555555",self.with_context(context))
        print("5555555",self.env.user.context_get())
        return res


