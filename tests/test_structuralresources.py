import pytest

from istacpy.structuralresources import (
    category,
    classifications,
    concepts,
    datastructures,
    variables,
)

from .services import assert_valid_response

# =====================================
# CATEGORY
# =====================================


def test_get_structuralresources_categorisations():
    response = category.get_structuralresources_categorisations(
        query='name LIKE "CAT"', orderby='id ASC'
    )
    assert_valid_response(response)


def test_get_structuralresources_categorisations_agency():
    response = category.get_structuralresources_categorisations_agency(
        agencyid='ISTAC', query='name LIKE "CAT"', orderby='id ASC'
    )
    assert_valid_response(response)


def test_get_structuralresources_categorisations_agency_resource():
    response = category.get_structuralresources_categorisations_agency_resource(
        agencyid='ISTAC', resourceid='cat2', query='name LIKE "CAT"', orderby='id ASC'
    )
    assert_valid_response(response)


def test_get_structuralresources_categorisations_agency_resource_version():
    response = category.get_structuralresources_categorisations_agency_resource_version(
        agencyid='ISTAC', resourceid='cat2', version='01.000'
    )
    assert_valid_response(response)


def test_get_structuralresources_category_schemes():
    response = category.get_structuralresources_category_schemes(
        query='name ILIKE "OPERACIONES"', orderby='id ASC'
    )
    assert_valid_response(response)


def test_get_structuralresources_category_schemes_agency():
    response = category.get_structuralresources_category_schemes_agency(
        agencyid='ISTAC', query='name ILIKE "OPERACIONES"', orderby='id ASC'
    )
    assert_valid_response(response)


def test_get_structuralresources_category_schemes_agency_resource():
    response = category.get_structuralresources_category_schemes_agency_resource(
        agencyid='ISTAC',
        resourceid='TEMAS_CANARIAS',
        query='name ILIKE "OPERACIONES"',
        orderby='id ASC',
    )
    assert_valid_response(response)


def test_get_structuralresources_category_schemes_agency_resource_version():
    response = category.get_structuralresources_category_schemes_agency_resource_version(
        agencyid='ISTAC', resourceid='TEMAS_CANARIAS', version='01.000'
    )
    assert_valid_response(response)


def test_get_structuralresources_category_schemes_agency_resource_version_categories():
    g = category.get_structuralresources_category_schemes_agency_resource_version_categories
    response = g(
        agencyid='ISTAC',
        resourceid='TEMAS_CANARIAS',
        version='01.000',
        query='name ILIKE "COMERCIO"',
        orderby='id ASC',
    )
    assert_valid_response(response)


def test_get_structuralresources_category_schemes_agency_resource_version_categories_id():
    c = category
    g = c.get_structuralresources_category_schemes_agency_resource_version_categories_id
    response = g(
        agencyid='ISTAC', resourceid='TEMAS_CANARIAS', version='01.000', categoryid='060'
    )
    assert_valid_response(response)


# =====================================
# CLASSIFICATIONS
# =====================================


def test_get_structuralresources_codelist_families():
    response = classifications.get_structuralresources_codelist_families(
        orderby='id ASC', query='id EQ 2090'
    )
    assert_valid_response(response)


@pytest.mark.skip(reason="There's no codelist family to test against")
def test_get_structuralresources_codelist_families_id():
    response = classifications.get_structuralresources_codelist_families_id('CODELIST_ID')
    assert_valid_response(response)


def test_get_structuralresources_codelists():
    response = classifications.get_structuralresources_codelists(
        query='name ILIKE "AEROPUERTOS"', orderby='id ASC'
    )
    assert_valid_response(response)


def test_get_structuralresources_codelists_agency():
    response = classifications.get_structuralresources_codelists_agency(
        agencyid='ISTAC', query='name ILIKE "AEROPUERTOS"', orderby='id ASC'
    )
    assert_valid_response(response)


def test_get_structuralresources_codelists_agency_resource():
    response = classifications.get_structuralresources_codelists_agency_resource(
        agencyid='ISTAC',
        resourceid='CL_AEROPUERTOS',
        query='name ILIKE "AEROPUERTOS"',
        orderby='id ASC',
    )
    assert_valid_response(response)


def test_get_structuralresources_codelists_agency_resource_version():
    response = classifications.get_structuralresources_codelists_agency_resource_version(
        agencyid='ISTAC', resourceid='CL_AEROPUERTOS', version='01.002'
    )
    assert_valid_response(response)


def test_get_structuralresources_codelists_agency_resource_version_codes():
    response = (
        classifications.get_structuralresources_codelists_agency_resource_version_codes(
            agencyid='ISTAC',
            resourceid='CL_AEROPUERTOS',
            version='01.002',
            query='name ILIKE "AEROPUERTOS"',
            orderby='id ASC',
            fields='+open',
            as_dataframe=False
        )
    )
    assert_valid_response(response)


def test_get_structuralresources_codelists_agency_resource_version_codes_codeid():
    c = classifications
    response = c.get_structuralresources_codelists_agency_resource_version_codes_codeid(
        agencyid='ISTAC', resourceid='CL_AEROPUERTOS', version='01.002', codeid='ES_GCFV'
    )
    assert_valid_response(response)


# =====================================
# CONCEPTS
# =====================================


@pytest.mark.skip(reason="Response does curiously not include selfLink field")
def test_get_structuralresources_concept_types():
    response = concepts.get_structuralresources_concept_types()
    assert_valid_response(response)


def test_get_structuralresources_concept_schemes():
    response = concepts.get_structuralresources_concept_schemes(
        query='name ILIKE "TRANSPORTE"', orderby='id ASC'
    )
    assert_valid_response(response)


def test_get_structuralresources_concept_schemes_agency():
    response = concepts.get_structuralresources_concept_schemes_agency(
        agencyid='ISTAC', query='name ILIKE "TRANSPORTE"', orderby='id ASC'
    )
    assert_valid_response(response)


def test_get_structuralresources_concept_schemes_agency_resource():
    response = concepts.get_structuralresources_concept_schemes_agency_resource(
        agencyid='ISTAC',
        resourceid='CSM_C00017A',
        query='name ILIKE "TRANSPORTE"',
        orderby='id ASC',
    )
    assert_valid_response(response)


def test_get_structuralresources_concept_schemes_agency_resource_version():
    response = concepts.get_structuralresources_concept_schemes_agency_resource_version(
        agencyid='ISTAC',
        resourceid='CSM_C00017A',
        version='01.000',
    )
    assert_valid_response(response)


def test_get_structuralresources_concept_schemes_agency_resource_version_concepts():
    response = (
        concepts.get_structuralresources_concept_schemes_agency_resource_version_concepts(
            agencyid='ISTAC',
            resourceid='CSM_C00010A_SIE',
            version='01.000',
            query='name ILIKE "TASA"',
            orderby='id ASC',
            fields='+description',
        )
    )
    assert_valid_response(response)


def test_get_structuralresources_concept_schemes_agency_resource_version_concepts_id():
    c = concepts
    r = c.get_structuralresources_concept_schemes_agency_resource_version_concepts_id(
        agencyid='ISTAC',
        resourceid='CSM_C00010A_SIE',
        version='01.000',
        conceptid='ELECTORES',
    )
    assert_valid_response(r)


# =====================================
# DATASTRUCTURES
# =====================================


def test_get_structuralresources_content_constraints():
    response = datastructures.get_structuralresources_content_constraints(
        query='name ILIKE "AFILIACIONES"', orderby='id ASC'
    )
    assert_valid_response(response)


def test_get_structuralresources_content_constraints_agency():
    response = datastructures.get_structuralresources_content_constraints_agency(
        agencyid='ISTAC', query='name ILIKE "AFILIACIONES"', orderby='id ASC'
    )
    assert_valid_response(response)


def test_get_structuralresources_content_constraints_agency_resource():
    response = datastructures.get_structuralresources_content_constraints_agency_resource(
        agencyid='ISTAC',
        resourceid='CSM_C00010A_SIE',
        query='name ILIKE "AFILIACIONES"',
        orderby='id ASC',
    )
    assert_valid_response(response)


@pytest.mark.skip(reason="There's no content constraint to test against")
def test_get_structuralresources_content_constraints_agency_resource_version():
    response = (
        datastructures.get_structuralresources_content_constraints_agency_resource_version(
            agencyid='ISTAC', resourceid='CSM_C00010A_SIE', version='01.000'
        )
    )
    assert_valid_response(response)


@pytest.mark.skip(reason="There's no content constraint to test against")
def test_get_structuralresources_content_constraints_agency_resource_version_regions():
    ds = datastructures
    response = (
        ds.get_structuralresources_content_constraints_agency_resource_version_regions(
            regioncode='0001',
            agencyid='ISTAC',
            resourceid='CSM_C00010A_SIE',
            version='01.000',
        )
    )
    assert_valid_response(response)


def test_get_structuralresources_data_structures():
    response = datastructures.get_structuralresources_data_structures(
        query='name ILIKE "ELECCIONES"', orderby='id ASC'
    )
    assert_valid_response(response)


def test_get_structuralresources_data_structures_agency():
    response = datastructures.get_structuralresources_data_structures_agency(
        agencyid='ISTAC', query='name ILIKE "ELECCIONES"', orderby='id ASC'
    )
    assert_valid_response(response)


def test_get_structuralresources_data_structures_agency_resource():
    response = datastructures.get_structuralresources_data_structures_agency_resource(
        agencyid='ISTAC',
        resourceid='DSD_C00010A_00001',
        query='name ILIKE "ELECCIONES"',
        orderby='id ASC',
    )
    assert_valid_response(response)


def test_get_structuralresources_data_structures_agency_resource_version():
    response = (
        datastructures.get_structuralresources_data_structures_agency_resource_version(
            agencyid='ISTAC', resourceid='DSD_C00010A_00001', version='01.001'
        )
    )
    assert_valid_response(response)


# =====================================
# VARIABLES
# =====================================


def test_get_structuralresources_variable_families():
    response = variables.get_structuralresources_variable_families(
        query='name ILIKE "SALUD"', orderby='id ASC'
    )
    assert_valid_response(response)


def test_get_structuralresources_variable_families_id():
    response = variables.get_structuralresources_variable_families_id(id='VRF_DEMOGRAFICAS')
    assert_valid_response(response)


def test_get_structuralresources_variable_families_id_variables():
    response = variables.get_structuralresources_variable_families_id_variables(
        id='VRF_DEMOGRAFICAS', query='name ILIKE "EDAD"', orderby='id ASC'
    )
    assert_valid_response(response)


def test_get_structuralresources_variables():
    response = variables.get_structuralresources_variables(
        query='name ILIKE "IDIOMA"', orderby='id ASC'
    )
    assert_valid_response(response)


def test_get_structuralresources_variables_id():
    response = variables.get_structuralresources_variables_id(id='VR_IDIOMA')
    assert_valid_response(response)


def test_get_structuralresources_variableelements():
    response = variables.get_structuralresources_variableelements(
        variableid='VR_SEXO', query='name ILIKE "MUJER"', orderby='id ASC'
    )
    assert_valid_response(response)


def test_get_structuralresources_variableelements_resource():
    response = variables.get_structuralresources_variableelements_resource(
        variableid='VR_SEXO', resourceid='FEMALE'
    )
    assert_valid_response(response)


def test_get_structuralresources_geoinfo():
    response = variables.get_structuralresources_geoinfo(
        variableid='VR_TERRITORIO',
        resourceid='MUN_ICOD_VINOS',
        fields='-geometry',
        orderby='id ASC',
    )
    assert isinstance(response, dict) is True
    assert 'type' in response
    assert 'features' in response
