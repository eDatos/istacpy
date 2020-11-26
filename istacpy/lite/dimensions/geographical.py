from .base import Granularity


class GeographicalGranularity(Granularity):
    COUNTRIES, COUNTRIES_ID = 'COUNTRIES', 'T'
    REGIONS, REGIONS_ID = 'REGIONS', 'R'
    ISLANDS, ISLANDS_ID = 'ISLANDS', 'I'
    PROVINCES, PROVINCES_ID = 'PROVINCES', 'P'
    COUNTIES, COUNTIES_ID = 'COUNTIES', 'C'
    MUNICIPALITIES, MUNICIPALITIES_ID = 'MUNICIPALITIES', 'M'

    CODES = {
        COUNTRIES_ID: COUNTRIES,
        REGIONS_ID: REGIONS,
        ISLANDS_ID: ISLANDS,
        PROVINCES_ID: PROVINCES,
        COUNTIES_ID: COUNTIES,
        MUNICIPALITIES_ID: MUNICIPALITIES,
    }


class GeographicalRepresentation:
    CODES = {
        'GRAN CANARIA': {
            GeographicalGranularity.REGIONS: {
                'ES70': 'CANARIAS',
            },
            GeographicalGranularity.ISLANDS: {
                'ES705': 'GRAN CANARIA',
            },
            GeographicalGranularity.PROVINCES: {
                'ES701': 'LAS PALMAS',
            },
            GeographicalGranularity.COUNTIES: {
                'ES705A11': 'GRAN CANARIA - ÁREA METROPOLITANA',
                'ES705A21': 'GRAN CANARIA NORTE - CENTRO NORTE',
                'ES705A22': 'GRAN CANARIA NORTE - NOROESTE',
                'ES705A23': 'GRAN CANARIA NORTE - OESTE',
                'ES705A31': 'GRAN CANARIA SUR - SUR',
                'ES705A32': 'GRAN CANARIA SUR - SURESTE',
            },
            GeographicalGranularity.MUNICIPALITIES: {
                '35001': 'AGAETE',
                '35002': 'AGÜIMES',
                '35005': 'ARTENARA',
                '35006': 'ARUCAS',
                '35008': 'FIRGAS',
                '35009': 'GÁLDAR',
                '35011': 'INGENIO',
                '35012': 'MOGÁN',
                '35013': 'MOYA',
                '35016': 'LAS PALMAS DE GRAN CANARIA',
                '35019': 'SAN BARTOLOMÉ DE TIRAJANA',
                '35020': 'LA ALDEA DE SAN NICOLÁS (LA ALDEA)',
                '35021': 'SANTA BRÍGIDA',
                '35022': 'SANTA LUCÍA DE TIRAJANA',
                '35023': 'SANTA MARÍA DE GUÍA DE GRAN CANARIA',
                '35025': 'TEJEDA',
                '35026': 'TELDE',
                '35027': 'TEROR',
                '35031': 'VALSEQUILLO DE GRAN CANARIA',
                '35032': 'VALLESECO',
                '35033': 'VEGA DE SAN MATEO',
            },
        },
        'TENERIFE': {
            GeographicalGranularity.REGIONS: {
                'ES70': 'CANARIAS',
            },
            GeographicalGranularity.ISLANDS: {
                'ES709': 'TENERIFE',
            },
            GeographicalGranularity.PROVINCES: {
                'ES702': 'SANTA CRUZ DE TENERIFE',
            },
            GeographicalGranularity.COUNTIES: {
                'ES709A11': 'TENERIFE - ÁREA METROPOLITANA',
                'ES709A21': 'TENERIFE NORTE - ACENTEJO',
                'ES709A22': 'TENERIFE NORTE - DAUTE',
                'ES709A23': 'TENERIFE NORTE - ICOD',
                'ES709A24': 'TENERIFE NORTE - VALLE DE LA OROTAVA',
                'ES709A31': 'TENERIFE SUR - ABONA',
                'ES709A32': 'TENERIFE SUR - SUROESTE',
                'ES709A33': 'TENERIFE SUR - VALLE DE GÜÍMAR',
            },
            GeographicalGranularity.MUNICIPALITIES: {
                '38001': 'ADEJE',
                '38004': 'ARAFO',
                '38005': 'ARICO',
                '38006': 'ARONA',
                '38010': 'BUENAVISTA DEL NORTE',
                '38011': 'CANDELARIA',
                '38012': 'FASNIA',
                '38015': 'GARACHICO',
                '38017': 'GRANADILLA DE ABONA',
                '38018': 'LA GUANCHA',
                '38019': 'GUÍA DE ISORA',
                '38020': 'GÜÍMAR',
                '38022': 'ICOD DE LOS VINOS',
                '38023': 'SAN CRISTÓBAL DE LA LAGUNA',
                '38025': 'LA MATANZA DE ACENTEJO',
                '38026': 'LA OROTAVA',
                '38028': 'PUERTO DE LA CRUZ',
                '38031': 'LOS REALEJOS',
                '38032': 'EL ROSARIO',
                '38034': 'SAN JUAN DE LA RAMBLA',
                '38035': 'SAN MIGUEL DE ABONA',
                '38038': 'SANTA CRUZ DE TENERIFE',
                '38039': 'SANTA ÚRSULA',
                '38040': 'SANTIAGO DEL TEIDE',
                '38041': 'EL SAUZAL',
                '38042': 'LOS SILOS',
                '38043': 'TACORONTE',
                '38044': 'EL TANQUE',
                '38046': 'TEGUESTE',
                '38051': 'LA VICTORIA DE ACENTEJO',
                '38052': 'VILAFLOR DE CHASNA',
            },
        },
        'EL HIERRO': {
            GeographicalGranularity.REGIONS: {
                'ES70': 'CANARIAS',
            },
            GeographicalGranularity.ISLANDS: {
                'ES703': 'EL HIERRO',
            },
            GeographicalGranularity.PROVINCES: {
                'ES702': 'SANTA CRUZ DE TENERIFE',
            },
            GeographicalGranularity.COUNTIES: {'ES703A00': 'EL HIERRO - EL HIERRO'},
            GeographicalGranularity.MUNICIPALITIES: {
                '38013': 'FRONTERA',
                '38048': 'VALVERDE',
                '38901': 'EL PINAR DE EL HIERRO',
            },
        },
        'LA GOMERA': {
            GeographicalGranularity.REGIONS: {
                'ES70': 'CANARIAS',
            },
            GeographicalGranularity.ISLANDS: {
                'ES706': 'LA GOMERA',
            },
            GeographicalGranularity.PROVINCES: {
                'ES702': 'SANTA CRUZ DE TENERIFE',
            },
            GeographicalGranularity.COUNTIES: {
                'ES706A01': 'LA GOMERA - NORTE',
                'ES706A02': 'LA GOMERA - SUR',
            },
            GeographicalGranularity.MUNICIPALITIES: {
                '38002': 'AGULO',
                '38003': 'ALAJERÓ',
                '38021': 'HERMIGUA',
                '38036': 'SAN SEBASTIÁN DE LA GOMERA',
                '38049': 'VALLE GRAN REY',
                '38050': 'VALLEHERMOSO',
            },
        },
        'LA PALMA': {
            GeographicalGranularity.REGIONS: {
                'ES70': 'CANARIAS',
            },
            GeographicalGranularity.ISLANDS: {
                'ES707': 'LA PALMA',
            },
            GeographicalGranularity.PROVINCES: {
                'ES702': 'SANTA CRUZ DE TENERIFE',
            },
            GeographicalGranularity.COUNTIES: {
                'ES707A01': 'LA PALMA - CAPITALINA',
                'ES707A02': 'LA PALMA - NORESTE',
                'ES707A03': 'LA PALMA - NOROESTE',
                'ES707A04': 'LA PALMA - VALLE DE ARIDANE',
            },
            GeographicalGranularity.MUNICIPALITIES: {
                '38024': 'LOS LLANOS DE ARIDANE',
                '38037': 'SANTA CRUZ DE LA PALMA',
                '38027': 'EL PASO',
                '38008': 'BREÑA ALTA',
                '38009': 'BREÑA BAJA',
                '38053': 'VILLA DE MAZO',
                '38045': 'TAZACORTE',
                '38033': 'SAN ANDRÉS Y SAUCES',
                '38047': 'TIJARAFE',
                '38030': 'PUNTALLANA',
                '38029': 'PUNTAGORDA',
                '38007': 'BARLOVENTO',
                '38014': 'FUENCALIENTE DE LA PALMA',
                '38016': 'GARAFÍA',
            },
        },
        'FUERTEVENTURA': {
            GeographicalGranularity.REGIONS: {
                'ES70': 'CANARIAS',
            },
            GeographicalGranularity.ISLANDS: {
                'ES704': 'FUERTEVENTURA',
            },
            GeographicalGranularity.PROVINCES: {
                'ES701': 'LAS PALMAS',
            },
            GeographicalGranularity.COUNTIES: {
                'ES704A01': 'FUERTEVENTURA - CENTRO',
                'ES704A02': 'FUERTEVENTURA - NORTE',
                'ES704A03': 'FUERTEVENTURA - SUR',
            },
            GeographicalGranularity.MUNICIPALITIES: {
                '35003': 'ANTIGUA',
                '35007': 'BETANCURIA',
                '35014': 'LA OLIVA',
                '35015': 'PÁJARA',
                '35017': 'PUERTO DEL ROSARIO',
                '35030': 'TUINEJE',
            },
        },
        'LANZAROTE': {
            GeographicalGranularity.REGIONS: {
                'ES70': 'CANARIAS',
            },
            GeographicalGranularity.ISLANDS: {
                'ES708': 'LANZAROTE',
            },
            GeographicalGranularity.PROVINCES: {
                'ES701': 'LAS PALMAS',
            },
            GeographicalGranularity.COUNTIES: {
                'ES708A01': 'Lanzarote - Este',
                'ES708A02': 'Lanzarote - Norte',
                'ES708A03': 'Lanzarote - Suroeste',
            },
            GeographicalGranularity.MUNICIPALITIES: {
                '35004': 'ARRECIFE',
                '35010': 'HARÍA',
                '35018': 'SAN BARTOLOMÉ',
                '35024': 'TEGUISE',
                '35028': 'TÍAS',
                '35029': 'TINAJO',
                '35034': 'YAIZA',
            },
        },
    }

    @classmethod
    def build_flattened_codes(cls):
        cls.FLATTENED_CODES = {}
        for granularity in cls.CODES.values():
            for items in granularity.values():
                cls.FLATTENED_CODES.update(items)

    @classmethod
    def build_flattened_codes_by_title(cls):
        cls.FLATTENED_CODES_BY_TITLE = {}
        for code, title in cls.FLATTENED_CODES.items():
            cls.FLATTENED_CODES_BY_TITLE[title] = code

    @classmethod
    def get_codes(cls, island, granularity):
        locations = cls.CODES[island][granularity]
        return locations.keys()

    @classmethod
    def get_title(cls, code):
        return cls.FLATTENED_CODES.get(code, code)

    @classmethod
    def get_code(cls, title):
        return cls.FLATTENED_CODES_BY_TITLE.get(title, title)


GeographicalGranularity.build_swapped_codes()
GeographicalRepresentation.build_flattened_codes()
GeographicalRepresentation.build_flattened_codes_by_title()