from cohortextractor import StudyDefinition, patients, codelist, codelist_from_csv  # NOQA


study = StudyDefinition(
    default_expectations={
        "date": {"earliest": "1900-01-01", "latest": "today"},
        "rate": "uniform",
        "incidence": 1.0,
    },

    population=patients.satisfying(
        "imd1 > 500 AND did_die",
        did_die=patients.with_death_recorded_in_primary_care(
                on_or_before="2018-12-31",
                on_or_after="2010-01-01",
                returning="binary_flag")
        ),

    dob=patients.date_of_birth(
        "YYYY-MM",
        return_expectations={
            "date": {"earliest": "1920-01-01", "latest": "2018-12-31"},
            "rate": "uniform",
        }
    ),

    died_date_gp=patients.with_death_recorded_in_primary_care(
        on_or_before="2018-12-31",
        on_or_after="2010-01-01",
        returning="date_of_death",
        return_expectations={
            "date": {"earliest" : "2010-01-01", "latest" : "2018-12-31"},
            "rate" : "uniform"
        },
    ),

    imd1=patients.address_as_of(
        "2010-01-01",
        returning="index_of_multiple_deprivation",
        round_to_nearest=100,
        return_expectations={
            "rate": "universal",
            "category": {"ratios": {"100": 0.1, "200": 0.2, "300": 0.7}},
        },
    ),

    imd2=patients.address_as_of(
        "2015-01-01",
        returning="index_of_multiple_deprivation",
        round_to_nearest=100,
        return_expectations={
            "rate": "universal",
            "category": {"ratios": {"100": 0.2, "200": 0.2, "300": 0.6}},
        },
    ),

    imd3=patients.address_as_of(
        "2020-12-31",
        returning="index_of_multiple_deprivation",
        round_to_nearest=100,
        return_expectations={
            "rate": "universal",
            "category": {"ratios": {"100": 0.2, "200": 0.2, "300": 0.1,"400" : 0.5}}
        }
    )
)
