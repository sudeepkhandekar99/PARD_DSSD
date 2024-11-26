import os
import django
import pandas as pd

# Set up Django settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')  # Replace 'myproject.settings' with your settings module
django.setup()

from core.models import Organization, Project  # Replace 'core' with your app's name

def import_data(excel_path):
    # Read Excel sheets
    org_df = pd.read_excel(excel_path, sheet_name='1. Organisations')
    projects_df = pd.read_excel(excel_path, sheet_name='2. Projects')

    # Organizations column mapping
    org_columns = {
        'Name of organisation': 'name',
        'Acronym': 'acronym',
        'Website': 'website',
        'Religious/spiritual affiliation': 'religious_affiliation',
        'Religious sub-group': 'religious_subgroup',
        'Continent (HQ)': 'continent_hq',
        'Country (HQ)': 'country_hq',
        'Environment project(s) URL': 'environment_projects_url',
        'Reports/publications': 'reports_publications',
    }

    # Extract the keys and values from org_columns
    org_keys = list(org_columns.keys())

    # Filter the DataFrame to only include the columns specified in org_keys
    filtered_org_df = org_df[org_keys]

    # Rename the columns using the mapping in org_columns
    filtered_org_df = filtered_org_df.rename(columns=org_columns)

    for _, row in filtered_org_df.iterrows():
        Organization.objects.get_or_create(
            name=row['name'],
            defaults={
                'acronym': row.get('acronym'),
                'website': row.get('website'),
                'religious_affiliation': row.get('religious_affiliation'),
                'religious_subgroup': row.get('religious_subgroup'),
                'continent_hq': row.get('continent_hq'),
                'country_hq': row.get('country_hq'),
                'environment_projects_url': row.get('environment_projects_url'),
                'reports_publications': row.get('reports_publications'),
            }
        )

    # Projects column mapping
    projects_columns = {
        'Source': 'source_name',
        'Name of organisation': 'organisation_name',
        'Name of project': 'project_name',
        'Website/URL of project': 'project_website',
        'Location of project': 'project_location',
        'Project aims and objectives': 'aims_objectives',
        'Project duration': 'duration',
        'Overall project budget': 'budget',
        'List of contributing/financing donors': 'donors',
        'Project partners': 'partners',
        'Target group(s) of the project': 'target_groups',
        'Summary of main activities': 'main_activities_summary',
        'Results of the project - evaluation measures': 'evaluation_results',
        'Lessons learned': 'lessons_learned',
        'Please describe how religion/faith played a role in the project': 'religion_role',
        'Please provide links/URLs to any reports, documents or publications relevant to the project': 'reports_documents_urls',
        'Any other comments': 'additional_comments',
        'Animals': 'animals',
        'Agriculture': 'agriculture',
        'Biodiversity': 'biodiversity',
        'Climate change': 'climate_change',
        'Climate justice': 'climate_justice',
        'Climate science': 'climate_science',
        'Conservation': 'conservation',
        'Development': 'development',
        'Divestment/investment': 'divestment_investment',
        'Economy/economic models': 'economic_models',
        'Ecology': 'ecology',
        'Ecosystems': 'ecosystems',
        'Ecotourism': 'ecotourism',
        'Emissions/greenhouse gasses': 'emissions',
        'Environmental awareness': 'environmental_awareness',
        'Food security': 'food_security',
        'Forests/deforestation': 'forests_deforestation',
        'Health/wellbeing': 'health_wellbeing',
        'Indigenous peoples/land': 'indigenous_peoples',
        'Lifestyle change/individual responsibility': 'lifestyle_change',
        'Livelihoods': 'livelihoods',
        'Losses and damages': 'losses_damages',
        'Natural hazards/extreme weather': 'natural_hazards',
        'Natural resources': 'natural_resources',
        'Nature-based solutions': 'nature_based_solutions',
        'Pollution': 'pollution',
        'Poverty': 'poverty',
        'Refugees': 'refugees',
        'Tree planting': 'tree_planting',
        'Waste': 'waste',
        'Water': 'water',
        'Other (please specify)': 'other_environmental_themes',
        'Do you use the Sustainable Development Goals (SDGs) in the planning or implementation of your project?': 'uses_sdgs',
        'GOAL 1: No Poverty': 'sdg_1',
        'GOAL 2: Zero Hunger': 'sdg_2',
        'GOAL 3: Good Health and Well-being': 'sdg_3',
        'GOAL 4: Quality Education': 'sdg_4',
        'GOAL 5: Gender Equality': 'sdg_5',
        'GOAL 6: Clean Water and Sanitation': 'sdg_6',
        'GOAL 7: Affordable and Clean Energy': 'sdg_7',
        'GOAL 8: Decent Work and Economic Growth': 'sdg_8',
        'GOAL 9: Industry, Innovation and Infrastructure': 'sdg_9',
        'GOAL 10: Reduced Inequality': 'sdg_10',
        'GOAL 11: Sustainable Cities and Communities': 'sdg_11',
        'GOAL 12: Responsible Consumption and Production': 'sdg_12',
        'GOAL 13: Climate Action': 'sdg_13',
        'GOAL 14: Life Below Water': 'sdg_14',
        'GOAL 15: Life on Land': 'sdg_15',
        'GOAL 16: Peace and Justice Strong Institutions': 'sdg_16',
        'GOAL 17: Partnerships to achieve the Goal': 'sdg_17',
        'Advocacy': 'advocacy',
        'Dialogue/interfaith work': 'dialogue_interfaith',
        'Disaster relief/management': 'disaster_relief',
        'Divestment/investment.1': 'divestment',
        'Education/training': 'education_training',
        'Greening places of worship': 'greening_worship_places',
        'Engaging with indigenous knowledge': 'indigenous_knowledge',
        'Promoting lifestyle change/individual responsibility': 'lifestyle_promotion',
        'Lobbying': 'lobbying',
        'Losses and damages.1': 'losses_damages_activities',
        'Mitigation/adaptation measures': 'mitigation_adaptation',
        'Nature-based solutions.1': 'nature_solutions',
        'Prayer/worship/meditation': 'prayer_worship',
        'Protection/conservation': 'protection_conservation',
        'Public engagement/awareness raising': 'public_engagement',
        'Renewable/green energy': 'renewable_energy',
        'Research': 'research',
        'Resilience-/capacity-building/empowerment': 'resilience_building',
        'Releasing a statement': 'statement_release',
        'Tree planting.1': 'tree_planting_activity',
        'Waste reduction/resource management': 'waste_management',
        'Youth engagement': 'youth_engagement',
    }

    # List of columns to apply the replacement
    sdg_columns = [
        'GOAL 1: No Poverty',
        'GOAL 2: Zero Hunger',
        'GOAL 3: Good Health and Well-being',
        'GOAL 4: Quality Education',
        'GOAL 5: Gender Equality',
        'GOAL 6: Clean Water and Sanitation',
        'GOAL 7: Affordable and Clean Energy',
        'GOAL 8: Decent Work and Economic Growth',
        'GOAL 9: Industry, Innovation and Infrastructure',
        'GOAL 10: Reduced Inequality',
        'GOAL 11: Sustainable Cities and Communities',
        'GOAL 12: Responsible Consumption and Production',
        'GOAL 13: Climate Action',
        'GOAL 14: Life Below Water',
        'GOAL 15: Life on Land',
        'GOAL 16: Peace and Justice Strong Institutions',
        'GOAL 17: Partnerships to achieve the Goal',
    ]

    # Replace values for the specified columns
    projects_df[sdg_columns] = projects_df[sdg_columns].applymap(
        lambda x: True if str(x).strip().lower() in ['yes', '1'] else False
    )

    # Extract the keys from proj_columns
    proj_keys = list(projects_columns.keys())

    # Filter the DataFrame to only include those columns
    filtered_proj_df = projects_df[proj_keys]

    # Rename the columns using the values in org_columns
    filtered_proj_df = filtered_proj_df.rename(columns=projects_columns)

    projects_df = filtered_proj_df

    bool_cols = [col for col in projects_df.columns if projects_df[col].dtype == 'object' and
                 projects_df[col].str.contains('Yes|No', na=False).any()]

    for col in bool_cols:
        projects_df[col] = projects_df[col].map({'Yes': True, 'No': False})
    
    boolean_fields = [
        'animals', 'agriculture', 'biodiversity', 'climate_change', 'climate_justice',
        'climate_science', 'conservation', 'development', 'divestment_investment',
        'economic_models', 'ecology', 'ecosystems', 'ecotourism', 'emissions',
        'environmental_awareness', 'food_security', 'forests_deforestation', 'health_wellbeing',
        'indigenous_peoples', 'lifestyle_change', 'livelihoods', 'losses_damages',
        'natural_hazards', 'natural_resources', 'nature_based_solutions', 'pollution',
        'poverty', 'refugees', 'tree_planting', 'waste', 'water', 'uses_sdgs',
        'sdg_1', 'sdg_2', 'sdg_3', 'sdg_4', 'sdg_5', 'sdg_6', 'sdg_7', 'sdg_8',
        'sdg_9', 'sdg_10', 'sdg_11', 'sdg_12', 'sdg_13', 'sdg_14', 'sdg_15',
        'sdg_16', 'sdg_17', 'advocacy', 'dialogue_interfaith', 'disaster_relief',
        'divestment', 'education_training', 'greening_worship_places', 'indigenous_knowledge',
        'lifestyle_promotion', 'lobbying', 'losses_damages_activities', 'mitigation_adaptation',
        'nature_solutions', 'prayer_worship', 'protection_conservation', 'public_engagement',
        'renewable_energy', 'research', 'resilience_building', 'statement_release',
        'tree_planting_activity', 'waste_management', 'youth_engagement'
    ]

    # Replace NaN values in the entire DataFrame with 0
    projects_df = projects_df.fillna(0)
    # Replace NaN with appropriate defaults
    projects_df = projects_df.fillna('').replace({'\n': '', '': False})
    # Replace curly quotes and other problematic values in the entire DataFrame
    projects_df.replace({'“': '', '”': '', '“9”': '9'}, regex=True, inplace=True)



    for _, row in projects_df.iterrows():
        row_dict = row.to_dict()

        # Sanitize and normalize boolean fields
        for field in boolean_fields:
            value = row_dict.get(field)

            # Sanitize string values
            if isinstance(value, str):
                value = value.strip()  # Remove whitespace and newlines

            # Normalize values
            if isinstance(value, (int, float)):  # Numeric values
                row_dict[field] = value > 0
            elif pd.isna(value) or value == '' or value is None:  # NaN, empty string, or None
                row_dict[field] = False
            else:  # String values
                row_dict[field] = str(value).lower() in ['yes', 'true', '1']
                    
            organization, created = Organization.objects.get_or_create(
                name=row['organisation_name'],
                defaults={
                    'acronym': '',
                    'website': '',
                    'religious_affiliation': '',
                    'religious_subgroup': '',
                    'continent_hq': '',
                    'country_hq': '',
                    'environment_projects_url': '',
                    'reports_publications': '',
                }
            )
        if created:
            print(f"Created missing organization: {organization.name}")
        try:
            Project.objects.get_or_create(
                organization=organization,
                project_name=row['project_name'],
                defaults={
                    'source_name': row.get('source_name'),
                    'project_website': row.get('project_website'),
                    'project_location': row.get('project_location'),
                    'aims_objectives': row.get('aims_objectives'),
                    'duration': row.get('duration'),
                    'budget': row.get('budget'),
                    'donors': row.get('donors'),
                    'partners': row.get('partners'),
                    'target_groups': row.get('target_groups'),
                    'main_activities_summary': row.get('main_activities_summary'),
                    'evaluation_results': row.get('evaluation_results'),
                    'lessons_learned': row.get('lessons_learned'),
                    'religion_role': row.get('religion_role'),
                    'reports_documents_urls': row.get('reports_documents_urls'),
                    'additional_comments': row.get('additional_comments'),
                    'animals': row.get('animals'),
                    'agriculture': row.get('agriculture'),
                    'biodiversity': row.get('biodiversity'),
                    'climate_change': row.get('climate_change'),
                    'climate_justice': row.get('climate_justice'),
                    'climate_science': row.get('climate_science'),
                    'conservation': row.get('conservation'),
                    'development': row.get('development'),
                    'divestment_investment': row.get('divestment_investment'),
                    'economic_models': row.get('economic_models'),
                    'ecology': row.get('ecology'),
                    'ecosystems': row.get('ecosystems'),
                    'ecotourism': row.get('ecotourism'),
                    'emissions': row.get('emissions'),
                    'environmental_awareness': row.get('environmental_awareness'),
                    'food_security': row.get('food_security'),
                    'forests_deforestation': row.get('forests_deforestation'),
                    'health_wellbeing': row.get('health_wellbeing'),
                    'indigenous_peoples': row.get('indigenous_peoples'),
                    'lifestyle_change': row.get('lifestyle_change'),
                    'livelihoods': row.get('livelihoods'),
                    'losses_damages': row.get('losses_damages'),
                    'natural_hazards': row.get('natural_hazards'),
                    'natural_resources': row.get('natural_resources'),
                    'nature_based_solutions': row.get('nature_based_solutions'),
                    'pollution': row.get('pollution'),
                    'poverty': row.get('poverty'),
                    'refugees': row.get('refugees'),
                    'tree_planting': row.get('tree_planting'),
                    'waste': row.get('waste'),
                    'water': row.get('water'),
                    'other_environmental_themes': row.get('other_environmental_themes'),
                    'uses_sdgs': row.get('uses_sdgs'),
                    'sdg_1': row.get('sdg_1'),
                    'sdg_2': row.get('sdg_2'),
                    'sdg_3': row.get('sdg_3'),
                    'sdg_4': row.get('sdg_4'),
                    'sdg_5': row.get('sdg_5'),
                    'sdg_6': row.get('sdg_6'),
                    'sdg_7': row.get('sdg_7'),
                    'sdg_8': row.get('sdg_8'),
                    'sdg_9': row.get('sdg_9'),
                    'sdg_10': row.get('sdg_10'),
                    'sdg_11': row.get('sdg_11'),
                    'sdg_12': row.get('sdg_12'),
                    'sdg_13': row.get('sdg_13'),
                    'sdg_14': row.get('sdg_14'),
                    'sdg_15': row.get('sdg_15'),
                    'sdg_16': row.get('sdg_16'),
                    'sdg_17': row.get('sdg_17'),
                    'advocacy': row.get('advocacy'),
                    'dialogue_interfaith': row.get('dialogue_interfaith'),
                    'disaster_relief': row.get('disaster_relief'),
                    'divestment': row.get('divestment'),
                    'education_training': row.get('education_training'),
                    'greening_worship_places': row.get('greening_worship_places'),
                    'indigenous_knowledge': row.get('indigenous_knowledge'),
                    'lifestyle_promotion': row.get('lifestyle_promotion'),
                    'lobbying': row.get('lobbying'),
                    'losses_damages_activities': row.get('losses_damages_activities'),
                    'mitigation_adaptation': row.get('mitigation_adaptation'),
                    'nature_solutions': row.get('nature_solutions'),
                    'prayer_worship': row.get('prayer_worship'),
                    'protection_conservation': row.get('protection_conservation'),
                    'public_engagement': row.get('public_engagement'),
                    'renewable_energy': row.get('renewable_energy'),
                    'research': row.get('research'),
                    'resilience_building': row.get('resilience_building'),
                    'statement_release': row.get('statement_release'),
                    'tree_planting_activity': row.get('tree_planting_activity'),
                    'waste_management': row.get('waste_management'),
                    'youth_engagement': row.get('youth_engagement'),
                }
            )
        except Exception as e:
            # Log the error to the file and skip this row
            with open('error_query.txt', 'a',  encoding='utf-8') as log_file:
                log_file.write(f"Error occurred with row: {row_dict}\n")
                log_file.write(f"Field causing the issue: {e}\n\n")
            continue  # Skip to the next row

def main():
    excel_path = r"C:\Users\sudee\Documents\Projects\DSSD\myproject\excel_data.xlsx"
    import_data(excel_path)
    print("Data imported successfully!")

if __name__ == "__main__":
    main()
