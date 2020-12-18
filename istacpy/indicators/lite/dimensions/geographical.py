from istacpy.exceptions import IslandNotFoundError

from .base import CodeStore


class GeographicalGranularity(CodeStore):
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
        'Gran Canaria': {
            GeographicalGranularity.REGIONS: {
                'ES70': 'Canarias',
            },
            GeographicalGranularity.ISLANDS: {
                'ES705': 'Gran Canaria',
            },
            GeographicalGranularity.PROVINCES: {
                'ES701': 'Las Palmas',
            },
            GeographicalGranularity.COUNTIES: {
                'ES705A11': 'Gran Canaria - Área Metropolitana',
                'ES705A21': 'Gran Canaria Norte - Centro Norte',
                'ES705A22': 'Gran Canaria Norte - Noroeste',
                'ES705A23': 'Gran Canaria Norte - Oeste',
                'ES705A31': 'Gran Canaria Sur - Sur',
                'ES705A32': 'Gran Canaria Sur - Sureste',
            },
            GeographicalGranularity.MUNICIPALITIES: {
                '35001': 'Agaete',
                '35002': 'Agüimes',
                '35005': 'Artenara',
                '35006': 'Arucas',
                '35008': 'Firgas',
                '35009': 'Gáldar',
                '35011': 'Ingenio',
                '35012': 'Mogán',
                '35013': 'Moya',
                '35016': 'Las Palmas de Gran Canaria',
                '35019': 'San Bartolomé de Tirajana',
                '35020': 'La Aldea de San Nicolás (La Aldea)',
                '35021': 'Santa Brígida',
                '35022': 'Santa Lucía de Tirajana',
                '35023': 'Santa María de Guía de Gran Canaria',
                '35025': 'Tejeda',
                '35026': 'Telde',
                '35027': 'Teror',
                '35031': 'Valsequillo de Gran Canaria',
                '35032': 'Valleseco',
                '35033': 'Vega de San Mateo',
            },
        },
        'Tenerife': {
            GeographicalGranularity.REGIONS: {
                'ES70': 'Canarias',
            },
            GeographicalGranularity.ISLANDS: {
                'ES709': 'Tenerife',
            },
            GeographicalGranularity.PROVINCES: {
                'ES702': 'Santa Cruz de Tenerife',
            },
            GeographicalGranularity.COUNTIES: {
                'ES709A11': 'Tenerife - Área Metropolitana',
                'ES709A21': 'Tenerife Norte - Acentejo',
                'ES709A22': 'Tenerife Norte - Daute',
                'ES709A23': 'Tenerife Norte - Icod',
                'ES709A24': 'Tenerife Norte - Valle de La Orotava',
                'ES709A31': 'Tenerife Sur - Abona',
                'ES709A32': 'Tenerife Sur - Suroeste',
                'ES709A33': 'Tenerife Sur - Valle de Güímar',
            },
            GeographicalGranularity.MUNICIPALITIES: {
                '38001': 'Adeje',
                '38004': 'Arafo',
                '38005': 'Arico',
                '38006': 'Arona',
                '38010': 'Buenavista del Norte',
                '38011': 'Candelaria',
                '38012': 'Fasnia',
                '38015': 'Garachico',
                '38017': 'Granadilla de Abona',
                '38018': 'La Guancha',
                '38019': 'Guía de Isora',
                '38020': 'Güímar',
                '38022': 'Icod de los Vinos',
                '38023': 'San Cristóbal de La Laguna',
                '38025': 'La Matanza de Acentejo',
                '38026': 'La Orotava',
                '38028': 'Puerto de la Cruz',
                '38031': 'Los Realejos',
                '38032': 'El Rosario',
                '38034': 'San Juan de la Rambla',
                '38035': 'San Miguel de Abona',
                '38038': 'Santa Cruz de Tenerife',
                '38039': 'Santa Úrsula',
                '38040': 'Santiago del Teide',
                '38041': 'El Sauzal',
                '38042': 'Los Silos',
                '38043': 'Tacoronte',
                '38044': 'El Tanque',
                '38046': 'Tegueste',
                '38051': 'La Victoria de Acentejo',
                '38052': 'Vilaflor de Chasna',
            },
        },
        'El Hierro': {
            GeographicalGranularity.REGIONS: {
                'ES70': 'Canarias',
            },
            GeographicalGranularity.ISLANDS: {
                'ES703': 'El Hierro',
            },
            GeographicalGranularity.PROVINCES: {
                'ES702': 'Santa Cruz de Tenerife',
            },
            GeographicalGranularity.COUNTIES: {'ES703A00': 'El Hierro - El Hierro'},
            GeographicalGranularity.MUNICIPALITIES: {
                '38013': 'Frontera',
                '38048': 'Valverde',
                '38901': 'El Pinar de El Hierro',
            },
        },
        'La Gomera': {
            GeographicalGranularity.REGIONS: {
                'ES70': 'Canarias',
            },
            GeographicalGranularity.ISLANDS: {
                'ES706': 'La Gomera',
            },
            GeographicalGranularity.PROVINCES: {
                'ES702': 'Santa Cruz de Tenerife',
            },
            GeographicalGranularity.COUNTIES: {
                'ES706A01': 'La Gomera - Norte',
                'ES706A02': 'La Gomera - Sur',
            },
            GeographicalGranularity.MUNICIPALITIES: {
                '38002': 'Agulo',
                '38003': 'Alajeró',
                '38021': 'Hermigua',
                '38036': 'San Sebastián de La Gomera',
                '38049': 'Valle Gran Rey',
                '38050': 'Vallehermoso',
            },
        },
        'La Palma': {
            GeographicalGranularity.REGIONS: {
                'ES70': 'Canarias',
            },
            GeographicalGranularity.ISLANDS: {
                'ES707': 'La Palma',
            },
            GeographicalGranularity.PROVINCES: {
                'ES702': 'Santa Cruz de Tenerife',
            },
            GeographicalGranularity.COUNTIES: {
                'ES707A01': 'La Palma - Capitalina',
                'ES707A02': 'La Palma - Noreste',
                'ES707A03': 'La Palma - Noroeste',
                'ES707A04': 'La Palma - Valle de Aridane',
            },
            GeographicalGranularity.MUNICIPALITIES: {
                '38024': 'Los Llanos de Aridane',
                '38037': 'Santa Cruz de La Palma',
                '38027': 'El Paso',
                '38008': 'Breña Alta',
                '38009': 'Breña Baja',
                '38053': 'Villa de Mazo',
                '38045': 'Tazacorte',
                '38033': 'San Andrés y Sauces',
                '38047': 'Tijarafe',
                '38030': 'Puntallana',
                '38029': 'Puntagorda',
                '38007': 'Barlovento',
                '38014': 'Fuencaliente de La Palma',
                '38016': 'Garafía',
            },
        },
        'Fuerteventura': {
            GeographicalGranularity.REGIONS: {
                'ES70': 'Canarias',
            },
            GeographicalGranularity.ISLANDS: {
                'ES704': 'Fuerteventura',
            },
            GeographicalGranularity.PROVINCES: {
                'ES701': 'Las Palmas',
            },
            GeographicalGranularity.COUNTIES: {
                'ES704A01': 'Fuerteventura - Centro',
                'ES704A02': 'Fuerteventura - Norte',
                'ES704A03': 'Fuerteventura - Sur',
            },
            GeographicalGranularity.MUNICIPALITIES: {
                '35003': 'Antigua',
                '35007': 'Betancuria',
                '35014': 'La Oliva',
                '35015': 'Pájara',
                '35017': 'Puerto del Rosario',
                '35030': 'Tuineje',
            },
        },
        'Lanzarote': {
            GeographicalGranularity.REGIONS: {
                'ES70': 'Canarias',
            },
            GeographicalGranularity.ISLANDS: {
                'ES708': 'Lanzarote',
            },
            GeographicalGranularity.PROVINCES: {
                'ES701': 'Las Palmas',
            },
            GeographicalGranularity.COUNTIES: {
                'ES708A01': 'Lanzarote - Este',
                'ES708A02': 'Lanzarote - Norte',
                'ES708A03': 'Lanzarote - Suroeste',
            },
            GeographicalGranularity.MUNICIPALITIES: {
                '35004': 'Arrecife',
                '35010': 'Haría',
                '35018': 'San Bartolomé',
                '35024': 'Teguise',
                '35028': 'Tías',
                '35029': 'Tinajo',
                '35034': 'Yaiza',
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
            cls.FLATTENED_CODES_BY_TITLE[title.upper()] = code

    @classmethod
    def get_codes(cls, island, granularity):
        try:
            locations = cls.CODES[island.title()][granularity]
            return locations.keys()
        except KeyError as err:
            raise IslandNotFoundError(island) from err

    @classmethod
    def get_title(cls, code):
        return cls.FLATTENED_CODES.get(code, code)

    @classmethod
    def get_code(cls, title):
        return cls.FLATTENED_CODES_BY_TITLE.get(title.upper(), title)


GeographicalGranularity.build_swapped_codes()
GeographicalRepresentation.build_flattened_codes()
GeographicalRepresentation.build_flattened_codes_by_title()
