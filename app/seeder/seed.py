INITIAL_DATA = {
      'aeropuertos': [
        {
            'idAeropuerto': '1',
            'nombreAeropuerto': 'Benito Juarez'
        },
        {
            'idAeropuerto': '2',
            'nombreAeropuerto': 'Guanajuato'
        },
        {
            'idAeropuerto': '3',
            'nombreAeropuerto': 'La paz'
        },
        {
            'idAeropuerto': '4',
            'nombreAeropuerto': 'Oaxaca'
        }
      ],
      'movimientos': [
            {'id_movimiento': '1', 'descripcion': 'Salida'},
            {'id_movimiento': '2', 'descripcion': 'Llegada'}
      ],
      'aerolineas': [
            {'id_aerolineas': '1', 'nombre_aerolinea': 'Volaris'},
            {'id_aerolineas': '2', 'nombre_aerolinea': 'Aeromar'},
            {'id_aerolineas': '3', 'nombre_aerolinea': 'Interjet'},
            {'id_aerolineas': '4', 'nombre_aerolinea': 'Aeromexico'}
      ]
}

def initialize_table(target, connection, **kw):
    tablename = str(target)
    if tablename in INITIAL_DATA and len(INITIAL_DATA[tablename]) > 0:
        connection.execute(target.insert(), INITIAL_DATA[tablename])
