from app.models.db_connection import execute_query

def get_filtered_journeys_by_countries(origin_countries, destination_countries):
    # Dynamically create placeholders based on the number of countries
    origin_placeholders = ','.join(['%s'] * len(origin_countries))
    destination_placeholders = ','.join(['%s'] * len(destination_countries))

    query = f"""
        SELECT 
            tf.id_origin_region,
            tf.name_origin_region,
            tf.id_destination_region,
            tf.name_destination_region,
            tf.edge_path_e_road,
            tf.traffic_flow_trucks_2010,
            tf.traffic_flow_trucks_2019,
            tf.traffic_flow_trucks_2030,
            tf.traffic_flow_tons_2010,
            tf.traffic_flow_tons_2019,
            tf.traffic_flow_tons_2030,
            r_origin.country AS country_origin_region,
            r_origin.geometric_centre AS geometric_centre_origin_region,
            r_origin.geometric_centre_x AS geometric_centre_x_origin_region,
            r_origin.geometric_centre_y AS geometric_centre_y_origin_region,
            r_dest.country AS country_destination_region,
            r_dest.geometric_centre AS geometric_centre_destination_region,
            r_dest.geometric_centre_x AS geometric_centre_x_destination_region,
            r_dest.geometric_centre_y AS geometric_centre_y_destination_region
        FROM 
            traffic_flow AS tf
        LEFT JOIN regions AS r_origin
            ON tf.id_origin_region = r_origin.etisplus_zone_id
        LEFT JOIN regions AS r_dest
            ON tf.id_destination_region = r_dest.etisplus_zone_id
        WHERE 
            r_origin.country IN ({origin_placeholders})
            AND r_dest.country IN ({destination_placeholders});
    """

    # Combine origin and destination country lists into one parameter tuple
    params = tuple(origin_countries) + tuple(destination_countries)

    return execute_query(query, params)

def get_filtered_journeys_by_regions(origin_regions, destination_regions):
    # Dynamically create placeholders based on the number of countries
    origin_placeholders = ','.join(['%s'] * len(origin_regions))
    destination_placeholders = ','.join(['%s'] * len(destination_regions))

    query = f"""
        SELECT 
            tf.id_origin_region,
            tf.name_origin_region,
            tf.id_destination_region,
            tf.name_destination_region,
            tf.edge_path_e_road,
            tf.traffic_flow_trucks_2010,
            tf.traffic_flow_trucks_2019,
            tf.traffic_flow_trucks_2030,
            tf.traffic_flow_tons_2010,
            tf.traffic_flow_tons_2019,
            tf.traffic_flow_tons_2030,
            r_origin.country AS country_origin_region,
            r_origin.geometric_centre AS geometric_centre_origin_region,
            r_origin.geometric_centre_x AS geometric_centre_x_origin_region,
            r_origin.geometric_centre_y AS geometric_centre_y_origin_region,
            r_dest.country AS country_destination_region,
            r_dest.geometric_centre AS geometric_centre_destination_region,
            r_dest.geometric_centre_x AS geometric_centre_x_destination_region,
            r_dest.geometric_centre_y AS geometric_centre_y_destination_region
        FROM 
            traffic_flow AS tf
        LEFT JOIN regions AS r_origin
            ON tf.id_origin_region = r_origin.etisplus_zone_id
        LEFT JOIN regions AS r_dest
            ON tf.id_destination_region = r_dest.etisplus_zone_id
        WHERE 
            tf.name_origin_region IN ({origin_placeholders})
            AND tf.name_destination_region IN ({destination_placeholders});
    """

    # Combine origin and destination country lists into one parameter tuple
    params = tuple(origin_regions) + tuple(destination_regions)

    return execute_query(query, params)

def create_origin_region_options(filtered_journeys):
    """
    Create a list of user-friendly origin region options.

    Args:
        filtered_journeys (DataFrame): Filtered journeys DataFrame.

    Returns:
        list: Origin region options as strings for display.
    """
    return filtered_journeys["name_origin_region"].unique().tolist()

def create_destination_region_options(filtered_journeys):
    """
    Create a list of user-friendly destination region options.

    Args:
        filtered_journeys (DataFrame): Filtered journeys DataFrame.

    Returns:
        list: Destination region options as strings for display.
    """
    return filtered_journeys["name_destination_region"].unique().tolist()




