from pickle import FALSE

from odoo import api, fields, models, _
from odoo.exceptions import UserError, ValidationError
from datetime import date


class ProjetIT(models.Model):
    _name = 'projet.ticket'
    _inherit = ['mail.thread']
    _description = 'Projet IT'

    title = fields.Char(string="Titre", required=True, tracking=True)
    task = fields.Char(string="Tache", required=True, tracking=True)
    creation_date = fields.Date(string="Date", default=fields.Date.context_today, tracking=True)
    estimated_time = fields.Char(string="Temps estimé", required=True, tracking=True)
    assigned = fields.Many2many('developer.tag', string='Assigner à')
    urgent = fields.Boolean(string="Urgent")
    description = fields.Text(string="Description")
    image_ids = fields.One2many('projet.ticket.image', 'ticket_id', string="Images")
    state = fields.Selection([('draft', 'Draft'), ('confirmed', 'Confirmed'), ('ongoing', 'Ongoing'),
                              ('done', 'Done'), ('cancel', 'Canceled')], tracking=True)


    def action_confirm(self):
        for rec in self:
            rec.state = 'confirmed'

    def action_ongoing(self):
        for rec in self:
            rec.state = 'ongoing'

    def action_done(self):
        for rec in self:
            rec.state = 'done'

    def action_cancel(self):
        for rec in self:
            rec.state = 'cancel'


    # @api.ondelete(at_uninstall=False)
    # def _check_patient_appointments(self):
    #     for rec in self:
    #         domain = [('patient_id', '=', rec.id)]
    #         appointments = self.env['hospital.appointment'].search(domain)
    #         if appointments:
    #             raise ValidationError(_("You cannot delete the patient now."
    #                                     "\nAppointments existing for this patient"))

    # def unlink(self):
    #     for rec in self:
    #         domain = [('patient_id', '=', rec.id)]
    #         appointments = self.env['hospital.appointment'].search(domain)
    #         if appointments:
    #             raise ValidationError(_("You cannot delete the patient now, \nAppointments existing for this patient: %s" % rec.name))
    #     return super().unlink()