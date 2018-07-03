odoo.define('dev_tools.Tools', function(require){
    var SystrayMenu = require('web.SystrayMenu');
    var Widget = require('web.Widget');

    var DevTool = Widget.extend({
        template: 'DevTool',

        events: {
            "click .oe_module_control": "module_control",
        },

        module_control: function() {
            this.do_action({
                type: 'ir.actions.act_window',
                res_model: 'base.module.control',
                view_mode: 'form',
                view_type: 'form',
                views: [
                    [false, 'form']
                ],
                target: 'new',
            });
        }

    });

    SystrayMenu.Items.push(DevTool);
});