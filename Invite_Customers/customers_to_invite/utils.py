import json

from customers_to_invite.customer import Customer


def read_json_file(filename):
    customers = []

    for line in open(filename, 'r'):
        customer_json = json.loads(line)
        customers.append(Customer(customer_json['user_id'], customer_json['name'], customer_json['latitude'],
                                  customer_json['longitude']))

    return customers


def print_sorted_dictionary_ascending(unsorted_dict):
    for key in sorted(unsorted_dict.iterkeys()):
        print '%s : %s' % (key, unsorted_dict[key])