# Copyright 2018 Eficent <http://www.eficent.com>
# Copyright 2018 Tecnativa - Pedro M. Baeza
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openupgradelib import openupgrade


@openupgrade.migrate()
def migrate(env, version):
    openupgrade.load_data(
        env.cr, 'calendar', 'migrations/12.0.1.0/noupdate_changes.xml')
    openupgrade.delete_record_translations(
        env.cr, 'calendar', [
            'calendar_template_meeting_invitation',
            'calendar_template_meeting_changedate',
            'calendar_template_meeting_reminder',
        ],
    )
    openupgrade.delete_records_safely_by_xml_id(
        env, [
            'calendar.categ_meet1',
            'calendar.categ_meet2',
            'calendar.categ_meet3',
            'calendar.categ_meet4',
            'calendar.categ_meet5',
        ],
    )
