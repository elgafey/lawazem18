{
    'name': 'Custom Invoice Design',
    'version': '18.0.1.0.0',
    'summary': 'Custom professional ZATCA-compliant invoice PDF report (bilingual Arabic/English)',
    'description': """
Custom Invoice Design Module
============================

Small Custom QWeb Report Module for Customer Invoices (account.move)
- Professional bilingual design (Arabic/English) matching ZATCA requirements
- Dynamic QR code (supports standard Saudi/GCC localization fields)
- Binds to Customer Invoices Print menu (account.move)
- Credit Note support (out_refund)
- Standalone: does NOT modify standard Odoo reports

Built for Odoo 18.0:

- QWeb `t-out` directives
- `tax_totals` JSON structure (subtotals -> tax_groups -> group_name/tax_amount_currency)
- Bank details read from `res.partner.bank`
  (`acc_number`, `acc_holder_name`, `bank_name`, `bank_bic`)
- Partner commercial registration read from `company_registry`
  (legacy `commercial_register` kept as fallback)
- Invoice lines: `display_type` values 'product' / 'line_section' / 'line_note'
- ZATCA QR taken from `l10n_sa_qr_code_str` and URL-encoded with `quote_plus`
- Branch banner removed from the printed document
    """,
    'author': 'Islam Elgafey',
    'category': 'Accounting/Accounting',
    'license': 'LGPL-3',
    'depends': ['base', 'account'],
    'data': [
        'report/invoice_report.xml',
        'report/invoice_report_template.xml',
    ],
    # No global report assets: all styling lives in the embedded <style> block
    # of report.invoice_report_document. Injecting into web.report_assets_common
    # (the bundle shared by EVERY report) from a path outside static/ broke the
    # whole report bundle and unstyled all printouts.
    'installable': True,
    'application': False,
    'auto_install': False,
}
