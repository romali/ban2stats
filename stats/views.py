from django.http.response import HttpResponse
from stats.packages.attacked_service import AttackedServicePackageBuilder
from stats.packages.blocked_country import BlockedCountryPackageBuilder
from stats.packages.blocked_location import BlockedLocationPackageBuilderMinimized
from stats.packages.location_details import LocationDetailsPackageBuilder


def return_json_content(content):
    response = HttpResponse(content, content_type="application/json")
    response["Access-Control-Allow-Origin"] = "*"
    return response


def get_attacked_services(request):
    content = AttackedServicePackageBuilder().render_all_objects_as_list()
    return return_json_content(content)


def get_blocked_countries(request):
    content = BlockedCountryPackageBuilder().render_all_objects_as_list()
    return return_json_content(content)


def get_block_locations(request):
    content = BlockedLocationPackageBuilderMinimized().render_all_objects_as_list()
    return return_json_content(content)


def get_location_details(request):
    lat = request.REQUEST.get('latitude')
    lon = request.REQUEST.get('longitude')
    content = LocationDetailsPackageBuilder(lat, lon).render_all_objects_as_list()
    # content = """
    # [
    # ["Wordpress Portal",
    # "202.99.83.24",
    # "2014-10-22 04:53:06.533996+00:00",
    # 200
    # ]
    # ]
    # """
    return return_json_content(content)