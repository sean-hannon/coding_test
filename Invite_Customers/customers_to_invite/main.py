import utils

if __name__ == '__main__':

    customers = []
    customers_to_invite = {}

    customers = utils.read_json_file('customers_to_invite/customers.txt')

    for customer in customers:
        dist_to_office = customer.distance_to_dublin_office()
        if dist_to_office <= 100.0:
            customers_to_invite.update({customer.id: customer.name})

    utils.print_sorted_dictionary_ascending(customers_to_invite)
