from rest_framework import serializers
from rest_framework_tricks.serializers import (
    HyperlinkedModelSerializer,
    ModelSerializer,
)

from .models import (
    Author,
    AuthorProxy,
    Book,
    Profile,
    Publisher,
)

__all__ = (
    'AddressInformationSerializer',
    'AuthorProxySerializer',
    'AuthorSerializer',
    'BookSerializer',
    'BusinessContactInformationSerializer',
    'ContactInformationSerializer',
    'PersonalContactInformationSerializer',
    'ProxyBusinessContactInformationSerializer',
    'ProxyContactInformationSerializer',
    'ProxyPersonalContactInformationSerializer',
    'PublisherSerializer',
    'PublishingInformationSerializer',
    'StockInformationSerializer',
    'ProfileSerializer',
)

# ****************************************************************************
# ******************************** Book **************************************
# ****************************************************************************


class PublishingInformationSerializer(serializers.ModelSerializer):
    """Publishing information serializer."""

    publication_date = serializers.DateField(required=False)
    isbn = serializers.CharField(required=False)
    pages = serializers.IntegerField(required=False)

    class Meta(object):
        """Meta options."""

        model = Book
        fields = (
            'publication_date',
            'isbn',
            'pages',
        )
        nested_proxy_field = True


class StockInformationSerializer(serializers.ModelSerializer):
    """Stock information serializer."""

    class Meta(object):
        """Meta options."""

        model = Book
        fields = (
            'stock_count',
            'price',
            'state',
        )
        nested_proxy_field = True


class BookSerializer(HyperlinkedModelSerializer):
    """Book serializer."""

    publishing_information = PublishingInformationSerializer(required=False)
    stock_information = StockInformationSerializer(required=False)

    class Meta(object):
        """Meta options."""

        model = Book
        fields = (
            'url',
            'id',
            'title',
            'description',
            'summary',
            'publishing_information',
            'stock_information',
        )

# ****************************************************************************
# ****************************** Publisher ***********************************
# ****************************************************************************


class AddressInformationSerializer(serializers.ModelSerializer):
    """Address information serializer."""

    class Meta(object):
        """Meta options."""

        model = Publisher
        fields = (
            'address',
            'city',
            'state_province',
            'country',
        )
        nested_proxy_field = True


class PublisherSerializer(ModelSerializer):
    """Publisher serializer."""

    address_information = AddressInformationSerializer(required=False)

    class Meta(object):
        """Meta options."""

        model = Publisher
        fields = (
            'id',
            'name',
            'info',
            'website',
            'address_information',
        )


# ****************************************************************************
# ******************************** Author ************************************
# ****************************************************************************


class PersonalContactInformationSerializer(serializers.ModelSerializer):
    """Personal contact information serializer."""

    class Meta(object):
        """Meta options."""

        model = Author
        fields = (
            'email',
            'phone_number',
            'website',
        )
        nested_proxy_field = True


class BusinessContactInformationSerializer(serializers.ModelSerializer):
    """Business contact information serializer."""

    class Meta(object):
        """Meta options."""

        model = Author
        fields = (
            'company',
            'company_email',
            'company_phone_number',
            'company_website',
        )
        nested_proxy_field = True


class ContactInformationSerializer(serializers.ModelSerializer):
    """Contact information serializer."""

    personal_contact_information = PersonalContactInformationSerializer(
        required=False
    )
    business_contact_information = BusinessContactInformationSerializer(
        required=False
    )

    class Meta(object):
        """Meta options."""

        model = Author
        fields = (
            'personal_contact_information',
            'business_contact_information',
        )
        nested_proxy_field = True


class AuthorSerializer(ModelSerializer):
    """Author serializer."""

    contact_information = ContactInformationSerializer(required=False)

    class Meta(object):
        """Meta options."""

        model = Author
        fields = (
            'id',
            'salutation',
            'name',
            'birth_date',
            'biography',
            'contact_information',
        )

# ****************************************************************************
# ****************************** AuthorProxy *********************************
# ****************************************************************************


class ProxyPersonalContactInformationSerializer(serializers.ModelSerializer):
    """Personal contact information serializer."""

    class Meta(object):
        """Meta options."""

        model = AuthorProxy
        fields = (
            'email',
            'phone_number',
            'website',
        )
        nested_proxy_field = True


class ProxyBusinessContactInformationSerializer(serializers.ModelSerializer):
    """Business contact information serializer."""

    class Meta(object):
        """Meta options."""

        model = AuthorProxy
        fields = (
            'company',
            'company_email',
            'company_phone_number',
            'company_website',
        )
        nested_proxy_field = True


class ProxyContactInformationSerializer(serializers.ModelSerializer):
    """Contact information serializer."""

    personal_contact_information = ProxyPersonalContactInformationSerializer(
        required=False
    )
    business_contact_information = ProxyBusinessContactInformationSerializer(
        required=False
    )

    class Meta(object):
        """Meta options."""

        model = AuthorProxy
        fields = (
            'personal_contact_information',
            'business_contact_information',
        )
        nested_proxy_field = True


class AuthorProxySerializer(ModelSerializer):
    """Author serializer."""

    contact_information = ProxyContactInformationSerializer(required=False)

    class Meta(object):
        """Meta options."""

        model = AuthorProxy
        fields = (
            'id',
            'salutation',
            'name',
            'birth_date',
            'biography',
            'contact_information',
        )


# ****************************************************************************
# ******************************* Profile ************************************
# ****************************************************************************


class PersonalInformationSerializer(serializers.ModelSerializer):
    """Personal information serializer."""

    class Meta(object):
        """Meta options."""

        model = Profile
        fields = (
            'salutation',
            'first_name',
            'last_name',
            'birth_date',
            'biography',
        )
        nested_proxy_field = True


class PersonalContactInformationSerializer(serializers.ModelSerializer):
    """Personal contact information serializer."""

    class Meta(object):
        """Meta options."""

        model = Profile
        fields = (
            'email',
            'phone_number',
            'website',
        )
        nested_proxy_field = True


class BusinessContactInformationSerializer(serializers.ModelSerializer):
    """Business contact information serializer."""

    class Meta(object):
        """Meta options."""

        model = Profile
        fields = (
            'company',
            'company_email',
            'company_phone_number',
            'company_website',
        )
        nested_proxy_field = True


class ContactInformationSerializer(serializers.ModelSerializer):
    """Contact information serializer."""

    personal_contact_information = PersonalContactInformationSerializer(
        required=False
    )
    business_contact_information = BusinessContactInformationSerializer(
        required=False
    )

    class Meta(object):
        """Meta options."""

        model = Profile
        fields = (
            'personal_contact_information',
            'business_contact_information',
        )
        nested_proxy_field = True


class BankInformationSerializer(serializers.ModelSerializer):
    """Bank information serializer."""

    class Meta(object):
        """Meta options."""

        model = Profile
        fields = (
            'bank_name',
            'bank_account_name',
            'bank_account_number',
        )
        nested_proxy_field = True


class DataSerializer(serializers.ModelSerializer):
    """Data serializer."""

    personal_information = PersonalInformationSerializer(
        required=False
    )
    contact_information = ContactInformationSerializer(
        required=False
    )
    bank_information = BankInformationSerializer(
        required=False
    )

    class Meta(object):
        """Meta options."""

        model = Profile
        fields = (
            'personal_information',
            'contact_information',
            'bank_information',
        )
        nested_proxy_field = True


class InformationSerializer(serializers.ModelSerializer):
    """information serializer."""

    data = DataSerializer(
        required=False
    )

    class Meta(object):
        """Meta options."""

        model = Profile
        fields = (
            'data',
        )
        nested_proxy_field = True


class ProfileSerializer(ModelSerializer):
    """Profile serializer."""

    information = InformationSerializer(required=False)

    class Meta(object):
        """Meta options."""

        model = Profile
        fields = (
            'id',
            'information',
        )
