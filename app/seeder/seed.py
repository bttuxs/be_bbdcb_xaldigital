INITIAL_DATA = {
      'aeropuertos': [
        {
            'id_aeropuerto': '1',
            'nombre_aeropuerto': 'Benito Juarez'
        },
        {
            'id_aeropuerto': '2',
            'nombre_aeropuerto': 'Guanajuato'
        },
        {
            'id_aeropuerto': '3',
            'nombre_aeropuerto': 'La paz'
        },
        {
            'id_aeropuerto': '4',
            'nombre_aeropuerto': 'Oaxaca'
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
