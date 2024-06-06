from ocpa.objects.log.importer.csv import factory as ocel_import_factory

# filename = "sample_logs/csv/test.csv"
# object_types = ["test"]
# timestamp = ["start"]
# parameters = {"obj_names":object_types,
#               "val_names":[],
#               "act_name":"activity",
#               "time_name":"end",
#               "start_timestamp":"start",
#               "sep":","}

filename = "sample_logs/csv/blood_test.csv"
object_types = ["test","sample"]
timestamp = ["start"]
parameters = {"obj_names":object_types,
              "val_names":[],
              "act_name":"activity",
              "time_name":"end",
              "start_timestamp":"start",
              "sep":","}

# filename = "sample_logs/csv/BPI2017-Top10.csv"
# object_types = ["A","O"]
# timestamp = ["start"]
# parameters = {"obj_names":object_types,
#               "val_names":[],
#               "act_name":"event_activity",
#               "time_name":"event_timestamp",
#               "start_timestamp":"event_start_timestamp",
#               "sep":","}

# filename = "sample_logs/csv/BPI2017-Final.csv"
# object_types = ["application", "offer"]
# timestamp = ["start"]
# parameters = {"obj_names":object_types,
#               "val_names":[],
#               "act_name":"event_activity",
#               "time_name":"event_timestamp",
#               "start_timestamp":"event_start_timestamp",
#               "sep":","}
ocel = ocel_import_factory.apply(file_path = filename,parameters = parameters)
#discovery
from ocpa.algo.discovery.ocpn import algorithm as ocpn_discovery_factory
ocpn = ocpn_discovery_factory.apply(ocel)
from ocpa.visualization.oc_petri_net import factory as ocpn_vis_factory
#ocpn = ocpn_discovery_factory.apply(ocel, parameters={"debug": False})
#gviz = ocpn_vis_factory.apply(ocpn, parameters={'format': 'png'})
#ocpn_vis_factory.view(gviz)

#measure
from ocpa.algo.enhancement.token_replay_based_performance import algorithm as performance_factory
diag_params = {'measures': ['waiting_time', 'service_time', 'sojourn_time', 'pooling_time', 'lagging_time', 'synchronization_time', 'object_count', 'flow_time'], 'agg': ['mean','median','min','max', 'stdev'], 'format': 'png'} 
diag = performance_factory.apply(ocpn, ocel, parameters=diag_params)
gviz = ocpn_vis_factory.apply(ocpn)
gviz = ocpn_vis_factory.apply(
    ocpn, diagnostics=diag, variant="annotated_with_opera", parameters=diag_params)
ocpn_vis_factory.view(gviz)