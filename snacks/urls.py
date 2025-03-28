from django.conf.urls import patterns, url
from django.views.generic import RedirectView
from snacks import views
from snacks import reports as r
from snacks import export_tracker as t
from snacks import cross_tracker as ct

urlpatterns = patterns('',	
	url(r'^master_entry/', views.master_entry, name = 'master_entry'),
	url(r'^submit_staff_master/', views.submit_staff_master, name = 'submit_staff_master'),
	url(r'^update_staff_master/', views.update_staff_master, name = 'update_staff_master'),
	url(r'^snacks_entry/', views.snacks_entry, name = 'snacks_entry'),
	url(r'^submit_snack_list/', views.submit_snack_list, name = 'submit_snack_list'),
	url(r'^update_snacks_items/', views.update_snacks_items, name = 'update_snacks_items'),
	url(r'^journal_entry/', views.journal_entry, name = 'journal_entry'),
	url(r'^get_staff_data/', views.get_staff_data, name = 'get_staff_data'),
	url(r'^get_rate_data/', views.get_rate_data, name = 'get_rate_data'),
	url(r'^get_total_tiffin/', views.get_total_tiffin, name = 'get_total_tiffin'),
	url(r'^get_amount_details/', views.get_amount_details, name = 'get_amount_details'),
	url(r'^submit_journal_data/', views.submit_journal_data, name = 'submit_journal_data'),
	url(r'^get_tab_name/', views.get_tab_name, name = 'get_tab_name'),

	url(r'^tiffin_entry/', views.tiffin_entry, name = 'tiffin_entry'),
	url(r'^submit_tiffin_list/', views.submit_tiffin_list, name = 'submit_tiffin_list'),
	url(r'^update_tiffin_items/', views.update_tiffin_items, name = 'update_tiffin_items'),

	url(r'^owner_list/', views.owner_list, name = 'owner_list'),
	url(r'^submit_owner_list/', views.submit_owner_list, name = 'submit_owner_list'),
	url(r'^update_owner_data/', views.update_owner_data, name = 'update_owner_data'),

	url(r'^reports/', r.reports, name = 'reports'),
	url(r'^get_owner_master/', r.get_owner_master, name = 'get_owner_master'),
	url(r'^get_reports_data/', r.get_reports_data, name = 'get_reports_data'),

	url(r'^export_tracker/', t.export_tracker, name = 'export_tracker'),
	url(r'^report_export/', t.report_export, name = 'report_export'),

	url(r'^cross_tracker/', ct.cross_tracker, name = 'cross_tracker'),
)
