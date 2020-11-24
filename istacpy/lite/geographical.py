ISLANDS = {
    'TENERIFE': {
        'COUNTIES': {
            'TENERIFE - ÁREA METROPOLITANA': 'ES709A11',
            'TENERIFE NORTE - ACENTEJO': 'ES709A21',
            'TENERIFE NORTE - DAUTE': 'ES709A22',
            'TENERIFE NORTE - ICOD': 'ES709A23',
            'TENERIFE NORTE - VALLE DE LA OROTAVA': 'ES709A24',
            'TENERIFE SUR - ABONA': 'ES709A31',
            'TENERIFE SUR - SUROESTE': 'ES709A32',
            'TENERIFE SUR - VALLE DE GÜÍMAR': 'ES709A33',
        },
        'MUNICIPALITIES': {
            'ADEJE': '38001',
            'ARAFO': '38004',
            'ARICO': '38005',
            'ARONA': '38006',
            'BUENAVISTA DEL NORTE': '38010',
            'CANDELARIA': '38011',
            'EL ROSARIO': '38032',
            'EL SAUZAL': '38041',
            'EL TANQUE': '38044',
            'FASNIA': '38012',
            'GARACHICO': '38015',
            'GRANADILLA DE ABONA': '38017',
            'GUÍA DE ISORA': '38019',
            'GÜÍMAR': '38020',
            'ICOD DE LOS VINOS': '38022',
            'LA GUANCHA': '38018',
            'LA MATANZA DE ACENTEJO': '38025',
            'LA OROTAVA': '38026',
            'LA VICTORIA DE ACENTEJO': '38051',
            'LOS REALEJOS': '38031',
            'LOS SILOS': '38042',
            'PUERTO DE LA CRUZ': '38028',
            'SAN CRISTÓBAL DE LA LAGUNA': '38023',
            'SAN JUAN DE LA RAMBLA': '38034',
            'SAN MIGUEL DE ABONA': '38035',
            'SANTA CRUZ DE TENERIFE': '38038',
            'SANTA ÚRSULA': '38039',
            'SANTIAGO DEL TEIDE': '38040',
            'TACORONTE': '38043',
            'TEGUESTE': '38046',
            'VILAFLOR DE CHASNA': '38052',
        },
    }
}


def get_codes(island, scope):
    locations = ISLANDS[island][scope]
    return locations.values()
