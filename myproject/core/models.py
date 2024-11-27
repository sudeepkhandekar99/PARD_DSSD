from django.db import models


class Organization(models.Model):
    name = models.CharField(max_length=5000, null=False)  # Not nullable
    acronym = models.CharField(max_length=5000, blank=True, null=True)
    website = models.URLField(max_length=5000, blank=True, null=True)
    religious_affiliation = models.CharField(max_length=5000, blank=True, null=True)
    religious_subgroup = models.CharField(max_length=5000, blank=True, null=True)
    continent_hq = models.CharField(max_length=5000, blank=True, null=True)
    country_hq = models.CharField(max_length=5000, blank=True, null=True)
    environment_projects_url = models.URLField(max_length=5000, blank=True, null=True)
    reports_publications = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class Project(models.Model):
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    source_name = models.CharField(max_length=5000, blank=True, null=True)
    project_name = models.CharField(max_length=5000)
    project_website = models.URLField(max_length=5000, blank=True, null=True)
    project_location = models.CharField(max_length=5000, blank=True, null=True)
    aims_objectives = models.TextField(blank=True, null=True)
    duration = models.CharField(max_length=5000, blank=True, null=True)
    budget = models.CharField(max_length=5000, blank=True, null=True)
    donors = models.TextField(blank=True, null=True)
    partners = models.TextField(blank=True, null=True)
    target_groups = models.TextField(blank=True, null=True)
    main_activities_summary = models.TextField(blank=True, null=True)
    evaluation_results = models.TextField(blank=True, null=True)
    lessons_learned = models.TextField(blank=True, null=True)
    religion_role = models.TextField(blank=True, null=True)
    reports_documents_urls = models.TextField(blank=True, null=True)
    additional_comments = models.TextField(blank=True, null=True)

    animals = models.BooleanField(default=False)
    agriculture = models.BooleanField(default=False)
    biodiversity = models.BooleanField(default=False)
    climate_change = models.BooleanField(default=False)
    climate_justice = models.BooleanField(default=False)
    climate_science = models.BooleanField(default=False)
    conservation = models.BooleanField(default=False)
    development = models.BooleanField(default=False)
    divestment_investment = models.BooleanField(default=False)
    economic_models = models.BooleanField(default=False)
    ecology = models.BooleanField(default=False)
    ecosystems = models.BooleanField(default=False)
    ecotourism = models.BooleanField(default=False)
    emissions = models.BooleanField(default=False)
    environmental_awareness = models.BooleanField(default=False)
    food_security = models.BooleanField(default=False)
    forests_deforestation = models.BooleanField(default=False)
    health_wellbeing = models.BooleanField(default=False)
    indigenous_peoples = models.BooleanField(default=False)
    lifestyle_change = models.BooleanField(default=False)
    livelihoods = models.BooleanField(default=False)
    losses_damages = models.BooleanField(default=False)
    natural_hazards = models.BooleanField(default=False)
    natural_resources = models.BooleanField(default=False)
    nature_based_solutions = models.BooleanField(default=False)
    pollution = models.BooleanField(default=False)
    poverty = models.BooleanField(default=False)
    refugees = models.BooleanField(default=False)
    tree_planting = models.BooleanField(default=False)
    waste = models.BooleanField(default=False)
    water = models.BooleanField(default=False)
    other_environmental_themes = models.TextField(blank=True, null=True)

    uses_sdgs = models.BooleanField(default=False)
    sdg_1 = models.BooleanField(default=False)
    sdg_2 = models.BooleanField(default=False)
    sdg_3 = models.BooleanField(default=False)
    sdg_4 = models.BooleanField(default=False)
    sdg_5 = models.BooleanField(default=False)
    sdg_6 = models.BooleanField(default=False)
    sdg_7 = models.BooleanField(default=False)
    sdg_8 = models.BooleanField(default=False)
    sdg_9 = models.BooleanField(default=False)
    sdg_10 = models.BooleanField(default=False)
    sdg_11 = models.BooleanField(default=False)
    sdg_12 = models.BooleanField(default=False)
    sdg_13 = models.BooleanField(default=False)
    sdg_14 = models.BooleanField(default=False)
    sdg_15 = models.BooleanField(default=False)
    sdg_16 = models.BooleanField(default=False)
    sdg_17 = models.BooleanField(default=False)

    advocacy = models.BooleanField(default=False)
    dialogue_interfaith = models.BooleanField(default=False)
    disaster_relief = models.BooleanField(default=False)
    divestment = models.BooleanField(default=False)
    education_training = models.BooleanField(default=False)
    greening_worship_places = models.BooleanField(default=False)
    indigenous_knowledge = models.BooleanField(default=False)
    lifestyle_promotion = models.BooleanField(default=False)
    lobbying = models.BooleanField(default=False)
    losses_damages_activities = models.BooleanField(default=False)
    mitigation_adaptation = models.BooleanField(default=False)
    nature_solutions = models.BooleanField(default=False)
    prayer_worship = models.BooleanField(default=False)
    protection_conservation = models.BooleanField(default=False)
    public_engagement = models.BooleanField(default=False)
    renewable_energy = models.BooleanField(default=False)
    research = models.BooleanField(default=False)
    resilience_building = models.BooleanField(default=False)
    statement_release = models.BooleanField(default=False)
    tree_planting_activity = models.BooleanField(default=False)
    waste_management = models.BooleanField(default=False)
    youth_engagement = models.BooleanField(default=False)

    def __str__(self):
        return self.project_name


class SDGGoal(models.Model):
    name = models.CharField(max_length=255)  # For storing the full goal name
    code = models.CharField(max_length=50, unique=True)  # For storing the short code (e.g., "sdg_1")

    def __str__(self):
        return self.name