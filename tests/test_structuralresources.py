from istacpy.structuralresources import (
    category,
    classifications,
    concepts,
    datastructures,
    variables,
)

from .services import is_valid_response

# =====================================
# CATEGORY
# =====================================


def test_get_structuralresources_categorisations():
    response = category.get_structuralresources_categorisations()
    assert is_valid_response(response) is True


def test_get_structuralresources_categorisations_agency():
    response = category.get_structuralresources_categorisations_agency('ISTAC')
    assert is_valid_response(response) is True


def test_get_structuralresources_categorisations_agency_resource():
    response = category.get_structuralresources_categorisations_agency_resource(
        'ISTAC', 'cat2'
    )
    assert is_valid_response(response) is True


def test_get_structuralresources_categorisations_agency_resource_version():
    response = category.get_structuralresources_categorisations_agency_resource_version(
        'ISTAC', 'cat2', '01.000'
    )
    assert is_valid_response(response) is True


def test_get_structuralresources_category_schemes():
    response = category.get_structuralresources_category_schemes()
    assert is_valid_response(response) is True


def test_get_structuralresources_category_schemes_agency():
    response = category.get_structuralresources_category_schemes_agency('ISTAC')
    assert is_valid_response(response) is True


def test_get_structuralresources_category_schemes_agency_resource():
    response = category.get_structuralresources_category_schemes_agency_resource(
        'ISTAC', 'TEMAS_CANARIAS'
    )
    assert is_valid_response(response) is True


def test_get_structuralresources_category_schemes_agency_resource_version():
    response = category.get_structuralresources_category_schemes_agency_resource_version(
        'ISTAC', 'TEMAS_CANARIAS', '01.000'
    )
    assert is_valid_response(response) is True


def test_get_structuralresources_category_schemes_agency_resource_version_categories():
    g = category.get_structuralresources_category_schemes_agency_resource_version_categories
    response = g('ISTAC', 'TEMAS_CANARIAS', '01.000')
    assert is_valid_response(response) is True


def test_get_structuralresources_category_schemes_agency_resource_version_categories_id():
    c = category
    g = c.get_structuralresources_category_schemes_agency_resource_version_categories_id
    response = g('ISTAC', 'TEMAS_CANARIAS', '01.000', '060')
    assert is_valid_response(response) is True


# =====================================
# CLASSIFICATIONS
# =====================================


def test_get_structuralresources_codelist_families():
    response = classifications.get_structuralresources_codelist_families()
    assert is_valid_response(response) is True


def test_get_structuralresources_codelist_families_id():
    response = classifications.get_structuralresources_codelist_families_id()
    assert is_valid_response(response) is True


def test_get_structuralresources_codelists():
    response = classifications.get_structuralresources_codelists()
    assert is_valid_response(response) is True


def test_get_structuralresources_codelists_agency():
    response = classifications.get_structuralresources_codelists_agency('ISTAC')
    assert is_valid_response(response) is True


def test_get_structuralresources_codelists_agency_resource():
    response = classifications.get_structuralresources_codelists_agency_resource(
        'ISTAC', 'CL_AREA_ES'
    )
    assert is_valid_response(response) is True


def test_get_structuralresources_codelists_agency_resource_version():
    response = classifications.get_structuralresources_codelists_agency_resource_version(
        'ISTAC', 'CL_AREA_ES', '01.000'
    )
    assert is_valid_response(response) is True


def test_get_structuralresources_codelists_agency_resource_version_codes():
    response = (
        classifications.get_structuralresources_codelists_agency_resource_version_codes(
            'ISTAC', 'CL_AREA_ES', '01.000'
        )
    )
    assert is_valid_response(response) is True


def test_get_structuralresources_codelists_agency_resource_version_codes_codeid():
    c = classifications
    response = c.get_structuralresources_codelists_agency_resource_version_codes_codeid(
        'ISTAC', 'CL_AREA_ES', '01.000', 'ES706A01'
    )
    assert is_valid_response(response) is True


# =====================================
# CONCEPTS
# =====================================


def test_get_structuralresources_concept_types():
    response = concepts.get_structuralresources_concept_types()
    assert is_valid_response(response) is True


def test_get_structuralresources_concept_schemes():
    response = concepts.get_structuralresources_concept_schemes()
    assert is_valid_response(response) is True


def test_get_structuralresources_concept_schemes_agency():
    response = concepts.get_structuralresources_concept_schemes_agency('ISTAC')
    assert is_valid_response(response) is True


def test_get_structuralresources_concept_schemes_agency_resource():
    response = concepts.get_structuralresources_concept_schemes_agency_resource('ISTAC')
    assert is_valid_response(response) is True


def test_get_structuralresources_concept_schemes_agency_resource_version():
    response = concepts.get_structuralresources_concept_schemes_agency_resource_version(
        'ISTAC', 'CL_AREA', '01.000'
    )
    assert is_valid_response(response) is True


def test_get_structuralresources_concept_schemes_agency_resource_version_concepts():
    response = (
        concepts.get_structuralresources_concept_schemes_agency_resource_version_concepts(
            'ISTAC', 'CL_AREA', '01.000'
        )
    )
    assert is_valid_response(response) is True


def test_get_structuralresources_concept_schemes_agency_resource_version_concepts_id():
    c = concepts
    r = c.get_structuralresources_concept_schemes_agency_resource_version_concepts_id(
        'ISTAC', 'CL_AREA', '01.000', 0
    )
    assert is_valid_response(r) is True


# =====================================
# DATASTRUCTURES
# =====================================


def test_get_structuralresources_content_constraints():
    response = datastructures.get_structuralresources_content_constraints()
    assert is_valid_response(response) is True


def test_get_structuralresources_content_constraints_agency():
    response = datastructures.get_structuralresources_content_constraints_agency('ISTAC')
    assert is_valid_response(response) is True


def test_get_structuralresources_content_constraints_agency_resource():
    response = datastructures.get_structuralresources_content_constraints_agency_resource(
        'ISTAC', 'CL_AREA'
    )
    assert is_valid_response(response) is True


def test_get_structuralresources_content_constraints_agency_resource_version():
    response = (
        datastructures.get_structuralresources_content_constraints_agency_resource_version(
            'ISTAC', 'CL_AREA', '01.000'
        )
    )
    assert is_valid_response(response) is True


def test_get_structuralresources_content_constraints_agency_resource_version_regions():
    ds = datastructures
    response = (
        ds.get_structuralresources_content_constraints_agency_resource_version_regions(
            '0001', 'ISTAC', 'CL_AREA', '01.000'
        )
    )
    assert is_valid_response(response) is True


def test_get_structuralresources_data_structures():
    response = datastructures.get_structuralresources_data_structures()
    assert is_valid_response(response) is True


def test_get_structuralresources_data_structures_agency():
    response = datastructures.get_structuralresources_data_structures_agency('ISTAC')
    assert is_valid_response(response) is True


def test_get_structuralresources_data_structures_agency_resource():
    response = datastructures.get_structuralresources_data_structures_agency_resource(
        'ISTAC', 'CL_AREA'
    )
    assert is_valid_response(response) is True


def test_get_structuralresources_data_structures_agency_resource_version():
    response = (
        datastructures.get_structuralresources_data_structures_agency_resource_version(
            'ISTAC', 'CL_AREA', '01.000'
        )
    )
    assert is_valid_response(response) is True


# =====================================
# VARIABLES
# =====================================


def test_get_structuralresources_variable_families():
    response = variables.get_structuralresources_variable_families()
    assert is_valid_response(response) is True


def test_get_structuralresources_variable_families_id():
    response = variables.get_structuralresources_variable_families_id('VRF_DEMOGRAFICAS')
    assert is_valid_response(response) is True


def test_get_structuralresources_variable_families_id_variables():
    response = variables.get_structuralresources_variable_families_id_variables(
        'VRF_DEMOGRAFICAS'
    )
    assert is_valid_response(response) is True


def test_get_structuralresources_variables():
    response = variables.get_structuralresources_variables()
    assert is_valid_response(response) is True


def test_get_structuralresources_variables_id():
    response = variables.get_structuralresources_variables_id('VR_SEXO')
    assert is_valid_response(response) is True


def test_get_structuralresources_variableelements():
    response = variables.get_structuralresources_variableelements('VR_SEXO')
    assert is_valid_response(response) is True


def test_get_structuralresources_variableelements_resource():
    response = variables.get_structuralresources_variableelements_resource(
        'VR_SEXO', 'FEMALE'
    )
    assert is_valid_response(response) is True


def test_get_structuralresources_geoinfo():
    response = variables.get_structuralresources_geoinfo('VR_TERRITORIO', 'MUN_ICOD_VINOS')
    assert is_valid_response(response) is True
