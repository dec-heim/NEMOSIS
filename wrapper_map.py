import query_wrapers

map = {'DISPATCHLOAD': query_wrapers.dispatch,
       'DISPATCHPRICE': query_wrapers.dispatch,
       'DISPATCH_UNIT_SCADA': query_wrapers.dispatch,
       'DISPATCHCONSTRAINT': query_wrapers.dispatch,
       'DUDETAILSUMMARY': query_wrapers.start_and_end,
       'GENCONDATA': query_wrapers.effective_date_search_all,
       'STATION': query_wrapers.last_changed,
       'STADUALLOC': query_wrapers.effective_date,
       'GENUNITS':  query_wrapers.last_changed,
       'PARTICIPANT': query_wrapers.last_changed,
       'SPDREGIONCONSTRAINT': query_wrapers.effective_date_search_all,
       'SPDCONNECTIONPOINTCONSTRAINT': query_wrapers.effective_date_search_all,
       'SPDINTERCONNECTORCONSTRAINT': query_wrapers.effective_date_search_all,
       'FCAS_4_SECOND': query_wrapers.fcas4s,
       'ELEMENTS_FCAS_4_SECOND': query_wrapers.static_table,
       'VARIABLES_FCAS_4_SECOND': query_wrapers.static_table,
       'MASTER_REGISTRATION_LIST': query_wrapers.static_table_xl,
       'BIDDAYOFFER_D': query_wrapers.dispatch_date,
       'BIDPEROFFER_D': query_wrapers.dispatch}
