import endpoints

from protorpc import messages
from protorpc import message_types
from protorpc import remote

package = 'companies'


class Company(messages.Message):
    name = messages.StringField(1)
    symbol = messages.StringField(2)
    sector = messages.StringField(3)
    subsector = messages.StringField(4)


class CompanyCollection(messages.Message):
    items = messages.MessageField(Company, 1, repeated=True)


DUMMY_COMPANIES = CompanyCollection(items=[
    Company(
        name='2GO Group, Inc.',
        symbol='2GO',
        sector='SERVICES',
        subsector='TRANSPORTATION SERVICES',
    ),
    Company(
        name='ABS-CBN Corporation',
        symbol='ABS',
        sector='SERVICES',
        subsector='MEDIA',
    ),
])


@endpoints.api(name='companies', version='v1')
class CompaniesApi(remote.Service):
    @endpoints.method(message_types.VoidMessage, CompanyCollection,
                      path='list', http_method='GET',
                      name='company.listCompanies')
    def companies_list(self, unused_request):
        return DUMMY_COMPANIES

app = endpoints.api_server([CompaniesApi])
