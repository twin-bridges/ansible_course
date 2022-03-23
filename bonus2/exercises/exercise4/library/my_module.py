#!/usr/bin/python

from ansible.module_utils.basic import AnsibleModule


def main():

    # Define your modules arguments
    module_args = dict(
        my_string=dict(type="str", required=True),
    )

    # Create an instance of the AnsibleModule class
    module = AnsibleModule(argument_spec=module_args, supports_check_mode=True)

    # Define standard results
    result = dict(changed=False)

    my_string = module.params["my_string"]
    result["output"] = my_string.upper()

    # Return items as JSON
    module.exit_json(**result)


if __name__ == "__main__":
    main()
