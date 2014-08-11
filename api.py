import logging
import endpoints

from protorpc import messages
from protorpc import message_types
from protorpc import remote

from models import Company

package = 'companies'


class CompanyMessage(messages.Message):
    name = messages.StringField(1)
    symbol = messages.StringField(2)
    sector = messages.StringField(3)
    subsector = messages.StringField(4)
    created = message_types.DateTimeField(5)
    updated = message_types.DateTimeField(6)


class CompanyCollection(messages.Message):
    items = messages.MessageField(CompanyMessage, 1, repeated=True)


DUMMY_COMPANIES = CompanyCollection(items=[
    CompanyMessage(
        name='2GO Group, Inc.',
        symbol='2GO',
        sector='SERVICES',
        subsector='TRANSPORTATION SERVICES',
    ),
    CompanyMessage(
        name='ABS-CBN Corporation',
        symbol='ABS',
        sector='SERVICES',
        subsector='MEDIA',
    ),
])


SYMBOL_RESOURCE = endpoints.ResourceContainer(
        message_types.VoidMessage,
        symbol=messages.StringField(1))


CompanyResource = endpoints.ResourceContainer(
        message_types.VoidMessage,
        name=messages.StringField(1),
        symbol=messages.StringField(2, required=True),
        sector=messages.StringField(3),
        subsector=messages.StringField(4),
        )


@endpoints.api(name='companies', version='v1')
class CompaniesApi(remote.Service):
    @endpoints.method(CompanyResource, CompanyMessage,
                      path='company/create', http_method='POST',
                      name='company.create')
    def companies_create(self, request):
        company = Company.get_by_symbol(request.symbol)
        if not company:
            company = Company.new(
                name=request.name,
                symbol=request.symbol,
                sector=request.sector,
                subsector=request.subsector,
            )
        return CompanyMessage(
            name=company.name,
            symbol=company.symbol,
            sector=company.sector,
            subsector=company.subsector,
        )

    @endpoints.method(message_types.VoidMessage, CompanyCollection,
                      path='company', http_method='GET',
                      name='company.list')
    def companies_list(self, unused_request):
        return DUMMY_COMPANIES

    @endpoints.method(SYMBOL_RESOURCE, CompanyMessage,
                      path='company/{symbol}', http_method='GET',
                      name='company.get')
    def company_get(self, request):
        logging.info(request.symbol)
        company = Company.get_by_symbol(request.symbol)
        logging.info(company)
        if company:
            return company.to_dict()
        else:
            raise endpoints.NotFoundException('Company %s not found.' % (request.symbol))


app = endpoints.api_server([CompaniesApi])
