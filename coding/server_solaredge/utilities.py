import time
import yaml


def getElapsedTime(startTime):
    elapsedTime = time.time() - startTime

    hours = elapsedTime // 360
    minutes = (elapsedTime - hours * 360) // 60
    seconds = (elapsedTime - hours * 360 - minutes * 60)

    return f'{int(hours)}h {int(minutes)}m {int(seconds)}s'


def read_yaml(file_path):
    with open(file_path, 'r') as f:
        return yaml.safe_load(f)


inputs = ['new_project',
          'info_section',
          'modelling_section',
          'positioning_section',
          'apply_positioning',
          'storage_section',
          'electrical_section',
          'financial_section',
          'report_section',
          'project_type',
          'project_name',
          'create_project',
          'country',
          'street',
          'city',
          # 'zip', DEPRECATED: not used anymore
          'consumption',
          'consumption_period',
          # 'electrical_grid', DEPRECATED: automatically selected when consumption is inserted
          # 'power_factor', DEPRECATED: automatically selected when consumption is inserted
          'name',
          'surname',
          'company',
          'notes',]

inputs_without_file = ['new_project', 'info_section', 'modelling_section', 'positioning_section', 'apply_positioning',
                       'storage_section', 'electrical_section', 'financial_section', 'report_section', 'create_project']
