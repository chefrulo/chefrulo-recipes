from odoo import api, fields, models


class ResConfigSettings(models.TransientModel):
    _inherit = "res.config.settings"

    recipe_labor_rate = fields.Float(
        string="Labor Rate (per hour)",
        config_parameter="chefrulo_recipe.labor_rate",
        default=0,
    )
    recipe_energy_rate = fields.Float(
        string="Energy Rate (per hour)",
        config_parameter="chefrulo_recipe.energy_rate",
        default=0,
    )
