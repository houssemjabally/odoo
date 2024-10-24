from odoo import models, fields

class TicketImage(models.Model):
    _name = 'projet.ticket.image'
    _description = 'Project Ticket Image'

    image = fields.Binary(string="Image", attachment=True)
    ticket_id = fields.Many2one('projet.ticket', string="Ticket", ondelete='cascade')
