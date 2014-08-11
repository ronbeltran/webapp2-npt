import logging
import endpoints

from protorpc import messages
from protorpc import message_types
from protorpc import remote

from models import Company as CompanyEntry

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


SYMBOL_RESOURCE = endpoints.ResourceContainer(
        message_types.VoidMessage,
        symbol=messages.StringField(1))


@endpoints.api(name='companies', version='v1')
class CompaniesApi(remote.Service):
    @endpoints.method(message_types.VoidMessage, CompanyCollection,
                      path='companies', http_method='GET',
                      name='companies.listCompanies')
    def companies_list(self, unused_request):
        return DUMMY_COMPANIES

    @endpoints.method(SYMBOL_RESOURCE, Company,
                      path='companies/{symbol}', http_method='GET',
                      name='companies.getCompany')
    def company_get(self, request):
        logging.info(request.symbol)
        company = CompanyEntry.get_by_symbol(request.symbol)
        logging.info(company)
        if company:
            return company.to_dict()
        else:
            raise endpoints.NotFoundException('Company %s not found.' % (request.symbol))


app = endpoints.api_server([CompaniesApi])
