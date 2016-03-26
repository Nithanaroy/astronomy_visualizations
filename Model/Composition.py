from Model import Model
from DataSource.MySQLDataSource import MySQL


class Composition(Model):
    """
    Composition Model class
    """
    TABLE = 'composition'
    DEFAULTS = {
        'hip': None,
        'cid': None,
        'element': None,
        'value': None
    }

    def __init__(self, hip, cid, element, value):
        """
        initializes a composition object
        :param hip: [required] unique id for the star. If not set now, has to be set later
        :param cid: [required] unique id for the star. If not set now, has to be set later
        :param element: [required] unique id for the star. If not set now, has to be set later
        :param value: [required] unique id for the star. If not set now, has to be set later
        :return: instance
        """
        super(Composition, self).__init__()
        self.columns.update(self.DEFAULTS)
        self.columns['hip'] = hip
        self.columns['cid'] = cid
        self.columns['element'] = element
        self.columns['value'] = value

    def find(self, connection, only_one=True):
        """
        Finds in the database for this composition
        :param connection: open connection
        :param only_one: if True, only the first record returned by DB is returned, else all are returned
        :return: record(s) if found, else None
        """
        find_composition = MySQL.select(self.TABLE, ['hip', 'cid', 'element'],
                                        ['=', '=', '='], ['AND', 'AND'])
        return super(Composition, self).find(find_composition,
                                             {'hip': self.columns['hip'], 'cid': self.columns['cid'],
                                              'element': self.columns['element'].strip()},
                                             connection, only_one)

    def upsert(self, connection):
        """
        saves or updates
        :param connection: open connection
        :return: record ID
        """
        inserted, rid = super(Composition, self).upsert(connection)
        if not inserted:
            rid = [self.columns['hip'], self.columns['cid'],
                   self.columns['element']]  # TODO: check if this is the way DB returns on c.lastrowid call
        return rid

    def update(self, connection):
        self.columns.pop('created_at', None)  # So that original timestamp is not overwritten with current one
        update_composition = MySQL.update(self.TABLE, self.columns.keys(), ['hip', 'cid', 'element'],
                                   ['=', '=', '='], ['AND', 'AND'])
        return super(Composition, self).update(update_composition, connection)
